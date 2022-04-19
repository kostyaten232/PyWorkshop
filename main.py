stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]

weights = {
  0: 5,
  1: 7,
  2: 5,
  3: 8,
  4: 7,
  5: 4,
  6: 6
}

max_value = max(weights.values())
print(max_value)

rev_weights = {v: k for k, v in weights.items()}

max_key = stock[rev_weights[max_value]]
print(max_key)