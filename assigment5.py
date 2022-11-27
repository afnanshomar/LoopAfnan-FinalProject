###Display numbers from a list using a loop
numbers=[12,75,150,180,145,525,50]
num = []
for i in numbers:
    if i > 150:
        if i > 500:
            break
        continue
    if i % 5 == 0:
        num.append(i)
print(num)
for i in range(5):
    print(i)
print("Done!")
###Revere number
num = 76542
print(str(num)[::-1])
### Convert two lists to dict
keys = ["Ten", "Twenty", "Thirty"]
values = [10, 20, 30]
res = {}
for key in keys:
    for value in values:
        res[key] = value
        values.remove(value)
        break
print(str(res))
####2 Delete a list of keys in dict
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york" }
keys = ["name", "salary"]
for k in keys:
    sampleDict.pop(k)
print(sampleDict)
###Add a list of element to a set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)
###return a new set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.intersection(set2))
### Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)
tuple1 = tuple1[::-1]
print(tuple1)
####Acess value 20 from the tuple
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])
####3: Unpack the tuple into 4 variables
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)
