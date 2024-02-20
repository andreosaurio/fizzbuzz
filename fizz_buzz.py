def fizzbuzz(max_number):
  for number in range(1, max_number + 1):
      if number % 3 == 0 and number % 5 == 0:
          print("FizzBuzz")
      elif number % 3 == 0:
          print("Fizz")
      elif number % 5 == 0:
          print("Buzz")
      else:
          print(number)

fizzbuzz(100)