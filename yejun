import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 제목
st.title("지수 함수 시각화")
st.write("형태: $f(x) = a^{(b \\cdot x)} + c$")

# 사용자 입력 받기
a = st.number_input("a 값 (밑수)", value=2.0)
b = st.number_input("b 값 (지수 계수)", value=1.0)
c = st.number_input("c 값 (상수항)", value=0.0)

# x 범위 설정
x_min = st.slider("x 최소값", -20, 0, -10)
x_max = st.slider("x 최대값", 0, 20, 10)

x = np.linspace(x_min, x_max, 500)
y = a ** (b * x) + c

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f'$f(x) = {a}^{{({b}x)}} + {c}$', color='blue')
ax.axhline(0, color='gray', linestyle='--')  # x축
ax.axvline(0, color='gray', linestyle='--')  # y축
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title("지수 함수 그래프")
ax.legend()
ax.grid(True)

# 그래프 출력
st.pyplot(fig)
