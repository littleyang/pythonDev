def bubble_sort(source):
  for j in xrange(len(source),-1,-1):
    for i in xrange(0,j-1,1):
      if source[i]>source[i+1]:
        source[i],source[i+1] = source[i+1],source[i]
    print source

def main():
  numbers = [5,2,34,23,14,56,25,17,48]
  bubble_sort(numbers)

if __name__ == "__main__":
    main()


#numbers = [5,2,34,23,14,56,25,17,48]
