from datetime import datetime
from pytz import timezone
import pytz

data0 = datetime.now(pytz.timezone("Europe/Oslo"))
data1 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data0)
print(data1)
# nao funcionnou o codigo esta quebbrado