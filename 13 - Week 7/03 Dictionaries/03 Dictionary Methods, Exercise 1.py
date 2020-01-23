# What will be printed after each of the following code segments? If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the correct Python output.

numbers={1: 2, 3:4}
numbers.pop(3)
print (numbers)
######################################################################
d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.pop("dos")) 
######################################################################
d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.get(3,'cat'))
######################################################################
numbers={"one": "uno", "two": "dos", "three": "tres"}
print (numbers.get("one","test"))
######################################################################
d={"uno":["one",1],"dos":["two",2],3:["tres","three"]}
print (d.has_key(3)) 
######################################################################
d={"uno":"one","dos":"two"}
d.setdefault('one', 'dog')
print (d["one"])