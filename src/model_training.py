import pickle
from sklearn.cluster import DBSCAN

def apply_dbscan(df):
    dbscan=DBSCAN(eps=0.5,min_samples=5)
    pred=dbscan.fit_predict(df)
    pickle.dump(dbscan,open(r'C:\Users\nirik\myfiles\myprojects\machine learning\DBSCAN\trained models\model.pkl','wb'))
    return pred