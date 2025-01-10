# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the [GitHub Issues](https://github.com/UBC-MDS/dsci_524_ezplot/issues) for bugs. Anything tagged with `bug` and `help wanted` is open for contributions.

To fix a bug:
* Create a branch named `bugfix/<description>` to address the issue.
* Link the issue to your branch and pull request for traceability.
* Open a pull request following the [Pull Request Guidelines](#pull-request-guidelines).

### Implement Features

Follow the **GitHub Flow** collaboration strategy:

* Create a new branch for your feature using a descriptive name, e.g., `feature/scatter-plot`.
* Commit changes incrementally with clear, meaningful messages.
* Open a pull request and link it to the corresponding issue.
* Request a review from another contributor before merging.

### Write Documentation

Contribute to any part of the documentation, including:
* Docstrings in the code.
* Project documentation in the `docs` directory.
* Examples in Jupyter notebooks or blog posts.

To contribute documentation:
* Create a branch for your changes, e.g., `docs/<description>`.
* Ensure your documentation is clear and adheres to our style guide (if applicable).
* Open a pull request for review.

### Submit Feedback

We welcome feedback and suggestions for new features! 
* Submit feedback by creating a [GitHub Issue](https://github.com/UBC-MDS/dsci_524_ezplot/issues).
* Label your issue as `feature-request` or `feedback` to help us prioritize.

When proposing a feature:
* Explain how it would work in detail.
* Keep the scope narrow for easier implementation.
* Remember that contributions are welcome and this is a volunteer-driven project.

## Get Started!

Ready to contribute? Here's how to set up `dsci_524_ezplot` for local development.

1. **Fork the repository**  
   Start by forking the `dsci_524_ezplot` repository to your GitHub account.

2. **Clone the repository**  
   Clone the forked repository to your local machine:
   ```console
   $ git clone https://github.com/<your-username>/dsci_524_ezplot.git

3. **Navigate to the project directory**
    Move into the project directory:
    ```console
    $ cd dsci_524_ezplot
    ```

4. **Install dependecies**
    Use `poetry` to install all dependecies:
     ```console
    $ poetry install
    ```

5. **Create a branch for your changes**
    Use `git` (or similar) to create a branch for local dvelopment:
     ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

6. **Keep your branch up-to-date**
    Regulary pull updates from `main` branch to stay synced:
    ```console
    $ git pull origin main
    ```
7. **Make and test your changes**
    Implement your changes locally and test to ensure they work as expected.

8. **Commit your changes**
    Write clear, meaningful commit messages:
     ```console
    $ git commit -m "Add a meaningful message describing your changes"
    ```
9. **Push your changes to Github**
    Push your branch to your forked repository:
     ```console
    $ git push origin name-of-your-branch
    ```
10. **Open a pull request**
    Open a pull request to the main repository, linking it to the relevant issue and following the [Pull Request Guidelines](#pull-request-guidelines).

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.
4. Assign reviewers to your pull request and address their feedback before merging. 

## Code of Conduct

Please note that the `dsci_524_ezplot` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.