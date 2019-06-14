g_a = 1
g_b = '소원'
# print(globals())

def f():
    l_a = 2
    l_b = '건형'
    print(locals())

f() # 두번째 symbol table로 볼 수 있다

class MyClass:
    x = 10
    y = 20

# 1. 정의된 함수에 symbol table이 있다
f.k = 'hello'  # f 라는 객체에 k 라는 이름으로 레퍼런스하는게 있다 레퍼런싱하는건 symbol table 밖에 없다.
               # 즉 객체 자체에도 symbol table이 있다

print(f.__dict__)  # 그 symbol table 보는 법

# 2. 클래스 객체에도 symbol table이 있다
MyClass.z = 10
# print(MyClass.__dict__)


# 내장함수는 symbol table 도 없다 -> extension X
# print(print.__dict__)

# 내장클래스는 symbol table이 있으나 extension 금지
# str.z = 10
# print(str.__dict__)


# f() # local 호출
# print(globals())

# 내장클래스로 생성된 객체
# 심벌테이블 X => 확장 X
# g_a.z = 10
# print(g_a.__dict__)


# 사용자 정의된 클래스로 생성된 객체
# 심벌테이블 X => 확장 X
o = MyClass()
o.z = 120
print(o.__dict__)