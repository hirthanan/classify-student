from sklearn import tree

## Sample Data

'''
0 -> waterloo
1 -> laurier
2 -> uoft
'''

# format: measures = [studying_per_day, sleep_per_day, university]
measures = [[8, 6, 0], [5, 4, 0], [1, 9, 1],
            [5, 8, 1], [6, 4, 2], [3, 10, 1]]

grade_level = ['outstanding', 'superior', 'good', "outstanding",
                'superior', 'good']

## Sample Data

# Initialize decision tree classifier object
classifier = tree.DecisionTreeClassifier()

# Use classifier object with sample data to train model
classifier = classifier.fit(measures, grade_level)

predict_grade_level = classifier.predict([[4, 7, 0]])

print predict_grade_level




