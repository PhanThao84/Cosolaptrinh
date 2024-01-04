# st=input()      #-->5 10 15
# a,b,c=st.split(" ")
# a=int(a)
# b=int(b)
# c=int(c)
# print("a=",a,sep='')
# print("b=",b,sep='')
# print("c=",c,sep='')

# n=int(input('n='))
# f=open('vd1.txt','w')
# f.write(str(n)+'\n')
# st=""
# for i in range(n):
#     x=input()
#     st=st+x+' '
# f.write(st)
# f.close()

# n=int(input('n='))
# f=open('vd1.txt','w')
# f.write(str(n)+'\n')
# l=[]
# for i in range(n):
#     x=input()
#     l.append(x+' ')
# f.writelines(l)
# f.close()

f=open("vd1.txt","r")
n=f.readline()
n=int(n)    #Chuyen chuoi sang So
st=f.readline()
f.close()
L=st.split()      #~ st.split(" ")
dem=0
for x in L:
    x=int(x)    #Chuyen sang So nguyen
    if x%2==0:
        dem+=1
# Cach 1:
# f=open("output.txt","w")
# f.write(dem)
# f.close()
# Cach 2:
with open("output.txt","w") as f:
    f.write(str(dem))

