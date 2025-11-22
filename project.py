import csv
from datetime import datetime
FILENAME="project"


FILENAME="studentopinion.csv"

def file_init():
     try:
         with open(FILENAME,"x",newline="",encoding="utf-8") as f:
             writer=csv.writer(f)
             writer.writerow(["date","meal","rating","comment"])
     except FileExistsError:
          pass

def give_opinion():
    print("\n___Give Feedback__")
    date=input("enter date(YYYY-MM-DD): ")
    print("Meal?")
    print("1.Breakfast")
    print("2.Lunch")
    print("3.snacks")
    print("4.dinner")
    choice=int(input("enter choice"))
    day=input("enter the day of week")
    day=day.lower()
    meal=" "
    if day=="monday":
        if choice==1:
            meal="idli,vada,sambhar,chutney,bread butter/jam and milk/coffee/tea"
        if choice==2:
            meal="khadai veg/besan gatte ki sabji,dal,rice,roti,kheer,salad"
        if choice==3:
            meal="vada pav/bhel puri"
        if choice==4:
            meal="veg kohlapuri/egg curry,rice,roti,soup"
    if day=="tuesday":
        if choice==1:
            meal="poha jalebi,chutney,bread butter"
        if choice==2:
            meal="chole,puri,rice,dal"
        if choice==3:
            meal="variety of samosa"
        if choice==4:
            meal="aloo mutter masala,dal,rice,roti,pineaple halwa"
    if day=="wednesday":
        if choice==1:
            meal="besan chilla,coriander chutney,boiled egg,sprouts"
        if choice==2:
            meal="veg kofta,rice,dal,boondi,salad"
        if choice==3:
            meal="aloo chana chaat"
        
        if choice==4:
            meal="chicken curry,paneer makhani,rice,roti,dal"
        
        
    if day=="thursday":
        if choice==1:
            meal="variety of paratha,aloo curry"
        
        if choice==2:
            meal="mix pulse dal,rice,roti,salad"

        if choice==3:
            meal="aloo vada/fried idli,chutney"
            
        if choice==4:
            meal="egg curry,green peas curry,rice,dal,roti"
            
    if day=="friday":
        if choice==1:
            meal="uttapam,dal chutney,boiled egg,"
            
        if choice==2:
            meal="kadi pakoda,salad,dal,rice,roti"
            
        if choice==3:
             meal="veg chowmin"
            
        if choice==4:
           meal="chicken curry,paneer makhani,rice,dal"            
    if day=="saturday":
        if choice==1:
             meal="chole bhature"
        
        if choice==2:
            meal="aloo jeera masala,rice,roti,salad,dal"

        if choice==3:
             meal="dhokla,green chutney"
        if choice==4:
             meal="gobhi mutter masala,rice,dal,roti"
    
    if day=="sunday":
        if choice==1:
             meal="masala dosa,sambhar,chutney"
        if choice==2:
             meal="chicken biriyani"
        if choice==3:
             meal="white sauce pasta"
        if choice==4:
            meal="rajma,dal,roti,soyabean,rice"
    rating=int(input("enter the rating from 0-10"))
    feedback=input("enter comment and improvement")
    with open(FILENAME,"a",newline="",encoding="utf-8") as f:
             writer=csv.writer(f)
             writer.writerow([date,meal,rating,feedback])
    print("feedback saved")

def view_average_rating():
    t=0
    c=0
    with open(FILENAME,"r")as f:
         reader=csv.reader(f)
         next(reader)
    for row in reader:
        date,meal,rating,comment=row
        rating=int(rating)
        t=t+rating
        c=c+1
    if c==0:
        print("no feedback yet")
        return
    average_rating=t/c
    print(average_rating)

def view_complanints():
    print("\n__Complainants__")
    complaint=False
    with open(FILENAME,"r") as f:
        reader=csv.reader(f)
        next(reader)
        for row in reader:
            date,meal,rating,comment=row
            rating=int(rating)
            if rating<=2:
                complaint=True
                print(comment)
        if complaint==False:
           print("no complaiants")
           print("good work")
           return

def main_menu():
    while True:
        print("====MESS FEEDBACK MENU====")
        print("1.give opinion")
        print("2.view complainants")
        print("3.View average rating")
        print("4.exit")
        choice=int(input("enter your choice"))
        if choice==1:
            give_opinion()
        elif choice==2:
            view_complanints()
        elif choice==3:
            view_average_rating()
        elif choice==4:
            break
        else:
            print("enter valid choice")
        


file_init()
main_menu()