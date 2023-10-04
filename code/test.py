# import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from pandas import read_csv

# Đọc file csv
df = pd.read_csv('AMD.csv')

# vẽ bảng 
df.plot(figsize=(10, 5))
plt.title('AMD', fontsize = 16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
