Name="Adarsh"
print(type(Name))
LastName=" pawade"
Age=19

#Concatination
print(Name + LastName)

# in python wwe can't concat the Int with Str



# String methods in python  of caseHandling
str1="adarsh"
str2="ADARSH"
print("Capitalized: ",str1.capitalize())
print("Upper Case : ", str1.upper())
print("lower Case : ", str2.lower())
print("Title :",str2.title() )
print("Swapcase : ", str1.swapcase())

#formatting and Alignment

print("Formatting of strings")
print("Center : ", str1.center(20,"_"))


#searching
s="hello, world!"

print(s)
print(s.find("world"))
print(s.rfind("l"))
print(s.index("world"))
print(s.count("l"))

#starts/Ends

print(s.startswith(" He"))
print(s.endswith("!  "))



#validation
num=123
num1="Hello123"
space = " \t\n"

print("Hello".isalpha)


title = "This Is A Title"
words = ["Python", "is", "awesome"]
multi_line = "Line1\nLine2\nLine3"


#joining & splitting

print(" Hii ".join(words))
print(s.split())
print(s.rsplit())
print(s.partition(","))
print(s.rpartition(","))

#replace & Modify

print("replace and modify")

print(s.replace("world", "Adarsh"))
table=str.maketrans("HW","hw")
print(s.translate(table))
print(s.strip())
print(s.rstrip())
print(s.removeprefix(" He"))
print(s.removesuffix("!  "))








#