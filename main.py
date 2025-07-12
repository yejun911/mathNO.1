import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="centered", page_title="기본 지수 함수 그래프")

st.title("기본 지수 함수 그래프")
st.write("`y = a^x + c` 형태의 지수 함수 그래프를 그려보세요.")

# --- 사용자 입력 ---
st.sidebar.header("함수 파라미터 설정")
a = st.sidebar.number_input("a 값 입력 (밑):", value=2.0, help="지수 함수의 밑입니다. (a > 0)")
c = st.sidebar.number_input("c 값 입력 (상수):", value=0.0, help="수직 이동을 결정하는 상수입니다. 수평 점근선 y=c를 결정합니다.")

# 입력 값 유효성 검사
if a <= 0:
    st.sidebar.warning("경고: 'a' 값 (밑)은 0보다 커야 합니다. 그래프가 올바르게 표시되지 않을 수 있습니다.")

# --- 함수 정의: y = a^x + c ---
def basic_exponential_function(x, a, c):
    # a가 음수이거나 0일 때 복소수가 되는 것을 방지 (실수 범위만 고려)
    if a <= 0:
        # a가 유효하지 않으면 NaN 값으로 채워 그래프를 그리지 않음
        return np.full_like(x, np.nan)
    return a**x + c

# --- x 값 범위 설정 ---
st.sidebar.subheader("x축 범위 설정")
x_min = st.sidebar.slider("x 최소값:", -5.0, 0.0, -2.0)
x_max = st.sidebar.slider("x 최대값:", 0.0, 5.0, 2.0)

if x_min >= x_max:
    st.sidebar.error("오류: x 최소값은 x 최대값보다 작아야 합니다.")
else:
    x = np.linspace(x_min, x_max, 400)
    y = basic_exponential_function(x, a, c)

    # --- 그래프 그리기 ---
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label=f'y = {a}^x + {c}', color='purple') # 라벨 업데이트 및 색상 변경
    ax.set_title('지수 함수 그래프: y = a^x + c')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8)  # x축
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)  # y축
    # 수평 점근선 표시 (y=c)
    ax.axhline(c, color='red', linestyle=':', linewidth=0.8, label=f'수평 점근선: y = {c}')
    ax.legend()
    ax.grid(True)

    # y축 범위 자동 조절 (NaN 값 고려)
    valid_y = y[~np.isnan(y)] # NaN이 아닌 유효한 y 값만 선택
    if valid_y.size > 0:
        y_min_plot = min(valid_y.min(), c) - abs(valid_y.min() - c) * 0.1 - 1
        y_max_plot = max(valid_y.max(), c) + abs(valid_y.max() - c) * 0.1 + 1
        ax.set_ylim(y_min_plot, y_max_plot)


    # Streamlit에 그래프 표시
    st.pyplot(fig)

    # --- 추가 정보 ---
    st.subheader("함수 정보")
    st.markdown(f"**함수식:** $y = {a}^x + {c}$")
    st.write(f"- **a (밑):** 그래프의 증가/감소 속도를 결정합니다. `a > 1`이면 증가, `0 < a < 1`이면 감소합니다.")
    st.write(f"- **c (상수):** 그래프의 수직 이동을 나타내며, 이는 수평 점근선 $y = {c}$를 의미합니다.")

st.markdown("---")
st.info("좌측 사이드바에서 'a', 'c' 값과 'x'축 범위를 조절하여 그래프 변화를 확인해보세요.")
