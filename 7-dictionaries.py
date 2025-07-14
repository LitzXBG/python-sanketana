#creating a dictionary
myCar = {
    "brand": "Mercedes",
    "model": "Benz", 
    "year": 2010,
    "prevOwners": [
        {
            "name": "abhinav",
            "location": "India",
            "kids": ["adi", "siddi"]
        },
        {
            "name": "Divit",
            "location": "Singapore"
        }
    ]
}
# for i in myCar:
#     print(i)
# for i in myCar:
#     print(myCar[i])

# print(dir(myCar.items()))

# for k,v in myCar.items():
#     print(k,v)
# print(type(myCar.values()))
lst = myCar["prevOwners"]
for i in lst:
    print(i["name"])

if "model1" in myCar:
    print("exists")
else:
    print("doesnt exist")
print (len(myCar))

myCar["Currentowner"] = "bill gates"
print(myCar)
myCar.pop("Currentowner")
print(myCar)
del myCar
