# Jupytext

https://github.com/mwouts/jupytext について

## Usage

## 新規 Notebook 作成

- `.ipynb` ファイルを作成する。
- Jupyterlab のコマンドパレットを開き(Cmd + shift + C)、「Pair Notebook with percent Script」にチェックを入れる
- `.ipynb` をセーブする
- 上記を実行すると `.py` ファイルが生成される

出力される `py` ファイルのサンプル

```python
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Try jupytext(v3)

# %% [markdown]
# ## 準備

# %%
from matplotlib import pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks")

# %matplotlib inline

# %% [markdown]
# ## グラフ

# %%
df = sns.load_dataset("anscombe")

# %%
df.head()

# %%
df.tail()

# %%
sns.lmplot(
    x="x",
    y="y",
    col="dataset",
    hue="dataset",
    data=df,
    col_wrap=2,
    ci=None,
    palette="muted",
    height=4,
    scatter_kws={"s": 50, "alpha": 1}
)

```

### 既存コード編集

- Jupyterlab を開き、対象の `.py` ファイルを右クリックして「Open With Notebook」を選択する
- `.py` ファイルを編集すると `.ipynb` ファイルも同様に変更される

※ テキストエディタで `.py` ファイルを編集した後に Jupyter lab で `.ipynb` ファイルを編集しようとすると
warning が表示され、そこで revert を選択すると `.py` ファイルの変更が反映される。
そうすると全ての出力が消えてしまう。

## 参考

https://towardsdatascience.com/jupyter-notebooks-in-the-ide-visual-studio-code-versus-pycharm-5e72218eb3e8
