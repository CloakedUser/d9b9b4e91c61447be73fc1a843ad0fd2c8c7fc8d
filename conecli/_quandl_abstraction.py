# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import quandl

from conecli import config

def _get_data_for_symbol(symbol, api_key, start_date=None, end_date=None):
    # TODO: Fix this to be more specific/filtered based upon the report type
    data_set_symbol = 'WIKI/%s' % symbol
    params = {}
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    quandl.ApiConfig.api_key = api_key
    return quandl.Dataset(data_set_symbol).data(params=params)

def func_for_report():
    if config.CONFIG.max_daily_profit:
        return _get_max_daily_profit
    elif config.CONFIG.busy_day:
        return _get_busy_day_data
    elif config.CONFIG.biggest_loser:
        return _get_biggest_loser
    else:
        return _get_monthly_data


def _get_monthly_data(symbol_list):
    results = {'report_type': 'monthly_avg',
               'symbols': {sym: [] for sym in symbol_list}}
    for symbol in symbol_list:
        dataset = _get_data_for_symbol(symbol, config.CONFIG.api_key,
                                       start_date=config.DATE_START,
                                       end_date=config.DATE_END)
        fields = dataset.column_names
        # Locate the fields we care about
        date_field_index = fields.index('Date')
        open_field_index = fields.index('Open')
        close_field_index = fields.index('Close')
        by_month = {}
        for element in dataset.to_list():
            month_str = element[date_field_index].strftime('%Y-%m')
            by_month.setdefault(month_str, {'open': [], 'close': []})
            by_month[month_str]['open'].append(element[open_field_index])
            by_month[month_str]['close'].append(element[close_field_index])

        for month in by_month.keys():
            open_list = by_month[month_str]['open']
            close_list = by_month[month_str]['close']
            results['symbols'][symbol].append({
                'month': month,
                'average_open': '%.2f' % (
                        sum(open_list)/float(len(open_list))),
                'average_close': '%.2f' % (
                        sum(close_list)/float(len(close_list)))
            })
    return results

def _get_max_daily_profit(symbol_list):
    results = {'report_type': 'max_profit',
               'symbols': {sym: {} for sym in symbol_list}}
    for symbol in symbol_list:
        max_profit_date = None
        profit = 0
        dataset = _get_data_for_symbol(symbol, config.CONFIG.api_key,
                                       start_date=config.DATE_START,
                                       end_date=config.DATE_END)
        fields = dataset.column_names
        # Locate the fields we care about
        date_field_index = fields.index('Date')
        high_field_index = fields.index('High')
        low_field_index = fields.index('Low')
        for values in dataset.to_list():
            calc_profit = (values[high_field_index] - values[low_field_index])
            if calc_profit > profit:
                max_profit_date = values[date_field_index].strftime('%Y-%m-%d')
                profit = calc_profit
        results['symbols'][symbol]['max_profit_date'] = max_profit_date
        results['symbols'][symbol]['profit'] = '%.2f' % profit

    return results


def _get_busy_day_data(symbol_list):
    results = {'report_type': 'busy_day',
               'symbols': {
                   sym: {'average_volume': 0, 'days_10_percent_above_avg': []}
                   for sym in symbol_list}}
    for symbol in symbol_list:
        max_profit_date = None
        profit = 0
        avg_volume = 0
        dataset = _get_data_for_symbol(symbol, config.CONFIG.api_key,
                                       start_date=config.DATE_START,
                                       end_date=config.DATE_END)
        fields = dataset.column_names
        # Locate the fields we care about
        date_field_index = fields.index('Date')
        volume_field_index = fields.index('Volume')
        dataset_list = dataset.to_list()
        v_list = [v[volume_field_index] for v in dataset_list]

        avg_volume = sum(v_list)/len(v_list)
        ten_percent_above = int(avg_volume * 1.1)
        results['symbols'][symbol]['average_volume'] = '%.1f' % int(avg_volume)

        for value in dataset_list:
            if value[volume_field_index] > ten_percent_above:
                results['symbols'][symbol]['days_10_percent_above_avg'].append(
                    {'date': value[date_field_index].strftime('%Y-%m-%d'),
                     'volume': value[volume_field_index]})
    return results

def _get_biggest_loser(symbol_list):
    results = {'report_type': 'biggest_loser',
               'results': {'symbol': None, 'days_closing_lower': 0}}
    symbol_days_loss = {sym: 0 for sym in symbol_list}

    for symbol in symbol_list:
        max_profit_date = None
        profit = 0
        avg_volume = 0
        dataset = _get_data_for_symbol(symbol, config.CONFIG.api_key,
                                       start_date=config.DATE_START,
                                       end_date=config.DATE_END)
        fields = dataset.column_names
        # Locate the fields we care about
        open_field_index = fields.index('Open')
        close_field_index = fields.index('Close')
        dataset_list = dataset.to_list()

        for value in dataset_list:
            if value[close_field_index] < value[open_field_index]:
                symbol_days_loss[symbol] += 1

    for s in symbol_days_loss.keys():
        if symbol_days_loss[s] > results['results']['days_closing_lower']:
            results['results']['symbol'] = s
            results['results']['days_closing_lower'] = symbol_days_loss[s]

    return results
