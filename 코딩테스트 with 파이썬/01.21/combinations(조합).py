#이것이 취업을위한 코딩테스트다 with 파이썬
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) #2개를 뽑는 모든 조합 구하기
print(result)
