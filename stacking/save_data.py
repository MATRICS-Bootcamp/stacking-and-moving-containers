import pandas as pd
import pickle
iris_df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

iris_df.to_csv("iris_df.csv",index=False)

with open("iris.pkl","wb") as file:
    pickle.dump(iris_df,file)

print("Data saved!")
