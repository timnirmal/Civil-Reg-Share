import sqlite3

import pandas as pd

# show all columns in head
pd.set_option('display.max_columns', None)

# read people_m.csv
df = pd.read_csv("user.csv")

# create a new dataframe to hold the search results
search_results = pd.DataFrame()

# Select 5 random people from df and add them to search_results
search_results = search_results.append(df.sample(n=5,ignore_index=True))

print(search_results)



with sqlite3.connect('../Database.db') as db:
    c = db.cursor()

    # Read all column names to list
    c.execute("SELECT * FROM user")
    col_names = [cn[0] for cn in c.description]
    print(col_names)
    # ['UserID', 'Name', 'Password', 'DOB', 'Phone', 'JoinedAt']

    # column list of df
    df_col_names = df.columns.tolist()

    print(df_col_names)
    # ['id', 'name', 'password', 'gender', 'email', 'phone', 'joinedat', 'dob', 'NIC', 'birthLocation', 'address', 'imgUrl']

    # select NIC, name, email, password, phone, address, imageUrl from df
    df = df[['id', 'name', 'password', 'dob', 'phone', 'joinedat']]

    # print(df)

    # rename as  NIC, name, email, password, phone, address, imageID
    df.rename(columns={'id': 'UserID', 'name': 'Name', 'password': 'Password', 'dob': 'DOB', 'phone': 'Phone', 'joinedat': 'JoinedAt'}, inplace=True)

    print(df)

    # Insert data into person table
    df.to_sql('user', db, if_exists='append', index=False)

    # # insert values to people table
    # for value in values:
    #     c.execute("INSERT INTO person({}) VALUES({})".format(','.join(col_names), ','.join(['?']*len(col_names))), value)
    #

    db.commit()


