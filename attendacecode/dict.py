'''ali={
     "name":"ubaid",
     "model":"mustang",
}
print(ali)

thisdict={
     "name" :"haider ",
     "model":" list",
     "year":"1234"
}
print(thisdict["model"])
#change in dict
car={
    "name":"ford",
    "model":"set",
    "year":"123"
}
x = car.values()
print(x)
car["year"]=2020
print(x)
#nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)'''
#match 
day=4
match day:
    
        case 1 :
          print("Monday")
        case 2 :
           print("Tuesday")
        case 3 :
          print("Wednesday")
        case 4 :
         print("Thursday")
        case 5 :
         print("Friday")
        case 6 :
         print("Saturday")
        case 7 :
         print("Sunday")

month=5
day=4
match day:
  case 1 | 2| 3 |4 |5 if month==4:
    print("A weekend in April")
  case 1 | 2| 3 |4 |5 if month==5:
    print("A weekend in may")
  case _:
    print("no match")