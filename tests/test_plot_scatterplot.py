import pytest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dsci_524_ezplot.plot_scatterplot import plot_scatterplot

@pytest.fixture
def sample_df():
    """Fixture for providing a sample dataset."""
    return pd.DataFrame({
        'height': [150, 160, 165, 170],
        'weight': [50, 60, 65, 70],
        'category': ['small', 'medium', 'medium', 'large']
    })
    
@pytest.mark.mpl_image_compare
def test_plot_scatterplot(sample_df):
    """Test if the scatter plot is generated correctly for a sample DataFrame."""
    fig, ax = plot_scatterplot(sample_df, x = 'height', y = 'weight', color = 'category', title = "Test Plot Sample DF", xlabel="X Axis", ylabel="Y Axis")
    return fig

    
# Expected Case 1
def test_plot_scatterplot_valid_dataframe(sample_df):
    """Test if plot_scatterplot successfully creates a scatter plot from a valid DataFrame."""
    fig, ax = plot_scatterplot(sample_df, x = 'height', y = 'weight', color = 'category', title = 'Test Plot Sample DF', xlabel = "X-Axis", ylabel = "Y-Axis")

    assert fig is not None  # Check that figure object is returned
    assert ax is not None  # Check that axes object is returned
    assert ax.get_xlabel() == "X-Axis"  # Check that x-axis label correct
    assert ax.get_ylabel() == "Y-Axis"  # Check that y-axis label correct
    assert ax.get_title() == 'Test Plot Sample DF', "The title is incorrect ." # Check that title is correct

    
# Expected Case 2
def test_plot_scatterplot_valid_numpy_array():
    """Expected: Test if plot_scatterplot successfully creates a scatter plot from a valid NumPy array."""
    array = np.array([[1, 2, 3], [4, 5, 6]])
    fig, ax = plot_scatterplot(array, x = 0, y = 1, title="Test Plot Sample from Array")
    assert fig is not None
    assert ax is not None
    
# Expected Case 3
def test_labels_correct(sample_df):
    """Test if the x and y labels are set correctly."""
    fig, ax = plot_scatterplot(sample_df, x = 'height', y = 'weight', color = 'category', title = 'Test Plot Sample DF', xlabel = "Height", ylabel = "Weight")
    assert ax.get_xlabel() == 'Height', "The x-axis label is incorrect."
    assert ax.get_ylabel() == 'Weight', "The y-axis label is incorrect."


# Edge Case 1
def test_plot_scatterplot_nan_values(sample_df):
    """Test if plot_scatterplot handles NaN values by replacing them with zeros."""
    df = pd.DataFrame([[1, 2], [np.nan, 4]])  # Dataframe with a NaN value
    fig, ax = plot_scatterplot(df, x = 0, y = 1, title="Test Plot Sample from NaN in DF")
    assert fig is not None
    assert ax is not None

# Edge Case 2
def test_scatterplot_no_color_column(sample_df):
    """Test if the scatterplot works without a color column."""
    fig, ax = plot_scatterplot(sample_df, x = 'height', y = 'weight', title = 'Scatter Plot Without Color', xlabel = "X Axis", ylabel = "Y Axis")
    assert fig is not None
    assert ax is not None
    assert ax.get_xlabel() == "X Axis"  # Verify the x-axis label
    assert ax.get_ylabel() == "Y Axis"  # Verify the y-axis label

#Edge Case 3
def test_no_title(sample_df):
    """Test if the plot works when no title is provided."""
    fig, ax = plot_scatterplot(sample_df, x = 'height', y = 'weight', color = 'category')
    assert ax.get_title() == "", "The default title is not empty when no title is provided."

#Edge Case 4
def test_mixed_data_types():
    """Test if an error is raised for mixed data types in x or y."""
    data = pd.DataFrame({
        'x': [1, 2, 'a'],
        'y': [4, 5, 6]
    })
    with pytest.raises(TypeError):
        plot_scatterplot(data, x = 'x', y = 'y')

#Edge Case 5
def test_non_numeric_data():
    """Test if plot_scatterplot raises and error for non-numeric data in x or y."""
    data = pd.DataFrame({
        'x': ['a', 'b', 'c'],
        'y': [1, 2, 3]
    })
    with pytest.raises(TypeError):
        plot_scatterplot(data, x = 'x', y = 'y')

# Edge Case 6
def test_non_numeric_y_column():
    """Test that a TypeError is raised when the y column contains non-numeric data."""
    df = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': ['a', 'b', 'c', 'd'], 
        'color': [10, 20, 30, 40]
    })
    with pytest.raises(TypeError):
        plot_scatterplot(df, x='x', y='y')

# Edge Case 7
def test_numeric_color_column():
    """Test that scatter plot uses a colormap when the color column is numeric."""
    df = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 20, 30, 40],
        'color': [100, 200, 300, 400]  # Numeric color column
    })
    
    fig, ax = plot_scatterplot(df, x='x', y='y', color='color')

    # Verify that a colormap is applied
    scatter = ax.collections[0]
    assert scatter.get_array() is not None, "Colormap is not applied when color is numeric."


# Error Case 1
def test_plot_scatterplot_invalid_input_type():
    """Test if plot_scatterplot raises a TypeError for invalid input types."""
    with pytest.raises(TypeError):
        plot_scatterplot("not_a_dataframe", x = 0, y = 1, color = 'category', title = "Invalid Test Plot")

# Error Case 2
def test_plot_scatterplot_empty_dataframe():
    """Test if plot_scatterplot raises a ValueError for an empty DataFrame."""
    df = pd.DataFrame(columns=[])  # Create empty DataFrame
    with pytest.raises(ValueError):
        plot_scatterplot(df, x = 0, y = 1, title = "Test Plot Empty DF")

# Error Case 3
def test_plot_scatterplot_empty_numpy_array():
    """Test if plot_scatterplot raises a ValueError for an empty NumPy array."""
    empty_array = np.array([])  # Create an empty NumPy array
    with pytest.raises(ValueError):
        plot_scatterplot(empty_array, x=0, y=1, title="Test Plot Empty NumPy Array")





    
