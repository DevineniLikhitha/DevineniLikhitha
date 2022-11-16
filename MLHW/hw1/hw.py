import pandas as pd
import matplotlib.pyplot as plt
import itertools
import termplotlib as tpl

class readdata:
    def __init__(self,data):
    
        self.df=pd.read_table(data,header=None,sep=",")
        self.df.columns=["sepallength","sepalwidth","petallength","petalwidth","species"]
        print(self.df)
        
        
        '''Question 2'''
    def count_rows_columns(self):
        #print no.of rows
        rows = len(self.df)
        print("No. rows are->", rows)

        #print the no.of columns

        columns = len(self.df.columns)

        print("No.of Columns are->", columns)
        
        
        '''queston 3'''
    def last_column(self):
        
        
        #Getting values of lastcolumn
        last_column = self.df.iloc[: , -1]
        print(last_column)

        #distinct values from the last column

        distinct=self.df.species.unique()
        print("unique values of lastcolumn->",distinct)
        
        '''Question 4'''
    def iris_setosa(self):
        
        #getting the data of iris-setosa
        irissetosa = self.df.loc[self.df["species"]=="Iris-setosa"]

        #printing the data that have last columns as iris-setosa
        print(irissetosa)


        #count no.of rows that have iris-setosa
        iris_setosa_rows=len(irissetosa)

        #printing the no.of rows that iris-setos as last column
        print("No.of iris-setosa rows->",iris_setosa_rows)

        #Average of first column

        avg = irissetosa['sepallength'].mean()
        print("average of first column->", avg)

        #printing the maximum value of second column
        maximum= irissetosa['sepalwidth'].max()

        print("Maximum value of second column->",maximum )

        #printing the minimum value of third column
        minimum = irissetosa['petallength'].min()

        print("Minimum value of third column->", minimum)
        
        '''question 5'''
    def scatter_plot(self):
        
        #grouping the category
        categories= self.df.groupby("species")

        #giving shapes to the categories
        marker = itertools.cycle(('+','o','<'))
        
        #scatter plot according to groups between sepallength(firstcolumns) and sepalwidth(secondcolum)
        for name, group in categories:
            plt.plot(group["sepallength"],group["sepalwidth"],marker=next(marker), linestyle="", label=name, )
        plt.legend()
        plt.show()
        
        
#calling the methods

data=readdata('iris.data.txt')
data.count_rows_columns()
data.last_column()
data.iris_setosa()
data.scatter_plot()

