# nested list comprehension practice
even = [23, 26, 25, 14, 7, 29, 21, 33, 1, 2, 3, 15, 99, 101, 7, 505, 69, 420, 80085, 30, 56, 18, 10]
ls = [digit for digit in [num for num in even if num%2 == 0] if digit in range(51)]
for i in ls:
  print(i, '\n', sep='')
