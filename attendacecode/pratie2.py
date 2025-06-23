'''f=open("C:/Users/Syed Ali Ubaid/Documents/file.txt")
print(f.readline())
f.close()'''

with open("C:/Users/Syed Ali Ubaid/Documents/file.txt", "w") as f:
    f.write("hi this is ali, i am a student of BSSE 5 semester at LGU. Now I am a python trainee at TeckSkillForge.")


with open("C:/Users/Syed Ali Ubaid/Documents/file.txt") as f:
    print(f.read())

