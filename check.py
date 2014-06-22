#!/usr/bin/env python

f = open('/usr/share/dict/words')
words = f.readlines()
f.close()

# trim
words = map(lambda w: w.strip(), words)

# only with 6 letters
words = filter(lambda w: len(w) == 6, words)

# all lowercase
words = map(lambda w: w.lower(), words)

codes = {}
f = open('country_codes.txt')
for line in f.readlines():
  line = line.strip()
  (name, code) = line.split("\t")
  name = name.strip()
  code = code.strip()
  code = code.lower()
  codes[code] = name
f.close()

for left in codes.keys():
  for right in codes.keys():
    # no pairings with the same country against itself
    if left == right:
      continue
    word = left + right
    if word in words:
      print "<tr><td>" + codes[left] + "</td><td>" + codes[right] + "</td><td><code>" + word + "</code></td></tr>"
