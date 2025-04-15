def custom_mapping(X):
    X = X.copy()

    X['Gender'] = X['Gender'].map({'Male': 1, 'Female': 0})
    X['Vehicle_Age'] = X['Vehicle_Age'].map({'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2})
    X['Vehicle_Damage'] = X['Vehicle_Damage'].map({'Yes': 1, 'No': 0})

    return X

def drop_columns(X):
    return X.drop(columns=['id', 'Region', 'Policy_Sales_Channel', 'Driving_License', 'Vintage'], errors='ignore')