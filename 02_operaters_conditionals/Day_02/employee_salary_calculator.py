Employee_Name=input("Enter Employee Name:")
Basic_Salary=int(input("Enter Basic Salary:"))
hra=int(input("Enter HRA in persent:"))
da=int(input("Enter DA in persent:"))
Tax=int(input("Enter Tax in persent:"))

HRA_Amount =( Basic_Salary * hra )/ 100

DA_Amount = (Basic_Salary * da) / 100

Gross_Salary = Basic_Salary + HRA_Amount + DA_Amount

Tax_Amount = (Gross_Salary * Tax) / 100

Net_Salary = Gross_Salary - Tax_Amount

print("="*34)
print("EMPLOYEE SALARY SLIP".center(34))
print("="*34)
print(f"{"Employee Name":<15}:{Employee_Name}")
print(f"{"Basic_Salary":<15}:{Basic_Salary}")
print(f"{"HRA":<15}:{hra}")
print(f"{"DA":<15}:{da}")
print(f"{"Gross Salary":<15}:{Gross_Salary}")
print(f"{"Tax":<15}:{Tax_Amount}")
print(f"{"Net_Salary":<15}:{Net_Salary}")
print("-"*34)