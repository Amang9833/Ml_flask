from flask import Flask , render_template, request
app = Flask(__name__)
import heart

@app.route('/p')
def hello_world():
    return 'Tu Aman hai bhai !!!'


k = [79545.45857431678,5.682861321615587,7.009188142792237,4.09,23086.800502686456]
 
@app.route('/', methods = ['POST', 'GET'])
def aman():
    if request.method == 'POST':
        aIncome = request.form['aIncome']
        hAge = request.form['hAge']
        nRooms = request.form['nRooms']
        nBedrooms = request.form['nBedrooms']
        aPopulation = request.form['aPopulation']
        val = [].append([aIncome, hAge, nRooms, nBedrooms, aPopulation])
        prize = heart.PrizePrediction(k)
        print(prize)
        return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True, port=80)