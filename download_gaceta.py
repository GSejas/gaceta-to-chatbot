import requests
from bs4 import BeautifulSoup

import datetime


url = "https://www.imprentanacional.go.cr/gaceta/"

def download_pdf():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    anchor = soup.select_one("#ctl00_PdfGacetaDescargarHyperLink")
    
    if anchor:
        pdf_url = anchor["href"]
        pdf_response = requests.get("https://www.imprentanacional.go.cr" + pdf_url)
        
        # get today's date as a string in format YYYY-MM-DD
        today = datetime.date.today().strftime('%Y-%m-%d')

        # set the file name with today's date
        file_name = f'input/gaceta_{today}.pdf'

        with open(file_name, "wb") as pdf_file:
            pdf_file.write(pdf_response.content)

    else:
        print("Error: The anchor tag was not found.")
    return 

if __name__ == "__main__":
    download_pdf()