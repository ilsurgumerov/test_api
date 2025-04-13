def custom_mapping(X):
    X = X.copy()

    X['Gender'] = X['Gender'].map({'Male': 1, 'Female': 0})
    X['Vehicle_Age'] = X['Vehicle_Age'].map({'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2})
    X['Vehicle_Damage'] = X['Vehicle_Damage'].map({'Yes': 1, 'No': 0})

    return X

def custom_policy_grouped(X):
    # ТУТ ПРОБЛЕМА, НАДО СОХРАНИТЬ top_channels, rare mean из обучающей выборки
    # так как без этого для предикта тут все будет ломаться
    
    X = X.copy()

    if "Policy_Sales_Channel" not in X.columns:
        return X

    # Создаем новый столбец, где все редкие значения заменяются на mean
    top_channels = X["Policy_Sales_Channel"].value_counts().nlargest(3)

    rare_mask = ~X["Policy_Sales_Channel"].isin(top_channels)
    rare_mean = int(X.loc[rare_mask, "Policy_Sales_Channel"].mean())
    
    top_channels_list = top_channels.index.tolist()
    X["Policy_Sales_Channel_Grouped"] = X["Policy_Sales_Channel"].apply(lambda x: x if x in top_channels_list else rare_mean)
    
    X.drop(columns=['Policy_Sales_Channel'])

    return X

def drop_columns(X):
    return X.drop(columns=['id', 'Region'], errors='ignore')