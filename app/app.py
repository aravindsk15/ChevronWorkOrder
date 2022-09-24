from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def run():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)