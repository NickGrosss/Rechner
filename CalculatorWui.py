from flask import Flask, render_template

from build.lib.calculator.service import CalculatorService

app = Flask(__name__)


class CalculatorWui:
    def __init__(self, service: CalculatorService):
        calc_service = service
        app.run()

    @staticmethod
    def abc():
        return render_template("templates.html")
    @staticmethod
    def about():
        return"<h1>About Page</h1>"


@app.route("/")
@app.route("/home")
def home():
    return CalculatorWui.abc()
@app.route("/about")
def aboutpage():
    return CalculatorWui.about()

