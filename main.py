from trendsAPI import TrendsAPI  # import my API class
from ransomwareApp import RansomwareApp  # import my GUI class 

if __name__ == "__main__":  # prevents the main from being imported through a library and being auto executed
    app = RansomwareApp()
    app.launch()
# To run from the vsc terminal > cd into the folder > source gr/bin/activate > python main.py 

