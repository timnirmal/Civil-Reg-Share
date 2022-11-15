# ---- PersonID, NIC, Name, Email, Password, Phone, Address, ImageID
# ---- UserID, Name, Password, DOB, Phone, JoinedAt
# ---- MotherID, FatherID, GrandfatherID, BirthLocation, Job, Address


import randominfo
import uuid
import random
import randomtimestamp
import datetime
import json
import pandas as pd


def random_email(first_name):
    domains = ["gmail", "yahoo", "hotmail", "express", "yandex", "nexus", "online", "omega", "institute", "finance",
               "company", "corporation", "community"]
    extentions = ['com', 'in', 'jp', 'us', 'uk', 'org', 'edu', 'au', 'de', 'co', 'me', 'biz', 'dev', 'ngo', 'site',
                  'xyz', 'zero', 'tech']

    random_Numeber = random.randint(0, 1000)

    return f"{first_name.lower()}{random_Numeber}@{random.choice(domains)}.{random.choice(extentions)}"


def random_join_date_generator():
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=2005, end_year=2022)

    return generated.strftime("%m/%d/%Y, %H:%M:%S")


def random_date_generator():
    now = datetime.datetime.now()
    generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)

    # IF generated timestamp is in the future, then generate a new one
    while generated > now:
        generated = randomtimestamp.randomtimestamp(start_year=1900, end_year=2022)

    return generated.strftime("%m/%d/%Y, %H:%M:%S")


def get_nic(dob):
    # print(dob)
    dob = "12 Jun, 1975"
    # last two digits of dob
    dob = dob.split(",")[1][-2:]
    # print(dob)

    # National Identity card with 10 digits and "V" at end
    # 1st two digits are the year of birth
    birthYear = dob
    # 8 digits are random
    randomDigits = str(random.randint(10000000, 99999999))
    IDnumber = birthYear + randomDigits + "V"
    return IDnumber


def get_uuid():
    return str(uuid.uuid4())


def generate_person():
    first_name = randominfo.get_first_name(gender=None)

    userid = uuid.uuid4()
    username = first_name + " " + randominfo.get_last_name()
    password = randominfo.random_password(length=8)
    gender = randominfo.get_gender(first_name=first_name)
    dob = randominfo.get_birthdate()
    email = random_email(first_name)
    phone = randominfo.get_phone_number()
    joined_date = random_date_generator()
    url = "https://robohash.org/c0eb5cc8f036ec7ecd9d1f5b1f2ccb69?set=set4&bgset=&size=400x400"
    NIC = get_nic(dob)
    birthLocation = "Colombo"
    address = "2nd Lane, Maharagama"
    imgUrl = "https://civilreg.org/" + get_uuid()

    # to json
    person = {
        # "id": str(userid),
        "name": username,
        "password": password,
        "gender": gender,
        "email": email,
        "phone": phone,
        "joinedat": joined_date,
        "dob": dob,
        "NIC": NIC,
        "birthLocation": birthLocation,
        "address": address,
        "imgUrl": imgUrl
    }

    return person


def generate_people(count):
    people = [generate_person() for i in range(count)]
    return people


if __name__ == "__main__":
    print("Generating Data...")

    people = generate_people(40)
    # list to dataframe
    df = pd.DataFrame(people)
    print(df)

    # save df to csv
    df.to_csv("people.csv", index=False)
