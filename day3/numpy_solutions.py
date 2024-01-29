import numpy as np
# Solutions to: https://gist.github.com/ynonp/06914f626cd4127899af53a96733157f#file-11_numpy-md

# 1:
np.arange(2, 202, 2)

# 2:
np.arange(1, 11).reshape(10, 1) * np.arange(1, 11)

# 3:
a = np.arange(1, 11).reshape(10, 1) * np.arange(1, 11)
np.diag(a)

# 4:
a = np.random.randint(100, size=10)
a[a % 2 == 1]

# 5:
np.where(a % 2 == 1, a, 0)

# 6:
a = np.random.randint(1, 100, size=10)
np.min(a[a > 50])

# 7:
np.sort(np.unique(a))[-5:]

