import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dsci_524_ezplot.plot_heatmap import plot_heatmap

# Fixture to provide a reproducible random number generator
@pytest.fixture
def rng():
    """
    Fixture to generate a reproducible random number generator.
    Ensures consistency across test runs by using a fixed seed.
    """
    return np.random.default_rng(19680801)

# Test for Missing Title
def test_plot_heatmap_no_title(rng):
    """
    Test if plot_heatmap works when no title is provided.
    The plot should render successfully with an empty title.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate random data
    fig, ax = plot_heatmap(df)  # Generate heatmap without a title
    assert ax.get_title() == "", "The default title should be empty when not provided."
    plt.close(fig)  # Clean up the figure

# Test for Non-Numeric Data
def test_plot_heatmap_non_numeric_data():
    """
    Test if plot_heatmap raises a TypeError for non-numeric data.
    Ensures only numeric data is accepted as input.
    """
    data = pd.DataFrame({
        "A": [1, 2, 3],
        "B": ["a", "b", "c"]  # Non-numeric column
    })
    with pytest.raises(TypeError, match="All columns in the DataFrame must contain numeric data."):
        plot_heatmap(data)

# Test for Mixed Data Types
def test_plot_heatmap_mixed_data_types():
    """
    Test if plot_heatmap raises a TypeError for mixed data types in the DataFrame.
    Ensures that inconsistent data is rejected.
    """
    data = pd.DataFrame({
        "A": [1, 2, "a"],  # Mixed data types
        "B": [4, 5, 6]
    })
    with pytest.raises(TypeError, match="All columns in the DataFrame must contain numeric data."):
        plot_heatmap(data)

# Test for Missing Labels
def test_plot_heatmap_no_labels(rng):
    """
    Test if plot_heatmap works when no axis labels are provided.
    The plot should render successfully with empty axis labels.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate random data
    fig, ax = plot_heatmap(df, title="No Labels Test")  # Generate heatmap without labels
    assert ax.get_xlabel() == "", "The default x-axis label should be empty."
    assert ax.get_ylabel() == "", "The default y-axis label should be empty."
    plt.close(fig)  # Clean up the figure

# Test for Empty DataFrame
def test_plot_heatmap_empty_dataframe():
    """
    Test if plot_heatmap raises a ValueError for an empty DataFrame.
    Ensures that the function rejects empty input data.
    """
    df = pd.DataFrame()  # Empty DataFrame
    with pytest.raises(ValueError, match="DataFrame must not be empty."):
        plot_heatmap(df)

# Test for Empty NumPy Array
def test_plot_heatmap_empty_array():
    """
    Test if plot_heatmap raises a ValueError for an empty NumPy array.
    Ensures that the function rejects empty input data.
    """
    arr = np.array([])  # Empty array
    with pytest.raises(ValueError, match="NumPy array must not be empty."):
        plot_heatmap(arr)

# Test for DataFrame Without Columns
def test_plot_heatmap_no_column_names():
    """
    Test if plot_heatmap works for a DataFrame without column names.
    Ensures that the function can handle unnamed columns gracefully.
    """
    df = pd.DataFrame([[1, 2], [3, 4]])  # DataFrame without column names
    fig, ax = plot_heatmap(df, title="No Column Names Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render even without column names."
    plt.close(fig)  # Clean up the figure

# Test for Single Cell DataFrame
def test_plot_heatmap_single_cell():
    """
    Test if plot_heatmap works for a single-cell DataFrame.
    Ensures that the function can handle minimal input data.
    """
    df = pd.DataFrame([[42]])  # Single-cell DataFrame
    fig, ax = plot_heatmap(df, title="Single Cell Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render for a single-cell DataFrame."
    plt.close(fig)  # Clean up the figure

# Test for NaN Values
def test_plot_heatmap_nan_values(rng):
    """
    Test if plot_heatmap handles NaN values by filling them with 0.
    Ensures that the function can handle missing values gracefully.
    """
    df = pd.DataFrame(rng.random((5, 5)))
    df.iloc[0, 0] = np.nan  # Introduce NaN
    fig, ax = plot_heatmap(df, title="NaN Values Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render even with NaN values."
    plt.close(fig)  # Clean up the figure

# Test for NumPy Array Input
def test_plot_heatmap_numpy_array(rng):
    """
    Test if plot_heatmap works with a NumPy array as input.
    Ensures that both DataFrames and NumPy arrays are supported.
    """
    arr = rng.random((5, 5))  # Generate random array
    fig, ax = plot_heatmap(arr, title="NumPy Array Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render for a NumPy array."
    plt.close(fig)  # Clean up the figure

# Test for Invalid Input Type
def test_plot_heatmap_invalid_input():
    """
    Test if plot_heatmap raises a TypeError for invalid input types.
    Ensures that only DataFrames and NumPy arrays are accepted.
    """
    data = {"A": [1, 2, 3], "B": [4, 5, 6]}  # Dictionary input
    with pytest.raises(TypeError, match="Input data must be a pandas DataFrame or a numpy array."):
        plot_heatmap(data)

# Test for Completely NaN DataFrame
def test_plot_heatmap_all_nan_dataframe():
    """
    Test if plot_heatmap replaces all NaN values with 0 in a DataFrame.
    Ensures that a completely NaN DataFrame can be rendered.
    """
    df = pd.DataFrame(np.nan, index=range(5), columns=range(5))  # All-NaN DataFrame
    fig, ax = plot_heatmap(df, title="All-NaN DataFrame Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render even if the DataFrame contains all NaN values."
    plt.close(fig)  # Clean up the figure

# Test for Custom Colormap
def test_plot_heatmap_custom_colormap(rng):
    """
    Test if plot_heatmap renders correctly with a custom colormap.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate random data
    fig, ax = plot_heatmap(df, cmap="coolwarm", title="Custom Colormap Test")  # Use a custom colormap
    assert fig is not None, "The heatmap should render with a custom colormap."
    plt.close(fig)  # Clean up the figure

# Test for Custom Axis Labels
def test_plot_heatmap_custom_labels(rng):
    """
    Test if plot_heatmap applies custom x-label and y-label correctly.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate random data
    fig, ax = plot_heatmap(df, xlabel="Custom X", ylabel="Custom Y", title="Custom Labels Test")
    assert ax.get_xlabel() == "Custom X", "The x-axis label should match the input."
    assert ax.get_ylabel() == "Custom Y", "The y-axis label should match the input."
    plt.close(fig)  # Clean up the figure

# Test for Valid NumPy Array Input
def test_plot_heatmap_valid_numpy_array():
    """
    Test if plot_heatmap works with a valid NumPy array.
    Ensures that numeric NumPy arrays are accepted as input.
    """
    arr = np.random.rand(5, 5)  # Generate a random numeric NumPy array
    fig, ax = plot_heatmap(arr, title="Valid NumPy Array Test")  # Generate heatmap
    assert fig is not None, "The heatmap should render for a valid NumPy array."
    plt.close(fig)  # Clean up the figure

# Test for Non-Numeric NumPy Array
def test_plot_heatmap_invalid_numpy_array():
    """
    Test if plot_heatmap raises a TypeError for non-numeric NumPy arrays.
    Ensures that only numeric data is accepted in NumPy arrays.
    """
    arr = np.array([["a", "b"], ["c", "d"]])  # Non-numeric NumPy array
    with pytest.raises(TypeError, match="NumPy array must contain numeric data."):
        plot_heatmap(arr)
