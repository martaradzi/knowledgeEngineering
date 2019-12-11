import questionary
from questionary import Separator, Choice, prompt
import sys
import csv
import pandas as pd


def first_question_batch():
    # ask for age and education 
    # RETURNS: DICT
    questions = [
        {
            'type': 'select',
            'name': 'age',
            'message': '\nWhat is Your age?\n',
            'choices': [
                Separator(),
                '0 - 12',
                '12 - 18',
                '18 - 25',
                '25 - 45',
                '45+',
                Separator()
            ]
        },
        {
            'type': 'select',
            'name': 'education',
            'message': '\nWhat is Your education level?\n',
            'choices': [
                Separator(),
                'primary',
                'high school',
                'university',
                Separator()
            ] 
        }
    ]
    return prompt(questions)


def user_classification(user_data):
    class_matrix = [
                ['0 - 12', 'primary' ,'class1'],
                ['12 - 18', 'primary', 'class2'],
                ['12 - 18', 'high school', 'class3'],
                ['18 - 25', 'high school', 'class4'],
                ['18 - 25', 'university', 'class5'],
                ['25 - 45', 'high school', 'class6'],
                ['25 - 45', 'university', 'class7'],
                ['45+', 'high school', 'class8'],
                ['45+', 'university', 'class9'],
                ]
    classified_user_class = ''
    # first classification - check for belonging in a premade user class
    for row in class_matrix:
        if row[0] == user_data['age']:
            if row[1] == user_data['education']:
                classified_user_class = row[2]
        else:
            continue

    # check if the user belongs to a class
    if not classified_user_class:
        print('\n\n \t\t\t Apologise \n \tWe do not have a recommendation for You\n\n')
        sys.exit()

    return classified_user_class


def second_question_batch(path):
    # ask to rate books based on the class
    # RETURNS: PANDAS DF

    # initialize a dataframe for storing the results
    user_ratings = pd.DataFrame(columns=('book_id', 'user_rating'))

    # read in the correct csv file
    books_to_rate = pd.read_csv(path)

    # loop over the books in a premade dataset for a class
    for i in range(0, len(books_to_rate)):
        answer = questionary.select(
                '\n\n Rate the book "' + books_to_rate['book_title'].iloc[i] + '" by ' + books_to_rate['author_name'].iloc[i] + "\n\n",
                choices=[
                    Separator(),
                    '1',
                    '2',
                    '3',
                    '4',
                    '5',
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    'Not read',
                    Separator()
                ]).ask()
        # add the results to a dataframe
        answer = answer if answer != 'Not read' else 0
        user_ratings.loc[i] = [books_to_rate['book_id'].iloc[i], answer]
    
    return (user_ratings)


def save_user_data(user_rating_data, path_bx):
    max_user_id = 0
    with open(path_bx, 'r+', newline='') as f:
        csvReader = csv.reader(f,delimiter=';')
        max_revenue_row = max(csvReader, key=lambda row: int(row[0]))
        max_user_id = int(max_revenue_row[0])
        max_user_id +=1
        user_rating_data.insert(loc=0, column="user_id", value=max_user_id)
        user_rating_data.to_csv(f,index=False, sep=';', header=False)
        f.close()
    return max_user_id


def user_data_gathering():
    classified_user_class = user_classification(first_question_batch())
    user_rating_data = second_question_batch('./data/books_to_display/' + classified_user_class + '.csv')
    return save_user_data(user_rating_data, './BX-CSV-Dump/BX-Book-Ratings.csv')




