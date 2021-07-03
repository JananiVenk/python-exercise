list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3=zip(list1,list2[::-1]) 
print("zip example code")
for i in list3:
  x,y = i
  print(x,y)
