if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    months = ["january-", "february-", "march-", "april-", "may-", "june-",
              "july-", "august-", "september-", "october-", "november-", "december-"]
    years = ["2021", "2022"]

    days = []
    for num in range(1, 32):
        days.append(str(num) + "-")

    # "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-9-february-2022"
    link_prefix = "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-"

    for year in years:
        for month in months:
            for day in days:
                link = link_prefix + day + month + year

                try:
                    soup = BeautifulSoup(urlopen(link))
                    print(soup.prettify())
                except:
                    print(link)
                    continue
