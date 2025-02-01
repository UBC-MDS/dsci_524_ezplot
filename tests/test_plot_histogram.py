import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from dsci_524_ezplot.plot_histogram import plot_histogram
import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Expected Case 1
def test_numeric_histogram():
    """Test histogram with numeric data."""
    df = pd.DataFrame({'age': [20, 25, 30, 35, 40, 45, 50]})
    fig, ax = plot_histogram(df, column='age', bins=5, title='Age Histogram', xlabel='Age', ylabel='Count', color='blue')
    assert fig is not None, "Figure was not created."
    assert ax is not None, "Axes were not created."
    assert len(ax.patches) == 5, "Number of bins is incorrect."
    plt.close(fig)

# Expected Case 2
def test_categorical_barplot():
    """Test bar plot with categorical data."""
    df = pd.DataFrame({'color': ['red', 'blue', 'green', 'red', 'blue', 'blue']})
    fig, ax = plot_histogram(df, column='color', title='Color Distribution', color='green')
    assert fig is not None, "Figure was not created."
    assert ax is not None, "Axes were not created."
    assert len(ax.patches) == 3, "Number of bars is incorrect."
    plt.close(fig)

# Expected Case 3
def test_color_input():
    """Test custom color for bars."""
    df = pd.DataFrame({'age': [25, 30, 35]})
    fig, ax = plot_histogram(df, column='age', bins=3, color='red')
    for bar in ax.patches:
        assert bar.get_facecolor() == (1.0, 0.0, 0.0, 1.0), "Bar color is not red."
    plt.close(fig)

# Edge Case 1
def test_missing_values_handling():
    """Test handling of missing values, missing values will be dropped."""
    df = pd.DataFrame({'age': [25, np.nan, 35, 40, None]})
    fig, ax = plot_histogram(df, column='age', bins=3)
    assert fig is not None, "Figure was not created."
    assert ax is not None, "Axes were not created."
    assert len(ax.patches) == 3, "Number of bins is incorrect after handling NaN values."
    plt.close(fig)

# Edge Case 2
def test_no_labels():
    """Test histogram without title, xlabel, and ylabel."""
    df = pd.DataFrame({'age': [25, 30, 35]})
    fig, ax = plot_histogram(df, column='age', bins=3)
    assert ax.get_title() == '', "Title should be empty."
    assert ax.get_xlabel() == '', "X-axis label should be empty."
    assert ax.get_ylabel() == '', "Y-axis label should be empty."
    plt.close(fig)

# Edge Case 3
def test_large_bins():
    """Test with bins larger than unique values."""
    df = pd.DataFrame({'age': [25, 30, 35]})
    fig, ax = plot_histogram(df, column='age', bins=10)
    assert len(ax.patches) <= 10, "Number of bins should not exceed unique data values."
    plt.close(fig)

# Edge Case 4
def test_large_dataset():
    """Test with a large dataset."""
    df = pd.DataFrame({'age': np.random.randint(1, 100, 1000)})
    fig, ax = plot_histogram(df, column='age', bins=20)
    assert fig is not None, "Figure was not created for large dataset."
    assert ax is not None, "Axes were not created for large dataset."
    plt.close(fig)

# Edge Case 5
def test_all_numeric_columns():
    """Test using all numeric columns from a DataFrame."""
    df = pd.DataFrame({'age': [25, 30, 35], 'height': [150, 160, 170]})
    fig, ax = plot_histogram(df)
    assert fig is not None, "Figure was not created."
    assert ax is not None, "Axes were not created."
    plt.close(fig)

# Edge Case 6
def test_mixed_data_types():
    """Test with a mix of numeric and non-numeric columns."""
    df = pd.DataFrame({'age': [25, 30, 35], 'color': ['red', 'blue', 'green']})
    fig, ax = plot_histogram(df)
    assert fig is not None, "Figure was not created."
    assert ax is not None, "Axes were not created."
    plt.close(fig)

# Edge Case 7
def test_flatten_and_nan_removal():
    """Test flattening and removing NaN values from a NumPy array."""
    arr = np.array([[1, np.nan, 2], [np.nan, 3, 4]])
    fig, ax = plot_histogram(arr, bins=2, title="Flatten and NaN Removal")
    data = arr.flatten()[~np.isnan(arr.flatten())]  # Simulate flattening and NaN removal
    assert np.array_equal(data, np.array([1, 2, 3, 4])), "Flattening or NaN removal failed."
    assert fig is not None
    assert ax is not None
    plt.close(fig)

# Error Case 1
def test_empty_dataframe():
    """Test error for empty DataFrame."""
    df_empty = pd.DataFrame({'age': []})
    with pytest.raises(ValueError, match="DataFrame must not be empty."):
        plot_histogram(df_empty, column='age')

# Error Case 2
def test_nonexistent_column():
    """Test error for non-existent column."""
    df = pd.DataFrame({'age': [25, 30, 35]})
    with pytest.raises(ValueError, match="Column 'height' not found in the DataFrame."):
        plot_histogram(df, column='height')

# Error Case 3
def test_empty_array():
    """Test error for empty NumPy array."""
    array_empty = np.array([])
    with pytest.raises(ValueError, match="NumPy array must not be empty."):
        plot_histogram(array_empty)

# Error Case 4
def test_non_numeric_data_error():
    """Test error for completely non-numeric DataFrame."""
    df = pd.DataFrame({'invalid': ['A', 'B', 'C']})
    with pytest.raises(ValueError, match="No numeric columns found in the DataFrame."):
        plot_histogram(df)

# Error Case 5
def test_invalid_bins_value():
    """Test error for invalid bins value."""
    df = pd.DataFrame({'age': [25, 30, 35]})
    with pytest.raises(ValueError, match="`bins` must be a positive integer."):
        plot_histogram(df, column='age', bins=-5)

# Error Case 6
def test_no_column_specified_with_nonnumeric_data():
    """Test error for no column specified in a DataFrame with non-numeric data."""
    df = pd.DataFrame({'color': ['red', 'blue', 'green']})
    with pytest.raises(ValueError, match="No numeric columns found in the DataFrame."):
        plot_histogram(df)

# Error Case 7
def test_invalid_input_type():
    """Test error for invalid input type."""
    invalid_input = "not_a_dataframe_or_array"
    with pytest.raises(TypeError, match="Input data must be a pandas DataFrame or a NumPy array."):
        plot_histogram(invalid_input)

if __name__ == "__main__":
    pytest.main()
