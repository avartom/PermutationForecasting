import numpy as np
import pandas as pd
class PermutationForecaster(object):
  def __init__(self, ser):
    self.series = pd.Series(ser)
  def getIndex(self, n):
    len_ser = len(self.series)
    if n <= len_ser:
      return self.series[n]
    else:
      print("The index exceeds the length of the series")
  def validArray(self, window_size=5):
    return len(self.series) >= 10 * window_size
  def sorter(self, window_size=5):
    sorted_list = []
    length_arr = len(self.series)
    if self.validArray(window_size):
      for index in range(length_arr - window_size):
        b = self.series[index:index + window_size].sort_values()
        sorted_list.append(b)
    return pd.Series(sorted_list)
  # def invIndex(self, a):
  #   return np.where(self.arr == a)
  def indexer(self, window_size=5):
    ind_list = []
    series = self.sorter(window_size)
    for ind in range(len(series)):
      arr = np.array(series[ind].index)
      arr1 = arr - ind
      ind_list.append(arr1)
    return ind_list
  # def indexer(self, window_size=5):
  #   ind_list = []
  #   arr = self.sorter(window_size)  #gives an array of sorted arrays of length window size
  #   length_arr = len(arr)
  #   for ind in range(length_arr):
  #     ar = np.where(arr[ind] > 0)
  #     #ind1 = np.array([ind]*window_size)
  #     #arr1 = ar - ind1
  #     ind_list.append(ar)
  #   return ind_list
  def targetFinder(self, window_size=5):
    target_list = []
    target = window_size - 1
    index_array = self.indexer(window_size)
    #length_arr = len(index_array)
    for arr in index_array:
      for i in range(window_size):
        if arr[i] == target:
          target_list.append(i)
    return pd.Series(target_list)


  def targetDeleter(self, window_size=5):
    target = window_size - 1
    ind_list = self.indexer(window_size)
    ind_list1 = []
    for i in ind_list:
      i = np.delete(i, np.where(i == target))
      ind_list1.append(i)
    return ind_list1

  def bin_maker(self, window_size=5, threshold=3):
    bin_lst = []
    target_ind = self.targetFinder(window_size)
    for  x in target_ind:
      if x <= threshold:
        bin_lst.append(0)
      else:
        bin_lst.append(1)
    return bin_lst

# clean_df = pd.DataFrame({"Sorted":df_sorted_ind})
# clean_df["target"] = clean_df["Sorted"].apply(index_finder)
# clean_df["target"] = clean_df["target"].apply(bin_maker)
# clean_df["Sorted"] = clean_df["Sorted"].apply(index_deleter)
#
# clean_df["Sprice0"] = clean_df.Sorted.apply(lambda col: col[0])
# clean_df["Sprice1"] = clean_df.Sorted.apply(lambda col: col[1])
# clean_df["Sprice2"] = clean_df.Sorted.apply(lambda col: col[2])
# clean_df["Sprice3"] = clean_df.Sorted.apply(lambda col: col[3])
# clean_df["Sprice4"] = clean_df.Sorted.apply(lambda col: col[4])
#
# clean_df.target.value_counts(normalize=True)
#
#
# def train_test(n, df=clean_df, test_size=10):
#   X_train = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[:244-test_size+n]
#   y_train = clean_df["target"].iloc[:244-test_size+n]
#   X_test = clean_df[['Sprice0',	'Sprice1',	'Sprice2','Sprice3', 'Sprice4']].iloc[244-test_size+n:245-test_size+n]
#   y_test = clean_df["target"].iloc[244-test_size:245]
#   return [X_train, y_train, X_test, y_test]