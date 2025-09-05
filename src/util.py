def drop(null_data:pd.Series, percentage:float,names)->list[str]:
    """
    Args:
        null_data : series of percentages of null values in the data
        percentage : allowed percentage in data
    output:   
        list of boolean -> tells you if this feature is with us or not (true = out)
    """
    return [names[i] for i in range(len(null_data)) if null_data[i]>percentage]
