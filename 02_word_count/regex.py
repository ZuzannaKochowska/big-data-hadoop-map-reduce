import re
# regular expressions

WORD_RE = re.compile(r'[\w]+')

words = WORD_RE.findall('Big Data, hadoop and map reduce. (hello world!)')
print(words)
