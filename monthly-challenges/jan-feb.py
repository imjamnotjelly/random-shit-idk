# good version
num = 0
while True:
  num += 1
  for i in range(2, 11):
    if num % i != i - 1:
      break
  else:
    print(num)
    break

# bad version (recursive)
import sys

sys.setrecursionlimit(5000)


def ans(num=1):
  for i in range(2, 11):
    if num % i != i - 1:
      return ans(num + 1)
  else:
    return num


print(ans())
