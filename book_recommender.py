# -*- coding: utf-8 -*-
import numpy as np
import csv
import pickle
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import scipy.sparse as sp
from sklearn.metrics import roc_auc_score
from lightfm.evaluation import auc_score

from book import book
from user_data_gathering import user_data_gathering



def get_recommendations(pretrain_model, coo_mtrx, users_ids, books_id):
    n_items = coo_mtrx.shape[1]

    # Books the model predicts they will like based on similar users
    results = pretrain_model.predict(users_ids, np.arange(n_items))
    top_results = np.argsort(-results)[:5]
    print(top_results)

    print('Book recomendations:')
    for x in top_results.tolist():
        print(books_id[str(x)])


def main():

    user_data_gathering()

    data = book(8)
    with open("BX-CSV-Dump/explicit_rec.pkl", "rb") as fid:
        pretrain_model = pickle.load(fid)
    
    max_user_id = 0
    with open('BX-CSV-Dump/BX-Book-Ratings.csv', 'r') as f:
        csvReader = csv.reader(f,delimiter=';')
        max_user_id_row = max(csvReader, key=lambda row: int(row[0]))
        max_user_id = int(max_user_id_row[0])
    user = max_user_id

    get_recommendations(pretrain_model, data['matrix'], user, data['books_id'])


if __name__ == "__main__":
    main()
