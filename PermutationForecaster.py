#Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the training set
filepath = 'JEPI (1).csv'
df = pd.read_csv(filepath)

''' '''
def sort_func(column,n=6):
  sorted_list = []
  length_col = 250
  for ind in range(length_col-n):
    sorted = column[ind:ind+n].sort_values()
    sorted_list.append(sorted)
  return sorted_list


def sort_index(col=df_high, m=6):
  ind_list = []
  df = sort_func(df_high, m)
  for ind in range(len(df)):
    arr = np.array(df[ind].index)
    arr1 = arr - ind
    #list1 = str(arr1)
    ind_list.append(arr1)
  return ind_list

df_sorted_ind = sort_index()

def index_finder(x):
  for i in range(len(x)):
    if x[i] == 5:
      return i
def index_deleter(x):
  arr = []
  for z in x:
    if z != 5:
      arr.append(z)
  return arr 

def bin_maker(y):
  if y <= 2:
    return 0
  else:
    return 1
clean_df = pd.DataFrame({"Sorted":df_sorted_ind})
clean_df["target"] = clean_df["Sorted"].apply(index_finder)
clean_df["target"] = clean_df["target"].apply(bin_maker)
clean_df["Sorted"] = clean_df["Sorted"].apply(index_deleter)

clean_df["Sprice0"] = clean_df.Sorted.apply(lambda col: col[0])
clean_df["Sprice1"] = clean_df.Sorted.apply(lambda col: col[1])
clean_df["Sprice2"] = clean_df.Sorted.apply(lambda col: col[2])
clean_df["Sprice3"] = clean_df.Sorted.apply(lambda col: col[3])
clean_df["Sprice4"] = clean_df.Sorted.apply(lambda col: col[4])

clean_df.target.value_counts(normalize=True)


def train_test(n, df=clean_df, test_size=10):
  X_train = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[:244-test_size+n]
  y_train = clean_df["target"].iloc[:244-test_size+n]
  X_test = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[244-test_size+n:245-test_size+n]
  y_test = clean_df["target"].iloc[244-test_size:245]
  return [X_train, y_train, X_test, y_test]