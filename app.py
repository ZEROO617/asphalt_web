import os
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_failure_load(temp_celsius, thickness_m, void_radius_m):
    # 상수값
    E_20 = 5_000 * 1e6   # 5000 MPa -> Pa
    k_shape = 1.33       # 형상 계수
    k_temp = 0.05        # 온도 민감도
    correction_factor = 0.3  # 보정 계수

    # 온도에 따른 탄성계수 계산
    E_temp = E_20 * (10 ** (-k_temp * (temp_celsius - 20)))

    # 파괴하중 계산 (단위: N)
    P_newton = (k_shape * E_temp * (thickness_m ** 3)) / (void_radius_m ** 2) * correction_factor

    # 단위를 kgf로 변환하고 반올림
    P_kgf = round(P_newton / 9.81)

    return P_kgf

def home():
    return "Hello, Render!"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            # 입력값 받기
            temp_celsius = float(request.form['temp_celsius'])
            thickness_m = float(request.form['thickness_m'])
            void_radius_m = float(request.form['void_radius_m'])

            # 결과 계산
            result = calculate_failure_load(temp_celsius, thickness_m, void_radius_m)
        except ValueError:
            result = "❌ 올바른 값을 입력해주세요!"
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    # Render에서 자동으로 설정한 포트를 사용하도록 수정
    port = int(os.environ.get("PORT", 5000))  # PORT 환경 변수를 사용하고, 없으면 기본 5000 사용
    app.run(host="0.0.0.0", port=port, debug=True)


