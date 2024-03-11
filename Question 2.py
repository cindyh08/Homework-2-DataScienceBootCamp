import pandas as pd

url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'
prices = pd.read_csv(url)


mean_Min_Price = prices['Min.Price'].mean()
mean_Max_Price = prices['Max.Price'].mean()

print("The minimal price is ", mean_Min_Price, "and the maximum price is", mean_Max_Price)