import csv
from datetime import datetime
FILENAME="studentopinion.csv"

def file_init():
     try:
         with open(projrcd,"x",newline="",encoding="utf-8") as f:
             writer=csv.writer(f)
             writer.writerow(["date","meal","rating","comment"])
     except FileExistsError:
          pass

def give_opinion():
    pass
def view_average_rating():
    pass
def view_complanints():
    pass
def main_menu():
    pass


if __name__ =="main_menu":
    file_init()
    main_menu()