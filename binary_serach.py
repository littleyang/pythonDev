numbers = [1,25,4,6,7,8,9,12,34,63,87,46,23,16,43,37,65,68,78,88,96]

def binary_search(dest,source):
  start = 0
  end = len(source)
  index = 0
  while True:
    index = start + ((end - start)/2)
    if source[index] > dest:
      end = index
    if source[index] < dest:
      start = index
    if source[index] == dest:
      print " the num %d index is %d" % (dest,index)
      break


def quick_sort(source,low =0,high = None):
  if high == None:
    high = len(source)-1
  if low < high:
    s,i,j = source[low],low,high
    while i<j:
      while i<j and source[j] >= s:
        j = j -1
      if i < j:
        source[i] = source[j]
        i = i+1
      while i<j and source[i] <= s:
        i = i+1
      if i<j:
        source[j]= source[i]
        j = j - 1
      source[i] = s
      quick_sort(source, low, i - 1)
      quick_sort(source, i + 1, high)
  return source

def show_result():
  data = quick_sort(numbers)
  print data
  binary_search(37,data)

show_result()

def hello():
    print "hello"


#print quick_sort(numbers)
#binary_search(37,numbers)
#print numbers[0]


