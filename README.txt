To run this CLI:

--[ NOTE ]--
This requires python3, a virtual environment, pip (including internet access) and the Quandl python library.

Ensure your current working directory is the main directory in the git repo.

-> pwd => /home/cloakeduser/projects/conecil

Create a Virtual Environment:

-> virtualenv -p `which python3` ./VENV

Activate the Virtual Environment:

-> source ./VENV/bin/activate

Install the conecli package:

-> pip install .

    Processing /home/cloakeduser/d9b9b4e91c61447be73fc1a843ad0fd2c8c7fc8d
    Collecting pbr!=2.1.0,>=2.0.0 (from c-one-cli==0.0.1.dev1)
      Using cached pbr-3.1.1-py2.py3-none-any.whl
    Collecting quandl (from c-one-cli==0.0.1.dev1)
      Using cached Quandl-3.3.0-py2.py3-none-any.whl
    Collecting more-itertools (from quandl->c-one-cli==0.0.1.dev1)
      Using cached more_itertools-4.0.1-py3-none-any.whl
    Collecting numpy>=1.8 (from quandl->c-one-cli==0.0.1.dev1)
      Using cached numpy-1.13.3-cp36-cp36m-manylinux1_x86_64.whl
    Collecting python-dateutil (from quandl->c-one-cli==0.0.1.dev1)
      Using cached python_dateutil-2.6.1-py2.py3-none-any.whl
    Collecting pandas>=0.14 (from quandl->c-one-cli==0.0.1.dev1)
      Using cached pandas-0.22.0-cp36-cp36m-manylinux1_x86_64.whl
    Collecting pyasn1 (from quandl->c-one-cli==0.0.1.dev1)
      Using cached pyasn1-0.4.2-py2.py3-none-any.whl
    Collecting six (from quandl->c-one-cli==0.0.1.dev1)
      Using cached six-1.11.0-py2.py3-none-any.whl
    Collecting inflection>=0.3.1 (from quandl->c-one-cli==0.0.1.dev1)
    Collecting ndg-httpsclient (from quandl->c-one-cli==0.0.1.dev1)
      Using cached ndg_httpsclient-0.4.3-py3-none-any.whl
    Collecting pyOpenSSL (from quandl->c-one-cli==0.0.1.dev1)
      Using cached pyOpenSSL-17.5.0-py2.py3-none-any.whl
    Collecting requests>=2.7.0 (from quandl->c-one-cli==0.0.1.dev1)
      Using cached requests-2.18.4-py2.py3-none-any.whl
    Collecting pytz>=2011k (from pandas>=0.14->quandl->c-one-cli==0.0.1.dev1)
      Using cached pytz-2017.3-py2.py3-none-any.whl
    Collecting cryptography>=2.1.4 (from pyOpenSSL->quandl->c-one-cli==0.0.1.dev1)
      Using cached cryptography-2.1.4-cp36-cp36m-manylinux1_x86_64.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests>=2.7.0->quandl->c-one-cli==0.0.1.dev1)
      Using cached urllib3-1.22-py2.py3-none-any.whl
    Collecting chardet<3.1.0,>=3.0.2 (from requests>=2.7.0->quandl->c-one-cli==0.0.1.dev1)
      Using cached chardet-3.0.4-py2.py3-none-any.whl
    Collecting certifi>=2017.4.17 (from requests>=2.7.0->quandl->c-one-cli==0.0.1.dev1)
      Using cached certifi-2017.11.5-py2.py3-none-any.whl
    Collecting idna<2.7,>=2.5 (from requests>=2.7.0->quandl->c-one-cli==0.0.1.dev1)
      Using cached idna-2.6-py2.py3-none-any.whl
    Collecting asn1crypto>=0.21.0 (from cryptography>=2.1.4->pyOpenSSL->quandl->c-one-cli==0.0.1.dev1)
      Using cached asn1crypto-0.24.0-py2.py3-none-any.whl
    Collecting cffi>=1.7; platform_python_implementation != "PyPy" (from cryptography>=2.1.4->pyOpenSSL->quandl->c-one-cli==0.0.1.dev1)
      Using cached cffi-1.11.2-cp36-cp36m-manylinux1_x86_64.whl
    Collecting pycparser (from cffi>=1.7; platform_python_implementation != "PyPy"->cryptography>=2.1.4->pyOpenSSL->quandl->c-one-cli==0.0.1.dev1)
    Installing collected packages: pbr, six, more-itertools, numpy, python-dateutil, pytz, pandas, pyasn1, inflection, asn1crypto, pycparser, cffi, idna, cryptography, pyOpenSSL, ndg-httpsclient, urllib3, chardet, certifi, requests, quandl, c-one-cli
      Running setup.py install for c-one-cli ... done
    Successfully installed asn1crypto-0.24.0 c-one-cli-0.0.1.dev1 certifi-2017.11.5 cffi-1.11.2 chardet-3.0.4 cryptography-2.1.4 idna-2.6 inflection-0.3.1 more-itertools-4.0.1 ndg-httpsclient-0.4.3 numpy-1.13.3 pandas-0.22.0 pbr-3.1.1 pyOpenSSL-17.5.0 pyasn1-0.4.2 pycparser-2.18 python-dateutil-2.6.1 pytz-2017.3 quandl-3.3.0 requests-2.18.4 six-1.11.0 urllib3-1.22


