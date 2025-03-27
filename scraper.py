import argparse
import pandas as pd
from bs4 import BeautifulSoup
import time
import os
from autoWeb import BrowserAutomation  # Import the BrowserAutomation class

# Function to scrape card data from the website
def get_card_data(driver_path, seller_username, card_list, wait_time=1):
    base_url = f"https://www.cardmarket.com/en/Magic/Users/{seller_username}/Offers/Singles?sortBy=price_asc&name="
    available_cards = []
    unavailable_cards = []

    # Create an instance of BrowserAutomation
    automation = BrowserAutomation(driver_path)

    for card_name in card_list:
        search_url = base_url + card_name.replace(" ", "+")
        automation.go_to_website(search_url)

        time.sleep(wait_time)

        # Scrape data with BeautifulSoup
        soup = BeautifulSoup(automation.browser.page_source, 'html.parser')
        card_elements = soup.find_all('div', class_='article-row')

        found = False
        for card in card_elements:
            title_element = card.find('a', href=True)
            price_element = card.find('span', class_='color-primary')

            if title_element and price_element:
                title = title_element.text.strip()
                price = price_element.text.strip()
                available_cards.append([title, price, search_url])

                print(f"Card: {title}, Price: {price}, Link: {search_url}")
                found = True
                break  # Get only the cheapest one
                

        if not found:
            unavailable_cards.append([card_name])
            print(f"No info found for {card_name}")

    automation.close_browser()  # Close the browser window
    return available_cards, unavailable_cards

# Function to save data to CSV
def save_to_csv(available_cards, unavailable_cards, name_prep, output_dir):
    pd.DataFrame(available_cards, columns=['Card Name', 'Price', 'Link']).to_csv(f'{output_dir}/{name_prep}_available_cards.csv', index=False)
    pd.DataFrame(unavailable_cards, columns=['Card Name']).to_csv(f'{output_dir}/{name_prep}_unavailable_cards.csv', index=False)
    print(f"CSV files generated in output directory: {output_dir}")

# Main script entry
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape card data from Cardmarket.")
    parser.add_argument("--driver_path", required=True, help="Path to the WebDriver executable.")
    parser.add_argument("--seller_name", required=True, help="The seller's username on Cardmarket.")
    parser.add_argument("--card_list_path", required=True, help="Path to a text file containing card names, one per line.")
    parser.add_argument("--output_dir", required=False, help="Output directory for the CSV files.")
    parser.add_argument("--wait_time", required=False, help="Time to wait between requests.", default=1)

    args = parser.parse_args()

    wait_time = float(args.wait_time)
    driver_path = args.driver_path
    seller_username = args.seller_name
    with open(args.card_list_path, 'r') as file:
        card_list = [line.strip() for line in file.readlines()]

    if args.output_dir is None:
        args.output_dir = "."

    available, unavailable = get_card_data(driver_path, seller_username, card_list, wait_time)

    # extract input file name from path using os
    input_file = os.path.basename(args.card_list_path)
    name_prep = input_file + '_' + seller_username
    save_to_csv(available, unavailable, name_prep, args.output_dir)
