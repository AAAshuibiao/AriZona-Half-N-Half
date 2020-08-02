import random
lst = ["Enderby", "JayK", "Riptide", "ZackWang"]
while lst:
  print(lst.pop(random.randint(0, len(lst)-1)))
