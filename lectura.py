import csv
import pandas as pd
from tabulate import tabulate
from prettytable import PrettyTable


to_do=pd.read_csv("todo.csv" )

print(tabulate(to_do, headers='keys', tablefmt='psql'))
#print(to_do.to_markdown())
