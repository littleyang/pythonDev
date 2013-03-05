f = open("list.py")
try:
  for line in f:
    print line,
finally:
  f.close()
