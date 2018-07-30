from sklearn.ensemble import RandomForestClassifier
import pandas as pd 
import csv

df = pd.read_csv('SrBachchan_tweets.csv')

#Splitting data into training and test set
from sklearn.model_selection import train_test_split
training_partition, test_partition = train_test_split(df, test_size = 0.2) ## Split 20% of the data to test set


'''
Building the training set
'''
train = training_partition[['length','hashtag_count', 'mention_count','likes_count','retweet_count','sentiment']]


'''
Building the test set
'''
train = training_partition[['length','hashtag_count', 'mention_count','likes_count','retweet_count','sentiment']]


#Shape of the training and test set
print "Length of training data: ",train.shape
print "Length of the test partition: ",test_partition.shape


exit()

#Appying the classifier from sklearn
from sklearn.ensemble import  RandomForestClassifier

alg = RandomForestClassifier()   #Load the estimator

alg.fit(train, labels)		#Fit the estimator

result = alg.predict(test_set)

#Results of the prediction
print result


#Predicting the probability values from the test set
print alg.predict_proba(test_set)

#The order of classes
#0 -> NotSpam		1 -> Spam
print alg.classes_

#Get accuracy score
from sklearn.metrics import accuracy_score
print "Accuracy score: ",accuracy_score(true_labels,result)
