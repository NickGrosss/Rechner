from tkinter import *
class CalculatorService:

    def __init__(self):
        print('Created service object.')

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b
