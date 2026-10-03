import math

dictionary = {
    "name": "Ligma Balls",
    "age": "69",
    "City": "West Viginia"
}


print(dictionary["name"])
print(dictionary["age"])
print(dictionary["City"])

# Access Keys And Values:

print(dictionary.keys())

# Iterate The Dictionary:

for key in dictionary:
    print(key," ",dictionary[key])

# Now Iterate Key And Value Both:

for key,value in dictionary.items():
    print(key," ",value)

# Remove Duplicate ID's


student_data={

"id1":{"name":"sara",

"class":"5",

"subject":"math"

    },

"id2":{"name":"Ligma",
    "class": "6",
    "subject": "english"
    
},

"id3":{"name":"sara",
    "class": "5",
    "subject": "math"
    
},
"id4":{"name":"Dissapointment",
    "class": "6",
    "subject": "english"

}

}

result = {}

seen_keys = []

for stduent_id, student_info in student_data.items():
    name = student_info["name"]
    if name not in seen_keys:
        seen_keys.append(name)
        result[stduent_id] = student_info

for student_id, student_info in result.items():
    print(student_id," : ", student_info)
    
# Use Pop Method

dictionary.pop("age")
print(dictionary)

# Use Update Method:


dictionary.update({"name": "Dissapoinment"})
print(dictionary)

# Add New Key Value Pair:


dictionary["Email"] = "doredxtheo@gmail.com"

print(dictionary)

dictionary["Phone"] = math.pi

print(dictionary)

# Createw Var tes_dict

tes_dict = {
    "Not_Codingal": 2,
    "is": 2,
    "best": 2
}

result = 0

for key in tes_dict:
    if tes_dict[key] == 2:
        result += 1
print(result)
