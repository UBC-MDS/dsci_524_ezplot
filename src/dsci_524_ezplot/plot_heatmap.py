import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_heatmap(data, title=None, cmap="viridis", xlabel=None, ylabel=None):
    """
    Create a heatmap using a pandas DataFrame or a 2D NumPy array.

    Parameters
    ----------
    data : pandas.DataFrame or numpy.ndarray
        Input data for the heatmap. Can be a pandas DataFrame or a 2D NumPy array.
        The data should be numeric; non-numeric values will cause errors.
    title : str, optional
        Title of the heatmap. Default is None.
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

    Raises
    ------
    TypeError
        If the input data is not a pandas DataFrame or a NumPy array.
    ValueError
        If the input data is empty or contains non-numeric values.

    Examples
    --------
    Using a pandas DataFrame:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame(np.random.rand(5, 5), columns=['A', 'B', 'C', 'D', 'E'])
    >>> fig, ax = plot_heatmap(df, title="Sample Heatmap", xlabel="Columns", ylabel="Rows")

    Using a NumPy array:
    >>> arr = np.random.rand(5, 5)
    >>> fig, ax = plot_heatmap(arr, title="Heatmap from NumPy array")
    """
    # Validate input type
    if not isinstance(data, (pd.DataFrame, np.ndarray)):
        raise TypeError("Input data must be a pandas DataFrame or a numpy array.")
    
    # Handle empty data
    if isinstance(data, pd.DataFrame) and data.empty:
        raise ValueError("DataFrame must not be empty.")
    if isinstance(data, np.ndarray) and data.size == 0:
        raise ValueError("NumPy array must not be empty.")
    
    # Ensure data is numeric
    if isinstance(data, pd.DataFrame):
        if not all(pd.api.types.is_numeric_dtype(dtype) for dtype in data.dtypes):
            raise TypeError("All columns in the DataFrame must contain numeric data.")
    elif isinstance(data, np.ndarray):
        if not np.issubdtype(data.dtype, np.number):
            raise TypeError("NumPy array must contain numeric data.")
    
    # Handle NaN values
    if isinstance(data, pd.DataFrame) and data.isnull().values.any():
        data = data.fillna(0)

    # Plot the heatmap
    fig, ax = plt.subplots()
    sns.heatmap(data, cmap=cmap, ax=ax)
    ax.set_title(title)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    
    return fig, ax
