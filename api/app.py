from flask import Flask, render_template, request
import math, os

app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    index_data = {
        "welcome": "Welcome to my Website",
        "name": "HI I'M ZY",
        "speech": "As an aspiring software engineer I want to make applications and websites that's more interactive and easy to use and learn more things that will help me grow my career.",
        "image": "static/images/zy.jpg.jpg"
    }
    return render_template('index.html', index=index_data, active_page='index')


@app.route('/profile')
def profile():
    profile_data = {
        "name": "Zy E. Bañez",
        "course": "Bachelor of Science in Computer Engineering (BSCPE)",
        "year": "BSCPE 2-3",
        "description": (
            "Hi my name is Zy E. Bañez, a second-year student from Polytechnic University of the Philippines "
            "majoring in Computer Engineering wanting to specialize in Full Stack Development. "
            'The saying that I believe is that "If you don\'t know the path you want to take, '
            'then make one that you wouldn\'t regret".'
        ),
        "image": "static/images/zy.jpg.jpg"
    }
    return render_template('profile.html', profile=profile_data, active_page='profile')


@app.route('/contact')
def contact():
    contact_info = {
        "name": "Zy E. Bañez",
        "phone": "+63 997 957 4218",
        "email": "zyescotebanes@gmail.com",
        "facebook": "Zy Escote Bañez",
        "github": "ITZMEXYZ",
        "image": "static/images/zy.jpg.jpg"
    }
    return render_template('contact.html', contact=contact_info, active_page='contact')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html',  active_page='works')


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


@app.route('/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    global linked_list
    if 'linked_list' not in globals():
        linked_list = []

    if request.method == 'POST':
        data = request.form.get('data', '')

        if 'add_begin' in request.form and data:
            linked_list.insert(0, data)

        elif 'add_last' in request.form and data:
            linked_list.append(data)

        elif 'remove_begin' in request.form and linked_list:
            linked_list.pop(0)

        elif 'remove_last' in request.form and linked_list:
            linked_list.pop()

        elif 'clear_list' in request.form:
            linked_list.clear()

    return render_template('linkedlist.html', items=linked_list)

@app.route('/infixtopostfix', methods=['GET', 'POST'])
def infixtopostfix():
    result = None

    def infix_to_postfix(expr):
        stack, output = [], ""
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

        for c in expr:
            if c.isalnum():
                output += c
            elif c == '(':
                stack.append(c)
            elif c == ')':
                while stack and stack[-1] != '(':
                    output += stack.pop()
                stack.pop()
            else:
                while stack and prec.get(stack[-1], 0) >= prec.get(c, 0):
                    output += stack.pop()
                stack.append(c)

        while stack:
            output += stack.pop()
        return output

    if request.method == 'POST':
        expr = request.form.get('expression', '')
        result = infix_to_postfix(expr)

    return render_template('infixtopostfix.html', result=result)
