import pytz
import datetime
from dateutil import parser


class DateHandler:

    @staticmethod
    def get_datetime_now():

        # Strip seconds from datetime
#        now_time = datetime.datetime.utcnow() -  datetime.timedelta(days=20)
        now_time = datetime.datetime.utcnow()
        datestring = str(now_time.strftime("%Y-%m-%d %H:%M:%S"))
        naive_date = now_time.strptime(datestring, "%Y-%m-%d %H:%M:%S")

        # Make datetime aware of timezone
        aware_date = pytz.utc.localize(naive_date)
        result = aware_date.astimezone(pytz.timezone("Europe/Berlin"))
        return result

    @staticmethod
    def parse_datetime(datetime):
        result = parser.parse(datetime)

        if result.tzinfo is None:
            aware_date = pytz.utc.localize(result)
            result = aware_date.astimezone(pytz.timezone("Europe/Berlin"))

        return result
