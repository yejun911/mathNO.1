import numpy as np
import matplotlib.pyplot as plt

# 사용자 입력
a = float(input("a 값을 입력하세요: "))
b = float(input("b 값을 입력하세요: "))
c = float(input("c 값을 입력하세요: "))

# 함수 정의: f(x) = a^x + c
def exponential_function(x):
    return a**(b * x) + c

# x 값 범위 설정
x = np.linspace(-10, 10, 400)
y = exponential_function(x)

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.plot(x, y, label=f'f(x) = {a}^({b}x) + {c}', color='blue')
plt.title('지수 함수 그래프')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axhline(0, color='gray', linestyle='--')  # x축
plt.axvline(0, color='gray', linestyle='--')  # y축
plt.legend()
plt.grid(True)
plt.show()
