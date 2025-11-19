import gradio as gr  # creates the UI 
from pytrends.request import TrendReq  # the Google Trends API
import matplotlib.pyplot as plt  # draws the chart 
import pandas as pd  # fills the chart with data 
import time  # controls delays (avoid rate limits)
from datetime import datetime  # for date/time manipulations



class TrendsAPI:
    def __init__(self):
        pass  # no class-level variables necessary

    def fetch_google_trends(self, keyword):
        try:
            pytrends = TrendReq(hl='en-US', tz=360) # sets language and timezone
            pytrends.build_payload([keyword], timeframe='today 12-m') # prepares the request by passing in key-words and timeframe
            time.sleep(2) # pause the program for 2sec to avoid overlaping and crashing
            data = pytrends.interest_over_time()  # fetches the data with the given payload
        except Exception as e:
            return f"Error fetching data from Google Trends: {str(e)}"
        if data.empty:
            return f"No data available for '{keyword}'. Please try another keyword."
        # plotting the chart outline using matplotlib and pandas 
        plt.figure(figsize=(10, 4))
        plt.plot(data.index, data[keyword], color='blue', label=keyword)
        plt.title(f"Google Trends: {keyword}")
        plt.xlabel("Date")
        plt.ylabel("Relative Search Interest (0-100)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plot_path = "trend_plot.png"
        plt.savefig(plot_path)
        plt.close()
        return plot_path, f"This chart is displaying relative search interest of {keyword} over the last 12 months. {keyword} was searched the most on {data[keyword].idxmax().date()}."
        ####
        # FIXME in the information tab use another api to give the user a definion of the keyword they search 
