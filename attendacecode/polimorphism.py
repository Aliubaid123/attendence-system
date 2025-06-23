l=[10,20,30]
print(len(l))
s="well come "
print(len(s))
 
 # function overloading 
class Ws:
    def displayinfo(self,name=""):
        print("well come to Ws",name)
obj=Ws()
obj.displayinfo()
obj.displayinfo("python")

# function override 

class Ws:
    def displayinfo(self):
        print("well come to Ws")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Well come to IIP ")
obj=IIP()
obj.displayinfo()




