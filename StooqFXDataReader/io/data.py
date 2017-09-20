#!/usr/local/bin python
# -*- coding: UTF-8 -*-
from pandas_datareader import data
from pandas_datareader.base import _BaseReader

from time import sleep
import urllib.request
import urllib.error
import pandas as pd
import datetime as dt

_SLEEP_TIME = 0.5
_MAX_RETRY_COUNT = 3


class StooqFXReader(_BaseReader):
    @property
    def url(self):
        return 'http://stooq.com/q/d/l/?s={symbol}&d1={date_from}&d2={date_to}&i=d'

    def read(self):
        # Use _DailyBaseReader's definition
        df = self._read_one_data(self.url, params=self._get_params(self.symbols))
        return df

    def _get_params(self, symbol):
        params = {
            'symbol': symbol,
            'date_from': dt.datetime.strftime(self.start, '%Y%m%d'),
            'date_to': dt.datetime.strftime(self.end, '%Y%m%d')
        }
        return params

    def _read_one_data(self, url, params):
        url = self.url.format(**params)

        result = pd.DataFrame()

        try:
            response = urllib.request.urlopen(url)
            result = pd.read_csv(response, encoding='Shift_JIS')
        except urllib.error.HTTPError:
            sleep(_SLEEP_TIME)

        return result


class SymbolError(Exception):
    pass


def DataReader(symbols, data_source=None, start=None, end=None, **kwargs):
    if data_source == 'stooqfx':
        return StooqFXReader(symbols=symbols, start=start, end=end, **kwargs).read()
    else:
        return data.DataReader(name=symbols, data_source=data_source, start=start, end=end, **kwargs)


DataReader.__doc__ = data.DataReader.__doc__

if __name__ == '__main__':
    df = DataReader('USDJPY', data_source='stooqfx', start='2015-12-01', end='2015-12-31')
    print(
        df.head(5)
    )
