from flask import Flask, render_template, request
from bmi import calculate_bmi

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height_feet = int(request.form['height_feet'])
        height_inches = int(request.form['height_inches'])
        weight_pounds = float(request.form['weight_pounds'])
        
        bmi, category = calculate_bmi(height_feet, height_inches, weight_pounds)
        
        return render_template('result.html', bmi=bmi, category=category)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
