import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from datetime import datetime

def parse_df(df):
    "df is a pandas dataframe"

    if '4 Mo' in df.columns:
        df = df.drop('4 Mo', axis=1)

    x_days = [
        30,
        60, 
        90,
        180,
        360,
        2 * 360,
        3 * 360,
        5 * 360,
        7 * 360,
        10 * 360,
        20 * 360,
        30 * 360
    ]

    regr_slopes = []
    dates = []

    for i, row in df.iterrows():
        dt = datetime.strptime(row['Date'], '%m/%d/%Y')
        dates += [dt]

        y_data = []
        for col in df.columns[1:]:
            y_data += [row[col]]

        x_data = x_days
        slope = linregress(x_data, y_data).slope
        regr_slopes += [slope]

    x_vals = dates
    y_vals = regr_slopes

    plt.title('Yield Regression Slopes')
    plt.xlabel('Dates')
    plt.ylabel('Slopes')
    plt.plot(x_vals, y_vals)
    plt.show()
    return

def parse_curr(df):

    ylds = []
    for col in df.columns[1:]:
        ylds += [df.iloc[-1][col]]

    x_days = [
        30,
        60, 
        90,
        120,
        180,
        360,
        2 * 360,
        3 * 360,
        5 * 360,
        7 * 360,
        10 * 360,
        20 * 360,
        30 * 360
    ]

    regr_line = linregress(x_days, ylds)
    slope = regr_line.slope

    plt.plot(x_days, ylds, '-o')
    plt.show()

    print(
        f"The regression line slope is {slope}"
    )
    return