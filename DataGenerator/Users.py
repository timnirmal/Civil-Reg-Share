# -- User Table
# ---- UserID, Name, Password
import sqlite3

import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd

# Read person table from database (../Database.db) # ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
conn = sqlite3.connect('../Database.db')
c = conn.cursor()
c.execute("SELECT * FROM Person")
rows = c.fetchall()
conn.close()

# Read people.csv file
df = pd.read_csv("people.csv")

# ---- UserID, Name, Password, DOB, Phone, JoinedAt

# select 8 random rows from person table where personID > 10 and age > 25 and insert into user table
for i in range(8):
    # random person
    person = random.choice(rows)
    # print(person)

    # random personID
    personID = person[0]

    # random name
    name = person[2]

    # random password
    password = person[4]

    # From people.csv find relevant data and insert age into person table
    # get person dob from people.csv
    personDob = df.loc[df["name"] == name, "dob"].iloc[0] # '02 Apr, 1984'
    dob = personDob
    # convert dob to datetime object
    personDob = datetime.datetime.strptime(personDob, "%d %b, %Y")
    # Find age from dob
    personAge = datetime.datetime.now().year - personDob.year

    # Find phone number from people.csv
    phone = df.loc[df["name"] == name, "phone"].iloc[0]

    # # Find address from people.csv
    # address = df.loc[df["name"] == name, "address"].iloc[0]

    # Find joinedAt from people.csv
    joinedAt = df.loc[df["name"] == name, "joinedat"].iloc[0]


    # insert into user table
    conn = sqlite3.connect('../Database.db')
    c = conn.cursor()
    c.execute("INSERT INTO User (UserID, Name, Password, DOB, Phone, JoinedAt) VALUES (?, ?, ?, ?, ?, ?)", (personID, name, password, dob, phone, joinedAt))
    conn.commit()
    conn.close()

# Create a list of users
users = []
for row in rows:
    users.append({
        "UserID": row[0],
        "Name": row[1],
        "Password": row[2],
        "DOB": row[3],
        "Phone": row[4],
        "JoinedAt": row[5]
    })

# Create a list of user names
userNames = []
for user in users:
    userNames.append(user["Name"])

# Create a list of user IDs
userIDs = []
for user in users:
    userIDs.append(user["UserID"])


#
# dataString = ""
#
#
# def random_join_date_generator():
#     now = datetime.datetime.now()
#     generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)
#
#     # IF generated timestamp is in the future, then generate a new one
#     while generated > now:
#         generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)
#
#     return generated.strftime("%m/%d/%Y, %H:%M:%S")
#
#
# def random_date_generator():
#     now = datetime.datetime.now()
#     generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)
#
#     # IF generated timestamp is in the future, then generate a new one
#     while generated > now:
#         generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)
#
#     return generated.strftime("%m/%d/%Y, %H:%M:%S")
#
#
# def generate_person():
#     first_name = randominfo.get_first_name(gender=None)
#     name = first_name + " " + randominfo.get_last_name()
#     password = randominfo.random_password(length=8)
#     dob = randominfo.get_birthdate()
#     phone = randominfo.get_phone_number()
#     joined_date = random_join_date_generator()
#
#     # to json Name, Password, DOB, Phone, JoinedAt
#     person = {
#         "Name": name,
#         "Password": password,
#         "DOB": dob,
#         "Phone": phone,
#         "JoinedAt": joined_date
#     }
#
#     return person
#
#
# def generate_people(count):
#     people = [generate_person() for i in range(count)]
#     return people
#
#
# if __name__ == "__main__":
#     with sqlite3.connect('../Database.db') as db:
#         c = db.cursor()
#
#     print("Generating Data...")
#     people = generate_people(10)
#     # list to dataframe
#     df = pd.DataFrame(people)
#     print(df)
#
#     # save data to sqllite database in users table
#     insert = 'INSERT INTO user(Name,Password,DOB,Phone,JoinedAt) VALUES(?,?,?,?,?)'
#     # for each item in df c.execute(insert, (df['Name'], df['Password'], df['DOB'], df['Phone'], df['JoinedAt']))
#     for index, row in df.iterrows():
#         c.execute(insert, (row['Name'], row['Password'], row['DOB'], row['Phone'], row['JoinedAt']))
#
#     db.commit()
#     db.close()
#
#
