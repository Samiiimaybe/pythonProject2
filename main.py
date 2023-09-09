# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("My script starting")
#It gives latest stock information for any particular stock
#ticker=yf.Ticker('SBUX').info

#It prints the data that we got from Yfinance for the stock
#print(ticker)

#we are entering start date and end date for the time period which we want the data for
start_date = '2021-01-01'
end_date = '2022-12-8'
ticker = 'AAPL'
data = yf.download(ticker,start_date,end_date)
print("we are printing 1st 5 rows of stocks")

#prints the 1st 5 rows of the data
print(data.head())

print("we are printing the last 5 rows of stocks")
#prints the last 5 rows of the data
print(data.tail())
print("My script completed")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#xaxis = np.array([8,12,16])
# yaxis = np.array([6,9,12])

#  plt.plot(xaxis,yaxis)
# plt.show()


data['Adj Close'].plot()
plt.show()
