num = int(input("enter number of rows:"))
for i in range(1,num+1):
    for j in range (1,i+1):
        print("*",end ="")
    print("")
print()


nom = int(input("enter number of rows:"))
for i in range (1,nom):
    print(" "*(nom-i)+"*"*i)


nem = int(input("enter number of rows:"))
for i in range (1,nem):
    print ("*"*(nom-i)+" "*i)

nam = int(input("enter number of rows:"))
for i in range (1,nam):
    print(" "*i+ "*"*(nam-i))

pyr = int(input("enter number of rows:"))   #pyramid    
gol = "*"
for i in range (1,pyr+1):
    print(" " * (pyr-i)+gol )
    gol=gol+"**"

you = int(input("enter number of rows:"))       #diamond
gel = "*"
for i in range (1,you+1):
    print(" " * (you-i)+gel)
    gel=gel+"**"

gel="*******"
for u in range (1,you+1):
    print(" "*u +gel)
    gel=gel[:-2]
