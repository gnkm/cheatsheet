# Jupyter Notebook

## imported packages

```
from pprint import pprint
import sys

import japanize_matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from tabulate import tabulate
import warnings
```

## settings

```
warnings.filterwarnings('ignore')
pd.set_option('display.precision', 2)
pd.set_option('display.max_columns', 60)
sns.set(
    font=['IPAexGothic'],
    style='darkgrid',
)

# `df.describe(percentiles=my_percentiles)` のように使う。
# default は `[.25, .5, .75]`.
percentiles_05 = [i / 100 for i in range(0, 100 + 5, 5)]
percentiles_10 = [i / 100 for i in range(0, 100 + 10, 10)]

%matplotlib inline
```
