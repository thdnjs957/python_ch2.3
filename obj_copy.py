# 레퍼런스 복사
import copy

a = 1
b = a

a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# swallow copy (얕은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x) # 레퍼런스 복사말고 copy는 y객체를 하나 만들고 그 안에꺼는 똑같은걸 가리킨다

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# deep copy (깊은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x) # y는 타고 들어가서 안에꺼 까지 다 copy해서 새로 만듦

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# 깊은 복사가 복합객체만을 생성하기 때문에
# 복합객체가 한개만 있는 경우에는
# 얕은복사, 깊은복사는 차이가 없다

a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

a = ['hello', 'world']
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

