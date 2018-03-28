import time
import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/<ts>')
def timestamp_flask(ts):
	#ts = time.time()
	#st = datetime.datetime.fromtimestamp(ts).strftime('%B %d,%Y')
	#return 'unix : {}, natural : {}'.format(ts,st)
	if(ts.isdigit()):
		st = datetime.datetime.fromtimestamp(float(ts)).strftime('%B %d, %Y')
		#print "unix:",ts,", natural:",st
	else:
		st = time.mktime(datetime.datetime.strptime(ts, "%B %d, %Y").timetuple())
		try:
			datetime.datetime.strptime(ts, '%B %d, %Y')
			#print "unix:",float(st),", natural:",ts
		except ValueError:
			raise ValueError("Incorrect data format, should be unix or Month dd, yyyy")
	return 'unix : {}, natural : {}'.format(st,ts)	

if __name__ == '__main__':
   app.run('0.0.0.0')
	