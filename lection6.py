#------------- 1 -------------

s = input('>>> ')
res = 0

for item in s:
    if item == 'b':
        res += 1

print(res)

# or

s = input('>>> ')
print(s.count('b'))

#------------- 2 -------------

name = input('Name: ')
res = 'Valid' if name.istitle() and name.isalpha() else 'NOT valid'

print(res)
#------------- 3 -------------

s = input('>>> ')
res = 0

for item in s:
    res += ord(item)

print(res)

#------------- 4 -------------

import math

for n in range(2, 12):
    print(f'{math.pi:.{n}f}')

#------------- 5 -------------
    
s = input('>>> ')
print(max(s.split(), key=len))

#------------- 6 -------------

s = input('>>> ')

  for i in range(1, len(s) // 2):
  pattern = s[:i]
  if s.count(pattern) * len(pattern) == len(s):
      print(pattern)
      break
else:
  print('Error')

#------------- 7 -------------

tags = ['p', 'a', 'h1', 'h2']

html_text = '''
<a parameters>Python is the best programming language</a>
<p parameters>Some text text text text text text <a parameters>LINK</a>
'''

for tag in tags:
    while f'<{tag}' in html_text:
        start = html_text.find(f'<{tag}') 
        stop = html_text.find('>', start + 1)

        html_text = html_text.replace(html_text[start : stop + 1], '')
    html_text = html_text.replace(f'</{tag}>', '')

print(html_text)
