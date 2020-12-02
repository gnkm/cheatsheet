# Jupyter Notebook

```
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
import seaborn as sns
import numpy as np
from scipy.stats import norm
from scipy import stats
import warnings


warnings.filterwarnings('ignore')
pd.set_option('display.float_format', lambda x: '{:20,.2f}'.format(x))
sns.set(style='darkgrid', font=['IPAexGothic'])
%matplotlib inline
```
