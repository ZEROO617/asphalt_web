from flask import Flask, render_template, request, jsonify
from Cal import calculate_failure_load

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            temp = float(request.form['temp'])
            thickness = float(request.form['thickness'])
            radius = float(request.form['radius'])
            
            result = calculate_failure_load(temp, thickness, radius)
            return jsonify({
                'status': 'success',
                'result': f'✅ 아스팔트 파괴하중: {result} kgf'
            })
            
        except ValueError:
            return jsonify({
                'status': 'error',
                'message': '❌ 숫자 형식으로 정확히 입력해주세요!'
            })
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)