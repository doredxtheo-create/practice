tuples = ("gg","oi","shrek")

for tuple in tuples:
    print(tuple)
    
tuples_1 = (
    ["Ryan Trahan",23],
    ["Shrek",14],
    ["Gian", 12]
)

print(tuples_1[0])
print("\n",tuples_1[1])   
print("\n",tuples_1[2]) 

tuple_x = (4,6,8,10)
tuple_x = tuple_x + (9,)
print(tuple_x)

# Count the number of apperence of item 4 from a tuple_x

print(tuple_x.count(4))

_slice = tuple_x[2:4]
print(_slice)

