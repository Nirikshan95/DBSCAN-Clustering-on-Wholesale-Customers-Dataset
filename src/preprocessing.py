from sklearn.preprocessing import StandardScaler

def scale(dataframe):
        ss=StandardScaler()
        scaled_data=ss.fit_transform(dataframe)
        return scaled_data