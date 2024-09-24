from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Store messages in memory (not persistent)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form.get('username')
    message = request.form.get('message')
    
    if username and message:
        messages.append({'username': username, 'message': message})
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

