import os

import flask


def hello_world(request):

    return "Hello World!"


def calculate_fibonacci(n):
    return 99
    # complete this function

def return_fibonacci(request):
    request_args = request.args

    if request_args and "n" in request_args:
        n = int(request_args["n"])
    else:
        n = 1
    return f"{calculate_fibonacci(n)}"
