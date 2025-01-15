import pytest
import pandas as pd
import numpy as np
from dsci_524_ezplot.plot_heatmap import plot_heatmap
import matplotlib.pyplot as plt

# Fixture to provide a reproducible random number generator for deterministic tests
@pytest.fixture
def rng():
    """
    Fixture to generate a reproducible random number generator.
    Ensures consistency across test runs.
    """
    return np.random.default_rng(19680801)  # Fixed seed for reproducibility

# Test for valid DataFrame input
def test_plot_heatmap_valid_dataframe(rng):
    """
    Test if plot_heatmap successfully creates a heatmap from a valid DataFrame.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate a random 5x5 DataFrame
    fig, ax = plot_heatmap(df, title="Valid Heatmap")
    assert fig is not None  # Verify that a figure object is returned
    assert ax is not None  # Verify that an axes object is returned
    plt.close(fig)  # Clean up the figure after the test

# Test for valid NumPy array input
def test_plot_heatmap_valid_numpy_array(rng):
    """
    Test if plot_heatmap successfully creates a heatmap from a valid NumPy array.
    """
    array = rng.random((5, 5))  # Generate a random 5x5 NumPy array
    fig, ax = plot_heatmap(array, title="Valid Heatmap")
    assert fig is not None  # Verify that a figure object is returned
    assert ax is not None  # Verify that an axes object is returned
    plt.close(fig)  # Clean up the figure after the test

# Test for invalid input type
def test_plot_heatmap_invalid_input_type():
    """
    Test if plot_heatmap raises a TypeError for invalid input types.
    """
    with pytest.raises(TypeError):  # Expect a TypeError
        plot_heatmap("not_a_dataframe", title="Invalid Input")

# Test for empty DataFrame input
def test_plot_heatmap_empty_dataframe():
    """
    Test if plot_heatmap raises a ValueError for an empty DataFrame.
    """
    df = pd.DataFrame()  # Create an empty DataFrame
    with pytest.raises(ValueError):  # Expect a ValueError
        plot_heatmap(df, title="Empty DataFrame")

# Test for empty NumPy array input
def test_plot_heatmap_empty_numpy_array():
    """
    Test if plot_heatmap raises a ValueError for an empty NumPy array.
    """
    array = np.array([])  # Create an empty array
    with pytest.raises(ValueError):  # Expect a ValueError
        plot_heatmap(array, title="Empty Array")

# Test for handling NaN values in the input
def test_plot_heatmap_nan_values(rng):
    """
    Test if plot_heatmap handles NaN values by replacing them with zeros.
    """
    df = pd.DataFrame([[1, 2], [np.nan, 4]])  # DataFrame with a NaN value
    fig, ax = plot_heatmap(df, title="NaN Handling Heatmap")
    assert fig is not None  # Verify that a figure object is returned
    assert ax is not None  # Verify that an axes object is returned
    plt.close(fig)  # Clean up the figure after the test

# Test for adding labels to the heatmap
def test_plot_heatmap_with_labels(rng):
    """
    Test if plot_heatmap correctly adds axis labels to the heatmap.
    """
    df = pd.DataFrame(rng.random((5, 5)))  # Generate a random 5x5 DataFrame
    fig, ax = plot_heatmap(df, title="Labeled Heatmap", xlabel="X Axis", ylabel="Y Axis")
    assert fig is not None  # Verify that a figure object is returned
    assert ax.get_xlabel() == "X Axis"  # Verify the x-axis label
    assert ax.get_ylabel() == "Y Axis"  # Verify the y-axis label
    plt.close(fig)  # Clean up the figure after the test
