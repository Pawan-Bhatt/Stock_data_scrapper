import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_stock_data(url, df):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
        soup = BeautifulSoup(response.text, 'html.parser')
        labels = ['Name', 'Price (Intraday)', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)']

        tr_elements = soup.find_all('tr', {'class': 'simpTblRow'})

        for tr_element in tr_elements:
            details = []

            for label in labels:
                td_element = tr_element.find('td', {'aria-label': label})
                details.append(td_element.text.strip() if td_element else None)

            # Append the details to the DataFrame
            df.loc[len(df)] = details

        print('-' * 50)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    

    return df

def main():
    url = 'https://finance.yahoo.com/most-active?offset=0&count=100'

    columns = ['Name', 'Price', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap', 'PE Ratio (TTM)']
    df = pd.DataFrame(columns=columns)

    # Scrape data for each stock
    df = scrape_stock_data(url, df)

    
    duration = 30*3 # duration here is use to run for a particular time 
    start_time = time.time()
    while  (time.time() - start_time) < duration:
        data = scrape_stock_data(url, df)

        if data is not None:
            # Append the data to the DataFrame
            df = df.append(data, ignore_index=True)
            print("Data scraped successfully.")
        else:
            print("Error scraping data. Retrying in 1 hour.")

        # Sleep for 1 hour before scraping again
        time.sleep(3600)  # 3600 seconds = 1 hour    
    df.to_csv('stock_data.csv', index=False)
    print("Data saved to stock_data.csv")

if __name__ == "__main__":
    main()
