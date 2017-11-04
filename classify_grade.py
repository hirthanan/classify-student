import sys
from sklearn import tree

class School:
    WATERLOO = 0
    LAURIER = 1
    UOFT = 2

## Sample Data

# format: measures = [studying_per_day, sleep_per_day, university]
measures = [[8, 6, School.WATERLOO], [5, 4, School.WATERLOO], [1, 9, School.LAURIER],
            [5, 8, School.LAURIER], [6, 4, School.UOFT], [3, 10, School.LAURIER],
            [8, 3, School.UOFT], [9, 9, School.UOFT], [4, 8, School.WATERLOO],
            [5, 8, School.LAURIER], [6, 4, School.UOFT], [3, 10, School.LAURIER],
            [2,5, School.WATERLOO], [2, 4, School.UOFT], [3, 4, School.WATERLOO]]

grade_level = ['outstanding', 'superior', 'good', 'outstanding',
                'superior', 'good', 'superior', 'outstanding',
                'good', 'outstanding', 'superior', 'superior',
                'satisfactory', 'satisfactory', 'satisfactory']

## Sample Data

# Initialize decision tree classifier object
classifier = tree.DecisionTreeClassifier()

# Use classifier object with sample data to train model
classifier = classifier.fit(measures, grade_level)

print "Enter students data in format : studying_per_day, sleep_per_day, university"

for line in sys.stdin:
    student = line.split(' ')
    predict_grade_level = classifier.predict([student])
    print predict_grade_level
