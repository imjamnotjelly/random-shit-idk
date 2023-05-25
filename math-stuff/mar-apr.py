def factor(num):
  return [i for i in range(1, num + 1) if num % i == 0]


num = 50
possibilities = 0
while True:
  num += 1
  factored_num = factor(num)
  if all(
    len(factored_num) == 4,
    len([i for i in factored_num if i < 50]) == 3
  ):
    possibilities += 1
    print(possibilities)

# ans: 94