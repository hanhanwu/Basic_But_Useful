import sys
import operator

if len(sys.argv) > 1:
    name = sys.argv[1]
    print("Hello", name)
else: print ("hehehe")


# prints whether python is version 3 or not
python_version = sys.version_info.major
if python_version == 3:
    print("is python 3")
else:
    print("not python 3")


print('Python', python_version)
my_generator = (letter for letter in 'abcdefg')
print (next(my_generator))
print (next(my_generator))


# round to the nearby even number
print(round(23.4))
print(round(23.5))
print(round(22.5))


p3_dct = {'a': 4, 'b': 1, 'c': 0}
for k,v in p3_dct.items():
    print (k,v,7)
sorted_x = sorted(p3_dct.items(), key=operator.itemgetter(1))
print (sorted_x)
