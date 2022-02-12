if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    years = ["2019", "2020", "2019"]

    days = []
    for num in range(1, 32):
        days.append(str(num))

    link = "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-9-february-2022"
    soup = BeautifulSoup(urlopen(link))

    print(soup.prettify())
