#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python 3.5
import urllib.request
import pandas as pd
import datetime


class PyStooqFX:
    """
    PythonでStooqから為替レートを取得する
    """
    def __init__(self, symbol):
        self.symbol = symbol

    def historical_daily(self, date_from, date_to):
        date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d')
        date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')

        f = lambda d: datetime.datetime.strftime(d, '%Y%m%d')
        args = dict(symbol=self.symbol, datefrom=f(date_from), dateto=f(date_to))
        # URL生成
        url = 'http://stooq.com/q/d/l/?s={symbol}&d1={datefrom}&d2={dateto}&i=d'.format(**args)
        response = urllib.request.urlopen(url)

        # データを取得しDataFrameに追加
        try:
            df = pd.read_csv(response, encoding='Shift_JIS')
        except pd.parser.CParserError:
            df = pd.DataFrame()

        return df

if __name__ == '__main__':
    myFX = PyStooqFX('usdjpy')
    df = myFX.historical_daily('2015-01-01', '2015-12-31')
    print(df)
