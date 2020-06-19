import pandas as pd
from Transportation_packages.data import get_fremont_data

def test_fremont_data():
    data=get_fremont_data()
    assert all(data.columns ==['Total', 'East', 'West'])
    assert(isinstance(data.index,pd.DatetimeIndex))
