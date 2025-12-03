# floor for calculating extra rotations
from math import floor
# import file
file=open("advent_day1_input", "r")
input=file.readlines()
# starting position
p=50
# length of possible options (0-99)
len=100
# number of times the dial stops at 0, initialized
nully=0
for x in input:
  # first letter of the input data (R/L)
  dir=x[0]
  # rest of the input being number of places rotated
  n=int(x[1:])
  # number of times the dial is rotated more than 100 places, initialized
  extra_rot=0
  # can probably not use this assignment at all
  rem=n
  # if number of steps taken is more than 100
  if (rem>len):
    # calculate number of extra rotations
    extra_rot+=floor(n/len)
    # add the amount of steps dial takes compared to previous position
    rem=n-(extra_rot*len)
    # add each extra rotation to counter
    nully+=extra_rot
  # if rotated clockwise
  if (dir=='R'):
    # add steps
    p+= rem
    # if steps and initial position add up to >=100
    if (p>99):
      # ground it to get real position
      p=p-100
      # add the extra rotation to counter
      nully+=1
  else:
    # if rotated counterclockwise
    p-=rem
    # same story as clockwise
    if (p<0):
      p=p+100
      nully+=1
  # if dial stops at 0
  if (p==0):
    nully+=1

# says my result is too high ;(
print(nully)
