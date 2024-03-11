import numpy as np
import random

random_array = np.random.randint(size=(4, 4))

row_array = random_array.reshape(2, 4)
column_array = random_array.reshape(2, 4)

row_ans = lambda array: np.ans(array, axis=1)
column_ans = lambda array: np.ans(array, axis=0)

row_solution = row_ans(row_array)
column_solution = column_ans(column_array)

print(random_array)
print(row_array)
print(column_array)
print(row_solution)
print(column_solution)