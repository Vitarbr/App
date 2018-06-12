from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#   Starting page is /send, make sure to change in future
#   In other words, go to ...5000/send/ locally to access

@app.route('/send', methods=['GET', 'POST'])

def send():
    if request.method == 'POST':

        risk_level = 0

#   First Question- How are you feeling?

        P1 = request.form['how_feeling']

        if P1 in ['0','1','2','3']:
            risk_level = risk_level + 20
        elif P1 in ['4','5','6']:
            risk_level = risk_level + 10
        elif P1 in ['7','8','9','10']:
            risk_level = risk_level + 0

        if risk_level == 0:
            return render_template('Q1a.html', risk_level=risk_level)
        if risk_level == 10:
            return render_template('Q1b.html', risk_level=risk_level)
        if risk_level == 20:
            return render_template('Q2.html', risk_level=risk_level)

    return render_template('index.html')

@app.route('/suicide_resources')

def suicide_resources():
    return render_template('suicide_resources.html')

#   Since we need to re-route for each new input,
#   this is rerouting to the follow up for
#   risk level 10.

@app.route('/send2', methods=['GET', 'POST'])

def send2():
    if request.method == 'POST':
        risk_level = 10
        P2 = request.form['today']
        if P2 == 'N':
            return render_template('Q1ba.html', risk_level=risk_level)
        elif P2 == 'Y':
            risk_level = risk_level + 10
            return render_template('Q2.html', risk_level=risk_level)

@app.route('/send3', methods=['GET', 'POST'])

def send3():
    if request.method == 'POST':

        risk_level = 10
        P3 = request.form['help_or_wait']

        if P3 == 'Wait':
            return render_template('Q1a.html', risk_level=risk_level)
        if P3 == 'Help':
            #PENDING#
            return 'list of resources pending. sorry!'

@app.route('/send4', methods=['POST', 'GET'])

def send4():
    if request.method == 'POST':

        risk_level = 20
        P4 = request.form['self_harm']

        if P4 == 'C':
            risk_level = risk_level + 0
        elif P4 == 'A':
            risk_level = risk_level + 10
        elif P4 == 'B':
            risk_level = risk_level + 20

        send4.risk_level = str(risk_level)

        return render_template('Q3.html', risk_level=risk_level)

@app.route('/send5', methods=['GET','POST'])

def send5():
    if request.method == 'POST':
        risk_level = int(send4.risk_level)
        P5 = request.form['traumatic_event']
        if P5 == 'Y':
            risk_level = risk_level + 10
        elif P5 == 'N':
            risk_level = risk_level + 0

        send5.risk_level = str(risk_level)

        return render_template('Q4.html', risk_level=risk_level)

@app.route('/send6', methods=['GET','POST'])

def send6():
    if request.method == 'POST':
        risk_level = int(send5.risk_level)
        P6 = request.form['considered_suicide']
        if P6 == 'Y':
            risk_level = risk_level + 20
        elif P6 == 'N':
            risk_level = risk_level + 0

        send6.risk_level = str(risk_level)

        return render_template('Q5.html', risk_level=risk_level)

@app.route('/send7', methods=['GET','POST'])

def send7():
    if request.method == 'POST':
        risk_level = int(send6.risk_level)
        P7 = request.form['how_long_sad']
        if P7== 'A':
            risk_level = risk_level + 10
        elif P7 == 'B':
            risk_level = risk_level + 0
        elif P7 == 'C':
            risk_level = risk_level + 20

        send7.risk_level = str(risk_level)

        return render_template('Q_physical.html', risk_level=risk_level)

@app.route('/send_physical', methods=['GET', 'POST'])

def send_physical():
    if request.method == 'POST':
        risk_level = int(send7.risk_level)
        P7a = request.form['physical_health']
        if P7a== 'Y':
            risk_level = risk_level + 0
        elif P7a == 'N':
            risk_level = risk_level + 10

        send_physical.risk_level = str(risk_level)

        return render_template('Q_stress.html', risk_level=risk_level)

@app.route('/send_stress', methods=['GET', 'POST'])

def send_stress():
    if request.method == 'POST':
        risk_level = int(send_physical.risk_level)
        P7a = request.form['stress']
        if P7a== 'Y':
            risk_level = risk_level + 10
        elif P7a == 'N':
            risk_level = risk_level + 0

        send_stress.risk_level = str(risk_level)

        return render_template('Q_mood_affect.html', risk_level=risk_level)

@app.route('/send_mood_affect', methods=['GET', 'POST'])

def send_mood_affect():
    if request.method == 'POST':
        risk_level = int(send_stress.risk_level)
        P7a = request.form['mood_affect']
        if P7a== 'Y':
            risk_level = risk_level + 10
        elif P7a == 'N':
            risk_level = risk_level + 0

        send_mood_affect.risk_level = str(risk_level)

        return render_template('Q_focus.html', risk_level=risk_level)

@app.route('/send_focus', methods=['GET', 'POST'])

def send_focus():
    if request.method == 'POST':
        risk_level = int(send_mood_affect.risk_level)
        P7a = request.form['focus']
        if P7a== 'Y':
            risk_level = risk_level + 10
        elif P7a == 'N':
            risk_level = risk_level + 0

        send_focus.risk_level = str(risk_level)

        return render_template('Q_sleep.html', risk_level=risk_level)

@app.route('/send_sleep', methods=['GET', 'POST'])

def send_sleep():
    if request.method == 'POST':
        risk_level = int(send_focus.risk_level)
        P7a = request.form['sleep']
        if P7a== 'Y':
            risk_level = risk_level + 10
        elif P7a == 'N':
            risk_level = risk_level + 0

        send_sleep.risk_level = str(risk_level)

        return render_template('Q6.html', risk_level=risk_level)

@app.route('/send8', methods=['GET','POST'])

def send8():
    if request.method == 'POST':
        risk_level = int(send_sleep.risk_level)
        P8 = request.form['can_parents_know']
        if P8 == 'Y':
            send8.can_parents_know = 'Y'
        elif P8 == 'N':
            send8.can_parents_know = 'N'

        return render_template('Q7.html', risk_level=risk_level)

@app.route('/send9', methods=['GET','POST'])

def send9():
    if request.method == 'POST':
        risk_level = int(send7.risk_level)
        P9 = request.form['meet_therapist']
        if P9 == 'Y' and send8.can_parents_know == 'N':
            return 'list of online therapists pending'
        elif P9 == 'Y':
            send9.meet_therapist = 'Y'
        elif P9 == 'N':
            return 'list of online resources pending'

        return render_template('Q8.html', risk_level=risk_level)

@app.route('/send10', methods=['GET','POST'])

def send10():
    if request.method == 'POST':
        risk_level = int(send7.risk_level)
        P10 = request.form['online_therapist']
        if P10 == 'Y':
            return redirect(url_for('send_online_therapists'))
        elif P10 == 'N':
            return 'list of in-person therapists pending'

@app.route('/send_online_therapists', methods=['GET','POST'])

def send_online_therapists():
    return render_template('online_therapists.html')

if __name__ == "__main__":
    app.run()
