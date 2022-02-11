if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    link = "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-9-february-2022"
    soup = BeautifulSoup(urlopen(link))

    print(soup.prettify())
