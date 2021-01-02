from argument_parser import ArgumentParser
import os
import pandas as pd
from datetime import datetime


argument_parser = ArgumentParser()
directory = argument_parser.get_directory()
outputName = argument_parser.get_outputName()

df = pd.DataFrame()
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print(filename + ', time: ' + str(datetime.now().strftime("%H:%M:%S")))
        file = os.path.join(directory, filename)
        df = df.append(pd.read_csv(file), ignore_index=True)
        print(filename + '_END, time: ' +
              str(datetime.now().strftime("%H:%M:%S")))
df.to_csv(outputName)
