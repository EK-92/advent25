# floor for calculating extra rotations
from math import floor
# import file
file=open("advent_day1_input", "r")
input=file.readlines()
# starting position
p=50
# length of possible steps (0-99)
len=100
# number of times the dial stops at 0, initialized
nully=0
for x in input:
  # first letter of the input data (R/L), indicates direction
  dir=x[0]
  # rest of the input being number of steps rotated
  n=int(x[1:])
  # number of times the dial is rotated more than 100 steps, initialized
  extra_rot=0
  # if number of steps taken is more than 100
  if (n>len):
    # calculate number of extra rotations
    extra_rot+=floor(n/len)
    # add the amount of steps dial takes compared to previous position
    n=n-(extra_rot*len)
  # if rotated clockwise
  if (dir=='R'):
    # add steps
    p+= n
    # if steps and initial position add up to >=100
    if (p>99):
      # ground it to get real position
      p=p-100
  else:
    # if rotated counterclockwise
    p-=n
    # same story as clockwise
    if (p<0):
      p=p+100
  # if dial stops at 0
  if (p==0):
    nully+=1

print(nully)
