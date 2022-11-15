# NIC
# ---- PersonID, NIC, Name, OtherName, DateOfBirth, BirthLocation, Job, Address
import sqlite3
import datetime
from random import random

import pandas as pd

# Read person table from database (../Database.db) # ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
conn = sqlite3.connect('../Database.db')
c = conn.cursor()
c.execute("SELECT * FROM Person")
rows = c.fetchall()
conn.close()

# Read people.csv file
df = pd.read_csv("people.csv")

for person in rows:
    personID = person[0]
    nic = person[1]
    name = person[2]

    # From people.csv find relevant data and insert age into person table
    # get person dob from people.csv
    personDob = df.loc[df["name"] == name, "dob"].iloc[0] # '02 Apr, 1984'
    dob = personDob
    # convert dob to datetime object
    personDob = datetime.datetime.strptime(personDob, "%d %b, %Y")
    # Find age from dob
    personAge = datetime.datetime.now().year - personDob.year

    # Find birth location from people.csv
    birthLocation = df.loc[df["name"] == name, "birthLocation"].iloc[0]

    # list of jobs
    jobList = ["Farmer", "Teacher", "Doctor", "Engineer", "Police", "Soldier", "Business", "Other"]

    # Find JOB from jobList
    job = jobList[int(random() * len(jobList))]

    # Find Address from people.csv
    address = df.loc[df["name"] == name, "address"].iloc[0]

    # insert into NIC table
    conn = sqlite3.connect('../Database.db')
    c = conn.cursor()
    c.execute("INSERT INTO NICCARD VALUES (?,?,?,?,?,?,?,?)", (personID, nic, name, None, dob, birthLocation, job, address))
    conn.commit()
    conn.close()