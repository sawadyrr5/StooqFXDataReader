# About this library
Downloading FX historical data from Stooq.

## How to install
```
pip install git+https://github.com/sawadyrr5/StooqFXDataReader
``` 

## How to use
```
from StoosFXDataReader.io.data import DataReader
```

## 1. Download price data.
```
DataReader('USDJPY', data_source='stooqfx', start='2015-12-01', end='2015-12-31')
```
