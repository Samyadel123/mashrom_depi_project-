from ucimlrepo import fetch_ucirepo

# fetch dataset
secondary_mushroom = fetch_ucirepo(id=848)

# data (as pandas dataframes)
X = secondary_mushroom.data.features
y = secondary_mushroom.data.targets

# log data as csv files
X.to_csv('data/secondary_mushroom_features.csv', index=False)
y.to_csv('data/secondary_mushroom_targets.csv', index=False)
