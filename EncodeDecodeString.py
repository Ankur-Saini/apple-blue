class solution:
  def encode(self, strs):
    result = ""
    for word in strs:
      result += str(len(word)) + '/' + word
    return result

  def decode(self, str):
    result = list()
    i = 0
    for char in str:
      e = i
      while e < len(str) and e != '/':
        e += 1
      size = int(str[i:e])
      word = str[e+1: e+1+size]
      i = e + 1 + size
      result.append(word)
    return result

# Time complexity - O(n)

