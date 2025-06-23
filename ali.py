#importing files
'''import pyjokes
a=pyjokes.get_joke
print(a)'''
'''import speech_recognition
x=speech_recognition
print(x)'''
#/variables
'''x=5
y='ali'
print(x)
print(y)
x=2
x='ali'
print(x)'''
#type casting 
'''x=9
x=float(x)
print(type(x))'''
#varible name 
'''myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(my_var)
print(MYVAR)'''
'''myVaribleName="ali"
print(myVaribleName)'''
#multiple value in one line 
'''a,b,c= "orange" ,"banana", "apple"
print(a)
print(b)
print(c)
a=c=d= "banana"
print(a,c,d)

fruits=["banana","apple","cheery"]
a,b,c=fruits
print(a)
print(c)
x="python"
y="is"
z="backend language"
print(x,y,z)
print(x+y+z)'''

'''x=4
y="ali"
print(x+y)
print(type(y))'''
# multi line string 
'''a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)'''
'''for x in "banana":
    print(x)


a = "Hello, World!"
print(len(a))'''
'''a= """ my name is ali ubaid i am a student of LGU i am currently which is given  below 
 SDA, CN, OR, BPE, PP """
print(len(a))
print(type(a))
print("LGU" not in a)
if "LGU" in a:
    print("LGU is present")'''
#slicing string 
'''v="hello, word"
print(v[2:8])
print(v[:6])
print(v[2:])
#negative indexing
x="ali ubaid"
print(x[-3:-5])
x="welcome"
print(x[3:5])
#format string
price=45
a=f"the price is {price} dollars"
print(a)
#escape string
e="my name is \"syed ali ubaid\" and i am 21"
print(e)'''
'''a= 'how are you'
print(a.split('o'))
a="hello "
b="word "
d="ali"
c=a+ b +d
print(len(a))'''
'''age=34
name="ali"
a=f"my name  is {name} , i am  {age} "
print(a)
txt = "\110\145\154\154\157"
print(txt) '''
#count
'''c="banana"
print(c.count( "a"))'''
#string methode 
'''w="hello ali kya hal ha "
print(w.find( "a"))'''

'''e="thon"
print(e.endswith("py"))'''
#operators 
#arithmetic operator 
'''z=7
c=3
print(z+c)
print(z-c)
print(z*c)
print(z/c)
print(z%c)
print(z//c)
print(z**c) 

#comparsion operator
r=10
o=8
print(r==o)
print(r!=o)
print(r>o)
print(r<o)
print(r>=o)
print(r<=o)
#identify  operator
x="banana","apple"
s="banana","apple"
z=s
print(x is s)
print(x is z)
print(x==z)
#logical operator 
#AND
x=4
y=5
print(x<5 and y<7)
#OR 
x=6
y=7
print(x<8 or x>7)

#call the variable 
print("z=", z)
print("c=", c)
print("r=" ,r)
print("o=", o)'''
#f string 
'''name="ali"
age=19
print(f"my age is:{age} ")
print(type(name))
print(type(age))'''
# lists
'''thislist=["apple " , " mango " ," orange"] 
print(thislist)
print(len(thislist))'''

'''list1=["apple", "mango" ,"orange"]
list2=[1,2,3,4]
list3=[True,False,False]
print(type(list1))
print(len(list2))
print(len(list3))
print=["abe", 12 , True]'''
#access list 
'''list=(" apple " , " banana " , " orange")
print(list[1])'''
#negative indexes 
'''list=(" apple " , " banana " , " orange")
print(list[-1])

newlist=(" apple" , " banana" , " kiwi" , " mango " , " orange")
print(newlist[2:5])

newlist=(" apple" , " banana" , " kiwi" , " mango " , " orange" , " melon" , "cheery")
print(newlist[:5])

newlist=(" apple" , " banana" , " kiwi" , " mango " , " orange" , " melon" , "cheery")
print(newlist[4:])

newlist=(" apple" , " banana" , " kiwi" , " mango " , " orange" , " melon" , "cheery")
print(newlist[-4:-1])

listNew=[" apple " , " banana " , " orange"]
if "banana" in listNew:
 print("yes , 'banana' is in the  lit" )
#change list item 

thislist=[" apple " , " banana " , " orange"]
thislist[1]=" water melon"
print(thislist)

thislist=[" apple " , " banana " , " orange"]
thislist.insert( 2," water melon")
print(thislist)'''
#append 
'''thislist=[" apple " , " banana " , " orange"]
thislist.append ('water melon')
print(thislist)
#pop 
ali=[" apple " , " banana " , " orange"]
ali.pop()
print(ali)'''
#loop in a trough index num
'''thislist=[" apple " , "mango",  "cheery"]
for i in range(len(thislist)):
    print(thislist)'''
#while loop 
'''thislist=[" apple " , "mango",  "cheery"]
i=0
while i< len(thislist):
    print(thislist[i])
    i=i+1'''
# list comprehension
'''fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)'''











