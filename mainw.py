# are all my quotes ascii?
import pandas as pd

quote_mast = "quotes.txt"
df = pd.read_csv(quote_mast, sep=" - ", engine='python', names=['quote', 'quoter'])
# put into a dict
my_dict = {row.quote: row.quoter for (index, row) in df.iterrows()}

my_list = list(my_dict.items())
row_number = 0
for w in my_list:
    quote = w[0]
    quoter = w[1]
    try:
        quote.encode('ascii')
    except UnicodeError:
        print(f"problem at row {row_number}")
    row_number += 1
