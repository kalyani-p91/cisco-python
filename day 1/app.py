import  repo

#Create 
employee=(101,'Banu',23,50000,True)
repo.create_employee(employee)
print(f'Employee {employee[1]} Creates Successfully')
print('After Add :',repo.read_all_employee())

employee = (102,'Manu', 23, 30000, True)
repo.create_employee(employee)
print(f'EMployee {employee[1]} Created Successfully')
print('After Add :',repo.read_all_employee())


# test Read by Id 
employee=repo.read_by_id(102)
if employee==None:
    print('Employee Not Found')
else:
    print(employee)
    
# test update 
employee_to_update = repo.read_by_id(102)

if employee_to_update is None:
    print('Employee Not Found')
else:
    id, name, age, salary, is_active = employee_to_update
    salary += 20000  # Increase salary
    updated_employee = (id, name, age, salary, is_active)
    repo.update(102, updated_employee)
    print(f'Employee {id} Updated Successfully')
    print('After Update:', repo.read_all_employee())

# test delete

repo.delete_employee(102)
print('After Delete:',repo.read_all_employee())
        
# Make us app


