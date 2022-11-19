import pandas as pd
import os

def return_yields_month(month):

    filename = f'datasets/{month}.csv'
    if bool(os.path.isfile(filename)):
        df = pd.read_csv(filename)
        return df

    else:
        url_month = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/{month}?type=daily_treasury_yield_curve&field_tdr_date_value_month={month}&page&_format=csv"
        df = pd.read_csv(url_month)
        df.to_csv(f'datasets/{month}.csv', index=False)

        return df

def return_yields_yr(year):

    filename = f'datasets/{year}.csv'
    if bool(os.path.isfile(filename)):
        df = pd.read_csv(filename)
        return df

    else:
        url_yr = f"https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/{year}/all?type=daily_treasury_yield_curve&field_tdr_date_value={year}&page&_format=csv"
        df = pd.read_csv(url_yr)
        df.to_csv(f'datasets/{year}.csv', index=False)

        return df

def return_yields_latest():

    url_curr = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/202211?type=daily_treasury_yield_curve&field_tdr_date_value_month=202211&page&_format=csv"
    df = pd.read_csv(url_curr)

    return df

