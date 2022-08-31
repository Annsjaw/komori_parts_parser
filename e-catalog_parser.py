import os

import pandas as pd
from bs4 import BeautifulSoup


def parts_only(path):
    """Create CSV file with parts num, name and type."""
    headers = ['item', 'id', 'quantity', 'title', 'type']
    df_parts = pd.DataFrame(columns = headers)
    html_files = os.listdir(path)
    filter = [x for x in html_files if x.__contains__('Print.html')]
    for file in filter:
        print(f'>>>> Iterable file {file}')
        with open(f'{path}{file}') as f:
            soup = BeautifulSoup(f, 'html.parser')
        table = soup.find('table', attrs={'class': 'item'})

        for j in table.find_all('tr')[1:]:
            row_data = j.find_all('td')
            row = [i.text for i in row_data]
            lenght = len(df_parts)
            df_parts.loc[lenght] = row
    filename = soup.title.text.replace(' ', '_').replace('#', '').split('_-_')[0]
    filename = f'parts_{filename}'
    print('>>>> Deleting unnecessary columns')
    df_parts.drop(labels=['item', 'quantity'], axis=1, inplace=True)
    print('>>>> Deleting duplicate rows')
    df_parts.drop_duplicates(subset=None, inplace=True)
    print(f'>>>> Creating and saving file {filename}.csv')
    df_parts.to_csv(f'{filename}.csv', index=False)

def main():
    try:
        path = str(input('Enter path to Html folder your e-catalog: '))
        parts_only(path)
    except FileNotFoundError:
        exit('>>>> File not found')
        

if __name__ == '__main__':
    main()
