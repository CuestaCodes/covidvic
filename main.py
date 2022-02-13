if __name__ == "__main__":
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import pandas as pd
    from datetime import datetime

    df = pd.DataFrame(columns=["timestamp", "day", "month", "year", "text"])

    date_time = datetime.now()

    days = []
    for num in range(1, 32):
        days.append(str(num))

    months = ["january", "february", "march", "april", "may", "june",
              "july", "august", "september", "october", "november", "december"]
    # years = ["2021", "2022"]

    years = ["2022"]

    # "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-9-february-2022"
    link_prefix = "https://www.health.vic.gov.au/media-releases/coronavirus-update-for-victoria-"

    for year in years:
        for month in months:
            for day in days:
                link = link_prefix + day + "-" + month + "-" + year

                try:
                    soup = BeautifulSoup(urlopen(link), features="html.parser")
                    # print(soup.prettify())

                    date_time = date_time.now()

                    df.loc[-1] = [date_time, day, month, year, soup.prettify()]
                    df.index = df.index + 1  # shifting index
                    df = df.sort_index()  # sorting by index
                    print(df)

                except:
                    print(link)
                    continue
