#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))




# names_file = open("../final_project/poi_names.txt","r")
# names_file_lines = names_file.readlines()
# names_file.close
# proper_names = []

# for item in iter(names_file_lines):  
#     if(item.startswith("(")):
#         proper_name = ((((item[4:]).replace(",","")).upper()).rstrip()).lstrip()
#         proper_names.append(proper_name)

# for item in iter(proper_names):
#     print (item)
#     print (item == "LOEHR CHRISTOPHER")

# print (enron_data)
# print(enron_data["METTS MARK"]["salary"])
# print(len(enron_data["METTS MARK"]))

# total_poi_count = 0

# poi_count = 0
# for key in enron_data:
#     print (key[:-2])
#     for item in iter(proper_names):
#         if(item == key):
#             total_poi_count += 1

#     poi_status = enron_data[key]["poi"]
#     if(poi_status):
#         poi_count += 1
# print (poi_count)

# print (total_poi_count)

# print (enron_data["SKILLING JEFFREY K"]["total_payments"])
# print (enron_data["LAY KENNETH L"]["total_payments"])
# print (enron_data["FASTOW ANDREW S"]["total_payments"])

known = 0
for key in enron_data:
    if(enron_data[key]["email_address"]!="NaN"):
        known +=1

print (known) 