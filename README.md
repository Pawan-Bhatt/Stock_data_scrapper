# Stock Data Scraper

## Overview

The Stock Data Scraper is a Python program designed to scrape stock data from Yahoo Finance at regular intervals and organize it into a structured DataFrame. This tool is useful for obtaining real-time stock information for analysis and integration into data pipelines.

## Features

- Automated web scraping of stock data from Yahoo Finance.
- Hourly data retrieval to ensure the dataset is up-to-date.
- Data organization into a Pandas DataFrame for easy analysis.
- Error-handling mechanisms to address changes in website structure and maintain data integrity.

## Prerequisites

- Python 3.x
- Required Python packages: BeautifulSoup, Selenium, Pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/stock-data-scraper.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Configure the scraper by updating the relevant settings in the configuration file (`config.py`).

2. Run the scraper:

    ```bash
    python stock_scraper.py
    ```

3. The program will automatically scrape stock data from Yahoo Finance every hour and store it in a CSV file.

## Configuration

Adjust the settings in the `config.py` file to customize the scraper's behavior, including the stock symbols to scrape, the output file format, and other parameters.

## Data Output

The scraped data will be stored in a CSV file (`output_data.csv` by default) in the specified output directory.

## Contributing

If you'd like to contribute to the development of the Stock Data Scraper, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) and [Selenium](https://www.selenium.dev/) teams for their fantastic tools.
