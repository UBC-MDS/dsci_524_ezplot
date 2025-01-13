import matplotlib.pyplot as plt
import pandas as pd

def plot_line(df, x, y, title, xlabel, ylabel, x_decimals=None, y_decimals=None):
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
    x_decimals : int, optional
        Number of decimal places for x-axis values (default: None)
    y_decimals : int, optional
        Number of decimal places for y-axis values (default: None)

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
    >>> fig, ax = plot_line(df, 'year', 'sales', 'Annual Sales', 'Year', 'Sales',
    ...                     x_decimals=0, y_decimals=2)
    """
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])

    # Format x-axis decimals
    if x_decimals is not None:
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.{x_decimals}f}'))
    
    # Format y-axis decimals
    if y_decimals is not None:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, p: f'{y:.{y_decimals}f}'))

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    ax.grid(True, linestyle='--', alpha=0.3)
    return fig, ax