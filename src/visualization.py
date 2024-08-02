import matplotlib.pyplot as plt
import seaborn as sns

def pairplt(dataframe):
    plt.figure(figsize=(8,6))
    sns.pairplot(dataframe)
    plt.savefig(fname=r'C:\Users\nirik\myfiles\myprojects\machine learning\DBSCAN\plots\data_pairplot.jpg')
    plt.show()

def scatterplt(df):
    plt.title('scatter plot with pca features')
    sns.scatterplot(x='component 1',y='component 2',data=df)
    plt.savefig(fname=r'C:\Users\nirik\myfiles\myprojects\machine learning\DBSCAN\plots\pca_scatterplot.jpg')
    plt.show()
    
def scatter_cluster(df,pred):
    plt.title('scatter plot with clusters')
    sns.scatterplot(x='component 1',y='component 2',c=pred,data=df)
    plt.savefig(fname=r'C:\Users\nirik\myfiles\myprojects\machine learning\DBSCAN\plots\clusters.jpg')
    plt.show()