from flask import Blueprint, render_template, redirect, url_for

views = Blueprint('views', __name__)
variables = {'cur': None, 'first': False}


@views.route('/', methods=['GET', 'POST'])
def home():
    if variables["first"] and variables["cur"] is None:
        return redirect(url_for('views.wait'))
    elif variables["cur"] is not None:
        variables["first"] = False
        return redirect(url_for(variables["cur"]))
    else:
        variables["first"] = True
        print("first connection is here, you must be the teacher")
        return render_template("home.html")


@views.route('/hello', methods=['GET', 'POST'])
def hello():

    variables["cur"] = 'views.hello'
    return render_template("hello.html", is_read_only=variables["first"])


@views.route('/counter', methods=['GET', 'POST'])
def counter():
    variables["cur"] = 'views.counter'

    return render_template("counter.html", is_read_only=variables["first"])


@views.route('/counter2', methods=['GET', 'POST'])
def counter2():
    variables["cur"] = 'views.counter2'

    return render_template("counter2.html", is_read_only=variables["first"])


@views.route('/filter', methods=['GET', 'POST'])
def filter():
    variables["cur"] = 'views.filter'
    return render_template("filter.html", is_read_only=variables["first"])


@views.route('/wait', methods=['GET', 'POST'])
def wait():
    if variables["cur"] is None:
        return render_template("wait.html")
    variables["first"] = False
    return redirect(url_for(variables["cur"]))

