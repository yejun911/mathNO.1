# ... (previous code) ...

# --- 함수 정의 (수정됨) ---
# f(x) = a^b + c 로 변경
def constant_function(x, a, b, c):
    # 여기서 핵심: x의 모든 요소에 대해 동일한 상수 값을 반환하도록 수정
    # NumPy의 fill 함수를 사용하거나, 단순히 x의 shape에 맞춰 상수를 반환
    return np.full_like(x, a**b + c) # x와 동일한 shape로 채워진 배열을 반환

# --- x 값 범위 설정 ---
st.sidebar.subheader("x축 범위 설정")
x_min = st.sidebar.slider("x 최소값:", -10.0, 0.0, -5.0)
x_max = st.sidebar.slider("x 최대값:", 0.0, 10.0, 5.0)

if x_min >= x_max:
    st.sidebar.error("오류: x 최소값은 x 최대값보다 작아야 합니다.")
else:
    x = np.linspace(x_min, x_max, 400)
    # 수정된 함수 호출
    y = constant_function(x, a, b, c) # 이제 y는 x와 같은 (400,) shape의 배열이 됩니다.

    # --- 그래프 그리기 ---
    fig, ax = plt.subplots(figsize=(10, 6))
    # 그래프 라벨도 변경
    ax.plot(x, y, label=f'f(x) = {a}^{b} + {c} = {a**b + c:.2f}', color='red')
    ax.set_title('상수 함수 그래프')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(a**b + c, color='blue', linestyle='--', linewidth=0.8, label=f'y = {a**b + c:.2f}')  # y = 결과값 선 추가
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8)  # y축
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
