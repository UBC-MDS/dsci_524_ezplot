import matplotlib.pyplot as plt
import pandas as pd

def plot_line(df, x, y, title=None, xlabel=None, ylabel=None, x_decimals=None, y_decimals=None):
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
    title : str, optional
        Title of the plot (default: None)
    xlabel : str, optional
        Label for x-axis (default: x column name)
    ylabel : str, optional
        Label for y-axis (default: y column name)
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
    # Data validation
    if len(df) < 2:
        raise ValueError("At least 2 data points are required to plot a line")

    if df[x].isna().any() or df[y].isna().any():
        raise ValueError("Data contains missing values")
        
    if not (pd.api.types.is_numeric_dtype(df[x]) and pd.api.types.is_numeric_dtype(df[y])):
        raise ValueError("Both x and y must be numeric")

    if df[x].isin([float('inf'), float('-inf')]).any() or df[y].isin([float('inf'), float('-inf')]).any():
        raise ValueError("Data contains invalid values (infinity)")
        
    if (df[x] < 0).any():
        raise ValueError(f"All values in {x} must be non-negative")
        
    if (df[y] < 0).any():
        raise ValueError(f"All values in {y} must be non-negative")

    # Create plot
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y])
    
    # Set labels and title
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    
    # Set decimal formatting
    if x_decimals is not None:
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.{x_decimals}f}"))
    if y_decimals is not None:
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.{y_decimals}f}"))
    
    return fig, ax