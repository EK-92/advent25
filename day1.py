from math import floor
file=open("advent_day1_input", "r")
input=file.readlines()
p=50
len=100
nully=0
for x in input:
  dir=x[0]
  n=int(x[1:])
  extra_rot=0
  rem=n
  if (rem>len):
    extra_rot+=floor(n/len)
    rem=n-(extra_rot*len)
  if (dir=='R'):
    p+= rem
    if (p>99):
      p=p-100
  else:
    p-=rem
    if (p<0):
      p=p+100
  if (p==0):
    nully+=1

print(nully)
