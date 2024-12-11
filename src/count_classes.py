def count_classes(data_frame, class_col):
    """
    Count class observations in a pandas DataFrame.

    Creates a new DataFrame with two columns, listing the classes present
    in the input DataFrame and the number of observations for each class.

    Parameters:
    ----------
    data_frame : pandas.DataFrame
        The input DataFrame containing the data to analyze.
    class_col : str
        The name of the column in the DataFrame containing class labels.

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with two columns:
        - 'class': Lists the unique classes found in the input DataFrame.
        - 'count': Lists the number of observations for each class in the input DataFrame.
        
    Examples:
    --------
    >>> import pandas as pd
    >>> data = pd.read_csv('mtcars.csv')  # Replace 'mtcars.csv' with your dataset file
    >>> result = count_classes(data, 'am')
    >>> print(result)
    
    Notes:
    -----
    This function uses the pandas library to perform grouping and counting
    of class observations in the input DataFrame.

    """
