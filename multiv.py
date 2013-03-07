def foo(a,b,c,*other):
  return len(other)

def bar(a,b,c,**other):
  if other.get("magicnum")==7:
    return True
  else:
    return False

print foo(1,2,3,4,5,6)

print bar(1,2,3,magicnum=7)

if foo(1,2,3,4) == 1:
  print "Good."
if foo(1,2,3,4,5) == 2:
  print "Better."
if bar(1,2,3,magicnumber = 6) == False:
  print "Great."
if bar(1,2,3,magicnumber = 7) == True:
  print "Awesome!"


