'''x=(" ali" , " utba" , " rizwan")
y=list(x)
y[1]="zain"
x=tuple(y)
print(x)'''

#add tuple to list
'''ali=(" 1" , "2" , " 3")
zain=list(ali)
zain.append(5)
ali=tuple(zain)'''
#add  tuple to tuple 
'''thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)'''
#delete 

'''thistuple = ("apple", "banana", "cherry")
y=list(thistuple)
y.remove("apple")
thistuple=tuple(y)
print(thistuple)'''
# add *
fruits=("apple" , " mango" , " orange" , " cherry" ," banana")
(green,red,*black)=fruits
print(green)
print(red)
print(black)



