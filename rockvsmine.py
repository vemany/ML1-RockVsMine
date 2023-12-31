
#Importing Variables
import numpy as np #for arrays ---> row/column - 1 Dimensional
import pandas as pd #for data processing steps
from sklearn.model_selection import train_test_split #splits data into train and test data --> example and results
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score #for accuracy of the model

#() to recall function
#[] to extract data

#Loading Sonar Data dataset to a pandas Dataframe
sonar_data = pd.read_csv('/Sonar data.csv', header = None) #head = name of the coloums in the dataset

sonar_data.head() #shows the first 5 rows of the dataset

#Number of rows and coloums
sonar_data.shape

#basic stats - mean,std,percentiles,etc
sonar_data.describe()

sonar_data[60].value_counts() #how many rocks and mines in the dataset

sonar_data.groupby(60).mean()

#separate data(0-59) and labels(60)
X = sonar_data.drop(columns=60, axis=1)#all columns except the last(60th), axis = 1 for column & 0 for row
Y = sonar_data[60]#just the 60th

print(X)
print(Y)

#Training and Test Data
#Training data is what the computer uses to find a pattern with all the data, test is what it uses to see if the pattern it found is correct
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)#80:20 split
print(X.shape, X_train.shape, X_test.shape)#number of rows and columns
print(X_train)
print(Y_train)

#Logistic regression --> finds the relationship between 2 data factors
model = LogisticRegression()

#training the Logistic Regression model with training data
model.fit(X_train, Y_train)

#Model Evaluation#
#accuracy of training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on training data : ', training_data_accuracy)#accuracy should be as close to 1 as possible

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy on test data : ', test_data_accuracy)#accuracy should be as close to 1 as possible

#Making a Predictive System
input_data = (0.0090,0.0062,0.0253,0.0489,0.1197,0.1589,0.1392,0.0987,0.0955,0.1895,0.1896,0.2547,0.4073,0.2988,0.2901,0.5326,0.4022,0.1571,0.3024,0.3907,0.3542,0.4438,0.6414,0.4601,0.6009,0.8690,0.8345,0.7669,0.5081,0.4620,0.5380,0.5375,0.3844,0.3601,0.7402,0.7761,0.3858,0.0667,0.3684,0.6114,0.3510,0.2312,0.2195,0.3051,0.1937,0.1570,0.0479,0.0538,0.0146,0.0068,0.0187,0.0059,0.0095,0.0194,0.0080,0.0152,0.0158,0.0053,0.0189,0.0102)

# changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the np array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]=='R'):
  print('The object is a Rock')
else:
  print('The object is a Mine')

