import numpy as np
import pandas as pd
import joblib

#Modellen som blir brukt på nettsiden
model = joblib.load('models/ferdig_model_huspris.joblib')

def preprocess(data):

    feature_values = {
        'MSSubClass': 20, 
        'MSZoning': 3, 
        'LotArea': 10517, 
        'Street': 1, 
        'LotShape': 3, 
        'LandContour': 3, 
        'Utilities': 0, 
        'LotConfig': 4, 
        'LandSlope': 0, 
        'Neighborhood': 12,
        'Condition1': 2, 
        'Condition2': 2, 
        'BldgType': 0, 
        'HouseStyle': 2, 
        'OverallQual': 5, 
        'OverallCond': 5, 
        'YearBuilt': 1971, 
        'YearRemodAdd': 1984, 
        'RoofStyle': 1, 
        'RoofMatl': 1, 
        'Exterior1st': 12,
        'Exterior2nd': 13, 
        'MasVnrType': 2, 
        'MasVnrArea': 103, 
        'ExterQual': 3, 
        'ExterCond': 4, 
        'Foundation': 2, 
        'BsmtFinSF1': 444, 
        'BsmtFinSF2': 47, 
        'BsmtUnfSF': 567, 
        'TotalBsmtSF': 1058, 
        'Heating': 1,
        'HeatingQC': 0, 
        'CentralAir': 1, 
        'Electrical': 4, 
        '_1stFlrSF': 1163, 
        '_2ndFlrSF': 347, 
        'LowQualFinSF': 6, 
        'GrLivArea': 1516, 
        'BsmtFullBath': 1, 
        'BsmtHalfBath': 0, 
        'FullBath': 2, 
        'HalfBath': 0,
        'BedroomAbvGr': 3, 
        'KitchenAbvGr': 1, 
        'KitchenQual': 3, 
        'TotRmsAbvGrd': 7, 
        'Functional': 6, 
        'Fireplaces': 1, 
        'GarageCars': 2, 
        'GarageArea': 473, 
        'PavedDrive': 2, 
        'WoodDeckSF': 94,
        'OpenPorchSF': 46, 
        'EnclosedPorch': 0, 
        '_3SsnPorch': 0, 
        'ScreenPorch': 0, 
        'PoolArea': 0, 
        'MiscVal': 43, 
        'MoSold': 6, 
        'YrSold': 2008, 
        'SaleType': 8, 
        'SaleCondition': 4 
    }

    # Parse the form inputs and return the defaults updated with values entered.
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values

def predict(data):
    # Navnet på de ulike attributtene:
    column_order = ['MSSubClass', 'MSZoning', 'LotArea', 'Street', 'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood',
    'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'OverallQual', 'OverallCond', 'YearBuilt', 'YearRemodAdd', 'RoofStyle', 'RoofMatl', 'Exterior1st',
    'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterQual', 'Foundation', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', 'Heating',
    'HeatingQC', 'CentralAir', 'Electrical', '_1stFlrSF', '_2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath',
    'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual', 'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'GarageCars', 'GarageArea', 'PavedDrive', 'WoodDeckSF',
    'OpenPorchSF', 'EnclosedPorch', '_3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 'MoSold', 'YrSold', 'SaleType', 'SaleCondition' ]

    data = np.array([data[feature] for feature in column_order], dtype=object)
    pred = model.predict(data.reshape(1,-1))
    return pred

    
def postprocess(prediction):

    # Gjør om til int for å få vekk komma, deretter til string
    predictionString = str(int(prediction[0]))

    # Returnerer
    return_dict = {'pred': predictionString}
    return return_dict