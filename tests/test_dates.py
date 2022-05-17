import pytest 
from datetime import datetime, timedelta
from aft3000_lib.dates_lib import date_monday_of_week, format_iso_no_tz, dt_fromisoformat

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

@pytest.mark.dates
def test_format_iso_no_tz():
  # arrange
  dt = datetime(2020,5,4,1,2,1,123456)

  # act , assert
  assert format_iso_no_tz(dt, microseconds=True) == '2020-05-04 01:02:01.123456'
  assert format_iso_no_tz(dt, ) == '2020-05-04 01:02:01'

@pytest.mark.dates
def test_dt_fromisoformat():
  assert dt_fromisoformat('2020-05-04 01:02:01:123456') == datetime(2020,5,4,1,2,1,123456)
  assert dt_fromisoformat('2020-05-04T01:02:01:123456+04:00', remove_tz=True) == datetime(2020,5,4,1,2,1,123456) , "remove txinfo"



