import numpy as np
import pandas as pd
from datetime import datetime


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here
    res = []
    # read files
    for file in files:
        companies = file.split('/')[-1].split('.')[0]
        df = pd.read_csv(file)

        df["date"] = pd.to_datetime(df["date"])
        df["year"] = df["date"].dt.year
        vol_max = df.groupby('year')['vol'].max()
        vol_date = df.groupby(['year', 'vol'])['date'].min().reset_index()
        vol_date = vol_date.rename(columns={'date': 'date_max_vol'})
        vol_data = pd.merge(vol_max, vol_date, on='year')
        close_max = df.groupby('year')['close'].max()
        close_date = df.groupby(['year', 'close'])['date'].apply(list).reset_index()
        close_date = close_date[close_date['date'].apply(len) > 1]
        close_date = close_date.explode('date')
        close_date = close_date.rename(columns={'date': 'date_max_close'})
        close_data = pd.merge(close_max, close_date, on='year')
        res.append([
            pd.DataFrame({
                'date': vol_data['date_max_vol'],
                'vol': vol_data['vol']
            }),
            pd.DataFrame({
                'date': close_data['date_max_close'],
                'close': close_data['close']
            })
        ])

    return res



