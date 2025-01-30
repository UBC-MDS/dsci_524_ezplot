# dsci_524_ezplot

[![Project Status](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
![Python Versions](https://img.shields.io/pypi/pyversions/dsci_524_ezplot)
[![Documentation Status](https://readthedocs.org/projects/dsci-524-ezplot/badge/?version=latest)](https://dsci-524-ezplot.readthedocs.io/en/latest/?badge=latest)
![CI-CD](https://github.com/UBC-MDS/dsci_524_ezplot/actions/workflows/ci-cd.yml/badge.svg)
[![codecov](https://codecov.io/github/UBC-MDS/dsci_524_ezplot/graph/badge.svg?token=bVVFkdjNRG)](https://codecov.io/github/UBC-MDS/dsci_524_ezplot)

Documentation Link: https://dsci-524-ezplot.readthedocs.io/en/latest/

ezplot is a Python package designed to simplify data visualization for data scientists and analysts. This package generates commonly used plots easily and quickly, allowing users to focus on insights rather than coding. The package provides robust and user-friendly functions for creating line plots, scatter plots, histograms, and heatmaps, making it a perfect tool for quick and effective data exploration and presentation.

## Installation

You can install the package directly from PyPi:

```bash
pip install dsci_524_ezplot
```

## Usage

The **ezplot** package provides the following functions:

- **`plot_line()`**: Generates line plots for visualizing trends and changes over time in your dataset.
- **`plot_scatterplot()`**: Creates scatter plots to analyze relationships between two continuous variables, with optional color and size adjustments.
- **`plot_histogram()`**: Quickly creates histograms to understand the distribution of a single variable, including options to adjust bin size.
- **`plot_heatmap()`**: Creates heatmaps to visualize correlations or matrix-like data, with customizable color palettes for better interpretability.

### Example

Here’s how you can create a heatmap using **ezplot**:

```python
from dsci_524_ezplot.plot_heatmap import plot_heatmap
import pandas as pd
import numpy as np

# Create sample data
data = pd.DataFrame(np.random.rand(5, 5), columns=["A", "B", "C", "D", "E"])

# Generate a heatmap
fig, ax = plot_heatmap(data, title="Sample Heatmap", xlabel="Columns", ylabel="Rows")

# Display the plot
import matplotlib.pyplot as plt
plt.show()
```

## Where This Package Fits in the Python Ecosystem

The Python ecosystem already offers powerful visualization libraries like Matplotlib, Seaborn, and Plotly. However, these libraries often require significant boilerplate code to customize and generate specific plots. ezplot aims to bridge the gap between flexibility and simplicity by providing pre-built functions tailored for common visualization needs. While Seaborn and Matplotlib offer extensive functionality; ezplot is designed to be lightweight and accessible for users who need straightforward plotting tools without diving into extensive customization.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`dsci_524_ezplot` was created by Daduica Julian, Elshaday Yoseph, Henry(Mu) Ha, Zhou Yining. It is licensed under the terms of the MIT license.

## Credits

`dsci_524_ezplot` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
