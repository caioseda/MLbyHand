import pandas as pd 
import matplotlib.pyplot as plt

#importação dos dados
def importa_dados(link: str, columns: list):
    
    df = pd.read_csv(link, names=columns)
    
    X = df.iloc[:,:-1].values
    y = df.iloc[:,-1].values
    
    return X, y

def plot(X,y):
    plt.scatter(X,y,marker='x',c='red',alpha=0.3)
    plt.xlabel("População da cidade em 10.000")
    plt.ylabel("Lucros em 10.000")