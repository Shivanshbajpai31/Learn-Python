#update()
ep1={122:45, 123:89, 567:89, 670: 69}
ep2={222: 67, 566 :90}

ep1.update(ep2)
print(ep1)

#info = {'name':'Karan', 'age':19, 'eligible':True}
#print(info)
#info.update({'age':20})
#info.update({'DOB':2001})
#print(info)

#clear()
ep1={122:45, 123:89, 567:89, 670: 69}
ep2={222: 67, 566 :90}
ep1.clear()

#pop
ep1={122:45, 123:89, 567:89, 670: 69}
ep2={222: 67, 566 :90}
ep1.pop(122)
print(ep1)

#pop item
ep1={122:45, 123:89, 567:89, 670: 69}
ep2={222: 67, 566 :90}
ep1.popitem()
print(ep1)

#del
ep1={122:45, 123:89, 567:89, 670: 69}
ep2={222: 67, 566 :90}
del ep1[122]
print(ep1)

