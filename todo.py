import csv
from prettytable import PrettyTable
from datetime import date

with open('todo.csv', 'a') as f:
    w = csv.writer(f, quoting=csv.QUOTE_ALL)

    Fecha =  date.today()
    t_d_1 = (input(" 1 "))
    t_d_2 = (input(" 2 "))
    t_d_3 = (input(" 3 "))
    t_d_4 = (input(" 4 "))
    t_d_5 = (input(" 5 "))
    t_d_6 = (input(" 6 "))
    t_d_7 = (input(" 7 "))
    t_d_8 = (input(" 8 "))

    w.writerow(['Fecha','1', '2', '3', '4','5', '6','7', '8'])
    w.writerow([Fecha,t_d_1,t_d_2,t_d_3,t_d_4,t_d_5,t_d_6,t_d_7,t_d_8])



table = PrettyTable()

table.field_names = ['Fecha','1', '2', '3', '4','5', '6','7', '8']
table.add_row([Fecha,t_d_1,t_d_2,t_d_3,t_d_4,t_d_5,t_d_6,t_d_7,t_d_8])

print(table)
