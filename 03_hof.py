def sum(x, y):
  return x + y


# This is a High Order Function
def operacion(x, y, func):
  return func(x, y)


print(operacion(1, 2, sum))

gg = lambda x, y, func: y +  func(x, 2)

print(gg(1, 2, sum))
