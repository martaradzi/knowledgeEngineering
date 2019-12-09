import questionary
from questionary import Separator, Choice, prompt
import sys
import csv
import pandas as pd


def first_questions():
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


def second_questions(path):
    # ask to rate books based on the class
    # RETURNS: PANDAS DF

    # initialize a dataframe for storing the results
    user_ratings = pd.DataFrame(columns=('book_id', 'user_rating'))

    # read in the correct csv file
    books_to_rate = pd.read_csv(path)

    # loop over the books in a premade dataset for a class
    for i in range(0, len(books_to_rate)):
        answer = questionary.select(
                "\n\n Rate the book " + books_to_rate['book_title'].iloc[i] + "\n\n",
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


def save_user_data(final_data):
    max_user_id = 0
    with open('BX-CSV-Dump/BX-Book-Ratings.csv', 'r+', newline='') as f:
        csvReader = csv.reader(f,delimiter=';')
        max_revenue_row = max(csvReader, key=lambda row: int(row[0]))
        max_user_id = int(max_revenue_row[0])
        max_user_id +=1
        final_data.insert(loc=0, column="user_id", value=max_user_id)
        final_data.to_csv(f,index=False, sep=';', header=False)
        f.close()


# setting up classes
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


if __name__ == '__main__':

    # initialize variables
    user_data = first_questions()
    final_class = ''
    path_books_to_rate = './data/books_to_display/'
    path_to_save = './data/user_data/user_ratings.csv'

    # first classification - check for belonging in a premade class
    for row in class_matrix:
        if row[0] == user_data['age']:
            if row[1] == user_data['education']:
                final_class = row[2]
        else:
            continue

    # check if the user belongs to a class
    if not final_class:
        print('\n\n \t\t\t Apologise \n \tWe do not have a recommendation for You\n\n')
        sys.exit()

    # second questionary - rating books
    final_data = second_questions(path_books_to_rate + final_class + '.csv')
    print (final_data)
    save_user_data(final_data)




