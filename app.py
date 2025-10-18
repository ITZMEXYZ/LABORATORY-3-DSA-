from flask import Flask, render_template, request
import math, os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/profile')
def profile():
    profile_data = {
        "name": "Zy E. Banez",
        "course": "Bachelor of Science in Computer Engineering (BSCPE)",
        "year": "BSCPE 2-3",
        "description": (
            "Hi my name is Zy E. Banez, a second-year student from Polytechnic University of the Philippines "
            "majoring in Computer Engineering wanting to specialize in Full Stack Development. "
            'The saying that I believe is that "If you don\'t know the path you want to take, '
            'then make one that you wouldn\'t regret".'
        ),
        "image": "static/images/zy.jpg.jpg"
    }
    # Pass the profile_data dictionary to the template
    return render_template('profile.html', profile=profile_data, active_page='profile')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html',  active_page='works')

@app.route('/contact')
def contact():
    contact_info = {
        "name": "Zy E. Banez",
        "phone": "+63 997 957 4218",
        "email": "zyescotebanes@gmail.com",
        "facebook": "Zy Escote Banez",
        "github": "ITZMEXYZ",
        "image": "static/images/zy.jpg.jpg"
    }
    return render_template('contact.html', contact=contact_info, active_page='contact')


@app.route('/touppercase', methods=['GET', 'POST'])
def uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)


@app.route('/areaofcircle', methods=['GET', 'POST'])
def area_of_circle():
    area = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        area = 3.14 * (radius ** 2)
    return render_template('areaofcircle.html', area=area)


@app.route('/areaoftriangle', methods=['GET', 'POST'])
def area_of_triangle():
    area = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area = 0.5 * base * height
    return render_template('areaoftriangle.html', area=area)


#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 5000))
#    app.run(host="0.0.0.0", port=port, debug=True)










