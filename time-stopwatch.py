# printout current time with time zone
from datetime import datetime

start = datetime.now()

input("Press Enter to continue...")

end = datetime.now()

print("Time spent: \n", end - start)