from estimator.rmse import Rmse
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from model.sarima import Sarima
from model.autoreg import Autoreg
from grid.grid_model import GridModel
from grid.grid_search import GridSearch
import pandas as pd
import utils

N_CLUSTERS = 10

water_consumptions = pd.read_csv('./src/data/water_consumption_100_clusters.csv', sep=',')

print(water_consumptions.head())

sarima_params_grid = {
    'order': [(1, 0, 0), (0, 1, 1)],
    'seasonal_order': [(0, 0, 0, 0)],
    'scaler': [
        StandardScaler(),
        MinMaxScaler()
    ]
}

autoreg_params_grid = {
    'regressor': [RandomForestRegressor, GradientBoostingRegressor], 
    'lags': [10, 20, 30],
    'random_state': [0],
}

models = [
        GridModel('SARIMA', Sarima, sarima_params_grid),
        GridModel('AUTOREG', Autoreg, autoreg_params_grid)
]

estimator = Rmse
steps = 30

best_models = {}

for cluster in range(N_CLUSTERS):
    print('Running for cluster:', cluster)
    cluster_consumption = utils.cluster_grouped_ts(water_consumptions, cluster)
    grid_search = GridSearch()
    search = grid_search.execute(cluster_consumption, models, estimator, steps)
    best_models[cluster] = search.best_model

print(best_models)
