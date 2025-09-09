def find_sum(first,second):
    result=first+second
    return result

res=find_sum(10,20)
print(res)

employees=[]
#create employee
employee=('bhanu',46,50000,True)
employees.append(employee)

employee=('mahesh',46,40000,True)
employees.append(employee)

print('after add all employeees:',employees)
#search employee
i=0
search="kalyani"
index=-1
for emp in employees:
    if emp[0]==search:
        index=i
        break
    i+=1
    if index==-1:
        print ('employee not found')
    else:
        search_employee=employees[index]
        print(search_employee)
        salary=float(input('salary:'))
        employee=(search_employee[0],search_employee[1])
        employees[index]=employee
        print('after search and update:',employees)
for emp in employees:
    if emp[0]==search:
        index=i
        break  
    i+=1
    if index == -1:
        print('employee not found')
    else:
        search_employee =employees[index]
        print(search_employee)
        salary=float(input('salary'))
        employees[index]=employee
        print ('after search and update:',employees)
        employee=('dravid',50,200,7,True)
        employees.append(employee)
        print('after add dravid:',employees)
        #delete employee mahesh by position
        position=1 
        employees.pop(position)
        print('after delete mahesh:',employees)
         