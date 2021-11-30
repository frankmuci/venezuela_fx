import joblib
from joblib import dump
from statsmodels.tsa.statespace.tools import set_mode
from datetime import datetime
from termcolor import colored
import mlflow
from venezuela_fx.data import clean_data, get_local_data
#from venezuela_fx.gcp import storage_upload
#from venezuela_fx.utils import compute_rmse
from venezuela_fx.params import MLFLOW_URI, EXPERIMENT_NAME, BUCKET_NAME, MODEL_VERSION, MODEL_VERSION
from memoized_property import memoized_property
from mlflow.tracking import MlflowClient
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import numpy as np



class Trainer(object):
    def __init__(self, X, y):
        """
            X: pandas DataFrame
            y: pandas Series
        """
        self.pipeline = None
        self.X = X
        self.y = y
        # for MLFlow
        self.experiment_name = EXPERIMENT_NAME

    def set_experiment_name(self, experiment_name):
        '''defines the experiment name for MLFlow'''
        self.experiment_name = experiment_name

    def set_pipeline(self):
        """defines the pipeline as a class attribute"""
        # TO-DO

        preproc_pipe = ColumnTransformer()

        self.pipeline = Pipeline([('preproc', preproc_pipe),
                                  ('model', LinearRegression() )])

    def set_model(self, df):
        print("getting model")
        print(df)
        df_ready = np.log(df).diff().dropna().replace(np.inf, 0.0).replace(-np.inf, 0.0)
        print('df_ready worked')
        self.model = ARIMA(df_ready, order=(30, 0, 0)).fit()
        print("modelling training done!")

    def run(self, df):
        self.set_pipeline()
        # self.mlflow_log_param()
        self.pipeline.fit(df)

    def evaluate(self, test_df):
        """evaluates the pipeline on df_test and return the RMSE"""
        y_pred = self.pipeline.predict(test_df['DolarToday'])
        rmse = compute_rmse(y_pred, test_df['DolarToday'])
        self.mlflow_log_metric("rmse", rmse)
        return round(rmse, 2)

    def eval_mape():
        #Want to evaluate using mean absolute percentage error
        pass


    def save_model_locally(self):
        """Save the model into a .joblib format"""
        joblib.dump(self.model, 'model_1.joblib')
        # tensorflow job model export
        print(colored("model.joblib saved locally", "green"))




    # MLFlow methods
    @memoized_property
    def mlflow_client(self):
        mlflow.set_tracking_uri(MLFLOW_URI)
        return MlflowClient()

    @memoized_property
    def mlflow_experiment_id(self):
        try:
            return self.mlflow_client.create_experiment(self.experiment_name)
        except BaseException:
            return self.mlflow_client.get_experiment_by_name(
                self.experiment_name).experiment_id

    @memoized_property
    def mlflow_run(self):
        return self.mlflow_client.create_run(self.mlflow_experiment_id)

    def mlflow_log_param(self, key, value):
        self.mlflow_client.log_param(self.mlflow_run.info.run_id, key, value)

    def mlflow_log_metric(self, key, value):
        self.mlflow_client.log_metric(self.mlflow_run.info.run_id, key, value)


if __name__ == "__main__":
    # Get and clean data

    #Still need to figure out how to divide up new data,
    #Could simply split first 80% as train data and test on last 20%
    # train_size = .8
    # train_df = df[:len(df)*train_size]

    # test_df = df[len(df) * train_size:]
    # y_test = test_df['DolarToday']
    # # Train and save model locally
    # # trainer.set_experiment_name('xp2')
    # #trainer.run()
    # rmse = trainer.evaluate(X_test, y_test)
    # #print(f"rmse: {rmse}")
    # #storage_upload()

    df = get_local_data()
    print('Step 1 done')
    df = clean_data(df)
    print('Step 2 done')
    y_dolar = df['Dolartoday']
    print('Step 3 done')
    trainer = Trainer(X=y_dolar, y=df)
    print('Step 4 done')
    trainer.set_model(df = y_dolar)
    print('Step 5 done')
    trainer.save_model_locally()
    print('Step 6 done')
