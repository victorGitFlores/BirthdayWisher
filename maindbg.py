# are all my quotes ascii?
import pandas as pd
import smtplib

quote_mast = "quotes_dbg.txt"
my_email = "vicDev957@gmail.com"  # this guy will be doing the emailing
target_email = "vicdev957@gmail.com"
quote_mast = "quotes_dbg.txt"
df = pd.read_csv(quote_mast, sep=" - ", engine='python', names=['quote', 'quoter'])
# put into a dict
my_dict = {row.quote: row.quoter for (index, row) in df.iterrows()}

my_list = list(my_dict.items())
row_number = 1
for w in my_list:
    quote = w[0]
    quoter = w[1]

    quote = ascii(quote)
    quoter = ascii(quoter)
    print(f"row: {row_number} {quote} - {quoter}")
    row_number += 1
