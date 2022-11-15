import sqlite3

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('../Database.db') as db:
    c = db.cursor()

# Create Tables
# -- User Table for Clerks
# ---- UserID, Name, Password, DOB, Phone, JoinedAt
c.execute('CREATE TABLE IF NOT EXISTS user (UserID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT , Password TEXT , DOB TEXT , Phone TEXT , JoinedAt TEXT );')

# -- Person Table for General Public
# ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
c.execute('CREATE TABLE IF NOT EXISTS person (PersonID INTEGER PRIMARY KEY AUTOINCREMENT, NIC TEXT , Name TEXT , Email TEXT , Password TEXT , Phone TEXT , Address TEXT , ImageID INTEGER );')

# -- Birth Certificate
# ---- CertificateID, PersonID, DateOfBirth, MotherID, FatherID, GrandfatherID (Later Calculate Age)
c.execute('CREATE TABLE IF NOT EXISTS birthcertificate (CertificateID INTEGER  PRIMARY KEY AUTOINCREMENT, PersonID TEXT , DateOfBirth TEXT , MotherID TEXT , FatherID TEXT , GrandfatherID TEXT );')

# -- NIC Card
# ---- PersonID, NIC, Name, OtherName, DateOfBirth, BirthLocation, Job, Address
c.execute('CREATE TABLE IF NOT EXISTS niccard (PersonID INTEGER  PRIMARY KEY AUTOINCREMENT, NIC TEXT , Name TEXT , OtherName TEXT , DateOfBirth TEXT , BirthLocation TEXT , Job TEXT , Address TEXT );')

# -- Vital Stats
# ---- FamilyCount, FamilyCount, GenderCount, TheirJobs
c.execute('CREATE TABLE IF NOT EXISTS vitalstats (PersonID INTEGER  PRIMARY KEY AUTOINCREMENT, FamilyCount TEXT , GenderCount TEXT , TheirJobs TEXT );')

# -- Marriage Certificate
# ---- PersonID1, PersonID2, (PersonID1 and PersonID2 as Primary key) DateOfMarriage
c.execute('CREATE TABLE IF NOT EXISTS marriagecertificate (PersonID1 INTEGER , PersonID2 INTEGER , DateOfMarriage TEXT , PRIMARY KEY (PersonID1, PersonID2));')


db.commit()
db.close()
