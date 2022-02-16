import datetime
from application.db.people import get_employees
from application.salary import calculate_salary


def current_time():
    today = datetime.datetime.now()
    print(today)


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    current_time()
