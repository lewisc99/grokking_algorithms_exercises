def maximum(numbers):
  if len(numbers) == 1:
    return numbers[0]
  rest_max = maximum(numbers[1:])
  return numbers[0] if numbers[0] > rest_max else rest_max

print(maximum([1,4,3,2]))