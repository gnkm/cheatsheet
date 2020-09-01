# Data Science Cheat Sheet

## Datetime

```
df['date'] = df['datetime'].dt.date
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['day'] = df['datetime'].dt.day
df['day_of_week'] = df['datetime'].dt.dow
```

## Preprocessing

```
train = pd.read_csv('../input/train.csv')
test = pd.read_csv('../input/test.csv')

# Now drop the  'Id' colum since it's unnecessary for  the prediction process.
train.drop("Id", axis = 1, inplace = True)
test.drop("Id", axis = 1, inplace = True)

ntrain = train.shape[0]
ntest = test.shape[0]
y_train = train['target_var'].values
all_data = pd.concat((train, test)).reset_index(drop=True)
all_data.drop(['target_var'], axis=1, inplace=True)

# Preprocessing
all_data['feature'] = all_data.apply(preprocessor, axis='columns')

train = all_data[:ntrain]
test = all_data[ntrain:]
```
