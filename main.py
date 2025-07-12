import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="Exponential Function Plotter")

st.title("지수 함수 그래프")
st.write("`f(x) = a^(bx) + c` 형태의 지수 함수 그래프를 그려보세요.")

# --- 사용자 입력 ---
st.sidebar.header("함수 파라미터 설정")
a = st.sidebar.number_input("a 값 입력:", value=2.0, help="지수 함수의 밑입니다. (a > 0)")
b = st.sidebar.number_input("b 값 입력:", value=1.0, help="x의 계수입니다.")
c = st.sidebar.number_input("c 값 입력:", value=0.0, help="수직 이동을 결정하는 상수입니다.")

# 입력 값 유효성 검사
if a <= 0:
    st.sidebar.warning("경고: 'a' 값은 0보다 커야 합니다. 그래프가 올바르게 표시되지 않을 수 있습니다.")

# --- 함수 정의 ---
def exponential_function(x, a, b, c):
    return a**(b * x) + c

# --- x 값 범위 설정 ---
st.sidebar.subheader("x축 범위 설정")
x_min = st.sidebar.slider("x 최소값:", -10.0, 0.0, -5.0)
x_max = st.sidebar.slider("x 최대값:", 0.0, 10.0, 5.0)

if x_min >= x_max:
    st.sidebar.error("오류: x 최소값은 x 최대값보다 작아야 합니다.")
else:
    x = np.linspace(x_min, x_max, 400)
    y = exponential_function(x, a, b, c)

    # --- 그래프 그리기 ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label=f'f(x) = {a}^({b}x) + {c}', color='blue')
    ax.set_title('지수 함수 그래프')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # x축
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)  # y축
    ax.legend()
    ax.grid(True)

    # Streamlit에 그래프 표시
    st.pyplot(fig)

    # --- 추가 정보 ---
    st.subheader("함수 정보")
    st.markdown(f"**함수식:** $f(x) = {a}^{{{b}x}} + {c}$")
    st.write(f"- **a (밑):** 그래프의 증가 또는 감소 속도를 결정합니다.")
    st.write(f"- **b (지수 계수):** 그래프의 수평 확장 또는 축소를 제어합니다.")
    st.write(f"- **c (상수):** 그래프의 수직 이동을 나타냅니다. 이는 수평 점근선 $y = {c}$를 의미합니다.")

st.markdown("---")
st.info("좌측 사이드바에서 'a', 'b', 'c' 값과 'x'축 범위를 조절하여 그래프 변화를 확인해보세요.")
