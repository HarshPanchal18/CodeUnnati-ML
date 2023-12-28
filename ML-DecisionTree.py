from sklearn import tree

features = [[140,1],[130,1],[150,0],[170,0]] # 1 - smooth, 0 - bumpy
labels = [0,0,1,1] # 0 for apple, 1 for orange

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels) # Train the dec-tree using the data and labels

print(clf.predict([[155,0]]))
print(clf.predict([[140,1]]))