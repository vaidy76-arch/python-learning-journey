"""
Employee Management System

Demonstrates 3-level inheritance:
- Employee (base)
- Manager (extends Employee)
- Director (extends Manager)

Includes polymorphic processing and JSON persistence.
"""

import json
from datetime import date


class Employee:
    """Base employee class - all other roles inherit from this."""
    
    def __init__(self, name, salary, hire_date):
        """
        Parameters:
            name (str): Employee's full name
            salary (float): Annual salary in USD
            hire_date (str): Date hired in ISO format (YYYY-MM-DD)
        """
        self.name = name
        self.salary = salary
        self.hire_date = hire_date
    
    def get_raise(self, percent):
        """
        Apply a percentage raise to the salary.
        
        Parameters:
            percent (float): Raise percentage (e.g., 0.05 for 5%)
        
        Returns:
            float: The new salary after raise
        """
        self.salary *=(1+percent)
        return self.salary
    
    def to_dict(self):
        """
        Convert this employee to a dictionary (for JSON storage).
        
        Returns:
            dict: Employee data as a dictionary
        """
        employee_data={
            "role": "Employee",
            "name": self.name,
            "salary": self.salary,
            "hire_date": self.hire_date
        }
        return employee_data
    
    def __str__(self):
        """String representation - useful for printing."""
        return f"{self.name} (${self.salary:,.2f})"


class Manager(Employee):
    """Manager - inherits from Employee, manages a team."""
    
    # TODO Step 4: implement __init__, get_raise, to_dict, run_meeting
    def __init__(self, name, salary, hire_date, team_size):
        super().__init__(name, salary, hire_date)
        self.team_size = team_size
    
    def get_raise(self, percent):
        super().get_raise(percent)
        self.salary*=1.02
        return self.salary
    
    def to_dict(self):
        data = super().to_dict()
        data["role"] = "Manager"
        data["team_size"] = self.team_size
        return data
    
    def run_meeting(self):
        return f"{self.name} is leading a meeting with {self.team_size} team members."


class Director(Manager):
    """Director - inherits from Manager, controls department budget."""
    
    # TODO Step 5: implement __init__, to_dict, approve_purchase
    def __init__(self, name, salary, hire_date, team_size, department_budget):
        super().__init__(name, salary, hire_date, team_size)
        self.department_budget = department_budget
    
    def to_dict(self):
        data = super().to_dict()
        data["role"] = "Director"
        data["department_budget"] = self.department_budget
        return data
    
    def approve_purchase(self, amount):
        """
        Approve a purchase if it's within the department budget.
    
        Returns:
            str: Approval or rejection message
        """
        if amount <=self.department_budget:
            return f"✅ {self.name} approved ${amount:,.2f} purchase (within budget)"
        else:
            return f"❌ {self.name} cannot approve ${amount:,.2f} (exceeds ${self.department_budget:,.2f} budget)"


def print_payroll_report(employees):
    """
    Print a payroll report for a mixed list of employees.
    Uses polymorphism - works on Employee, Manager, AND Director.
    
    Parameters:
        employees (list): List of Employee (or subclass) objects
    """
    
    print("💼 Payroll Report")
    print("==================")

    total_salary = 0

    for emp in employees:
        if isinstance(emp, Director):
            line = f"{emp.name} (Director): ${emp.salary:,.2f} - manages {emp.team_size} people, budget ${emp.department_budget:,.2f}"
        elif isinstance(emp, Manager):
            line = f"{emp.name} (Manager): ${emp.salary:,.2f} - manages {emp.team_size} people"
        else:
            line = f"{emp.name} (Employee): ${emp.salary:,.2f}"
        print(line)
        total_salary+=emp.salary
    print(f"\nTotal Payroll: ${total_salary:,.2f}")


def save_employees_to_json(employees, filename):
    """
    Save a list of employees to a JSON file.
    
    Parameters:
        employees (list): List of Employee (or subclass) objects
        filename (str): Path to output JSON file
    """
    
    employee_dicts = [emp.to_dict() for emp in employees]

    report = {
        "total_employees" : len(employees),
        "employees" : employee_dicts
    }

    try:
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
    except IOError as e:
        print(f"❌ Failed to save: {e}")
            
def main():
    """Build a sample workforce and demonstrate everything."""
    # Build a mixed list of employees
    workforce = [
        Employee("Alice Chen", 65000, "2022-03-15"),
        Employee("Bob Patel", 72000, "2021-08-01"),
        Manager("Carol Singh", 95000, "2020-01-10", team_size=5),
        Manager("David Kim", 105000, "2019-06-22", team_size=8),
        Director("Eva Rodriguez", 175000, "2017-11-05", 
                 team_size=20, department_budget=500000),
    ]
    
    # Show the polymorphic report
    print_payroll_report(workforce)
    
    # Demonstrate raises (polymorphic - each role has different rules)
    print("\n💰 Applying year-end raises...")
    for emp in workforce:
        new_salary = emp.get_raise(0.05)
        print(f"  {emp.name}: ${new_salary:,.2f}")
    
    # Save the whole workforce to JSON
    save_employees_to_json(workforce, "workforce.json")
    print(f"\n💾 Saved workforce to workforce.json")



if __name__ == "__main__":
    main()