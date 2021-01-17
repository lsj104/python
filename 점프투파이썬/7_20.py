import re

pat = re.compile(".*[@].*[.](?=com$|net$).*$")

print(pat.match("kkk@gmail.com"))
print(pat.match("kkk@daum.net"))
print(pat.match("kkk#myhome.co.kr"))
