# TEM Image Analysis

This project is in a collaboration with Alexis Bergsma (Moore Lab). While the main analysis was carried out using QuPath, the scripts here were used to analyze the resulting data.

## Getting started

### Prerequisites

- [Python](https://www.python.org/downloads/) version 3.14.0

### Installation

1. Download or clone the GitHub repository
   ```bash
   git clone git@github.com:vaioic/OIC-216.git
   cd OIC-216
   ```

2. Create a python virtual environment
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment
   ```bash
   .\venv\Scripts\activate
   ```

4. Install the dependencies using Pip
   ```bash
   python -m pip install -r .\requirements.txt
   ```

### Running the code

1. Start the virtual environment if not already loaded
   ```bash
   .\venv\Scripts\activate
   ```

2. Start Jupyter Lab
   ```bash
   python -m jupyterlab
   ```

3. Open the ``analyze_data.ipynb`` notebook

4. Modify the variable ``data_directory`` as needed to point to the folder containing the CSV files

## Issues

If you encounter any issues with running the code or have any questions, please create an [Issue](https://github.com/vaioic/OIC-216/issues) or send an email to opticalimaging@vai.org. If you are reporting a programmatic bug, please include any error messages to aid with troubleshooting.

## Acknowledgements

### Dependencies

This project relies on the following packages:

- jupyterlab v4.4.10
- numpy v2.3.4
- scipy v1.16.3

**Note:** For full dependency list, see [requirements.txt](requirements.txt).

