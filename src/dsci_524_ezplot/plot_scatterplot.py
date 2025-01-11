
def create_scatter_plot(data, x, y, color=None, title=None):
    """
    Create a scatter plot from the provided dataset.

    Parameters:
    ----------
    data : pandas.DataFrame
        The dataset containing the variables to plot.
    x : str
        The name of the column to use for the x-axis values.
    y : str
        The name of the column to use for the y-axis values.
    color : str, optional
        The name of the column to use for color-coding the points (default is None).
    title : str, optional
        The title of the scatter plot (default is None).

    Returns:
    -------
    matplotlib.figure.Figure
        A Matplotlib figure object containing the scatter plot.

    Example:
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    >>>     'height': [150, 160, 165, 170],
    >>>     'weight': [50, 60, 65, 70],
    >>>     'gender': ['male', 'female', 'female', 'male']
    >>> })
    >>> scatter_plot, ax = create_scatter_plot(df, x='height', y='weight', color='gender', title='Height vs. Weight')
    """
    pass
