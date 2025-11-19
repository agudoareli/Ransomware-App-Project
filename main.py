from trendsAPI import TrendsAPI  # import the API class
from ransomwareApp import RansomwareApp  # import the GUI class 

# FIXME expand the wanrning signs and preventon tips 

if __name__ == "__main__":  # prevents the main from being imported through a library and being auto executed
    app = RansomwareApp()
    app.launch()


