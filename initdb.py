import pandas as pd
import pymongo
import json
import csv
from pymongo import MongoClient


# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# create db
db = client['tiktokspotify_db']

# connect to mongo db and collection
tiktok = db['tiktok']

tiktok_df = pd.read_csv("tiktok_data/.csv")
tiktok_dict = tiktok_df.to_dict("records")
tiktok.insert_one({"data": tiktok_dict})

# connect to mongo db and collection



