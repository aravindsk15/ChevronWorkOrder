from flask import Flask, jsonify, render_template, request
import json
from TimeSlot import TimeSlot

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def run():
    if request.method == "POST":
        name = request.form.get("name")
        idw = request.form.get("idw")
        quals = {'Qualification 1': request.form.get("Q1"), 
                 'Qualification 2': request.form.get("Q2"),
                 'Qualification 3': request.form.get("Q3")}
        times = ['0900', '0930', '1000', '1030', '1100', '1130', '1200', '1230', '1300'
                 '1330', '1400', '1430', '1500', '1530', '1600', '1630', '1700']
        time_avail = []
        for time_slot in request.form.getlist('time'):
            curr_start_time = str(time_slot)
            curr_end_time = times[times.index(curr_start_time) + 1]
            time_avail.append(TimeSlot(curr_start_time, curr_end_time))
        return name, idw, quals, str(time_avail)
                
    return render_template('base.html')

if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)