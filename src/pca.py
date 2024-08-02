from sklearn.decomposition import PCA
import pandas as pd

pca=PCA(n_components=2,random_state=42)
def apply_pca(df):
    pca_=pca.fit_transform(df)
    pca_data=pd.DataFrame(pca_,columns=['component 1','component 2'])
    return pca_data