import gradio as gr  # creates the UI 
from pytrends.request import TrendReq  # the Google Trends API
import matplotlib.pyplot as plt  # draws the chart 
import pandas as pd  # fills the chart with data 
import time  # controls delays (avoid rate limits)
from datetime import datetime  # for date/time manipulations



class TrendsAPI:
    def __init__(self):
        self.region_choices = {
            "U.S.": "US",
            "Canada": "CA",
            "Mexico": "MX",
            "Worldwide": ''
        }
        
    def fetch_google_trends(self, keyword, geo=""):
        try:
            pytrends = TrendReq(hl='en-US', tz=360, retries=3, backoff_factor=0.5) 
            pytrends.build_payload([keyword], timeframe='today 12-m', geo=geo)  
            data = pytrends.interest_over_time()  # fetches the data with the given payload
        except Exception as e:
            print("Error: ", e)
            return "", f"Error fetching data from Google Trends: {str(e)}"    # analyzeKeyword() expects 2 values 
        if data.empty:
            return "", f"No data available for '{keyword}'. Please try another keyword."
        # plotting the chart outline using matplotlib and pandas 
        plt.figure(figsize=(10, 4))
        plt.plot(data.index, data[keyword], color='blue', label=keyword)
        plt.title(f"Google Trends: {keyword}")
        plt.xlabel("Date")
        plt.ylabel("Relative Search Interest (%)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plot_path = "trend_plot.png"
        plt.savefig(plot_path)
        plt.close()
        return plot_path, f"This chart is displaying relative search interest of {keyword} over the last 12 months. {keyword} was searched the most on {data[keyword].idxmax().date()}."