def is_subset_or_equal(tuple1, tuple2):
  a1, a2 = tuple1
  b1, b2 = tuple2
  return (((a1 != b1) and (a1 <= b1)) or ((a1 == b1) and (a2 <= b2)))

def find_subset_pairs(sets):
  subset_pairs = []
  for i, set1 in enumerate(sets):
    for set2 in sets[i+1:]:
      if is_subset_or_equal(set1, set2):
          subset_pairs.append((set1, set2))
  return subset_pairs

s = [({2}, {1, 3}), ({2, 3}, {1}), ({2}, {1, 2}), ({1, 2}, {2}), ({1, 2, 3}, set()), ({2}, {1, 2, 3})]
tuple_s = find_subset_pairs(s)
print(s)
print(is_subset_or_equal(s[0], s[0]))
print(tuple_s)
