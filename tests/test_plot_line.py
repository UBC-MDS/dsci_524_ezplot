from dsci_524_ezplot.plot_line import plot_line
import pandas as pd
import matplotlib.pyplot as plt

def test_plot_line():
    """Test plot_line function."""
    df = pd.DataFrame({'year': [2020, 2021, 2022], 'sales': [100, 150, 200]})
    fig, ax = plot_line(df, 'year', 'sales', 'Annual Sales', 'Year', 'Sales ($)')
    
    # Existence checks
    assert fig is not None, "Figure is None!"
    assert ax is not None, "Axes is None!"
    
    # Legends checks
    assert ax.get_title() == 'Annual Sales', "Title is incorrect"
    assert ax.get_xlabel() == 'Year', "X-label is incorrect"
    assert ax.get_ylabel() == 'Sales ($)', "Y-label is incorrect"
    
    # Data checks
    line = ax.get_lines()[0]
    assert len(line.get_xdata()) == 3, "Incorrect number of data points"