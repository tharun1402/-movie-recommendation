from flask import Flask,render_template,request
from mlproject import recomandMovie,similarMovie
app = Flask(__name__)
 
@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        recomandations = recomandMovie(form_data['Name'])
        similar = similarMovie(form_data['Name'])
        return render_template('data.html',recomandations = recomandations,similar=similar)
 
 
# app.run(host='localhost', port=5000)
if __name__ == "__main__":
    app.run(debug=True)