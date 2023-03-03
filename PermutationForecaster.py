import pandas as pd
import numpy as np
class PermutationForecaster(pd.Series):
  def __init__(self, series, window_size):
    series = pd.Series(series)
    self.series = series
    self.window_size = window_size
    super().__init__(series)

  def ValidSeries(self):
    return len(self.series) >= 10 * self.window_size
  def Sorter(self):
    sorted_list = []
    n  = self.window_size
    length_series = len(self.series)
    if self.ValidSeries():
      for index in range(length_series - n):
        sorted = self.series[index:index+n].sort_values()
        sorted_list.append(sorted)
    return sorted_list


  def Indexer(self):
    ind_list = []
    series = self.Sorter()
    for ind in range(len(series)):
      arr = np.array(series[ind].index)
      arr1 = arr - ind
      ind_list.append(arr1)
    return ind_list
  def TargetFinder(self):
    target = self.window_size - 1
    ind = self.Indexer()
    for i in ind:
      for j in i:
        if i[j] == target:
          return j
  def TargetDeleter(self):
    target = self.window_size - 1
    ind_list = self.Indexer()
    for i in ind_list:
      i.pop(target)
    return ind_list

  def bin_maker(self, threshold):
    target_ind = TargetFinder()
    threshold = self.window_size//2
    if target_ind <= threshold:
      return 0
    else:
      return 1
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