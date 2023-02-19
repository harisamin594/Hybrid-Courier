import tkinter as tk
import random
parcelID_list = []
employeeID_list = []
branchID_list = []

window = tk.Tk() 
window.title("Courier Management System")
window.geometry("650x500")

class Delivery_Charges(): 

    def __init__(self, parcel_weight, delivery_type):
        self.parcel_weight = int(parcel_weight)
        self.delivery_type = int(delivery_type)
        
    def Calculate_Charges(self):    # calculating delivery charges

        if self.delivery_type == 1:     #if delivery type is normal delivery
            charges = int(self.parcel_weight * 0.25)

        elif self.delivery_type == 2:   #if delivery type is fast delivery
            charges = int(self.parcel_weight * 0.35)

        return str(charges)

class Customer():
    
    def Get_SenderName(self):
        sender_name = input("Enter Sender Name: ")
        return sender_name

    def Get_SenderPhone(self):
        sender_phone = input("Sender Phone Number: ")
        return sender_phone
    
    def Get_SenderAddress(self):
        sender_address = input("Enter Sender Address: ")
        return sender_address
    
    def Get_ReceiverName(self):
        receiver_name = input("Enter Receiver Name: ")
        return receiver_name
    
    def Get_ReceiverPhone(self):
        receiver_phone = input("Receiver Phone Number: ")
        return receiver_phone
    
    def Get_ReceiverAddress(self):
        receiver_address = input("Enter Receiver Address: ")
        return receiver_address

class Parcel():
    def __init__(self):
        self.obj_customer = Customer()
    
    def Create_ParcelDetail(self): #parcel weight is to be in grams and delivery type is either fast delivery or normal delivery
        parcel_type = input("What Kind of A Parcel Is It? \n")
        parcel_weight = input("Enter The Weight of The Parcel In Grams: \n")
        delivery_type = input("Do You Want a Normal Delivery or a Fast Delivery? \nEnter 1 for Normal Delivery and 2 for Fast Delivery: ")

        sender_name = self.obj_customer.Get_SenderName()
        sender_phone = self.obj_customer.Get_SenderPhone()
        sender_address = self.obj_customer.Get_SenderAddress()
        receiver_name = self.obj_customer.Get_ReceiverName()
        receiver_phone = self.obj_customer.Get_ReceiverPhone()
        receiver_address = self.obj_customer.Get_ReceiverAddress()

        global parcelID_list
        flag = False
        parcelID = random.randint(1000,10000)
        while flag == False:
            if parcelID in parcelID_list:
                parcelID = random.randint(1000,10000)
            else:
                parcelID_list.append(parcelID)
                outfile = open("Parcel detail.txt", "a")
                if delivery_type == "1":
                    delivery_speed = "Normal Delivery"
                elif delivery_type == "2":
                    delivery_speed = "Fast Delivery"

                print("Parcel Details: " + "\nParcel ID: " + str(parcelID) + "\nParcel Type: " + parcel_type.title() + "\nParcel Weight: " + str(parcel_weight) + "\nDelivery Type: " + delivery_speed, file = outfile)
                print("Sender Details: " + "\nSender Name: " + str(sender_name) + "\nSender Phone Number: " + str(sender_phone) + "\nSender Address: " + str(sender_address), file = outfile)
                print("Receiver Details: " + "\nReceiver Name: " + str(receiver_name) + "\nReceiver Phone Number: " + str(receiver_phone) + "\nReceiver Address: " + str(receiver_address) + "\n-------------------------------", file = outfile)
                outfile.close()
                obj_charges = Delivery_Charges(parcel_weight, delivery_type)
                print("Your Parcel ID is " + str(parcelID) + " and delivery charges are " + obj_charges.Calculate_Charges() + " Rs.") 
                flag = True

# sample driver code for parcel class
#parcel = Parcel()
#watch.Create_ParcelDetail()

class AllOrders():  
    
    def Display_AllParcels(self):   #displaying all orders
        infile = open("Parcel detail.txt", 'r')
        for line in infile:
            print(line)
        infile.close()    
                
#sample driver code for all orders
#display = AllOrders()
#display.Display_AllParcels()


class Employee():

    def Get_EmployeeDetail(self):   #acquiring employee details from user
        self.employee_name = input("Enter Employee Name: ")
        self.employee_phone = input("Enter Employee Phone Number: ")
        self.employee_address = input("Enter Employee Address: ")
        self.employee_category = int(input("Are You: \n1. Manager\n2.Mid-Level\n3.Entry-level\n"))

    def Create_EmployeeDetail(self):    #adding employee details to employee file
        global employeeID_list
        flag = False
        employee_ID = random.randint(100,1000)
        while flag == False:
            if employee_ID in employeeID_list:
                employee_ID = random.randint(100,1000)
            else:
                employeeID_list.append(employee_ID)
                outfile = open("Employee detail.txt", "a")
                if self.employee_category == 1:
                    rank = "Manager"
                elif self.employee_category == 2:
                    rank = "Mid-Level"
                elif self.employee_category == 3:
                    rank = "Entry-Level"

                print("\n-------------------------------" + "Employee Details: " + "\nEmployee Name: " + self.employee_name + "\nEmployee ID: " + str(employee_ID) + "\nEmployee Phone Number: " + self.employee_phone + "\nEmployee Address: " + self.employee_address + "\nEmployee Category: " + rank + "\n-------------------------------", file = outfile)
                outfile.close()
                return "Your Employee ID is: " + str(employee_ID)
                flag = True
              
    def Display_Employee(self):     #displaying employee list
        
        infile = open("Employee detail.txt", "r")
        for line in infile:
            print(line)
            
        infile.close

    def Calculate_Pay(self):    #printing pay slip of employee
        flag = False
        emp_cat = int(input("Enter Your Category: "))
        while flag == False:

            if emp_cat == 1:
                pay = "75,000 Rs"           #STANDARD PAY OF MANAGERS
                print("Pay is: ", pay)
                break
            
            elif emp_cat == 2:    
                pay = "50,000 Rs"           #STANDARD PAY OF MID-LEVEL EMPLOYEES
                print("Pay is: ", pay)
                break
        
            elif emp_cat == 3:    
                pay = "$30,000 Rs"          #STANDARD PAY OF ENTRY-LEVEL EMPLOYEES
                print("Pay is: ", pay)
                break

            else:
                print("Category doesn't exist!\n")
                emp_cat = int(input("Enter Your Category: "))
             

