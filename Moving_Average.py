import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from datetime import datetime

def moving_average_difference(ticker):
    btn = Button(root, text=ticker, command=lambda: moving_average_difference(ticker))
    btn.pack(side="top")
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    # Retrieve historical data for the stock
    data = yf.download(ticker, start='2022-01-01', end=current_date)
    
    # Calculate the 50-day moving average
    data['50ma'] = data['Close'].rolling(window=50).mean()
    
    # Calculate the 200-day moving average
    data['200ma'] = data['Close'].rolling(window=200).mean()
    
    # Calculate the difference between the moving averages
    data['difference'] = data['200ma'] - data['50ma']
    data = data.iloc[-30:] # Select last rows 
    plt.clf()
    plt.plot(data['difference'])
    plt.xlabel('Date')
    plt.ylabel('Difference')
    plt.title('( ' + ticker.upper() + ' )' + '\nDifference between 50MA and 200MA')
    plt.show()
    return data

# GUI build
root = Tk()
root.title("Stock Analysis")
root.geometry("400x200")

# Create a label and an entry widget to enter the stock ticker
ticker_label = Label(root, text="Enter the stock ticker:")
ticker_entry = Entry(root)

# Submit button
submit_button = Button(root, text="Submit", command= lambda: moving_average_difference(ticker_entry.get()))

# History Label
ticker_history = Label(root, text="History:")

# Widget pack
ticker_label.pack()
ticker_entry.pack()
submit_button.pack()
ticker_history.pack(side="top")

# Run
root.mainloop()


