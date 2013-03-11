def insert_sort(source):
  for i in xrange(1,len(source)):
    num = source[i]
    j = i
    while j>0 and source[j-1]>num:
      source[j] = source[j-1]
      j = j-1
    source[j] = num
  print source
  return source

def main():
  numbers = [3,21,45,34,25,27,38,12,43,86,95]
  print numbers
  print insert_sort(numbers)

if __name__ == "__main__":
  main()
