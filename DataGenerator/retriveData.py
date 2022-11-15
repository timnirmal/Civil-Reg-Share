# ---- UserID, Name, Password, DOB, Phone, JoinedAt
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
c.execute("SELECT * FROM user")
rows = c.fetchall()
conn.close()

# show all columns in df head
max_columns = pd.get_option('display.max_columns')

# print rows
for row in rows:
    print(row)

