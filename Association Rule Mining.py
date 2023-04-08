import pandas as pd 
import matplotlib.pyplot as plt
from efficient_apriori import apriori 

s=float(input("Enter Min Support : "))
c=float(input("Enter Min Confidence : "))

df=pd.read_csv("Grocery Products Purchase.csv")
print("The Dataframe is: ")
print(df)
print()

txns=df.values.reshape(-1).tolist()


df_list=pd.DataFrame(txns)
df_list['Count']=1

df_list=df_list.groupby(by=[0], as_index=False).count()
df_list=df_list.sort_values(by=['Count'], ascending=True)

df_list=df_list.rename(columns={0 : 'Item'})

most_pop=df_list[len(df_list)-10:len(df_list)]
print("The Top 10 Most Popular Items are: ")
print(most_pop)

plt.ylabel('Item Name')
plt.xlabel('Count')
plt.barh(most_pop['Item'], width=most_pop['Count'])
   
plt.show()
txns2=df.stack().groupby(level=0).apply(list).tolist()
print(txns2)
print()




itemsets, rules = apriori(txns2, min_support=s, min_confidence=c,verbosity=1)

print("The Strong association Rules are: ")
for i in itemsets:
    print("Itemsets of Size",i,"Satisfying the Support")
    for j in itemsets[i]:
        print(j)
    print()    
print(rules)

