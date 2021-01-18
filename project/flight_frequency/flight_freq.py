# import findspark
# findspark.init()
# from pyspark import SparkContext, SparkConf
#
# sc = SparkContext(conf=SparkConf())
# data_from_file = sc.textFile('ignore/full.csv')
import copy

import matplotlib.pyplot as plt
from pandas import Grouper, date_range
import dask.dataframe as dd


filepath1 = "../../../flights/loty2019.csv"
filepath2 = "../../../flights/loty2020.csv"
filepath = "../../ignore/full.csv"

relevant_columns = ['FL_DATE', 'CANCELLED']
df = dd.read_csv(filepath, usecols=relevant_columns,  parse_dates=['FL_DATE']).dropna()

df = df[df.CANCELLED!=1.0]
df = df[df.FL_DATE.dt.year > 2011]
gr = Grouper(key="FL_DATE", freq='M')
months = df.groupby([df['FL_DATE'].dt.to_period("M")])['CANCELLED'].count().compute()
quarters = df.groupby(df['FL_DATE'].dt.to_period('Q'))['CANCELLED'].count().compute()
months.to_csv("csv_files/months.csv")
quarters.to_csv("quarters.csv")


