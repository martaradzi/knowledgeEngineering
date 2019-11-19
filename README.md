# Knowledge Engineering Course Repository for Group 20

For the course, we will create a knowledge intensive system concerning book recommendation system. 

*FOR NOW*: The recommendation system will ask the user basic questions about their backgroup (age, education level, etc.) and come up with 5 to 10 book the user has to rate based 1-5 scale. The system then will recommend 5 more books to read based on the users answers.

1. User imputs the info about themselvs - age and education level
2. User is classified into a certain "user_group class"
3. Based on the user_group class, a number of books is displayed for the user to rate
4. Based on the user ratings and other user rating we sing the most similar "other user" and recommend books based on that


---
## Task Knowledge:

1. Classification task:
    - 9 classes made from education level and age 
    
2. Assignment Task:
    - subject -> user
    - resource -> books
    - subject-group -> other users and their ratings
    - acclocation -> ratings
  
---
## Classes we recognize

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

We do not recognize other classes for the users.

---

## DATA: 
  - books_final1.csv 
  - ratings.csv
  - explicit_ratings.csv - this file is the final data we use
  
