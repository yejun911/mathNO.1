import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("지수 함수 시각화")
st.write("형태: f(x) = a^(b*x) + c")

a = st.number_input("a 값 입력", value=2.0)
b = st.number_input("b 값 입력", value=1.0)
c = st.number_input("c 값 입력", value=0.0)

x = np.linspace(-10, 10, 400)
y = a ** (b * x) + c

fig, ax = plt.subplots()
ax.plot(x, y, label=f'f(x) = {a}^({b}x) + {c}', color='blue')
ax.axhline(0, color='gray', linestyle='--')
ax.axvline(0, color='gray', linestyle='--')
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.grid(True)
st.pyplot(fig)
