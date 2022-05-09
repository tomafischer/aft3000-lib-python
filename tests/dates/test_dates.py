import pytest 
from datetime import datetime, timedelta
from aft3000_lib.dates.dates import date_monday_of_week

@pytest.mark.parametrize('midweek',[[datetime(2021,10,4),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,4),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,5),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,6),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,7),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,8),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,9),datetime(2021,10,4,0,0,0)],
  [datetime(2021,10,10),datetime(2021,10,4,0,0,0)]
  ])
@pytest.mark.dates
def test_date_monday_of_week(midweek):
    monday = date_monday_of_week(midweek[0])
    #print(f"{monday} - {midweek[1]}")
    assert monday == midweek[1]


