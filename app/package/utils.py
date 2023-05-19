
import logging



# 转换日期
from datetime import datetime,timedelta,timezone
def change_dateime(val):
        try:
            UTC_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
            utc_time1 = datetime.strptime(val, UTC_FORMAT)
            local_date = utc_time1 + timedelta(hours=8)
            return datetime.strftime(local_date ,'%Y-%m-%d %H:%M:%S')
        except Exception as e:
            logging.error(str(e))
            return val




def get_today(hms=False):
    SHA_TZ = timezone(
        timedelta(hours=8),
        name='Asia/Shanghai',
    )

    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    beijing_now = utc_now.astimezone(SHA_TZ)

    _now = beijing_now.strftime("%Y-%m-%d")
    if hms:
        _now = beijing_now.strftime("%Y-%m-%d %H:%M:%S")

    return _now
    
    