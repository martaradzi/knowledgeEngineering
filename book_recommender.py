# -*- coding: utf-8 -*-
import numpy as np
import csv
import pickle
from lightfm.datasets import fetch_movielens
from lightfm import LightFM
import scipy.sparse as sp
from book import book
from user_data_gathering import user_data_gathering


def get_recommendations(pretrain_model, coo_mtrx, users_ids, books_id):
    n_items = coo_mtrx.shape[1]

    # retrive the books the model predicts will like based on similar user
    results = pretrain_model.predict(users_ids, np.arange(n_items))
    top_results = np.argsort(-results)[:5] # get 5 top recommendations  

    print('\n\n \t\t Book recomendations: \n')
    for x in top_results.tolist():
        print(books_id[str(x)])
        print('\n')

def main():

    user_id = user_data_gathering()  # gather user input 

    data = book(8, user_id)  # start data processing, specify the minimal score of the recommended books

    # retrive pretrained model
    with open("BX-CSV-Dump/explicit_rec.pkl", "rb") as fid:
        pretrain_model = pickle.load(fid)
    
    # create recommendation for the current user 
    get_recommendations(pretrain_model, data['matrix'], user_id, data['books_id'])


if __name__ == "__main__":
    main()
