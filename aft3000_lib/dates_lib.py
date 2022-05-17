from datetime import datetime, timedelta
from xmlrpc.client import Boolean
from pytz import timezone

format_iso_sec = "%Y-%m-%d %H:%M:%S"
format_iso_ns = "%Y-%m-%d %H:%M:%S.%f"


def date_monday_of_week(day_of_week: datetime = datetime.now()):
    """
    Returns Monday midnight of the week
    """
    # Monday = 1... sunday = 7
    delta = timedelta(days=(day_of_week.isoweekday() -1  ))  
    dt = day_of_week - delta
    monday_morning = datetime(dt.year,dt.month, dt.day, 0, 0, 0)
    return monday_morning

def format_iso_no_tz(dt: datetime, microseconds= False ) -> str:
  """
  Formats the datetime object into iso format
  """
  if microseconds:
    return dt.strftime(format_iso_ns)
  else:
    return dt.strftime(format_iso_sec)

def dt_fromisoformat(dt_str: str, remove_tz: Boolean = False) -> datetime:
    """
    Parse Iso datetime to datetime and remove txinfo if required
    """
    dt=  datetime.fromisoformat(dt_str)
    if remove_tz:
      return dt.replace(tzinfo= None)
    return dt

def CST_now() -> datetime: 
  """
  Returns the curren timestamp for CST
  """
  tz = timezone('US/Central')
  ts =datetime.now(tz) #+ timedelta(hours = -1)
  ts = ts.replace(tzinfo=None)
  return ts