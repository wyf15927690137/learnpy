import sys

print('this is a test file')
print('this is the second line from cloud')
print('this is the second line from cloud1')
print('this is the third line from Local')
print('this is the third line from Local1')
s1 = sys.argv[1]
s2 = sys.argv[2]
s3 = sys.argv[3]
print(sys.argv[0])  # return current file path
print(s1)
print(s2)
print(type(s3))  # view the datatype
s4 = int(s3)
print(type(s4))
print(int(s2) * int(s3))
