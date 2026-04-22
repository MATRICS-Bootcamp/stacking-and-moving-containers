import pandas as pd
import pickle

iris_df = pd.read_csv("iris_df.csv")
print("Rows in DF: "+str(len(iris_df)))

with open("iris.pkl","rb") as file:
    pkl_df = pickle.load(file)

print("Rows from Pickle: "+str(len(iris_df)))
