"""
Created on Fri Oct 30 10:50:30 2020

@author: gunnarschmidtmann
"""
# Gunnar Schmidtmann, University of Plymouth, November 2020
# Create a subfolder 'Data'
# import required packages

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import norm


# read in 'shoe_size1.csv' file 
df = pd.read_csv('Data/shoe_size1.csv', usecols=['Sex','Shoe Size.1'])

# extract male and female data
male = df.loc[df['Sex'] == 1]
female = df.loc[df['Sex'] == 2]


# plot scatter plots
plt.figure(1)
plt.plot(male['Shoe Size.1'],'og',label='male')
plt.plot(female['Shoe Size.1'],'or',label='female')
plt.legend()
plt.xlabel('Subjects',fontsize=20)
plt.ylabel('Shoe Size',fontsize=20)
plt.grid(True)
plt.savefig('scatter.eps', format='eps')
plt.show() 

# calculate parameters for normal distribution
mean_male, std_male=norm.fit(male['Shoe Size.1'])
mean_female, std_female=norm.fit(female['Shoe Size.1'])


# fit normal distribution
plt.figure(2)
sns.set_style("whitegrid")
sns.distplot(male['Shoe Size.1'],fit=norm,bins=10,kde=False,color='g')
sns.distplot(female['Shoe Size.1'],fit=norm,bins=10,kde=False,color='r')
plt.xlabel('Shoe Size',fontsize=20)
plt.ylabel('Frequency',fontsize=20)
plt.xlim(0, 15)
plt.savefig('histfit.eps')
plt.show()
