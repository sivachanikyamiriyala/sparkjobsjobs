'''import os
login_id=os.getlogin()
print(login_id)'''
from pytz import timezone
timeZ_one=timezone('US/Central')
print(timeZ_one)
from datetime import datetime
run_time=datetime.now(timeZ_one)
print(run_time)
run_time_format=run_time.strftime('%m%d%Y%H%M%S')
print(run_time_format)
