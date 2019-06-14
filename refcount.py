import sys

x = object()
print(type(x))
print(sys.getrefcount(x)) # 파라미터 호출할때까지 합해서 2개

y = x
print(sys.getrefcount(x))

# 레퍼런스 값 줄이기
# del 은 심볼 테이블에서 이름을 삭제한다.
del x
print(sys.getrefcount(y))
print(globals())
