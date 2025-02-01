
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_scatterplot(df, x, y, color=None, title=None, xlabel=None, ylabel=None):
    """
    Create a scatter plot from the provided dataset or Array.

    Parameters
    ----------
    df : pandas.DataFrame or numpy.ndarray
        The dataset containing the variables to plot. Must be a pandas DataFrame 
        or a NumPy array. 
    x : str
        The name of the column to use for the x-axis values.
    y : str
        The name of the column to use for the y-axis values.
    color : str, optional
        The name of the column to use for color-coding the points. If the column 
        is categorical, colors will be mapped to unique categories (default is None).
    title : str, optional
        The title of the scatter plot (default is None).
    xlabel : str, optional
        The label for the x-axis (default is None).
    ylabel : str, optional
        The label for the y-axis (default is None).

    Returns
    -------
    matplotlib.figure.Figure, matplotlib.axes.Axes
        A Matplotlib figure and axes object containing the scatter plot.

    Raises
    ------
    TypeError
        If the input data is not a pandas DataFrame or NumPy array.
        If the `x` or `y` column contains non-numeric or mixed data types.
    ValueError
        If the DataFrame or NumPy array is empty.

    Example
    -------
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'height': [150, 160, 165, 170],
    ...     'weight': [50, 60, 65, 70],
    ...     'category': ['small', 'medium', 'medium', 'large']
    ... })
    >>> fig, ax = plot_scatterplot(df, x='height', y='weight', color='category', 
    ...                            title='Height vs. Weight', 
    ...                            xlabel='Height (cm)', ylabel='Weight (kg)')
    """
    
    # Validate input data type
    if not isinstance(df, (pd.DataFrame, np.ndarray)):
        raise TypeError("Input data must be a pandas DataFrame or a NumPy array.")
    
    # Handle empty dataframe gracefully
    if isinstance(df, pd.DataFrame) and df.empty:
        raise ValueError("DataFrame must not be empty.")
    if isinstance(df, np.ndarray) and df.size == 0:
        raise ValueError("NumPy array must not be empty.")
    
    # Handle NaN values by filling with zeros
    if isinstance(df, pd.DataFrame) and df.isnull().values.any():
        df = df.fillna(0)
        
    # x and y columns contain numeric data only, cannot be mixed
    try:
        pd.to_numeric(df[x])
    except ValueError:
        raise TypeError(f"Column '{x}' contains non-numeric data.")
    try:
        pd.to_numeric(df[y])
    except ValueError:
        raise TypeError(f"Column '{y}' contains non-numeric data.")
        
    # Create scatterplot with matplotlib
    fig, ax = plt.subplots()

    if color is not None:
        # Check if the color column is categorical or continuous
        if isinstance(df[color].dtype, pd.CategoricalDtype) or df[color].dtype == object:
            # Create the scatter plot with categorical color
            categories = pd.Categorical(df[color])
            scatter = ax.scatter(df[x], df[y], c=categories.codes, cmap='viridis')
            ax.legend(handles=scatter.legend_elements()[0], labels=list(categories.categories), title=color)
        else:
            scatter = ax.scatter(df[x], df[y], c=df[color], cmap='viridis')
    else:
        scatter = ax.scatter(df[x], df[y])

    ax.set_title(title or '')
    ax.set_xlabel(xlabel or '')
    ax.set_ylabel(ylabel or '')

    return fig, ax
