from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST', 'GET'])
def calculate_volume():
    if request.method == 'POST':
        shape = request.form.get('shape')
        precision = int(request.form.get('precision'))

        if shape == 'cube':
            side = float(request.form.get('side'))
            volume = round(side ** 3, precision)
        elif shape == 'sphere':
            radius = float(request.form.get('radius'))
            volume = round((4 / 3) * 3.141592653589793 * radius ** 3, precision)
        elif shape == 'cylinder':
            radius = float(request.form.get('radius'))
            height = float(request.form.get('height'))
            volume = round(3.141592653589793 * radius ** 2 * height, precision)
        else:
            volume = "Invalid shape"

        return render_template('index.html', ans=volume)
    return render_template('index.html', ans=None)


if name == '__main__':
    app.run(debug=True)