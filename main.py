"""
import os

from flask import Flask, render_template, request

# app = Flask(__name__, template_folder='src')

app = Flask(__name__, template_folder='src')


@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f"Thank you for submitting form, {name} yodha we have received your {email}"
   

def main():
    
    port = int(os.environ.get('PORT', 5000)) 

    app.run(port = port,  debug=True )


if __name__ == '__main__':
    main()

"""

import os

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src')

@app.route('/')
def form():
    return  render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    return f" Maharaj {name}, email {email}"


def main():
    
    port = int(os.environ.get('PORT', 5000))
    app.run(port = port, debug=True)

if __name__ == '__main__':

     main()
