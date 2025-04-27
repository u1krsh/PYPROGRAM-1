from pymongo import MongoClient

client = MongoClient("localhost",27017)

db = client["school"]

col = db["Students"]
# x = col.insert_one({"name":"Saumya", "age":19,"gpa":8.1})

for i in col.find({"age":19}).sort("gpa",1) :
    print(i)