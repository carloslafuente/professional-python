from datetime import datetime, date

my_date = datetime.now()
print(my_date)


today_date = date.today()
print(today_date)


formated_date = datetime.now().strftime('%d-%m-%Y')
print(formated_date)


formated_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
print(formated_date)