#sample driver code for employee class
#employee = Employee()
#employee.Get_EmployeeDetail()
#employee.Create_EmployeeDetail()
#employee.Display_Employee()
#employee.Calculate_Pay()

class Branch():

    def Get_BranchDetail(self):     #getting detail for a newly opened branch
        self.branch_address = input("Enter Address of New Branch: ")
        self.branch_city = input("Enter City of New Branch: ")
        self.branch_timing = input("Enter Timing of New Branch: ")
        self.branch_manager = input("Enter Name of Branch Manager: ")
        self.branch_phone = input("Enter Branch Phone Number: ")
     
    def Create_Branches(self):  #creating/updating detail of branches
        global branchID_list
        branchID = random.randint(1,1000)
        flag = False
        while flag == False:
            if branchID in branchID_list:
                branchID = random.randint(1,1000)
            else:
                branchID_list.append(branchID)
                outfile = open("Branch detail.txt", "a")
                print("\n-------------------------------" + "Branch Details: ""\nBranch ID: " + str(branchID) + "\nBranch Area: " + self.branch_address + "\nBranch City: " + self.branch_city + "\nBranch Timing: " + self.branch_timing + "\nBranch Manager: " + self.branch_manager + "\nBranch Phone Number: " + self.branch_phone + "\n-------------------------------", file = outfile)
                outfile.close()
                flag = True

    def Display_Branches(self):     # displaying all information in branch detail file
        infile = open("Branch detail.txt", "r")
        for line in infile:
            print(line)

        infile.close()

#sample driver code for branch class         
#branch = Branch()
#branch.Get_BranchDetail()
#branch.Create_Branches()
#branch.Display_Branches()


# Code for GUI below
def emp_func():
    employee = Employee()
    employee.Get_EmployeeDetail()
    employee.Create_EmployeeDetail()
    print("Welcome Aboard! Your Details Have Been Added to The Employee List.")
    
def pay_func():
    employee = Employee()
    employee.Calculate_Pay()
        
def branch_func():
    branch = Branch()
    branch.Get_BranchDetail()
    branch.Create_Branches()
    print("Branch File Updated!")
    
def display_orders_func():
    display = AllOrders()
    display.Display_AllParcels()

def place_order_func():
    parcel = Parcel()
    parcel.Create_ParcelDetail()
        
def display_branches_func():
    branch = Branch()
    branch.Display_Branches()

def display_employee_list():
    employee = Employee()
    employee.Display_Employee()

def admin_func():
    signup_button = tk.Button(text = 'Add New Employee Details', command = emp_func).pack(side = 'bottom')
    pay_button = tk.Button(text = 'Print Pay Slip', command = pay_func).pack(side = 'bottom')
    update_branch_button = tk.Button(text = 'Add New Branch', command = branch_func).pack(side ='bottom')
    display_orders_button = tk.Button(text = 'Display All Orders', command = display_orders_func).pack(side = 'bottom')
    display_employee_button = tk.Button(text = 'Display Employee List', command = display_employee_list).pack(side = 'bottom')

def customer_func():
    place_order_button = tk.Button(text = 'Place an Order', command = place_order_func).pack(side = 'bottom')
    display_branches_button = tk.Button(text = 'Display All Branches', command = display_branches_func).pack(side = 'bottom')

def exit_func():
    window.destroy()

main_label = tk.Label(text = 'Welcome to Hybrid Courier Management System', font = ('Helvetica', 25, "bold"), fg = 'purple').pack(side = 'top')
signin_label = tk.Label(text = 'Sign in as: ', font = ('Helvetica', 20)).pack(side = 'top')
info_label = tk.Label(text = 'After your pressed button turns blue, head over to the python interpretor for the program to continue.').pack(side = 'bottom')
exit_button = tk.Button(text = 'Exit The Program', command = exit_func, fg = 'red', height = 2, width = 25).pack(side = 'bottom')
admin_button = tk.Button(text = 'Admin', command = admin_func, fg = 'green', height = 2, width = 25).pack(side = 'left')
customer_button = tk.Button(text = 'Customer', command = customer_func, fg = 'green', height = 2, width = 25).pack(side = 'right')

window.mainloop()


