import numpy as np
marks = np.array([65, 72, 81, 55, 90, 68])
print(marks)
print("number of students:", len(marks))
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))
print("Average Mark:", np.mean(marks))
print("Total marks:", np.sum(marks))

Passed  = marks[marks >=50]
print("Students who passed:")
print (Passed)