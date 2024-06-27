#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return '''
    <h1>Enter Your Details</h1>
    <form action="/echo_user_input" method="POST">
        <label for="input1">Input 1:</label>
        <input type="text" name="user_input1" id="input1"><br>
        <label for="input2">Input 2:</label>
        <input type="text" name="user_input2" id="input2"><br>
        <label for="input3">Input 3:</label>
        <input type="text" name="user_input3" id="input3"><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text1 = request.form.get("user_input1", "")
    input_text2 = request.form.get("user_input2", "")
    input_text3 = request.form.get("user_input3", "")
    return f'''
    <h1>You Entered:</h1>
    <p>Input 1: {input_text1}</p>
    <p>Input 2: {input_text2}</p>
    <p>Input 3: {input_text3}</p>
    <a href="/">Go back</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)
