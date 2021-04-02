import pandas as pd
import numpy as np
from numpy import *
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")



dataset = pd.read_csv("Corona_NLP_test.csv")

sentiment = dataset["Sentiment"]

#print('Describe: ',dataset.describe())


sentiment = sentiment.replace(['Positive', 'Negative', 'Neutral', 'Extremely Positive', 'Extremely Negative'],
                              ['1', '-1', '0', '10' ,'-10'])
        
dataset['Sentiment score'] = sentiment
      

""" Taking analytic look at the dataset, you can see that only 'TweetAt and Sentiment have 'unifrom trends'

* Username & ScreenName are more or less indexes - they are not decisive factors here

The most significant plots you can make would only be of Location, TweetAt (time of tweet) and the Sentiment score"""


dataset["Sentiment"].value_counts().plot(kind='pie', autopct='%1.0f%%').get_figure().savefig('COVID-19 Sentiment (Pie plot)')
""" You can see from this pie chart you have more of negative opinions that others, with Positive being close to it
Other are apparently the same. """

""" Let's now see one for Time of Tweet. That is, to know their views at a particular time"""
Time_Sentiment = dataset.groupby(['TweetAt', 'Sentiment']).Sentiment.count().unstack()

Time_Sentiment.plot(kind='bar').get_figure().savefig('COVID-19 Sentiment (Bar plot)')

""" So, using KDE plot to get the probailistic view of how their opinions will go over time """
Time_Sentiment.plot(kind='kde').get_figure().savefig('COVID-19 Sentiment (KDE plot)')






""" Some statistical analyis here: """

Statistical_Analysis_1 = pd.DataFrame(columns = ['Tweet count'])

Statistical_Analysis_1['Tweet count'] = dataset.groupby('TweetAt')['Sentiment'].count()

Statistical_Analysis_2 = pd.DataFrame(columns = ['count'])
Statistical_Analysis_2['count'] = dataset.groupby('Sentiment')['TweetAt'].count()

Statistical_Analysis_1.to_excel('Statistical Analysis 1.xlsx')
Statistical_Analysis_2.to_excel('Statistical Analysis 2.xlsx')



