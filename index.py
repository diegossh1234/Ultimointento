from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('sierra.html')

@app.route('/sierra')
def sierra():
    return render_template('sierra.html')

@app.route('/costa')
def costa():
    return render_template('costa.html')

@app.route('/amazonia')
def amazonia():
    return render_template('amazonia.html')


if __name__ =='__main__':
    app.run(debug=True)