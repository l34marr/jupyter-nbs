# https://datahub.io/dataset/world-top-incomes-database
# wget https://commondatastorage.googleapis.com/ckannet-storage/2012-01-07T150817/data.csv
import csv
data_file = "data.csv"
with open(data_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
#   data = list(reader)
    for row in reader:
        print(row['Country'], row['Year'], row['Price index'])

#len(reader)
#   for i in reader.fieldnames:
#       print(i)
#   print(reader.fieldnames)
# len(reader.fieldnames)

# def dataset(path):
#     with open(path, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             yield row
# 
# print(set([row["Country"] for row in dataset(data_file)]))
# print(min(set([int(row["Year"]) for row in dataset(data_file)])))
# print(max(set([int(row["Year"]) for row in dataset(data_file)])))
# 
# filter(lambda row: row["Country"] == "United States", dataset(data_file))
# 
