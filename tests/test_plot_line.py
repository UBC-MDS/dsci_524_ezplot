from dsci_524_ezplot.plot_line import plot_line
import pandas as pd
import matplotlib.pyplot as plt

def test_plot_line():
    """Test plot_line function."""
    df = pd.DataFrame({'year': [2020, 2021, 2022], 'sales': [100, 150, 200]})
    fig, ax = plot_line(df, 'year', 'sales', 'Annual Sales', 'Year', 'Sales ($)', x_decimals=0, y_decimals=2)
    
    # Existence checks
    assert fig is not None, "Figure is None!"
    assert ax is not None, "Axes is None!"

    # Minimum data points check
    df_single = pd.DataFrame({'year': [2020], 'sales': [100]})
    try:
        plot_line(df_single, 'year', 'sales', 'Annual Sales', 'Year', 'Sales ($)')
    except ValueError as e:
        assert str(e) == "At least 2 data points are required to plot a line", "Incorrect error message"
    
    # Legends checks
    assert ax.get_title() == 'Annual Sales', "Title is incorrect"
    assert ax.get_xlabel() == 'Year', "X-label is incorrect"
    assert ax.get_ylabel() == 'Sales ($)', "Y-label is incorrect"
    
    # Data checks
    line = ax.get_lines()[0]
    assert len(line.get_xdata()) == 3, "Incorrect number of data points"

    # Decimals checks
    x_formatter = ax.xaxis.get_major_formatter()
    y_formatter = ax.yaxis.get_major_formatter()
    assert x_formatter.format_data(2020) == '2020', "X-axis decimals are incorrect"
    assert y_formatter.format_data(100) == '100.00', "Y-axis decimals are incorrect"
    plt.close(fig)
