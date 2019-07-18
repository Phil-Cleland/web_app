
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Hello Philemon'

@app.route('/whereami')
def whereami():
	return "I'm in Ghana, hahahaa" 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

