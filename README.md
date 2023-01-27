# Permutation Forecasting

    Given a time series data, we forecast using permutations. More specifically, we take a window of size $n$, and then sort the values from $0$ to $n-1$ in ascending order. In other words, if $\{ X_{n} \}$ is a time series we take a window of size $n$ then  $(X_0, X_1, \cdots X_{n-1})$ and consider it as a permutation of the of the set  $S_{n}$ which is  set $\{0,1,2 \dots n-1\}$. But this amounts to a bijective function $\sigma : S_{n} \to S_{n}$ where $S_{n}$ is the set $(0,1,2 \dots n-1)$. For example, if $(X_{0}=5, X_{1}=1, X_{2}=10)$ then after sorting the above time series with window of size $n=3$ becomes $(X_{1},X_{0},X_{2})$. Therefore, $\sigma: (0,1,2)\to (1,0,2)$. Now, if we take $X_{2}$ to be the future value we are trying to  predict based on the previous two values of the time series, then  we see that $X_{0}$ and $X_{1}$ become the training set and $X_{2}$ is the target variable in our prediction. In this case, there are $3$ cases for $X_{2}$ can take i.e. $X_{2}$ is the lowest, middle, or the greatest of the three positions in our window of size $n=3$. And this is what we are going to predict. As in the above example, $X_{2}$ is greatest of all the three random variables. And in this case, $X_{0}$ is a lower bound for the predicted random variable $X_{2}$. It is not hard to imagine if $X_{2}$ was the lowest of the three random variables then whichever variable came after $X_{0}$ would be the upper bound for our predicted $X_{2}$. Our algorithm traverses through the time series data with window size of $n$ and looks for the index of the target random variable $X_{n-1}$ (in this case it is $2$ starting from $0$) and either gives an upper bound or a lower bound for the target variable. We can turn the target variable into a binary random variable by stipulating $X_{n-1}$ to be $0$, if $X_{n-1} < t$ and $X_{n-1}$ to be $1$, if $X_{n-1} < t$ where $t\in { 0,1,2\dots,n-1 }$ again where $n$ is the window size. 
