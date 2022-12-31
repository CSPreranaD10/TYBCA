import pandas as pd 
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

#Read the dataset 
df = pd.read_csv('iris.data.csv')

#Data preprocessing 
df.columns = ["Sepal length", "Sepal width", "Petal length", "Petal width", "Class"]
print(df.head()) 

#Convert the dataset into a list of lists
transactions = []
for i in range(0, df.shape[0]):
    transactions.append([str(df.values[i,j]) for j in range(0,5)])

#Create Apriori model
frequent_itemsets = apriori(transactions, min_support = 0.05, max_len = 3, 
                            use_colnames = True)

#Results 
frequent_itemsets.head()

#Generate the rules 
rules = association_rules(frequent_itemsets, metric ="lift", min_threshold = 1)
rules.head()

#slip 10
