from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

now = datetime.now()
before_one_week = now - relativedelta(weeks=1)

def date_range(start, end):
    start = datetime.strptime(start, "%Y-%m-%d")
    end = datetime.strptime(end, "%Y-%m-%d")
    dates = [(start + timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates


