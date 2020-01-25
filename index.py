from bs4 import BeautifulSoup
import requests

data = ''

url = 'https://www.bahai.org/library/authoritative-texts/downloads'
response = requests.get(url)

# make sure we got a valid response
if(response.ok):
    # get the full data from the response
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')
    alist = soup.find_all('a', title=True)
    links = [a['href']
             for a in alist if a['title'].find("HTML") > -1]
    for link in links:
        page = requests.get("https://www.bahai.org" + link)
        soup = BeautifulSoup(page.text, 'html.parser')
        data = data + ' ' + soup.get_text()

    with open("source.txt", "w") as f:
        f.write(data)
