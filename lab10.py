# Author: Nicole Giron nqg5259@psu.edu
# Collaborator: Joshua Mclntyre jjm7410@psu.edu
# Collaborator: Youhyun Kim yfk5109@psu.edu
# Collaborator: Linghe Du lpd5243@psu.edu
# Section: 4
# Breakout: 13

def remove_duplicate_sorted(t):
  """
  this function returns a new list generated from t that has t's
  elements without duplicates and is sorted from smallest to largest.
  """
  return sorted(set(t))

def list_to_dictionary(t):
  """
  t is a list of values (values could be str, list, tuple, set, dictionary),
  create and return a dictionary such that the key is len(v) for some v in t,
  and the value is a list of values [v1, v2, ...] from t (in the order they
  appeared in t) whose len(vi) is the key.
  for example: if t = [(1,2,3), "abc", [1, 2], (), ""]
  then return value of this function should be:
  {3: [(1, 2, 3), 'abc'], 2: [[1, 2]], 0: [(), '']}
  """
  newDict = {}
  for value in t:
    if len(value) in newDict:
      newDict[len(value)].append(value)
    else:
      newDict[len(value)] = [value]
  return newDict

def run():
  """
  This function repeatedly ask user to enter a string and store them in a
  list and print it out.
  It also passes this list to remove_duplicate_sorted() function and
  list_to_dictionary() function and print out the results of the function
  calls.
  """
  l = []
  while True:
    value = input("Enter a string: ")
    if value == "done":
      break
    l.append(value)
  print("List: " + str(l))
  print("Sorted List: " + str(remove_duplicate_sorted(l)))
  print("Dict: " + str(list_to_dictionary(l)))
  return

if __name__ == "__main__":
  run()
