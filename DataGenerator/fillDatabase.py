import pandas as pd

# Read the dataset
df = pd.read_csv("user.csv")

# show all columns of df head
pd.set_option('display.max_columns', None)

# read people table in "../Database.db"
import sqlite3

"""
# Person Table for General Public
"""
#
# with sqlite3.connect('../Database.db') as db:
#     c = db.cursor()
#
#     # Read all column names to list
#     c.execute("SELECT * FROM person")
#     col_names = [cn[0] for cn in c.description]
#
#
#     print(col_names)
#     # ['PersonID', 'NIC', 'Name', 'Email', 'Password', 'Phone', 'Address', 'ImageID']
#
#
#     # conver col_names to lower case
#     col_names = [x.lower() for x in col_names]
#
#     print(col_names)
#     # ['personid', 'nic', 'name', 'email', 'password', 'phone', 'address', 'imageid']
#
#     # column list of df
#     df_col_names = df.columns.tolist()
#
#     print(df_col_names)
#     # ['id', 'name', 'password', 'gender', 'email', 'phone', 'joinedat', 'dob', 'NIC', 'birthLocation', 'address', 'imgUrl']
#
#     # select NIC, name, email, password, phone, address, imageUrl from df
#     df = df[['NIC', 'name', 'email', 'password', 'phone', 'address', 'imgUrl']]
#
#     print(df)
#
#     # rename as  NIC, name, email, password, phone, address, imageID
#     df.rename(columns={'NIC': 'nic', 'name': 'name', 'email': 'email', 'password': 'password', 'phone': 'phone', 'address': 'address', 'imgUrl': 'imageID'}, inplace=True)
#
#     print(df)
#
#     # Insert data into person table
#     df.to_sql('person', db, if_exists='append', index=False)
#
#     # # insert values to people table
#     # for value in values:
#     #     c.execute("INSERT INTO person({}) VALUES({})".format(','.join(col_names), ','.join(['?']*len(col_names))), value)
#     #
#
#     db.commit()

"""
# Person Table for General Public
"""

with sqlite3.connect('../Database.db') as db:
    c = db.cursor()

    # Read all column names to list
    c.execute("SELECT * FROM person")
    col_names = [cn[0] for cn in c.description]
    print(col_names)
    # ['UserID', 'Name', 'Password', 'DOB', 'Phone', 'JoinedAt']

    # column list of df
    df_col_names = df.columns.tolist()

    print(df_col_names)
    # ['id', 'name', 'password', 'gender', 'email', 'phone', 'joinedat', 'dob', 'NIC', 'birthLocation', 'address', 'imgUrl']

    # select NIC, name, email, password, phone, address, imageUrl from df
    df = df[['NIC', 'name', 'email', 'password', 'phone', 'address', 'imgUrl']]

    print(df)

    # rename as  NIC, name, email, password, phone, address, imageID
    df.rename(columns={'NIC': 'nic', 'name': 'name', 'email': 'email', 'password': 'password', 'phone': 'phone', 'address': 'address', 'imgUrl': 'imageID'}, inplace=True)

    print(df)
    print("print done")

    # get number of rows in c
    c.execute("SELECT COUNT(*) FROM person")
    count = c.fetchone()[0]
    print(count)

    # Insert data into person table
    df.to_sql('person', db, if_exists='append', index=False)

    # # insert values to people table
    # for value in values:
    #     c.execute("INSERT INTO person({}) VALUES({})".format(','.join(col_names), ','.join(['?']*len(col_names))), value)
    #

    db.commit()
