import sqlite3
import os

DIR = os.path.abspath(os.path.dirname(__file__))


def get_all_customers(limit=0):
    conn = sqlite3.connect(DIR + '/chinook.db')
    print("Opened database successfully")
    cursor = conn.cursor()
    if limit > 0:
        cursor.execute('''SELECT * FROM customers LIMIT {}'''.format(limit))
    else:
        cursor.execute('''SELECT * FROM customers''')

    result = cursor.fetchall()
    conn.close()
    return result


class User:
    def __init__(self, tuple):
        self.customer_id = tuple[0]
        self.first_name = tuple[1]
        self.last_name = tuple[2]
        self.company = tuple[3]
        self.address = tuple[4]
        self.city = tuple[5]
        self.state = tuple[6]
        self.country = tuple[7]
        self.postal_code = tuple[8]
        self.phone = tuple[9]
        self.fax = tuple[10]
        self.email = tuple[11]
        self.support_repld = tuple[12]

    def to_dict(self):
        return dict(self.__dict__)


def filter_by_name(start='', end=''):
    conn = sqlite3.connect(DIR + '/chinook.db')
    print("Opened database successfully")
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM customers 
WHERE FirstName LIKE "{}%" AND FirstName LIKE "%{}"'''.format(start, end))
    result = cursor.fetchall()
    conn.close()
    return result


def filter_company_city_state(city='', company='',  state=''):
    city = city if len(city) > 0 else '%'
    company = company if len(company) > 0 else None
    state = state if len(state) > 0 else None
    conn = sqlite3.connect(DIR + '/chinook.db')
    print("Opened database successfully")
    cursor = conn.cursor()
    if company and state:
        cursor.execute('''SELECT * FROM customers 
        WHERE Company LIKE "{}" AND City LIKE "{}" 
        AND State LIKE "{}"'''.format(company, city, state))
    elif company:
        cursor.execute('''SELECT * FROM customers 
        WHERE Company LIKE "{}" AND City LIKE "{}"'''.format(company, city))
    elif state:
        cursor.execute('''SELECT * FROM customers 
        WHERE City LIKE "{}" 
        AND State LIKE "{}"'''.format(city, state))
    else:
        cursor.execute('''SELECT * FROM customers 
        WHERE City LIKE "{}"'''.format(city))
    result = cursor.fetchall()
    conn.close()
    return result


if __name__ == '__main__':
    customers = get_all_customers()
    user_customers = {i[0]: User(i).to_dict() for i in customers}
    print(user_customers)
    
    customers = filter_company_city_state()
    user_customers = {i[0]: User(i).to_dict() for i in customers}
    print(user_customers)



