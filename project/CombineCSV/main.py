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
        time = str(datetime.now().strftime("%H:%M:%S"))
        print(f'{filename}, time: {time}')
        file = os.path.join(directory, filename)
        df = df.append(pd.read_csv(file), ignore_index=True)
        time = str(datetime.now().strftime("%H:%M:%S"))
        print(f'{filename}_END, time: {time}')
df.to_csv(outputName)
