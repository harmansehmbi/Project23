from sklearn import tree

# Representation of Data
data = [ [100, 100],
         [150, 110],
         [180, 150],
         [200, 180],
         [800, 1000],
         [1000, 1200],
         [1200, 1300],
         [1500, 1500],
       ]

labels = [0, 0, 0, 0, 1, 1, 1, 1]

# DecisionTreeClassifier : 1. Represent 2. Evaluate = MODEL
clf = tree.DecisionTreeClassifier()

# Process Data
# fit function will do processing on data: i.e. Training of MODEL
# Supervised Learning
clf.fit(data, labels)

# Predictions
# input = [[1150, 1220]]
input = [[350, 350]]
output = clf.predict(input)
# print(output)

if output[0] == 0:
    print("Its a Bike")
else:
    print("Its a Car")