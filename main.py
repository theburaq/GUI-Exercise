#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# #trial 1:
# for image in picture:
#   for pixel in image:
#     if pixel == 1:
#       print('*')
#     else:
#       print(' ')

# #since the above code didnt print the picture how we wanted, so we can # # # use 'end' to align them
# #trial 2:
# for image in picture:
#   for pixel in image:
#     if pixel == 1:
#       print('*', end='')
#     else:
#       print(' ', end='')

#as we still didnt get the desired output, we'll add 'print()' at the end so # that'll add a line b/w the rows
#trial 3:
for row in picture:
  for pixel in row:
    if pixel == 1:
      print('*', end='')
    else:
      print(' ', end='')
  print('')
