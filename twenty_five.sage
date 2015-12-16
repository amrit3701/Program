import pdb
#pdb.set_trace()
x = input()

x=int(x)

if(x<1):
  print 25


elif(x % 25 != 0):
  y = int(x / 25)
  y = y +  1
  z = y * 25
  print z


else:
  print x
