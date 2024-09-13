# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Class created called employee with PRIVATE data members.
# Class method will create employee dictionary that can accept employees' details as list arguments

class Employee:
    """Represents an Employee"""

    def __init__(self, name, id_number, salary, email_address):
        """Creates a name, ID number, salary, and email address for Employee """
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        """Gets name of employee"""
        return self._name

    def set_name(self, new_name):
        """Sets the name to a new value"""
        self._name = new_name

    def get_id_number(self):
        """Gets ID number of employee"""
        return self._id_number

    def set_id_number(self, new_id_number):
        """Sets the ID number to a new value"""
        self._id_number = new_id_number

    def get_salary(self):
        """Gets the salary of Employee"""
        return self._salary

    def set_salary(self, new_salary):
        """Sets the salary to a new value"""
        self._salary = new_salary

    def get_email_address(self):
        """Gets the email address of Employee"""
        return self._email_address

    def set_email_address(self, new_email_address):
        """Sets the email address to a new value"""
        self._email_address = new_email_address


def make_employee_dict(names, id_nums, salaries, emails):
    """Takes employees' information, adds to dictionary, sets key to ID, and returns dictionary entry"""
    database = {}  # Begin with empty dictionary for employee database
    roster_length = len(names)  # Need length of list to for iteration range

    # Iterate through multiple lists for employee attributes
    for value in range(roster_length):  
        name = names[value]
        id_num = id_nums[value]
        salary = salaries[value]
        email_address = emails[value]

        employee = Employee(name, id_num, salary, email_address)   # Object for employee is created

        database[id_num] = employee  # Database is filled with employees with id_number as key

    return database


if __name__ == '__main__':

    emp_names = ["Jean", "Kat", "Pomona"]
    emp_ids = ["100", "101", "102"]
    emp_sals = [30, 35, 28]
    emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
    result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)
    print(result["101"].get_name())
