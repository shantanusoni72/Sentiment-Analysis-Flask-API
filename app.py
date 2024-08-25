from flask import Flask, request
from src.features.sentiment_analysis.main import sentiment as Sentiments
from settings import host_ip, port

app = Flask(__name__)

@app.route('/sentiments/', methods=['GET', 'POST'])
def sentiment():
    if request.method == 'POST':
        text = request.form['text']
        if text != '':
            s1 = Sentiments()
            return s1.main(text)
        else:
            return { 'Error': 'Please insert any value.' }
    else:
        return { 'Error': 'Please use the POST method.' }

if __name__ == '__main__':
    app.run(host=host_ip, port=port, debug=False)