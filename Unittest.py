import unittest
import pandas as pd

from PermutationForecaster import PermutationForecaster
df = pd.read_csv("/Users/ara_vartomian/Downloads/JEPI (1).csv")
pf = PermutationForecaster(df['High'])
print(pf.bin_maker())


