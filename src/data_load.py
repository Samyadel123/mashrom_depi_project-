from ucimlrepo import fetch_ucirepo


def load_data():
    """Load the secondary mushroom dataset.

    Returns
    -------
    X : pandas.DataFrame
        Features.
    y : pandas.Series
        Target.
    """
    # fetch dataset
    secondary_mushroom = fetch_ucirepo(id=848)

    # data (as pandas dataframes)
    X = secondary_mushroom.data.features
    y = secondary_mushroom.data.targets  # Convert to Series if single column

    return X, y
