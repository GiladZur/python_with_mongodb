#!/usr/bin/python3

import pymongo
import sys

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["first_database"]
mycol = mydb["people"]

if sys.argv[1] == "insert":
	f=sys.argv[2]
	ff=sys.argv[3]
	print("first name :"+f)
	print("last name :"+ff)
	mydict = {"firstname":sys.argv[2],"lastname":sys.argv[3]}
	x=mycol.insert_one(mydict)
if sys.argv[1] == "show":
	for x in mycol.find():
		print(x)
