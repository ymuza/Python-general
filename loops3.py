from datetime import datetime

date = "13/03/1987"

# date_formated = datetime.date(date)


date_formated2 = datetime.strptime(date, '%d/%m/%Y').date()

# date_formated3 = datetime.date(date_formated2)


print(date_formated2)

print("\n")

# print(date_formated3)
