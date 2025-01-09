def plot_line(df, x, y, title, xlabel, ylabel):
    """
    Create a line plot using data from a pandas DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame containing the data to plot
    x : str
        Column name for x-axis values
    y : str
        Column name for y-axis values
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
    >>> df = pd.DataFrame({'year': [2020, 2021, 2022], 'sales': [100, 150, 200]})
    >>> fig, ax = plot_line(df, 'year', 'sales', 'Annual Sales', 'Year', 'Sales ($)')
    """
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax