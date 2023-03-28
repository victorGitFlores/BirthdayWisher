import smtplib
import datetime as dt
import random
import pandas as pd
import time as tm

#
# # ------------------------------------------------------------------------------#
#

email_mast = "email_mast.txt"
quote_mast = "quotes.txt"
my_email = "vicDev957@gmail.com"  # this guy will be doing the emailing

# load email master into a list: lst_ema_mast
with open(email_mast) as fil_ema_mast:
    w = fil_ema_mast.read()
    lst_ema_mast = w.split("\n")


# the mailer
def email_the_quote(quote, quoter, tgt_email):
    #quote.encode("utf-8") # i think default is ascii, and otherwise failing when trying to email if a char is not ascii
    #above does not help! idea: just make sure all the chars in txt file are ascii!
    #print("got this far")
    target_email = tgt_email
    # # smtp.aol.com     smtp.gmail.com

    ctr_tries = 0
    sent_ok = False
    while sent_ok is False and ctr_tries < 10:
        sent_ok = True
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                 password   = "pfwgxnugziwfqvnk"

                 # transport layer security, which replaces ssl (secure socket layer) -to secure connection to server
                 connection.starttls()
                 connection.login(user=my_email, password=password)
                 connection.sendmail(
                     from_addr=my_email,
                     to_addrs=target_email,
                     msg=f"Subject:It is Monday!....\n\n{quote}\n{quoter}"
                 )
        except:
            sent_ok = False
            ctr_tries += 1
            # sleep 3 seconds
            tm.sleep(3)
        else:
            sent_ok = True

# capture current date/time
now = dt.datetime.now()
# print(now) # 2023-03-22 17:49:34.356222 (type datetime)
# print(now.year) # 2023  (type int)
# print(now.weekday()) # prints 2 (i guess 0=mon, 1=tue...)

# ---------------------------------------------------------------------------- #

#if today is Monday,0,.... do it:
today = dt.datetime.now()
if today.weekday() == 0:
    df = pd.read_csv(quote_mast, sep=" - ", engine='python', names=['quote', 'quoter'])
    # put into a dict
    my_dict = {row.quote:row.quoter for (index, row) in df.iterrows()}

    # ----------------------------------------------------------------------------
    # SEND A RANDOM QUOTE TO EACH OF THE EMAIL ADDRESSES IN email_mast.txt
    # ----------------------------------------------------------------------------
    for w in lst_ema_mast:
        if "@" in w:
            my_tup  = random.choice(list(my_dict.items()))
            my_quote  = my_tup[0]
            my_quoter = my_tup[1]
            email_to  = w
            email_the_quote(my_quote, my_quoter, email_to)
            # Sleep a little, dont wanna overwhelm the email server!
            tm.sleep(1)

