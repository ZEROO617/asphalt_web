import os
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_failure_load(temp_celsius, thickness_m, void_radius_m):
    E_20 = 5_000 * 1e6
    k_shape = 1.33
    k_temp = 0.05
    correction_factor = 0.3

    E_temp = E_20 * (10 ** (-k_temp * (temp_celsius - 20)))
    P_newton = (k_shape * E_temp * (thickness_m ** 3)) / (void_radius_m ** 2) * correction_factor
    P_kgf = round(P_newton / 9.81)

    return P_kgf

def home():
    return "Hello, Render!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    try:
        temp = float(request.form['temp'])
        thickness = float(request.form['thickness'])
        radius = float(request.form['radius'])
        load = calculate_failure_load(temp, thickness, radius)
        return render_template('result.html', load=load)
    except:
        return "<h3>입력을 다시 확인해주세요! 숫자만 입력 가능합니다.</h3>"

if __name__ == "__main__":
    # Render에서 자동으로 설정한 포트를 사용하도록 수정
    port = int(os.environ.get("PORT", 5000))  # PORT 환경 변수를 사용하고, 없으면 기본 5000 사용
    app.run(host="0.0.0.0", port=port, debug=True)
