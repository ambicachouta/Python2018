import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

print(list(enumerate(text)))

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))
