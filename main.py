from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def wel():
    return render_template('login.html')

name1 = ''
password1 = ''

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        try:           
            name = str(request.form['name'])
            password = str(request.form['password'])
           
            if name1 == name and password1 == password :
                return render_template('vehical_details.html')
            else:
                return '<h1>name or password in correct......</h1>'
        except Exception as e:
            return f"An error occurred: {e}"

@app.route('/vehical_details')
def vehical_details():
    return render_template('vehical_details.html')

@app.route('/insurence')
def insurence():
    return render_template('insurence.html')


@app.route('/revenue')
def revenue():
    return render_template('revenue.html')

@app.route('/emssion')
def emssion():
    return render_template('emssion.html')

@app.route('/permit')
def permit():
    return render_template('permit.html')

@app.route('/driverdetails')
def driverdetails():
    return render_template('driverdetails.html')

@app.route('/conductordetails')
def conductordetails():
    return render_template('conductordetails.html')

@app.route('/daily_input')
def daily_input():
    return render_template('input.html')

@app.route('/expenses')
def expenses():
    return render_template('expenses.html')

@app.route('/oil')
def oil():
    return render_template('oil.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/left_front_tyer')
def left_front_tyer():
    return render_template('left_front_tyer.html')

@app.route('/rigth_front_tyer')
def rigth_front_tyer():
    return render_template('rigth_front_tyer.html')

@app.route('/left_back_inside_tyer')
def left_back_inside_tyer():
    return render_template('left_back_inside_tyer.html')

@app.route('/left_back_outside_tyer')
def left_back_outside_tyer():
    return render_template('left_back_outside_tyer.html')

@app.route('/right_back_inside_tyer')
def right_back_inside_tyer():
    return render_template('right_back_inside_tyer.html')

@app.route('/rigth_back_outside_tyer')
def rigth_back_outside_tyer():
    return render_template('rigth_back_outside_tyer.html')

@app.route('/issues')
def issues():
    return render_template('issues.html')



if __name__ == '__main__':
    app.run(debug=True,port=5000)
