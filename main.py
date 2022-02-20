# TODO:
# run for all dates
# save into csv
# alter to run for new records checking csv

import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from datetime import datetime
import time

if __name__ == "__main__":
    df = pd.DataFrame(columns=["timestamp", "day", "month",
                      "year", "cases", "icu", "ventilator", "cleared"])

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
                try:
                    time.sleep(random.randint(0, 3))

                    link = link_prefix + day + "-" + month + "-" + year
                    soup = BeautifulSoup(urlopen(link), features="html.parser")
                    # print(soup.prettify())

                    date_time = date_time.now()
                    # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#searching-the-tree (keyword arguments)
                    text = soup.find_all("meta", attrs={"name": "description"})

                    for item in text:
                        try:
                            item['content'] = item['content'][item['content'].index(
                                str(year))+4:]
                        except:
                            pass

                        extracted_numbers = [
                            int(s) for s in item['content'].split() if s.isdigit()]

                    if len(extracted_numbers) == 4:
                        df.loc[-1] = [date_time, day, month,
                                      year, extracted_numbers[0], extracted_numbers[1], extracted_numbers[2], extracted_numbers[3]]
                    else:
                        df.loc[-1] = [date_time, day, month,
                                      year, extracted_numbers[0], extracted_numbers[1], extracted_numbers[2], None]
                    df.index = df.index + 1  # shifting index
                    df = df.sort_index()  # sorting by index

                    print(df)
                except:
                    print(link)
                    continue
