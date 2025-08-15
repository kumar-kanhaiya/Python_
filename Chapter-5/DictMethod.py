
"""

Methods: 
.items // it provide the key value pairs 
        in the form of tupple 
.keys // it provide the  key 
.values // it provide the value from key value pairs 
.update // used to update the value of key 


"""

marks = {
    "kanhaiya" : 95,
    "shubham" : 85,
    "manish" : 98 
}

# print(marks.items())
# print(marks.keys())
marks.update({"kanhaiya":92})
marks.update({"muskan":99}); # it add the muskan in the disct

# print(marks.values())
print(marks)