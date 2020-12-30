from argument_parser import ArgumentParser
import os
import pandas as pd


argument_parser = ArgumentParser()
directory = argument_parser.get_directory()
outputName = argument_parser.get_outputName()

df = pd.DataFrame()
for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        file = os.path.join(directory, filename)
        df = df.append(pd.read_csv(file), ignore_index=True)
df.to_csv(outputName)