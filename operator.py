x = object()
y = object()

x_list = [x,x,x,x,x,x,x,x,x,x]
y_list = [y,y,y,y,y,y,y,y,y,y]

big_list = []

big_list = x_list + y_list

print "x_list contain %d object" % len(x_list)
print "y_list contain %d object" % len(y_list)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
  print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
  print "Great!"
