# System Repository for  [Knowledge Engineering](https://studiegids.vu.nl/en/Master/2018-2019/computer-science/X_405099) assignment for Group 20

For the course, we will create a knowledge intensive system concerning book recommendation system. 

The system works in the following way:

1. The system asks the user about their age group and their education level
2. The system then asks the user to rate 10 books personalized based on the previous answer (not read oprion avaiable)
3. The system then displays 5 - 10 recommended books for the user.

# Running the program

To run this program you need to run Python 3.6.

The program works using libraries listed in ```requirements.txt``` file. To run the program correcty run the following code before running the program.

```python
pip install -r requirements.txt
```

To run the program use the command:

```python
python user_data_gathering.py
```

# Information about the system

The system is implemented using [commonKADS](https://commonkads.org/ "CommonKADS.org Main Page") methodology for knowledge based systems. A full report can be found in ```report.pdf```. The most important parts are shown below:

## Task Knowledge:

1. Classification tasks:
    - classify to one of the 9 classes made from education level and age 
    - classify to most similar external user based on your ratings of books
    
2. Assignment Task:
    - from the most similar user assign the best rated books which you did not read yet.
  

## User classes we recognize

**First classification task**

| class name|age|education-level|
|-----------------|---------|---------|
| class1 | 0 - 12 | primary  |
| class2 | 12 - 18 | primary |
| class3 | 12 - 18 | high-school |
| class4 | 18 - 25 | high-school |
| class5 | 18 - 25 | university |
| class6 | 25 - 45 | high-school |
| class7 | 25 - 45 | university |
| class8 | 45+ | high-school |
| class9 | 45+ | university |

We do not recognize other classes for the users as we think the classes would be edge cases and not used often.

**Second classification task**

The external user dataset consists of 60 000 users with at least 10 books reviewed. The users similarity to external users is classified using cosine similarity matrix.

---

## DATA: 

The following data is used by the system:
  - ```.\data\books_to_display\``` - contains .csv files with the expert's knowledge and is used to displayed personalized books for the user to rate
  - ```.\data\user_data\user_ratings.csv``` - created from the user rating, contains the books title, unique book ID, and the user's rating of te book title
  - ```.\data\ratings.csv``` - external user dataset obtained from [Goodreads](https://www.goodreads.com/ " Goodreads") containg a unique external user ID, unique book ID and the external user's rating of the book
  
## Executable file explanation: 
 - ```.\user_data_gathering.py``` - main executable program