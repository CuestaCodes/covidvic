# TODO:
# fix infinite loop at most recent date
# run for all dates
# save into csv
# alter to run for new records checking csv

import random
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from datetime import datetime
import time


def get_date(date_time):
    # if csv is empty return None, else get most current datetime
    # str(day) etc.
    month_dict = {1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
                  7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"}

    current_day = str(date_time.day)
    current_month = month_dict[date_time.month]
    current_year = str(date_time.year)

    try:
        date_df = pd.read_csv("vic_gov_covid.csv", usecols=[
            0], header=None)
        date_df[0] = pd.to_datetime(date_df[0], format='%Y-%m-%d')
        print(date_df[0])
        recent_date = date_df[0].max()
        recent_day = str(recent_date.day)
        recent_month = month_dict[recent_date.month]
        recent_year = str(recent_date.year)

        return recent_day, recent_month, recent_year, current_day, current_month, current_year

    except:
        return None, None, None, current_day, current_month, current_year


def check_date(day, month, year, current_day, current_month, current_year):
    if day == current_day and month == current_month and year == current_year:
        return True
    else:
        return False


def scrape():
    df = pd.DataFrame(columns=["timestamp", "day", "month",
                      "year", "cases", "icu", "ventilator", "cleared"])

    date_time = datetime.today()
    recent_day, recent_month, recent_year, current_day, current_month, current_year = get_date(
        date_time)
    day_trigger, month_trigger, year_trigger = False, False, False

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
        if year_trigger == False and year != recent_year and recent_year != None:
            continue
        elif year_trigger == False:
            year_trigger = True

        for month in months:
            if month_trigger == False and month != recent_month and recent_month != None:
                continue
            elif month_trigger == False:
                month_trigger = True

            for day in days:
                if day_trigger == False and day != recent_day and recent_day != None:
                    continue
                elif day_trigger == False and recent_day == None:
                    day_trigger = True
                elif day_trigger == False:
                    day_trigger = True

                    if check_date(day, month, year, current_day, current_month, current_year):
                        return df

                    continue

                try:
                    time.sleep(random.randint(0, 3))
                    link = link_prefix + day + "-" + month + "-" + year
                    soup = BeautifulSoup(urlopen(link), features="html.parser")

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
                        df.loc[-1] = [date_time.strftime('%Y-%m-%d'), day, month,
                                      year, extracted_numbers[0], extracted_numbers[1], extracted_numbers[2], extracted_numbers[3]]
                    else:
                        df.loc[-1] = [date_time.strftime('%Y-%m-%d'), day, month,
                                      year, extracted_numbers[0], extracted_numbers[1], extracted_numbers[2], None]
                    df.index = df.index + 1  # shifting index
                    df = df.sort_index()  # sorting by index

                    print(link)

                except:
                    if check_date(day, month, year, current_day, current_month, current_year):
                        return df

                    print(link)

                    continue

                if check_date(day, month, year, current_day, current_month, current_year):
                    return df


def main():
    df = scrape()

    df.to_csv("vic_gov_covid.csv", mode="a", index=False,
              header=False)


if __name__ == "__main__":
    main()
