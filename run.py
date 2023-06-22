from flask import Flask, render_template, request,redirect
from main import main
import threading
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    
    youtube_url = request.form['youtube_url']
    threshold = int(request.form['threshold'])
    email=request.form['email_ID']
    def run_main():
        main(youtube_url,threshold,email)
    thread=threading.Thread(target=run_main)
    thread.start()
    return redirect('/thankyou')
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()