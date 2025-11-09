import requests
from bs4 import BeautifulSoup
import pandas
import time
import csv


data = []

def main():
    scrape_history()
    write_file()

def write_file():
    with open('wordle_history.csv', 'w', newline='') as file:
        header = ['date', 'problem #', 'answer']
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    with open('word_history.txt', 'w') as file:
        for item in data:
            file.write(item[2] + '\n')

def scrape_history():
    url = "https://wordfinder.yourdictionary.com/wordle/answers/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser") #lxml is an html parser from bs4
    print(type(soup))
    title = soup.title
    print(title)
    tables = soup.find_all('table')
    #print(tables)

    global data
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            row_data = row.find_all(['td'])
            row_text = [cell.text.strip() for cell in row_data]
            if len(row_text) > 0:
                data.append(row_text)
            #print(row_data)
            #print(row_text) 
    data = data[1:]

if __name__ == "__main__":
    main()