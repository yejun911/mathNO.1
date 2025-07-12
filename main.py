import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="Modified Exponential Function Plotter")

st.title("수정된 지수 함수 그래프")
st.write("`f(x) = a^b + c` 형태의 함수 그래프를 그려봅니다. (x 값은 결과에 영향을 미치지 않습니다.)")

# --- 사용자 입력 ---
st.sidebar.header("함수 파라미터 설정")
a = st.sidebar.number_input("a 값 입력:", value=2.0, help="a 값입니다.")
b = st.sidebar.number_input("b 값 입력:", value=3.0, help="b 값 (a의 지수)입니다.")
c = st.sidebar.number_input("c 값 입력:", value=0.0, help="수직 이동을 결정하는 상수입니다.")

# --- 함수 정의 ---
# f(x) = a^b + c 로 변경
def constant_function(x, a, b, c):
    # x의 모든 요소에 대해 동일한 상수 값을 반환하도록 수정
    return np.full_like(x, a**b + c) # x와 동일한 shape로 채워진 배열을 반환

# --- x 값 범위 설정 (수정된 부분) ---
# subheader를 sidebar에 표시하려면 이렇게 작성해야 합니다.
st.sidebar.subheader("x축 범위 설정")
x_min = st.sidebar.slider("x 최소값:", -10.0, 0.0, -5.0)
x_max = st.sidebar.slider("x 최대값:", 0.0, 10.0, 5.0)

if x_min >= x_max:
    st.sidebar.error("오류: x 최소값은 x 최대값보다 작아야 합니다.")
else:
    x = np.linspace(x_min, x_max, 400)
    y = constant_function(x, a, b, c)

    # --- 그래프 그리기 ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label=f'f(x) = {a}^{b} + {c} = {a**b + c:.2f}', color='red')
    ax.set_title('상수 함수 그래프')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(a**b + c, color='blue', linestyle='--', linewidth=0.8, label=f'y = {a**b + c:.2f}')
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)
    ax.legend()
    ax.grid(True)

    # Streamlit에 그래프 표시
    st.pyplot(fig)

    # --- 추가 정보 ---
    st.subheader("함수 정보")
    st.markdown(f"**함수식:** $f(x) = {a}^{b} + {c}$")
    st.write(f"- 이 함수는 **x 값에 관계없이** 항상 **{a}^{b} + {c} = {a**b + c:.2f}** 값을 가집니다.")
    st.write(f"- 그래프는 수평선으로 나타납니다.")

st.markdown("---")
st.info("좌측 사이드바에서 'a', 'b', 'c' 값을 조절하여 그래프 변화를 확인해보세요.")
