# import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from pandas import read_csv

# Đọc file csv
df = pd.read_csv('AMD.csv')

# vẽ bảng 
<<<<<<< HEAD

=======
>>>>>>> d26b5e0656626a2fea18251bf75913cdf4852f01
df.plot(figsize=(10, 5))
plt.title('AMD', fontsize = 16)
plt.ylabel('Price', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
<<<<<<< HEAD
plt.show()
=======
plt.show()
>>>>>>> d26b5e0656626a2fea18251bf75913cdf4852f01
