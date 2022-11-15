# -- Person Table
# ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
import sqlite3

import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd

# Read person table from database (../Database.db)
conn = sqlite3.connect('../Database.db')
c = conn.cursor()
c.execute("SELECT * FROM Person")
rows = c.fetchall()
conn.close()

# show all columns in df head
max_columns = pd.get_option('display.max_columns')

# print rows
for row in rows:
    print(row)


# From people.csv find relevant data and insert age into person table
df = pd.read_csv("people.csv")
# for i in range(len(rows)):
#     # get person name
#     personName = rows[i][2]
#     # get person dob from people.csv
#     personDob = df.loc[df["name"] == personName, "dob"].iloc[0] # '02 Apr, 1984'
#     # convert dob to datetime object
#     personDob = datetime.datetime.strptime(personDob, "%d %b, %Y")
#     # Find age from dob
#     personAge = datetime.datetime.now().year - personDob.year
#     # update person table
#     conn = sqlite3.connect('../Database.db')
#     c = conn.cursor()
#     c.execute("UPDATE Person SET Age = ? WHERE PersonID = ?", (personAge, rows[i][0]))
#     conn.commit()
#     conn.close()
