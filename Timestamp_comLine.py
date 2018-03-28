import time
import datetime
import sys

ts = str(sys.argv[1])

if(ts.isdigit()):
	st = datetime.datetime.fromtimestamp(float(ts)).strftime('%B %d, %Y')
	print "unix:",ts,", natural:",st
else:
	st = time.mktime(datetime.datetime.strptime(ts, "%B %d, %Y").timetuple())
	try:
		datetime.datetime.strptime(ts, '%B %d, %Y')
		print "unix:",float(st),", natural:",ts
	except ValueError:
		raise ValueError("Incorrect data format, should be unix or Month dd, yyyy")