import pandas as pd


# # Read the dataset
# df = pd.read_csv("people.csv")

# # Remove first column
# df = df.drop(df.columns[0], axis=1)
#
# # Separate m and f to different datasets by g column
# df_m = df[df['gender'] == 'male']
# df_f = df[df['gender'] == 'female']
#
# # Save the new datasets
# df_m.to_csv("people_m.csv", index=False)
# df_f.to_csv("people_f.csv", index=False)

# read people_m.csv
df = pd.read_csv("people.csv")
# df = pd.read_csv("people_f.csv")


# create a new dataframe to hold the search results
search_results = pd.DataFrame()

# funtion to search for a person by name
def search(name, search_results=None):
    # search for the name in the dataset
    result = df[df['name'].str.contains(name, case=False, na=False)]
    # # convert dataframe to json
    # json_data = result.to_json(orient='records',  indent=4)
    # # save json to file
    # with open('search.json', 'w') as f:
    #     f.write(json_data)
    # # load json file and return
    # with open('search.json') as f:
    #     data = json.load(f)
    # add the result to a dataframe
    search_results = pd.concat([search_results, result], ignore_index=True)


    return search_results


# Gotama Vyas + Jyotsna Nayak
# 	- Dinesh Dayal + Anima Dar
# 		- Mahinder Biswas + Ila More
# 			- Ananta-Sesa Kumar + Anuja Ramakrishnan (Change dob to 2000)

# search for a person by name
search_results = search("Gotama Vyas", search_results)
search_results = search("Jyotsna Nayak", search_results)
search_results = search("Dinesh Dayal", search_results)
search_results = search("Anima Dar", search_results)
search_results = search("Mahinder Biswas", search_results)
search_results = search("Ila More", search_results)
search_results = search("Ananta-Sesa Kumar", search_results)
search_results = search("Anuja Ramakrishnan", search_results)

# change dob of Anuja Ramakrishnan to 2000
search_results.loc[search_results['name'] == 'Anuja Ramakrishnan', 'dob'] = '2000-07-01'

# print the search results
print(search_results)

# save the search results to a csv file
search_results.to_csv("search_results.csv", index=False)
