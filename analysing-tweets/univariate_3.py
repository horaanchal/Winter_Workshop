#Compare and analyze probability mass functions (PMFs) of features (b,c,d) through PMF plots. Draw all PMF plots in same graph. You should draw the PMF plot using matplotlib module of python.
import numpy as np
import pandas as pd
import csv
from scipy.stats import binom
import matplotlib.pyplot as plt
df = pd.read_csv('SrBachchan_tweets.csv')
print (df)

x = df['length']
y = df['mention_count']
plt.plot(x,y)
plt.show()

fig, ax=plt.subplots(1,1)
n,p=100,0.4

