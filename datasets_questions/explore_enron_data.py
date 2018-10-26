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

# print (enron_data)
# print(enron_data["METTS MARK"]["salary"])
# print(len(enron_data["METTS MARK"]))

poi_count = 0
for key in enron_data:
    poi_status = enron_data[key]["poi"]
    print (poi_status)
    if(poi_status):
        print ("POI!")
        poi_count += 1
    else:
        print ("false")

print (poi_count)


