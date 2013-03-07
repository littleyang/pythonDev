read_file = open("test.txt")
file_list = []
try:
  for line in read_file.readlines():
    line = line.strip()
    if not len(line) or line.startswith('#'):
      continue
    file_list.append(line)
finally:
  read_file.close()
file_list.sort()
open('result_test.txt','w').write('%s' % '\n'.join(file_list))
#print file_list

