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

import argparse

SYMBOLS = ['COF', 'GOOGL', 'MSFT']
DATE_START = '2017-01-01'
DATE_END = '2017-06-30'
CONFIG = argparse.Namespace()


PARSER = argparse.ArgumentParser(description='Process Stock Price via Quandl '
                                             'WIKI API')
PARSER.add_argument('api_key',
                    help='The API-Key used to access Quandl API (required)')

_optional_features_group = PARSER.add_mutually_exclusive_group()
_optional_features_group.add_argument('--max-daily-profit',
                                      action='store_true',
                                      help='Display which day has the largest '
                                           'profit for each security if '
                                           'purchased at the low and sold at '
                                           'the high.')
_optional_features_group.add_argument('--busy-day', action='store_true',
                                      help='Display which days generated '
                                           'unusually high activity for the '
                                           'securities.')
_optional_features_group.add_argument('--biggest-loser', action='store_true',
                                      help='Display which security had the '
                                           'most days where the closing price '
                                           'was lower than the opening price.')


def parse_args():
    global CONFIG
    CONFIG = PARSER.parse_args()