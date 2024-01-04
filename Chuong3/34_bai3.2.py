#a=int(input('M1='))
#b=int(input('M2='))
#c=int(input('M3='))
#S=int(input('S='))
#if 0<S<=100:
     #print('Phai tra='+str(S*a))
#if 101<S<=150:
    #print('Phai tra='+str((100*a)+(S-100)*b))
#if S>150:
     #print('Phai tra='+str(((100*a)+50*b+(S-150)*c)))
M1=int(input('M1='))
M2=int(input('M2='))
M3=int(input('M3='))
S=int(input('S='))
if S<=100:
     Phaitra=S*M1   
elif 101<=S<=150:
     Phaitra=100*M1+(S-100)*M2
elif S>=151:
     Phaitra=100*M1+50*M2+(S-150)*M3
print('Phaitra=',round(Phaitra),sep='')