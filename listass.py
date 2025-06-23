list1 = ['Zain']
list2 = ['ali']
list3 = ['moeez']
list4 = ['utba']
list5=['Rizwan']

choise1=int(input('Enter the List number you want to join Between 1 to 5:'))

choise2=int(input('Enter the List number you want to join Between 1 to 5:'))
if choise1==1:
    if choise2==2:
        print(list1 + list2)
    elif choise2==3:
        print(list1+list3)
    elif choise2==4:
        print(list1 + list4)
    elif choise2==5:
        print(list1 + list5)
    else:
        print('Enter the valid Entery')
elif choise1 ==2:
    if choise2==1:
        print(list2 + list1)
        
    elif choise2==2:
        print(list2 + list2)
    elif choise2==3:
        print(list2+list3)
    elif choise2==4:
        print(list2 + list4)
    elif choise2==5:
        print(list2 + list5)
    else:
        print('Enter the valid Entery')
elif choise1 ==3:
    if choise2==1:
        print(list3 + list1)
        
    if choise2==2:
        print(list3 + list2)
    elif choise2==3:
        print(list3+list3)
    elif choise2==4:
        print(list3 + list4)
    elif choise2==5:
        print(list3 + list5)
    else:
        print('Enter the valid Entery')
elif choise1 ==4:
    if choise2==1:
        print(list4 + list1)
        
    if choise2==2:
        print(list4 + list2)
    elif choise2==3:
        print(list4+list3)
    elif choise2==4:
        print(list4 + list4)
    elif choise2==5:
        print(list4 + list5)
    else:
        print('Enter the valid Entery')
elif choise1 ==5:
    if choise2==1:
        print(list5 + list1)
        
    if choise2==2:
        print(list5 + list2)
    elif choise2==3:
        print(list5+list3)
    elif choise2==4:
        print(list5 + list4)
    elif choise2==5:
        print(list5 + list5)
    else:
        print('Enter the valid Entery')
else:
    print('You input is invalid')