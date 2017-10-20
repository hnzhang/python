def test1():
  l = []
  for i in range(1000):
     l = l +[i]
def test2():
  l = []
  for i in range(1000):
    l.append(i)

def test3():
  l = [ i for i in range(1000)]

def test4():
   l = list(range(1000))

def is_happy_number(number):
    if number == 1:
        return True
    histoy = set()
    
    while number not in histoy:
        new_number  = 0
        histoy.add(number)
        while number > 0:
            digit = number % 10
            
            new_number += digit*digit
            number = number //10
        if new_number == 1:
            return True
        number = new_number
        
    return False


import timeit

t1 = timeit.Timer(stmt="test1()", setup="from __main__ import test1")
print("concat", t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer(stmt="test2()", setup="from __main__ import test2")
print("append", t2.timeit(number=1000), "milliseconds")


t3 = timeit.Timer(stmt="test3()", setup="from __main__ import test3")
print("apprehension", t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer(stmt="test4()", setup="from __main__ import test4")
print("list range", t4.timeit(number=1000), "milliseconds")

test_happy_num = [12]
for num in test_happy_num:
  print("testing happy num:", num, "result:", is_happy_number(num))