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
    print(f"about to email: {row_number}")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        password = "pfwgxnugziwfqvnk"

        # transport layer security, which replaces ssl (secure socket layer) -to secure connection to server
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=target_email,
            msg=f"Subject:It is Monday!....\n\n{quote}\n{quoter}"
        )
        row_number += 1

