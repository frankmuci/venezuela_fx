import pandas as pd
from google.cloud import storage
#from venezuela_fx.params import BUCKET_NAME, BUCKET_TRAIN_DATA_PATH



# def get_data_from_gcp(nrows=10000, optimize=False, **kwargs):
#     """method to get the training data (or a portion of it) from google cloud bucket"""
#     # Add Client() here
#     # Grab the DataFrame with Time Series from Google Cloud
#     client = storage.Client()
#     path = f"gs://{BUCKET_NAME}/{BUCKET_TRAIN_DATA_PATH}"
#     df = pd.read_csv(path, nrows=nrows)
#     return df


def get_local_data():
    #'/Users/daraalizadeh/code/frankmuci/venezuela_fx/
    # path = '/Users/daraalizadeh/code/frankmuci/venezuela_fx/venezuela_fx/data_csv/since_2012_master.csv'
    path = '/Users/daraalizadeh/code/frankmuci/venezuela_fx/venezuela_fx/data_csv/working_df.csv'

    df = pd.read_csv(path)
    return df









def clean_data(df, test=False):

    # Looking through Frank and Joe's notebooks cleaning the data,
    # repeat steps of filling null values (front-fill, back-fill), transforming
    # Dolartoday values into Log Values.
    df['Unnamed: 0'] = df['Unnamed: 0'].apply(pd.to_datetime)
    df.set_index('Unnamed: 0', inplace=True)
    return df
    # unused_column = "Unnamed: 0"
    # if unused_column in df.keys():
    #     df = df.drop(axis=1, columns=["Unnamed: 0"])
    # df = df.dropna(how='any', axis='rows')
    # df = df[(df.dropoff_latitude != 0) | (df.dropoff_longitude != 0)]
    # df = df[(df.pickup_latitude != 0) | (df.pickup_longitude != 0)]
    # if "fare_amount" in list(df):
    #     df = df[df.fare_amount.between(0, 4000)]
    # df = df[df.passenger_count < 8]
    # df = df[df.passenger_count >= 0]
    # df = df[df["pickup_latitude"].between(left=40, right=42)]
    # df = df[df["pickup_longitude"].between(left=-74.3, right=-72.9)]
    # df = df[df["dropoff_latitude"].between(left=40, right=42)]
    # df = df[df["dropoff_longitude"].between(left=-74, right=-72.9)]
    # return df


if __name__ == '__main__':
    df = get_local_data()
    print('Created df')
    df = clean_data(df)
    print('Cleaned df')
