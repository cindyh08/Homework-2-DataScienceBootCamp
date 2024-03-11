import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

data = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))


filter_rows = data[data.sum(axis=1) > 100]

print(filter_rows)