--[ NOTE ]-- PBR requires either a git repository or an sdist. For this example, a git repo is perfectly sufficient

* Run the CLI (ensure you use your API Key as the first positional argument)

    $ c-one-cli <API-KEY>
        {'report_type': 'monthly_avg',
         'symbols': {'COF': [{'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-01'},
                             {'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-02'},
                             {'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-03'},
                             {'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-04'},
                             {'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-05'},
                             {'average_close': '80.33',
                              'average_open': '80.10',
                              'month': '2017-06'}],
                     'GOOGL': [{'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-01'},
                               {'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-02'},
                               {'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-03'},
                               {'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-04'},
                               {'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-05'},
                               {'average_close': '973.37',
                                'average_open': '975.78',
                                'month': '2017-06'}],
                     'MSFT': [{'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-01'},
                              {'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-02'},
                              {'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-03'},
                              {'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-04'},
                              {'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-05'},
                              {'average_close': '70.52',
                               'average_open': '70.56',
                               'month': '2017-06'}]}}

    $ c-one-cli <API-KEY> --biggest-loser
        {'report_type': 'biggest_loser',
         'results': {'days_closing_lower': 62, 'symbol': 'COF'}}


    $ c-one-cli <API-KEY> --busy-day
            {'report_type': 'busy_day',
             'symbols': {'COF': {'average_volume': '2757167.0',
                     'days_10_percent_above_avg': [{'date': '2017-01-03',
                                                    'volume': 3441067.0},
                                                   {'date': '2017-01-10',
                                                    'volume': 3141198.0},
                                                   {'date': '2017-01-25',
                                                    'volume': 5304078.0},
                                                   {'date': '2017-01-30',
                                                    'volume': 3550371.0},
                                                   {'date': '2017-02-07',
                                                    'volume': 3514042.0},
                                                   {'date': '2017-02-17',
                                                    'volume': 4044661.0},
                                                   {'date': '2017-02-21',
                                                    'volume': 3825225.0},
                                                   {'date': '2017-02-28',
                                                    'volume': 3122357.0},
                                                   {'date': '2017-03-01',
                                                    'volume': 3387946.0},
                                                   {'date': '2017-03-15',
                                                    'volume': 3178963.0},
                                                   {'date': '2017-03-17',
                                                    'volume': 3388267.0},
                                                   {'date': '2017-03-21',
                                                    'volume': 4559025.0},
                                                   {'date': '2017-03-22',
                                                    'volume': 3133651.0},
                                                   {'date': '2017-03-27',
                                                    'volume': 4282097.0},
                                                   {'date': '2017-03-28',
                                                    'volume': 3784720.0},
                                                   {'date': '2017-03-30',
                                                    'volume': 4081656.0},
                                                   {'date': '2017-04-03',
                                                    'volume': 3158771.0},
                                                   {'date': '2017-04-06',
                                                    'volume': 4378949.0},
                                                   {'date': '2017-04-13',
                                                    'volume': 3400095.0},
                                                   {'date': '2017-04-17',
                                                    'volume': 3759420.0},
                                                   {'date': '2017-04-18',
                                                    'volume': 3119402.0},
                                                   {'date': '2017-04-25',
                                                    'volume': 3080861.0},
                                                   {'date': '2017-04-26',
                                                    'volume': 7386158.0},
                                                   {'date': '2017-04-27',
                                                    'volume': 3604560.0},
                                                   {'date': '2017-04-28',
                                                    'volume': 6133211.0},
                                                   {'date': '2017-05-01',
                                                    'volume': 3543401.0},
                                                   {'date': '2017-05-04',
                                                    'volume': 3154418.0},
                                                   {'date': '2017-05-11',
                                                    'volume': 3741154.0},
                                                   {'date': '2017-05-12',
                                                    'volume': 3931119.0},
                                                   {'date': '2017-05-17',
                                                    'volume': 3145845.0},
                                                   {'date': '2017-05-18',
                                                    'volume': 4884650.0},
                                                   {'date': '2017-05-31',
                                                    'volume': 4205013.0},
                                                   {'date': '2017-06-01',
                                                    'volume': 3295232.0},
                                                   {'date': '2017-06-09',
                                                    'volume': 3476989.0},
                                                   {'date': '2017-06-15',
                                                    'volume': 3854218.0},
                                                   {'date': '2017-06-16',
                                                    'volume': 3255538.0},
                                                   {'date': '2017-06-19',
                                                    'volume': 3225890.0},
                                                   {'date': '2017-06-28',
                                                    'volume': 3773097.0},
                                                   {'date': '2017-06-29',
                                                    'volume': 6009615.0}]},
             'GOOGL': {'average_volume': '1632363.0',
                       'days_10_percent_above_avg': [{'date': '2017-01-03',
                                                      'volume': 1959033.0},
                                                     {'date': '2017-01-06',
                                                      'volume': 2017097.0},
                                                     {'date': '2017-01-23',
                                                      'volume': 2457377.0},
                                                     {'date': '2017-01-26',
                                                      'volume': 3493251.0},
                                                     {'date': '2017-01-27',
                                                      'volume': 3752497.0},
                                                     {'date': '2017-01-30',
                                                      'volume': 3516933.0},
                                                     {'date': '2017-01-31',
                                                      'volume': 2020180.0},
                                                     {'date': '2017-02-01',
                                                      'volume': 2251047.0},
                                                     {'date': '2017-03-01',
                                                      'volume': 1818671.0},
                                                     {'date': '2017-03-17',
                                                      'volume': 1868252.0},
                                                     {'date': '2017-03-21',
                                                      'volume': 2537978.0},
                                                     {'date': '2017-03-23',
                                                      'volume': 3287669.0},
                                                     {'date': '2017-03-24',
                                                      'volume': 2105682.0},
                                                     {'date': '2017-03-27',
                                                      'volume': 1935211.0},
                                                     {'date': '2017-04-03',
                                                      'volume': 1969402.0},
                                                     {'date': '2017-04-05',
                                                      'volume': 1855153.0},
                                                     {'date': '2017-04-25',
                                                      'volume': 2020460.0},
                                                     {'date': '2017-04-27',
                                                      'volume': 1817740.0},
                                                     {'date': '2017-04-28',
                                                      'volume': 3753169.0},
                                                     {'date': '2017-05-01',
                                                      'volume': 2294856.0},
                                                     {'date': '2017-05-04',
                                                      'volume': 1934652.0},
                                                     {'date': '2017-05-08',
                                                      'volume': 1863198.0},
                                                     {'date': '2017-05-17',
                                                      'volume': 2414323.0},
                                                     {'date': '2017-05-25',
                                                      'volume': 1951402.0},
                                                     {'date': '2017-06-09',
                                                      'volume': 3613964.0},
                                                     {'date': '2017-06-12',
                                                      'volume': 4167184.0},
                                                     {'date': '2017-06-13',
                                                      'volume': 1992456.0},
                                                     {'date': '2017-06-15',
                                                      'volume': 2349212.0},
                                                     {'date': '2017-06-16',
                                                      'volume': 2484914.0},
                                                     {'date': '2017-06-27',
                                                      'volume': 2428048.0},
                                                     {'date': '2017-06-28',
                                                      'volume': 2713366.0},
                                                     {'date': '2017-06-29',
                                                      'volume': 3182331.0},
                                                     {'date': '2017-06-30',
                                                      'volume': 2185444.0}]},
             'MSFT': {'average_volume': '23748646.0',
                      'days_10_percent_above_avg': [{'date': '2017-01-20',
                                                     'volume': 30213462.0},
                                                    {'date': '2017-01-26',
                                                     'volume': 43554645.0},
                                                    {'date': '2017-01-27',
                                                     'volume': 44817972.0},
                                                    {'date': '2017-01-30',
                                                     'volume': 31651445.0},
                                                    {'date': '2017-02-01',
                                                     'volume': 39671528.0},
                                                    {'date': '2017-02-02',
                                                     'volume': 45827013.0},
                                                    {'date': '2017-02-03',
                                                     'volume': 30301759.0},
                                                    {'date': '2017-03-01',
                                                     'volume': 26937459.0},
                                                    {'date': '2017-03-17',
                                                     'volume': 49219686.0},
                                                    {'date': '2017-03-21',
                                                     'volume': 26640480.0},
                                                    {'date': '2017-04-19',
                                                     'volume': 26992771.0},
                                                    {'date': '2017-04-21',
                                                     'volume': 32522645.0},
                                                    {'date': '2017-04-24',
                                                     'volume': 29721254.0},
                                                    {'date': '2017-04-25',
                                                     'volume': 29983174.0},
                                                    {'date': '2017-04-27',
                                                     'volume': 32219234.0},
                                                    {'date': '2017-04-28',
                                                     'volume': 38940853.0},
                                                    {'date': '2017-05-01',
                                                     'volume': 31304672.0},
                                                    {'date': '2017-05-03',
                                                     'volume': 28725646.0},
                                                    {'date': '2017-05-11',
                                                     'volume': 27985424.0},
                                                    {'date': '2017-05-15',
                                                     'volume': 30705323.0},
                                                    {'date': '2017-05-16',
                                                     'volume': 33250702.0},
                                                    {'date': '2017-05-17',
                                                     'volume': 29964198.0},
                                                    {'date': '2017-05-19',
                                                     'volume': 26496478.0},
                                                    {'date': '2017-05-31',
                                                     'volume': 29538356.0},
                                                    {'date': '2017-06-02',
                                                     'volume': 34586054.0},
                                                    {'date': '2017-06-05',
                                                     'volume': 29507429.0},
                                                    {'date': '2017-06-06',
                                                     'volume': 31220057.0},
                                                    {'date': '2017-06-09',
                                                     'volume': 48619420.0},
                                                    {'date': '2017-06-12',
                                                     'volume': 47363986.0},
                                                    {'date': '2017-06-16',
                                                     'volume': 46911637.0},
                                                    {'date': '2017-06-29',
                                                     'volume': 28231562.0}]}}}


    $ c-one-cli <API-KEY> --max-daily-profit
        {'report_type': 'max_profit',
         'symbols': {'COF': {'max_profit_date': '2017-03-21', 'profit': '3.76'},
                     'GOOGL': {'max_profit_date': '2017-06-09', 'profit': '52.13'},
                     'MSFT': {'max_profit_date': '2017-06-09', 'profit': '3.49'}}}

