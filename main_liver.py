import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.model_selection import GridSearchCV
np.random.seed(42)
import pickle

# load data
liver_df = pd.read_csv(r"indian_liver_patient.csv")

# view sample from the data 
#print(liver_df.head(3)) #by defult = 5

# handle missing data
#print(liver_df.info())
#print(liver_df.isna().sum())

#print(liver_df["Albumin_and_Globulin_Ratio"])
avarage_AGR =liver_df["Albumin_and_Globulin_Ratio"].mean() 

liver_df["Albumin_and_Globulin_Ratio"].fillna(avarage_AGR , inplace=True)
#print(liver_df.isna().sum())


# map labled data to number 
liver_df["Gender"] = liver_df["Gender"].map({"Female": 0 , "Male":1 })
print(liver_df.head())

x = liver_df.drop("Dataset" , axis =1)
y = liver_df["Dataset"]


# split data to train/test
x_train , x_test , y_train , y_test = train_test_split(x ,y , test_size=0.3)     # test by 30%


# choose modle (estimator)
model = svm.SVC(kernel = 'rbf' , C =1 , gamma = 0.01) 

# train (input , output)
model.fit(x_train , y_train )

# validate modle 
print(model.score(x_train , y_train))
print(model.score(x_test , y_test))

'''
# tune modle prams
prams = {"kernel":('linear','rbf') , 'C' : [1 ,20] , 'gamma': [ 0.1 , 0.01 , 0.2 , 0.03 , 0.07]}   # c --> line    # kernel --> shape of line
grid = GridSearchCV(svm.SVC(),prams , verbose = 2)   
grid.fit(x_train,y_train)
print(grid.best_params_)
print(grid.best_score_)
'''
# save model
pickle.dump(model , open(r"F:\python ml\projects\Liver Disease\liversavemo.pkl","wb"))





















