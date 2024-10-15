def task_1():
  total = 0
  try:
  with open('task_1.text', 'r') as file:
    for line in file:
      int(line.strip())
      return total
except fileNotFoundError:
return "File not found."
except valueError:
return "File contains non intger values."


result = task_1()
print(result)
