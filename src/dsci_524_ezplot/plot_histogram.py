import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(df, column=None, bins=10, title=None, xlabel=None, ylabel=None, color=None):
    """
    Create a histogram for numeric data or a bar plot for categorical data
    from a pandas DataFrame or a NumPy array.

    Parameters
    ----------
    df : pandas.DataFrame or numpy.ndarray
        Input data containing the values to plot.
    column : str or None, optional
        Column name for the values to plot in the histogram/bar plot (only applicable for DataFrame).
        If None, all columns will be used (only for DataFrame input with numeric data).
    bins : int, optional
        Number of bins for the histogram. Default is 10 (ignored for categorical data).
    title : str, optional
        Title of the plot. If None, no title is added.
    xlabel : str, optional
        Label for the x-axis. If None, no label is added.
    ylabel : str, optional
        Label for the y-axis. If None, no label is added.
    color : str or list, optional
        Color for the bars in the plot. Default is None (Matplotlib default colors are used).

    Returns
    -------
    tuple
        - matplotlib.figure.Figure
            The figure object containing the plot.
        - matplotlib.axes.Axes
            The axes object containing the plot elements.

    Raises
    ------
    TypeError
        If input data is not a DataFrame or a NumPy array.
    ValueError
        If the data is empty or contains all NaN values.
        If `bins` is not a positive integer.
    """

    # Validate input type
    if not isinstance(df, (pd.DataFrame, np.ndarray)):
        raise TypeError("Input data must be a pandas DataFrame or a NumPy array.")

    # Handle empty data
    if isinstance(df, pd.DataFrame) and df.empty:
        raise ValueError("DataFrame must not be empty.")
    if isinstance(df, np.ndarray) and df.size == 0:
        raise ValueError("NumPy array must not be empty.")
    
    # Validate bins
    if not isinstance(bins, int) or bins <= 0:
        raise ValueError("`bins` must be a positive integer.")

    # If the input is a DataFrame and remove NaN values
    if isinstance(df, pd.DataFrame):
        if column is None:
            data = df.select_dtypes(include=[np.number]).values.flatten()
            if data.size == 0:
                raise ValueError("No numeric columns found in the DataFrame.")
        else:
            if column not in df.columns:
                raise ValueError(f"Column '{column}' not found in the DataFrame.")
            data = df[column].dropna()
    else:
        data = df.flatten()
        data = data[~np.isnan(data)]

    # Check if the data is categorical
    if isinstance(data.dtype, pd.CategoricalDtype) or isinstance(data[0], (str, bool)):
        # Create a bar plot for categorical data
        unique_values, counts = np.unique(data, return_counts=True)
        fig, ax = plt.subplots()
        ax.bar(unique_values, counts, color=color or 'skyblue', edgecolor='black')
    else:
        # Create a histogram for numeric data
        fig, ax = plt.subplots()
        ax.hist(data, bins=bins, edgecolor='black', color=color or 'skyblue')
    if title:
        ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)

    return fig, ax
