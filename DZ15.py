print((lambda x,y,z:x*y*z)(2,5,5))


test=[{'name': 'Jenifer', 'final':95},
      {'name': 'David', 'final':92},
      {'name': 'Nikolas', 'final':98}]

test.sort(key=lambda x:x['name'], reverse=False)
print(test)

test.sort(key=lambda x:x['final'], reverse=True)
print(test)
print(test[0])
print(test[-1])

# либо можно так
maximum=max(test,key=lambda x:x['final'])
print(maximum)
minimum=min(test,key=lambda x:x['final'])
print(minimum)

nums=[3,5,7,3,9,5,7,2]
sq=[]
for num in nums:
    sq.append((lambda x:x**2)(num))
print(sq)
cb=[]
for num in nums:
    cb.append((lambda x:x**3)(num))
print(cb)
