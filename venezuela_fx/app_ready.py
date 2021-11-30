import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score, max_error
import matplotlib.pyplot as plt
import joblib



class Model(object):
    def __init__(self,df=None, target_distance=7, model=None):
        """initialises a df to model"""
        self.pipeline = None
        self.df = df
        self.target_distance = target_distance
        self.model = model
        if self.df == None:
            self.df = pd.read_csv(
                '/Users/daraalizadeh/code/frankmuci/venezuela_fx/since_2012_master.csv'
            )

    def set_experiment_name(self, experiment_name):
        """name the monster"""
        self.experiment_name = experiment_name

    def sort_data(self):
        """tidy data"""
        self.df['date'] = self.df['date'].apply(pd.to_datetime)
        self.df.set_index('date', inplace=True)
        self.df = np.log(self.df).diff()

    def splitting_data(self):
        """split data into chronological train_test_split"""
        self.train_size = int(np.round(self.df.shape[0]*0.7))
        self.train = self.df.iloc[:self.train_size]
        self.test = self.df.iloc[self.train_size:]
        self.X_train = self.train.drop(columns=['Dolartoday'])
        self.y_train = self.train['Dolartoday']
        self.X_test = self.test.drop(columns=['Dolartoday'])
        self.y_test = self.test['Dolartoday']


    def flattening_train(self):
        """Flatten train_set in order to machine learn that time series"""
        values = []
        y_list = []
        seq_length = self.target_distance
        for idx in list(range(self.X_train.shape[0]-self.target_distance)):
            X_temp = self.X_train.iloc[idx+seq_length]
            values.append(X_temp.values.reshape(-1))
            y_list.append(self.y_train[idx+self.target_distance])
        self.X_train = pd.DataFrame(np.vstack(values))
        self.y_train = pd.Series(y_list)

    def flattening_test(self):
        """Flatten test_set in order to machine learn that time series"""
        values = []
        y_list = []
        seq_length = self.target_distance
        for idx in list(range(self.X_test.shape[0]-self.target_distance)):
            X_temp = self.X_test.iloc[idx+seq_length]
            values.append(X_temp.values.reshape(-1))
            y_list.append(self.y_test[idx+self.target_distance])
        self.X_test = pd.DataFrame(np.vstack(values))
        self.y_test = pd.Series(y_list)

    def fixing_logged_data(self):
        """Fix the nan, infinites that result from taking log of small values"""
        def easy_fix(X):
            """Define process for fixing"""
            X.fillna(method='ffill', inplace=True)
            X.fillna(method='bfill', inplace=True)
            X.replace(np.inf, 0.0, inplace=True)
            X.replace(-np.inf,0.0, inplace=True)
            return X
        self.X_test = easy_fix(self.X_test)
        self.y_test = easy_fix(self.y_test)
        self.X_train = easy_fix(self.X_train)
        self.y_train = easy_fix(self.y_train)


    def set_pipeline(self):
        """Creates a simple pipeline for machine learning"""
        if self.model == None:
            model = RandomForestRegressor()
        self.pipeline = Pipeline([('model', model)])

    def run(self):
        """runs the model"""
        self.set_pipeline()
        self.pipeline.fit(self.X_train, self.y_train)

    def evaluate(self):
        """evaluates model"""
        self.y_pred = self.pipeline.predict(self.X_test)
        self.mse = mean_squared_error(self.y_test, self.y_pred)
        self.mae = mean_absolute_error(self.y_test, self.y_pred)
        self.me = max_error(self.y_test, self.y_pred)
        self.r2_score = r2_score(self.y_test, self.y_pred)

    def show_metrics(self):
        """Show metrics"""
        print(f"mean squared error: {self.mse}")
        print(f"Mean absolute error: {self.mae}")
        print(f"Max error: {self.me}")
        print(f"R2 score: {self.r2_score}")

    def prediction_graph(self):
        """Plots prediction against test"""
        # plt.plot(self.y_pred)
        # plt.plot(self.y_test)

        dict = {
            'pred': self.y_pred,
            'test': self.y_test
        }

        return pd.DataFrame.from_dict(dict)


    def save_model_locally(self):
        """Save the model in .joblib format"""
        joblib.dump(self.pipeline, 'models/model.joblib')
        print("Suprisingly this seems to have worked...")


if __name__ == "__main__":
    #Initialise a model with optional params:
    # Dataframe -(date column must be called 'date')
    # target_distance - How far does the model need to predict
    # model - which regressor to be used

    def test(train = False):
        model = Model()
        model.set_experiment_name('Tester')
        if train == True:
            model.sort_data()
            model.splitting_data()
            model.flattening_test()
            model.flattening_train()
            model.fixing_logged_data()
            model.set_pipeline()
            model.run()
        else:
            # read processed csv
            # load model
            pass
        model.evaluate()
        model.show_metrics()
        model.prediction_graph()
        model.save_model_locally()
