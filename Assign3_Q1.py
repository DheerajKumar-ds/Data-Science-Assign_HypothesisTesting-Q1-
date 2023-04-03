# -*- coding: utf-8 -*-


import numpy as np
import pandas as pd

df = pd.read_csv("Cutlets.csv")

#Applying Descriptive Statistics
df.describe()

#Checking for Null Values
df.isnull().sum()

#Checking for Duplicate Values
df[df.duplicated()].shape

#Checking the data type
df.info()

#Plotting the data
import matplotlib.pyplot as plt
import seaborn as sns

#Boxplot
plt.subplots(figsize = (9,6))
plt.subplot(1,2,1)
plt.boxplot(df['Unit A'])
plt.title('Unit A')
plt.subplot(1,2,2)
plt.boxplot(df['Unit B'])
plt.title('Unit B')
plt.show()

#Histogram
plt.subplots(figsize = (9,6))
plt.subplot(121)
plt.hist(df['Unit A'], bins = 15)
plt.title('Unit A')
plt.subplot(122)
plt.hist(df['Unit B'], bins = 15)
plt.title('Unit B')
plt.show()

#Conducting Two sample Z test
from scipy import stats
zcalc, pval = stats.ttest_ind(df["Unit A"], df["Unit B"])
print("Z statististical value : ", zcalc.round(3))
print("p value : ", pval.round(3))

#Interpreting P value

alpha = 0.025
print('Significnace=%.3f, p=%.3f' % (alpha, pval))
if pval <= alpha:
    print('Ho is rejected & H1 is accepted')
else:
    print('Ho is accepted & H1 is rejected')

