import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import pandas as pd


def get_website_content(url):
    # We first send a GET request to the URL
    response = requests.get(url)
    
    # If the request was successful, we parse the HTML content with BeautifulSoup
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # We use BeautifulSoup to find the first table on the page
        table = soup.find('table')
        
        # We then iterate over each row in the table
        rows = []
        for row in table.find_all('tr'):
            # We use BeautifulSoup to find all the cells in the current row
            cells = row.find_all(['th', 'td'])
            
            # We iterate over each cell in the current row and append its text content to a list
            row_data = [cell.text.strip() for cell in cells if cell.text.strip()] # <-- ignore empty cells
            rows.append(row_data)
        
        # We create a DataFrame from the list of lists and display it
        df = pd.DataFrame(rows)
        
        # To display all the rows in the DataFrame, we can use the following code:
        pd.set_option('display.max_rows', None)
        print(df)
    else:
        print("Error: Unable to access the URL.")

url = "https://www.coinmarketcap.com/" # replace with the actual URL of the site
get_website_content(url)
