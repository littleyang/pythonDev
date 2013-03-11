def mergesort(L):
  print "before: ", L
  if len(L)<2:
    return L[:]
  else:
    middle = len(L)/2

    left = mergesort(L[:middle])
    right = mergesort(L[middle:])
    together = merge(left,right)
    print "left: " , left
    print "right: ", right
    print "together: ",together
    return together


def merge(left,right):
  result = []
  i,j = 0,0
  while i<len(left) and j<len(right):
    if left[i]<=right[j]:
      result.append(left[i])
      i= i+1
    else:
      result.append(right[j])
      j= j+1

  while i<len(left):
    result.append(left[i])
    i=i+1

  while j<len(right):
    result.append(right[j])
    j=j+1
  return result

def main():
  numbers = [3,5,28,2,45,34,67,13,23]
  mergesort(numbers)

if __name__ == "__main__":
  main()



