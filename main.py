import random
x = list(range(0, 93))
output = list(random.sample(x, 91))
for i in range(0, len(output)):
  print(output[i])