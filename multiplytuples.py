tuple1 = (4, 2, 3,2,-1,18)
tuple2 = (2,4,8,8,3,2,9)


result_tuple = tuple(a * b for a, b in zip(tuple1, tuple2))
print(f"Element-wise multiplied tuple: {result_tuple}")

