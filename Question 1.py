import pandas as pd


url = 'https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv'

items = pd.read_csv(url)

ans_items = items.loc[:: 20, ['Manufacturer','Model', 'Type']]
# loc means location so since items is == to the url this
# code will search for the Manufacture, model , and type for evey 20 rows

print(ans_items)