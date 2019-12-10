import os.path
from scipy import sparse
import csv
import numpy as np
from lightfm import LightFM
import pickle


def book(min_score, max_user_id):

    # Data for creating coo_matrix
    # min_score, user_id, book_id
    data, row, col = [], [], []

    # books by id, and users
    books_id, users = {}, {}
    max_book_id = 0
    
    # exptract max book ID
    with open('BX-CSV-Dump/BX-Books.csv', 'r', encoding='ISO-8859-1') as text:
        csvReader = csv.reader(text, delimiter=';')
        max_book_id_row = max(csvReader, key=lambda row: int(row[0]))
        max_book_id = int(max_book_id_row[0])
    
    #extract books
    with open('BX-CSV-Dump/BX-Books.csv', 'r', encoding='ISO-8859-1') as text:
        csvReader = csv.reader(text, delimiter=';')
        for row_of_file in csvReader:
            book_id = row_of_file[0]
            book_name = row_of_file[1]
            book_author = row_of_file[2]
            if book_id not in books_id:
                books_id[book_id] = {
    			'name' : book_name,
                'author' : book_author
    			}

    # extract users 
    with open('BX-CSV-Dump/BX-Users.csv', 'r', encoding='ISO-8859-1') as text:
    	csvReader = csv.reader(text, delimiter=';')
    	for row_of_file in csvReader:
    		user = row_of_file[0]
    		if user not in users:
	    		users[user] = user

    #extract ratings of books
    with open('BX-CSV-Dump/BX-Book-Ratings.csv', 'r', encoding='ISO-8859-1') as text:
    	csvReader = csv.reader(text, delimiter=';')
    	for row_of_file in csvReader:
            if row_of_file[1] == "":
                continue
            if int(row_of_file[2]) >= min_score:
                data.append(int(row_of_file[2]))
                row.append(row_of_file[0])
                col.append(row_of_file[1])

    # numpy array to pass it to coo_matrix
    data = np.array(data)
    row = np.array(row, dtype=np.int32)
    col = np.array(col, dtype=np.int32)
    
    # creating the matrix;
    # this matrix is used to later compare the new user 
    # to users that have similar ratings to him/her
    sm = sparse.coo_matrix((data,(row,col)),shape=(
                max_user_id + 1, max_book_id + 1))

    # train the model
    pretrain_model = LightFM(loss="warp").fit(sm, epochs=30, num_threads=2)
    
    # save trained model; model is always retrained when a new user is inputed
    with open("BX-CSV-Dump/explicit_rec.pkl", "wb") as fid:
        pickle.dump(pretrain_model, fid)

    # Return the matrix, books_id dictionary and amount of users
    dictionary = {
    	'matrix' : sm,
    	'books_id' : books_id,
    	'users'	: len(users)
    }

    return dictionary
