import yfinance as yf
import requests
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

def get_gdp_growth(year):
    url = f"https://api.worldbank.org/v2/country/US/indicator/NY.GDP.MKTP.KD.ZG?date={year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            return float(data[1][0]["value"])
        except (KeyError, IndexError, TypeError):
            pass
    return 1

def get_vix_at_date(date):
    vix = yf.Ticker("^VIX")
    vix_data = vix.history(start=date.strftime("%Y-%m-%d"), end=(date + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    return float(vix_data["Close"].iloc[-1]) if not vix_data.empty else 1

def get_pe_ratio(ticker):
    stock = yf.Ticker(ticker)
    try:
        pe_ratio = stock.info.get("trailingPE", 1)
        return float(pe_ratio) if pe_ratio else 1
    except:
        return 1

def get_revenue_growth(ticker):
    stock = yf.Ticker(ticker)
    try:
        revenue_growth = stock.info.get("revenueGrowth", 1)
        return float(revenue_growth) if revenue_growth else 1
    except:
        return 1

def get_max_min_changes(ticker):
    stock = yf.Ticker(ticker)
    df = stock.history(period="10y")
    df["Change"] = df["Close"].pct_change() * 100
    max_change_date = df["Change"].idxmax()
    min_change_date = df["Change"].idxmin()
    return max_change_date, df.loc[max_change_date, "Change"], min_change_date, df.loc[min_change_date, "Change"]

def plot_doughnut_charts(max_gdp, current_gdp, max_revenue, current_revenue, max_pe, current_pe, max_vix, current_vix):
    values = {
        "GDP Growth": (current_gdp, max_gdp),
        "Revenue Growth": (current_revenue, max_revenue),
        "PE Ratio": (current_pe, max_pe),
        "VIX": (current_vix, max_vix)
    }

    colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.flatten()

    for i, (metric, (current, maximum)) in enumerate(values.items()):
        if not maximum or np.isnan(maximum) or maximum <= 0:
            maximum = 1
        if not current or np.isnan(current) or current < 0:
            current = 0

        fraction = current / maximum
        axes[i].pie(
            [fraction, 1 - fraction],
            labels=[f"Current ({fraction*100:.1f}%)", "Remaining"],
            autopct='%1.1f%%',
            startangle=140,
            colors=[colors[i], "#e0e0e0"],
            wedgeprops={'edgecolor': 'black'}
        )

        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        axes[i].add_artist(centre_circle)
        axes[i].set_title(f"{metric}: {current:.2f} / {maximum:.2f}", fontsize=14)

    plt.suptitle("Current vs Historical Max: Market Indicators", fontsize=16, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

def predict_stock_change(ticker):
    max_date, max_change, min_date, min_change = get_max_min_changes(ticker)
    past_gdp_max = get_gdp_growth(max_date.year)
    past_vix_min = get_vix_at_date(min_date)
    past_revenue_growth = get_revenue_growth(ticker)
    past_pe_ratio = get_pe_ratio(ticker)

    current_gdp = get_gdp_growth(datetime.datetime.now().year)
    current_vix = get_vix_at_date(datetime.date.today())
    current_revenue_growth = get_revenue_growth(ticker)
    current_pe = get_pe_ratio(ticker)

    score = (.25 * (max_change / past_vix_min) * current_vix) +             (.25 * (max_change / past_revenue_growth) * current_revenue_growth) +             (.25 * (max_change / past_pe_ratio) * current_pe) +             (.25 * (max_change / past_gdp_max) * current_gdp)

    print(f"Prediction Analysis for {ticker}:")
    print(f"- Max One-Day Change: {max_change:.2f}% on {max_date.date()}")
    print(f"- Min One-Day Change: {min_change:.2f}% on {min_date.date()}")
    print()
    print(f"- Predicted Change for Tomorrow: {score:.2f}%")
    plot_doughnut_charts(past_gdp_max, current_gdp, past_revenue_growth, current_revenue_growth, past_pe_ratio, current_pe, past_vix_min, current_vix)

if __name__ == "__main__":
    ticker_symbol = input("Enter Stock Ticker (e.g., AAPL, TSLA, MSFT): ").upper()
    predict_stock_change(ticker_symbol)