import os
from setuptools import setup

# just in case setup.py is launched from elsewhere that the containing directory
original_dir = os.getcwd()
working_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(working_directory)

try:
    setup(
        name="Calculator",
        version='1.0.0',

        author="Nick Groß",
        description="Calculator with Gui and Wui",

        url="https://platform.sw-machines.io",
        py_modules=['Calculator.service.CalculatorService'],

        tests_require=['pytest', 'pytest-runner', 'pytest-cov', 'pytest-mock', 'mock'],
        setup_requires=['pytest-runner'],
        install_requires=['click==7.0', 'flask==1.1.1']
    )

finally:
    os.chdir(original_dir)
