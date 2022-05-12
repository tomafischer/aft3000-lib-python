from datetime import datetime, timedelta
from pytz import timezone

def date_monday_of_week(day_of_week: datetime = datetime.now()):
    """
    Returns Monday midnight of the week
    """
    # Monday = 1... sunday = 7
    delta = timedelta(days=(day_of_week.isoweekday() -1  ))  
    dt = day_of_week - delta
    monday_morning = datetime(dt.year,dt.month, dt.day, 0, 0, 0)
    return monday_morning

def CST_now() -> datetime: 
  tz = timezone('US/Central')
  ts =datetime.now(tz) #+ timedelta(hours = -1)
  ts = ts.replace(tzinfo=None)
  return ts