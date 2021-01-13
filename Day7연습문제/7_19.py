import re

s="""
park 010-9999-9988
kim 010-9009-0000
lee 010-9007-0000
"""

pat = re.compile("(\d{3}[-]\d{4})[-]\d{4}")
result = pat.sub("\g<1>-####", s)

print(result)
