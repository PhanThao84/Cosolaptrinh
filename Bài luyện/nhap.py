# code trái tim bằng kí tự nha ae
def t(n,s):
  for i in range(1,n):
    print(s,end='')
  return s
i=20;d=2;dau=6;sao=4;giua=8
for dau in range(6,2,-1):
 t(dau,' ')
 print(end='')
 t(sao,'*')
 print(end='')
 t(giua,' ')
 print(end='')
 t(sao,'*')
 print()
 giua-=2
 sao+=2
for k in range(1,3):
  t(2,' ')
  print(end='')
  t(22,'*')
  print()
while i>1:
  d+=1
  t(d,' ')
  print(end='')
  t(i,'*')
  print()
  i-=2

print('   ','Mãi iu :>')