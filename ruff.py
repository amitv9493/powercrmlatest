def func(num1, num2, *args, **kwargs):
    print(args)
    print(kwargs)


func(1, 2, 3, 4, 5, Name="Amit")


from dotenv import load_dotenv

load_dotenv()
from sp_api.base import Marketplaces

from sp_api.api import Orders

from sp_api.api import Orders
from sp_api.api import Reports
from sp_api.api import Feeds
from sp_api.base import SellingApiException
from sp_api.base.reportTypes import ReportType
from datetime import datetime, timedelta

try:
    res = Orders().get_orders(
        CreatedAfter=(datetime.utcnow() - timedelta(days=7)).isoformat()
    )
    print(res.payload)  # json data
except SellingApiException as ex:
    print(ex)
