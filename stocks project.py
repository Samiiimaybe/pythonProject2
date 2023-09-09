# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
import yfinance as yf


print("My script starting")
#It gives latest stock information for any particular stock
#ticker=yf.Ticker('SBUX').info

#It prints the data that we got from Yfinance for the stock
#print(ticker)

#we are entering start date and end date for the time period which we want the data for
start_date = '2021-01-01'
end_date = '2023-08-25'
ticker = 'AAPL'
data = yf.download(ticker,start_date,end_date)
print("we are printing 1st 5 rows of stocks")

