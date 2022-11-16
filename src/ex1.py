
import string

def get_day_of_week(week: int) -> string:
    day={
        1:"Monday",
        2:"Thuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",
        7:"Sunday"
    }
    return day.get(week,"ERROR!")


if __name__ == "__main__":
    print("insert number(1-7):")
    week= int(input())
    day=get_day_of_week(week)
    print(day) 
