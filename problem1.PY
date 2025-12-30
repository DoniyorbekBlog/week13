# x1 = {'foo', 'bar', 'baz'}
# x2 = {'baz', 'qux', 'quux'}

# print(x1 | x2) # same as x1.union(x2)
# {'baz', 'quux', 'qux', 'bar', 'foo'}

# print(x1 & x2) # x1.intersection(x2)
# {'baz'}

# print(x1 - x2) # x1.difference(x2)
# {'foo', 'bar'}

# print(x1 ^ x2) # x1.symmetric_difference(x2)
# {'foo', 'qux', 'quux', 'bar'}

import datetime
year = 2024 #int(input("Enter exam year: "))
month = 12 #int(input("Enter exam month: "))
day = 23 #int(input("Enter exam day: "))
exam_date = datetime.date(year, month, day)
today_date = datetime.date.today()
if today_date<exam_date:
    print(f"You have {(exam_date-today_date).days} days left to study!")
elif exam_date<today_date:
    difference = today_date-exam_date
    print(f"The exam was {difference.days} days ago.")
else:
    print("Good luck! The exam is today.")

