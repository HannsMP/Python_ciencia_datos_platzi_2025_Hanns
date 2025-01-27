import pandas as pd
import numpy as np
from os import path, getcwd

cwd = getcwd()
dir_main = path.abspath(path.join(cwd, '..'))

path_csv = path.join(dir_main, 'csv','online_retail.csv')

df = pd.read_csv(path_csv, encoding='latin1')