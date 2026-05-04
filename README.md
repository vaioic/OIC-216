# Analysis of organelles in TEM images

The goal of this project is to identify and measure organelles in TEM images. In particular, we are interested in identifying and measuring the size (area) of the mitochondria, Golgi bodies, lysosomes, and endoplasmic reticulum (ER) in each cell. Additionally, we want to know whether individual mitochondria and lysosomes are in contact with the ER.

This project is a collaboration with Alexis Bergsma (Moore Lab). 

## Getting started

The project uses QuPath and the SAM plugin for annotation and a custom Python script for analysis.

### Prerequisites

- [QuPath](https://qupath.github.io/) Version 0.6.0 (although v0.7.0 also works)
   - [QuPath SAM extension](https://github.com/ksugar/qupath-extension-sam) Version 0.8.0 (v0.9.0 also works)
   - [SAM API server](https://github.com/ksugar/samapi) version 0.6.1 (v0.7.1 also works)
- [Python](https://www.python.org/downloads/) version 3.14.0

### Installation

#### QuPath

1. Download and install [QuPath](https://github.com/qupath/qupath/releases/tag/v0.7.0)

2. Install the SAM extension:
   1. In QuPath, click on **Extensions** > **Manage extensions**.   
   2. In the Extension Manager window, click on **Manage extension catalogs**.
   3. In the Extension Catalog Manager window, copy the following URL in the Catalog URL: ``https://github.com/ksugar/qupath-catalog-ksugar``
   4. Click on **Add**.
   5. Close the Extension Catalog Manager.
   6. In the Extension Manager window, there should now be a section called "QuPath catalog ksugar" (likely at the very bottom).
   7. Click on the green plus icon next to "QuPath SAM extension".
   8. A dialog box should open up. Click on **Install**.
   9. When the installation is complete, check that SAM appears under the **Extensions** menu.

3. Install the SAM API server:
   1. Open a web browser and navigate to https://www.anaconda.com/.
   2. Click on the "Free Download" link at the top of the page.
   3. You will need to sign up for an Anaconda account to download the software. If you don't already have an account, click on the green "Get Started" button.
   4. Click on the **Sign Up with Email** button, then create an account. I suggest using your VAI email.
   5. Check your email for the verification email, then click the **Verify Email** link to complete the sign up process.
   6. You may then need to click on the Sign In link and sign into your account.
   7. Finally, under **Miniconda Installers**, click on the green **Download** button.
   8. Run the downloaded installer to install Miniconda on your computer. You can accept the default settings when installing.
   9. After installing Miniconda, run the **Anaconda prompt** program.
   Create a new conda environment called ``samapi``. In the Anaconda Prompt window, type in the following command:
      ``conda create -n samapi -y python=3.10`` (Update: Now uses 3.12)
   11. Activate the environment:
      ``conda activate samapi``
   12. After activating the environment, the 
   13. Install ``samapi``:
   ```
   python -m pip install git+https://github.com/ksugar/samapi.git
   ```
   14. Finally, run the API server:
   ```
   conda activate samapi
   python -m uvicorn samapi.main:app --workers 2
   ```
   15. Wait for the server to start fully. You should see a line that says ``INFO: Application startup complete.`` Leave this window open while you are using QuPath.
   16. To shut the server down, make sure the Anaconda Prompt window is selected, then press **CTRL+C** twice to stop the processes. You can then close the window.

#### Cloning the repository

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

### Annotating the images

1. Create a QuPath project, then add the images to analyze. I suggest creating a new project for each cell and only adding images from each cell.

2. Once the images are added, click on the **Annotations** tab. You will need to create the classes below. To simplify the creation of the classes, you can run the [import_classes](QuPath scripts/import_classes.groovy) script:
   1. Open the Script Editor: **Automate** > **Script Editor**
   2. Either open the [import_classes](QuPath scripts/import_classes.groovy) script or copy and paste it in the editor window.
   3. Click on "Run"

3. If you prefer to add the classes manually, remove all default annotations and create the following (spelling is critical):
  - Mitochondria
  - Golgi body
  - Cell
  - Lysosome
  - Secondary Lysosome
  - ER
  - Autophagosome
  - MVB
  - Vacuole
  - ILV
  - Unsure
  Note: ILV stands for intraluminal vesicle.

4. In each image, organelles can be pre-segmented using SAM:
   1. Use the **Rectangle** tool (R key) to draw a rectangle around each organelle of interest.
   2. Open the SAP API window.
   3. Select the rectangles in the **Annotation list**, then click on **Run for selected**.

4. Edit the annotations manually as necessary. Each annotation should also be labeled by their appropriate class by selecting the annotation, then clicking on **Set selected** in the Class list.

### Exporting the labels

1. To export the labels, first open the Script Editor: **Automate** > **Script Editor**.
2. Either open the file [import_classes.groovy](/QuPath%20scripts/import_classes.groovy) or copy and paste it in the editor window.
3. On the bottom right, click on the button with the three vertical dots (**⋮**), then select **Run for project**.
4. In the dialog box, select all images by clicking on the **>>** button.
5. Click **OK**.

> [!NOTE]
> If you get warning messages such as ``WARN: Unknown Correction value 'Unknown' will be stored as "Other"`` when running the export script, it is likely that there some annotations have not bees assigned to a valid class. You can fix this by opening each image and checking that each annotation has been classified accordingly (the SAM generated ROIs will typically be labeled 0, 1, or -1).

### Running the code

1. Start the virtual environment if not already loaded
   ```bash
   .\venv\Scripts\activate
   ```
2. Run the script ``analyze_images``
   ```bash
   python -m analyze_images
   ```

## Issues

If you encounter any issues with running the code or have any questions, please create an [Issue](https://github.com/vaioic/OIC-216/issues) or send an email to opticalimaging@vai.org. If you are reporting a programmatic bug, please include any error messages to aid with troubleshooting.

## Acknowledgements

### Dependencies

This project relies on the following packages:

- jupyterlab v4.4.10
- numpy v2.3.4
- scipy v1.16.3

**Note:** For full dependency list, see [requirements.txt](requirements.txt).

