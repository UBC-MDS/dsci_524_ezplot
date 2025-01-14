import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_heatmap(df, title, cmap="viridis", xlabel=None, ylabel=None):
    """
    Create a heatmap using data from a pandas DataFrame or a 2D array.

    Parameters
    ----------
    df : pandas.DataFrame or numpy.ndarray
        Input data for the heatmap. Can be a pandas DataFrame or a 2D NumPy array.
        The data should be numeric, as non-numeric values will cause errors.
    title : str
        Title of the heatmap.
    cmap : str, optional
        Colormap for the heatmap. Defaults to 'viridis'.
    xlabel : str, optional
        Label for the x-axis. Defaults to None.
    ylabel : str, optional
        Label for the y-axis. Defaults to None.

    Returns
    -------
    tuple
        - matplotlib.figure.Figure
            The figure object containing the heatmap.
        - matplotlib.axes.Axes
            The axes object containing the heatmap elements.

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
    >>> fig, ax = plot_heatmap(df, title="Sample Heatmap", xlabel="Columns", ylabel="Rows")
    """
    # Validate input type
    if not isinstance(df, (pd.DataFrame, np.ndarray)):
        raise TypeError("Input data must be a pandas DataFrame or a numpy array.")
    
    # Handle empty data
    if isinstance(df, pd.DataFrame) and df.empty:
        raise ValueError("DataFrame must not be empty.")
    if isinstance(df, np.ndarray) and df.size == 0:
        raise ValueError("NumPy array must not be empty.")
    
    # Handle NaN values
    if isinstance(df, pd.DataFrame) and df.isnull().values.any():
        df = df.fillna(0)

    # Plot the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(df, cmap=cmap, ax=ax)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    
    return fig, ax