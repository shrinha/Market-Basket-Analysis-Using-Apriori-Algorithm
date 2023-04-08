# Market-Basket-Analysis-Using-Apriori-Algorithm
Uses Association Rule Mining By Apriori Algorithm to Generation Strong Correlations between products purchased
>This was done as a project under the Course CS250 : Artificial Intelligence Lab in Spring Semester, 2023

## The Dataset
The Project learns from a csv file called Grocery Products Purchase.csv.
Each row corresponds to a consumer buying a set of products. The products are layed across columns - upto a maximum of 32 items.
The entire data was collected for 9835 customers, accounting for the same number of rows.

## Input
* The minimum support that the itemsets generated must satisfy
* The minimum confidence that association rules must satisfy

## Output 
* The dataframe made by the dataset
* Most Frequent Items and bar plot associated with it
* Frequent Itemsets Satisfying the Support
* Strong Association Rules Generated

## Code

### 1. Import the Libraries
https://github.com/shrinha/Market-Basket-Analysis-Using-Apriori-Algorithm/blob/01947eb2605ddf78895499ed7ece68a3b329f53f/Association%20Rule%20Mining.py#L1-L3

### 2. Read The Dataset and Create the Dataframe
https://github.com/shrinha/Market-Basket-Analysis-Using-Apriori-Algorithm/blob/01947eb2605ddf78895499ed7ece68a3b329f53f/Association%20Rule%20Mining.py#L8-L22

### 3. Transform the Dataset on the basis of Item frequency to plot bar
https://github.com/shrinha/Market-Basket-Analysis-Using-Apriori-Algorithm/blob/01947eb2605ddf78895499ed7ece68a3b329f53f/Association%20Rule%20Mining.py#L24-L32

### 4. Use the Apriori Algorithm
Generate the frequent itemsets using the apriori library and from them find the confidence values and strong association rules

https://github.com/shrinha/Market-Basket-Analysis-Using-Apriori-Algorithm/blob/01947eb2605ddf78895499ed7ece68a3b329f53f/Association%20Rule%20Mining.py#L40-L48



