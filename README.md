# Cardmarket Scraper Tool

This project is a Python-based tool for scraping card data from the Cardmarket website. It retrieves card availability and pricing information for a specific seller and saves the results in CSV files.

## Features

- Scrapes card data using a seller's username and a list of card names.
- Retrieves the cheapest available card and its price.
- Saves available and unavailable card data into separate CSV files.
- Uses Selenium for browser automation and BeautifulSoup for HTML parsing.

## Requirements

- Python 3.7+
- Selenium WebDriver (Edge)
- Required Python libraries: `argparse`, `pandas`, `bs4`, `selenium`

## Current know limitations

- Double sided cards

## Usage

1. Install the required Python libraries:
    ```bash
    pip install pandas beautifulsoup4 selenium
    ```

2. Run the script:
    ```bash
    python scraper.py --driver_path <path_to_webdriver> --seller_name <seller_username> --card_list_path <path_to_card_list> --output_dir <output_directory> --wait_time <time_in_seconds>
    ```

    - `--driver_path`: Path to the Edge WebDriver executable.
    - `--seller_name`: Seller's username on Cardmarket.
    - `--card_list_path`: Path to a text file containing card names (one per line).
    - `--output_dir`: Directory to save the output CSV files (default: current directory).
    - `--wait_time`: Time to wait between requests (default: 1 second).

## Example

```bash
python scraper.py --driver_path "D:/Programs/edgedriver_win32/msedgedriver.exe" --seller_name "Manamaze" --card_list_path "cards.txt" --output_dir "output" --wait_time 2
```

## Output

- `<input_file>_<seller_name>_available_cards.csv`: Contains available cards with their prices and links.
- `<input_file>_<seller_name>_unavailable_cards.csv`: Contains cards that were not found.

## Notes

- Ensure the Edge WebDriver version matches your browser version.
- The `autoWeb.py` file contains the `BrowserAutomation` class used for browser interactions.

## License

This project is licensed under the MIT License.  
