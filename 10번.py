import os
os.chdir("c:\doit") #C:\doit 디렉터리로 이동
result = os.opne("dir") #dir 명령을 실행하고 그 결과를 변수에 담는다
print(result.read()) #dir 명령의 결과를 출력 
