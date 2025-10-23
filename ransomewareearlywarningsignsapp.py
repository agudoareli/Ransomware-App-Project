# An educational app that combines technical warning signs with real-world spikes in public attention.
!pip install gradio --quiet
!pip install pytrends --quiet # python API for google trends
import gradio as gr # imports gradio and calls it gr
from pytrends.request import TrendReq # allows us to get data from google trends
import matplotlib.pyplot as plt # used to make charts and save them as images
import pandas as pd # helps us work with data tables
from datetime import datetime # helps us work with date and time
import time 

class TrendsAPI:
  def __init__(self):
    self.request = TrendReq(hl='en-US', tz=360)

  def _fetch_google_trends(self, keyword): # define a function to fetch the google trends using a keyword
    self.request.build_payload([keyword], cat=0, timeframe='today 12-m', geo='', gprop='')
    time.sleep(2)
    # [keyword]: a list of the search term
    # cat=0: no specific category
    # timeframe='today 12-m': search from the last 12 months of data
    # geo='': no specific country
    # gprop='': no search filter, search from any info source
    data = self.request.interest_over_time() # downloads the trend data as a table, rows = days/weeks, cols = the frequency of search for the keyword
    time.sleep(2)
    if not data:
      return "No data available for this keyword."
    # Plotting the data
    plt.figure(figsize=(10, 4)) # make a chart, 10 cols, 4 rows
    plt.plot(data.index, data[keyword], label=keyword)  # draws a line on the chart and plots the dates, how popular the keyword was per date, adds a label
    plt.title(f"Google Trends: {keyword}")  # adds a title to the top of the chart
    plt.xlabel("Date")  # labels the x axis as Date
    plt.ylabel("Interest")  # labels the y axis as interest
    plt.grid(True)  # adds grid lines to teh chart
    plt.tight_layout()  # makes sure nothing in the chart is cut off or overlapping
    plot_filename = "trend_plot.png"  # choose a file name before saving the chart
    plt.savefig(plot_filename)  # save the chart as a png
    plt.close() # remove the chart from memory
    return f"Trend data for '{keyword}' shown below.", plot_filename  # show the user a message and the image file that was saved

  def fetch_google_trends_safely(self, keyword):
    return self._fetch_google_trends(keyword)
    # try:
    #   result = self._fetch_google_trends(keyword)
    #   return result 
    # except:
    #   return "Too many calls, please wait 15 seconds and try again."


