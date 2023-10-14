def যোগ(x, y):
  return x + y

def বিয়োগ(x, y):
  return x - y

def গুণ(x, y):
  return x * y

def ভাগ(x, y):
  return x / y

def মড(x, y):
  return x % y

def সমান(x, y):
  return x == y

def অসমান(x, y):
  return x != y

def কম(x, y):
  return x < y

def বড়(x, y):
  return x > y

def কম_বা_সমান(x, y):
  return x <= y

def বড়_বা_সমান(x, y):
  return x >= y

def এবং(x, y):
  return x and y

def অথবা(x, y):
  return x or y

def নয়(x):
  return not x

def মুদ্রণ(*args):
  print(*args)

def গ্রহণ(prompt):
  return input(prompt)

def স্ট্রিং_প্রিন্ট(string):
  print(string)

def যতক্ষণ_না(condition):
  while not condition:
    yield

def যতক্ষণ(condition):
  while condition:
    yield

def জন্য(iterable):
  for item in iterable:
    yield

def যদি(condition):
  if condition:
    yield

def অন্যথা():
  yield
