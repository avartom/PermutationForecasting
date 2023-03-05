import numpy as np
import pandas as pd
class PermutationForecaster(object):
  """A class to preprocess time series data for prediction.
    Attributes
    ----------
    series: pd.Series
        Series representing time series data

    Methods
    ----------
    getIndex(int n)

    validArray(window_size=5)

    sorter(window_size=5)

    indexer(window_size=5)

    targetFinder(window_size=5)

    targetDeleter(window_size=5)

    bin_maker(window_size=5, threshold=3)

  """
  def __init__(self, ser):
    self.series = pd.Series(ser)
    """
    Constructs the attributes to represent a time series.
    
    parameters
    ----------
    series: pd.Series
    """
  def getIndex(self, n):
    """
        Selects the element of the series corresponding to index n,
        if n is less than the length of the series. Otherwise, the user
        is prompted that the index n is greater than the length of the
        series.

        parameters
        ----------
        n: int

        Returns
        -------
        The element of the series corresponding to the index n.
        """
    len_ser = len(self.series)
    if n < len_ser and n >= 0:
      return self.series[n]
    else:
      print("The index exceeds the length of the series")
  def validSeries(self, window_size=5):
    """
            Determines whether a time series data is valid
            to apply other methods.

            parameters
            ----------
            window_size: int

            Returns
            -------
            Boolean: if the window size is within valid bounds. Else it prompts the user
                      is prompted to select window size within valid bounds.
            """
    if window_size > 0:
      return len(self.series) >= 10 * window_size
    else:
      print("Invalid window size. Select a window size < len(series)/10")
  def sorter(self, window_size=5):
    """
                Breaks the series into series of window size
                and sorts the arrays of the input window size
                before returning a nested series.

                parameters
                ----------
                window_size: int

                Returns
                -------
                Series: A series of sorted arrays of the input window size
                """
    sorted_list = []
    length_arr = len(self.series)
    if self.validSeries(window_size):
      for index in range(length_arr - window_size):
        b = self.series[index:index + window_size].sort_values()
        sorted_list.append(b)
    return pd.Series(sorted_list)

  def indexer(self, window_size=5):
    """         Selects the indices of the sorted series for
              further processing.


              parameters
              ----------
              window_size: int

              Returns
              -------
              list: A list of indices of the sorted nested series
                """
    ind_list = []
    series = self.sorter(window_size)
    for ind in range(len(series)):
      arr = np.array(series[ind].index)
      arr1 = arr - ind
      ind_list.append(arr1)
    return ind_list

  def targetFinder(self, window_size=5):
    """
                Finds the index of the target variable, which is by default window_size-1

                parameters
                ----------
                window_size: int

                Returns
                -------
                Series: A pd.Series of the index of each nested target variable
                """
    target_list = []
    target = window_size - 1
    index_array = self.indexer(window_size)
    for arr in index_array:
      for i in range(window_size):
        if arr[i] == target:
          target_list.append(i)
    return pd.Series(target_list)


  def targetDeleter(self, window_size=5):
    """
                Deletes the target variable from each nested series
                to return a series for training.

                parameters
                ----------
                window_size: int

                Returns
                -------
                List: A list of nested indexers with target variable deleted.
                """
    target = window_size - 1
    ind_list = self.indexer(window_size)
    ind_list1 = []
    for i in ind_list:
      i = np.delete(i, np.where(i == target))
      ind_list1.append(i)
    return ind_list1

  def bin_maker(self, window_size=5, threshold=3):
    """
                Gives a list of 1's and 0's determined by whether the
                targetFinder is above or below the threshold.

                parameters
                ----------
                window_size: int
                threshold: int

                Returns
                -------
                list: Returns 0's and 1's base on whether the result of
                the targetFinder is less than or greater than the threshold,
                respectively.
                """
    bin_lst = []
    target_ind = self.targetFinder(window_size)
    for  x in target_ind:
      if x <= threshold:
        bin_lst.append(0)
      else:
        bin_lst.append(1)
    return bin_lst
