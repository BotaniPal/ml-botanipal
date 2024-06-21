# How to train the Plant Type Model

## Requirements

To install the necessary libraries, use the provided `requirements.txt` file.

### Installation
1. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Preparing Data

1. **Upload Dataset to Google Drive**
- Link: https://drive.google.com/file/d/1i8uZoSZyXESE0vGOrbYH_QnCyL6iYxlv/view?usp=drive_link


2. **Mount Google Drive in Your Notebook**

    - If you are using a Jupyter notebook or Google Colab, you need to mount your Google Drive:

    ```python
    from google.colab import drive
    drive.mount('/content/drive')
    ```

    - This will prompt you to authorize and provide an access token. Follow the instructions to complete the authorization.

3. **Set Up the Dataset Path**

    - Define the path to your dataset in your script:

    ```python
    import os

    dataset_path = '/content/drive/MyDrive/dataset'
    ```

### 2. Running the Code

- Run the `PreTrained_VGG16_Plant_Type_Detection.ipynb` notebook to train the model. Ensure that the dataset path is correctly set in the notebook.

## Contributing

If you want to contribute to this project, feel free to fork the repository and submit a pull request. Make sure to update tests as appropriate.
