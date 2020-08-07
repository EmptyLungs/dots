import argparse
from datetime import datetime, timedelta


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--arr', help='arrival time with format hh:mm')
    args = parser.parse_args()
    arrival = args.arr
    if not arrival:
        print("no arrival date provided")
    
    work_day = timedelta(hours=8, minutes=30)
    arrival_hrs, arrival_mins = map(int, arrival.split(':'))
    now = datetime.now()
    arrival_date = now.replace(hour=arrival_hrs, minute=arrival_mins)
    dippin_time = arrival_date + work_day
    print("Home: {}".format(dippin_time.strftime('%H:%M')))
    worked = now - arrival_date - timedelta(minutes=30)
    worked_hrs = worked.seconds // 3600
    worked_mins = (worked.seconds // 60) % 60
    print("Worked: {}h {}m".format(worked_hrs, worked_mins))

