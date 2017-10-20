import random

def init_RandomStr():
  template_str = "jasper is a smarthead"
  
  STR_LEN = len(template_str)
  l = list(range(STR_LEN))
  char_pool='abcdefghijklmnopqrstuvwxyz '
  lower_bound = 0
  higher_bound = len(char_pool)-1
  for i in range(STR_LEN):
    index = random.randrange(lower_bound, higher_bound )
    l[i] = char_pool[index]
  return  l

def RandomStr(l):
  template_str = "esther says she is smart but she is not that smart"
  template_str = "jasper is a smarthead"
  
  STR_LEN = len(template_str)
  char_pool='abcdefghijklmnopqrstuvwxyz '
  lower_bound = 0
  higher_bound = len(char_pool)
  
  for i in range(STR_LEN):
    if l[i] == template_str[i]:
      continue
    else:
      index = random.randrange(lower_bound, higher_bound )
      l[i] = char_pool[index]

def CompareStr(input_str):
  template_str = "esther says she is smart but she is not that smart"
  template_str = "jasper is a smarthead"
  score = 0
  for i in range(len(template_str)):
    if input_str[i] == template_str[i]:
      score +=1
  return score

def generate_and_score():
  template_str = "esther says she is smart but she is not that smart"
  template_str = "jasper is a smarthead"

  match_score = len(template_str)
  l = init_RandomStr()

  i = 0
  max_score = -1
  str_of_max_score = None
  while True:
    RandomStr(l)
    random_str = ''.join(l)
    score = CompareStr(random_str)
    if score == match_score:
      print("Got it", random_str, i)
      break
    
    if score > max_score:
      max_score = score
      str_of_max_score = random_str
    print("Guess:", random_str)
    #if i%1000 == 0:
    #  print("best match:", str_of_max_score, " score", max_score, i )
    i+=1
def randomTest():
  low = 10
  high = 100
  i = 0
  while True:
    n =  random.randrange(low, high)
    if n == low: print("low")
    elif n == high-1:
       print("high and stop ut")
       break
    if i % 1000 == 0: print("i", i)
    i+=1

#randomTest()
generate_and_score()
