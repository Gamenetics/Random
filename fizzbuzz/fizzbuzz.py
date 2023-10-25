for a in range(1, 100):
  a = "fizzbuzz" if a % 3 == 0 and a % 5 == 0 else ( "fizz" if a % 3 == 0 else "buzz" if a % 5 == 0 else a)
  print(a)