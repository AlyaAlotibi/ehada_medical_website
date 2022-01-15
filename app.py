from flask import Flask , render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/awareness')
def awareness():
    return render_template('awareness.html')
@app.route('/help_tools')
def help_tools():
    return render_template('help_tools.html')
@app.route('/donation')
def donation():
    return render_template('donation.html')
@app.route('/clinical_trials')
def clinical_trials():
    return render_template('clinical_trials.html')
@app.route('/societies')
def societies():
    return render_template('societies.html')
if __name__=='__main__':
    app.debug = True
    app.run()
