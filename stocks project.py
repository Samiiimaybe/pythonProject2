# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings
import yfinance as yf


print("My script starting")
ticker=yf.Ticker('SBUX').info
print(ticker)
print("My script completed")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
