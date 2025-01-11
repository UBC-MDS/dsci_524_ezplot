def plot_histogram(df, column, bins, title, xlabel, ylabel):
    """
    Create a histogram using data from a pandas DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing the data to plot
    column : str
        Column name for the values to plot in the histogram
    bins : int
        Number of bins for the histogram
    title : str
        Title of the plot
    xlabel : str
        Label for x-axis
    ylabel : str
        Label for y-axis

    Returns
    -------
    tuple
        - matplotlib.figure.Figure
            The figure object containing the plot
        - matplotlib.axes.Axes
            The axes object containing the plot elements

    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'age': [25, 30, 35, 40, 45, 30, 25]})
    >>> fig, ax = plot_histogram(df, 'age', bins=5, title='Age Distribution', xlabel='Age', ylabel='Frequency')
    """
