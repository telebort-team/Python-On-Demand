my_list = ['apple', 'banana', 'orange']
print(my_list)			# [‘apple’, ‘banana’, ‘orange’]
my_list[1]				# ‘banana’
my_list[2] = 'grape'
print(my_list)			# [‘apple’, ‘banana’, ‘grape’]

x = [21, 30, 42, 9, 47, 90, 78, 87]
x[2:5]              # [42, 9, 47]
x[3:]			    # [9, 47, 90, 78, 87]
x[:5]			    # [21, 30, 42, 9, 47]
len(x)			    # 8
x.append(54)	    # [21, 30, 42, 9, 47, 90, 78, 87, 54]
x.insert(2, 77)	    # [21, 30, 77, 42, 9, 47, 90, 78, 87, 54]
x.pop()			    # [21, 30, 77, 42, 9, 47, 90, 78, 87]
x.pop(4)		    # [21, 30, 77, 42, 47, 90, 78, 87]
x.clear()		    # []
