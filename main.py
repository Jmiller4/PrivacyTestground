from consumer import *
from vendor import *
from federation import *

con = consumer()
con.generateData()
print(con.toString())