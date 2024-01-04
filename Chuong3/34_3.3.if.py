S=int(input('Tieu thu='))
if 1<S<100:
    giatien=S*550
elif S<=150:
    giatien=100*550+(S-100)*750
elif S<=200:
    giatien=100*550+50*750+(S-150)*950
elif S>=201:
    giatien=100*550+50*750+50*950+(S-200)*1350
VAT=giatien*(10/100)
print('Phaitra=',giatien+VAT,sep='')