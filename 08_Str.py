Fname = "Python"
LName = "3.8"
msg1 = "This's the message"
msg2 = '"Yes Congrats!", Yes u did a awesome job. Yes Yes u did'
msg3 = "Test \ncmp"
alphanum = "alpha1214"
num = "11111123123123"
spac = " "
upp = "TEST"
mult= """This's 
the multiline
string"""

esc = 'This\'s the escape string'
print(Fname, LName, Fname+LName)
print("first" "second")
print(Fname[2] , type(Fname[2]))
print(msg1)
print(msg2)
print(msg3)
print(mult)
print(esc)
print("count", esc.count("T"))

print("StartWith", msg2.startswith("\"Yes"))
print("endwith", msg2.endswith("job"))

print("find", msg2.find("Yes"))
print("rfind", msg2.rfind("Yes"))

print("index",msg2.index("did"),msg2.index("u"))
print("rindex",msg2.rindex("did"),msg2.rindex("u"))

print("isalnum", alphanum.isalnum() )
print("isdecimal", LName.isdecimal() )
print("isdecimal", num.isdigit() )
print("isnumeric", num.isnumeric() )

print("isspace", spac.isspace())
print("istitle", Fname.istitle())

print("is upper",upp.isupper())

print("convert to Lower",msg2.lower())
print("convert to Upper",msg2.upper())
print("swapcase", msg2.swapcase())

print("Join", Fname.join("N0"))
print("Replace", msg2.replace("did","didn\'t"))

print("split", msg1.split())
print("split", msg1.split("'"))

print("rsplit", msg1.rsplit())
print("splitlines", mult.splitlines())
