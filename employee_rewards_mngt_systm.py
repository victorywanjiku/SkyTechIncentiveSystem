#create an employee rewards management system.Set up an appropriate project directory structure.Create all necessary Python projocet files within the structure.Create a class named Employee that stores the following details for each employee:employee_id,employee_name,basic_salary,productivity_score,attendance_rate
#the system should collect employee details from the user repeatedly until the user decides to stop. Include error handling for invalid inputs. Productivity Bonus RulesProductivity Score,Bonus:90-100	18% of basic_salary,80-89 10% of basic_salary,70-79 5% of basic_salary,Below 70 No bonus.Attendance Reward Rules,Attendance Rate,Bonus≥ 97%	Ksh 5,000,92 – 96%	Ksh 2,000,Below 92%	No bonus.Create a member function calculateProductivityBonus() that calculates and returns the productivity bonus.Create a member function calculateAttendanceReward() that calculates attendance reward.Create a member function calculateTotalReward() that returns the total reward earned by the employee.Create a subclass named TeamLeader that inherits from Employee and:Includes a function calculateLeadershipBonus(),Overrides calculateTotalReward() to include an additional leadership bonus equal to 10% of basic_salary.Implement a function that generates a reward report listing all employees with their total reward earned.Add functionality to save the report into a file named:EmployeeRewardsReport.txt
#import os
class Employee:
    def __init__(self, employee_id, employee_name, basic_salary, productivity_score, attendance_rate):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary
        self.productivity_score = productivity_score
        self.attendance_rate = attendance_rate

    def calculateProductivityBonus(self):
        if 90 <= self.productivity_score <= 100:
            return 0.18 * self.basic_salary
        elif 80 <= self.productivity_score < 90:
            return 0.10 * self.basic_salary
        elif 70 <= self.productivity_score < 80:
            return 0.05 * self.basic_salary
        else:
            return 0

    def calculateAttendanceReward(self):
        if self.attendance_rate >= 97:
            return 5000
        elif 92 <= self.attendance_rate < 97:
            return 2000
        else:
            return 0

    def calculateTotalReward(self):
        return self.calculateProductivityBonus() + self.calculateAttendanceReward()

class TeamLeader(Employee):
    def calculateLeadershipBonus(self):
        return 0.10 * self.basic_salary

    def calculateTotalReward(self):
        return super().calculateTotalReward() + self.calculateLeadershipBonus()
def generateRewardReport(employees):
    report_lines = []
    for emp in employees:
        total_reward = emp.calculateTotalReward()
        report_lines.append(f"Employee ID: {emp.employee_id}, Name: {emp.employee_name}, Total Reward: Ksh {total_reward:.2f}")
    
    report_content = "\n".join(report_lines)
    with open("EmployeeRewardsReport.txt", "w") as file:
        file.write(report_content)
    print("Reward report generated and saved to EmployeeRewardsReport.txt")
def main():
    employees = []
    while True:
        try:
            employee_id = input("Enter Employee ID: ")
            employee_name = input("Enter Employee Name: ")
            basic_salary = float(input("Enter Basic Salary: "))
            productivity_score = float(input("Enter Productivity Score (0-100): "))
            attendance_rate = float(input("Enter Attendance Rate (0-100): "))
            
            if not (0 <= productivity_score <= 100):
                raise ValueError("Productivity score must be between 0 and 100.")
            if not (0 <= attendance_rate <= 100):
                raise ValueError("Attendance rate must be between 0 and 100.")
            
            employee = Employee(employee_id, employee_name, basic_salary, productivity_score, attendance_rate)
            employees.append(employee)
        except ValueError as e:
            print(f"Invalid input: {e}")
        
        cont = input("Do you want to add another employee? (yes/no): ").strip().lower()
        if cont != 'yes':
            break
    
    generateRewardReport(employees)
if __name__ == "__main__":    
    main()









       


       
