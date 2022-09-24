hour = 9
minutes30 = False
while hour <= 17:
    if minutes30:
        time = str(hour) + ":" + "30"
        minutes30 = False
        hour += 1
    else:
        time = str(hour) + ":" + "00"
        minutes30 = True
    print("str_html += \"<option value=\"time1\">" + time + "</option>\"")