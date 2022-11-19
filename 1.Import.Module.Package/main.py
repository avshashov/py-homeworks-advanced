from datetime import datetime
import pandas as pd
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.today())
    calculate_salary()
    get_employees()
    salary = pd.read_csv('application/Employee_Salaries_-_2020.csv', encoding='utf-8')
    print(salary['Base Salary'].head())