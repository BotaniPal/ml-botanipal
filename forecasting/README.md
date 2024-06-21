# Forecasting Commodity Prices with LSTM

This repository contains a Jupyter notebook that demonstrates how to forecast the prices of a commodity using a Long Short-Term Memory (LSTM) model.

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

## Data Collection and Preparation

### Data Source

The commodity price data used in this project is sourced from the official website of Sistem Informasi Ketersediaan dan Perkembangan Harga Bahan Pokok di Jawa Timur. The data is fetched using the following endpoint:

```plaintext
base_url = 'https://siskaperbapo.jatimprov.go.id/home2/getDataMap/'
```

### Scraping Data

Before training the LSTM model, historical price data for the commodities of interest is collected using the `automation.ipynb` notebook. This notebook handles both data scraping and the conversion of raw data to mean prices.

#### File: `automation.ipynb`

- **Purpose**: Automates data scraping and conversion to mean prices.
- **Steps**:
  1. **Data Scraping**: Utilizes `scrape_data(date, commodity)` function to fetch daily price data from the specified endpoint.
  2. **Mean Price Calculation**: Computes mean prices for each commodity across all regions or data points using `calculate_mean_and_save(commodity_name)` function.
  3. **Output**: Saves scraped raw data to `{commodity_name}.csv` and mean price data to `{commodity_name}_mean.csv`.

### LSTM Model Training

#### Overview

The LSTM model is trained using historical mean price data obtained from the `automation.ipynb` notebook. LSTM is chosen due to its ability to capture temporal dependencies in sequential data, making it suitable for time series forecasting.

#### Implementation

The Jupyter notebook provided (`forecast_commodity_prices.ipynb`) demonstrates how to:
- Load and preprocess the mean price data using `pandas` and `sklearn.preprocessing`.
- Construct an LSTM model using `tensorflow.keras`.
- Train the model on historical data to predict future commodity prices.
- Evaluate model performance using metrics like mean absolute percentage error (MAPE).
- Visualize predictions against actual prices using `matplotlib`.

#### Example Usage

1. Ensure all dependencies are installed (`tensorflow`, `pandas`, `numpy`, etc.).
2. Run each cell in the Jupyter notebook sequentially.
3. Adjust model parameters and preprocessing techniques as needed based on the quality and quantity of your data.

## Conclusion

By following the steps outlined in this repository, you can effectively forecast commodity prices using LSTM models. The provided scripts and notebooks offer a starting point for integrating real-world commodity data into predictive analytics workflows.

---