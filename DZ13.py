lst=[("Иван", 25), ("Мария", 23), ("Петр", 25),("Анна", 23)]
d={}
for name, age in lst:
    if age not in d:
        d[age]=[]
        d[age].append(name)
    else:
        d[age].append(name)
print(d)


def top(nums,k):
    count={}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    items=[]
    for num, val in count.items():
        items.append((num, val))
    def get_freq(pair):
        return pair[1]
    items.sort(key=get_freq, reverse=True)

    result=[]
    for i in range(k):
        result.append(items[i][0])
    return result

nums=[1,1,1,2,2,3]
k=2
print(top(nums,k))


dict1={
    1:{"name":"Иван", "age":17},
    2:{"name":"Максим", "age":27},
    3:{"name":"Петр", "age":30},
}

dict2={
    2:{"name":"Мария", "age":20},
    4:{"name":"Анна", "age":22},
}
dict1_2={}
for key,value in dict1.items():
    if value["age"]>18:
        dict1_2[key]=value

d3=dict1_2 | dict2
print(d3)