# SYSS-Employee-Management
Syntax to execute curl commands inside the “SYSS Employee Management” project. 
**Note: All syntax is formatted for Windows CMD Prompt. For Unix OS, format accordingly if necessary.**

1) **GET** method: The GET method is used to retrieve resources from the localhost URL - in this case - returning
a list of all employees inside the database.
<br/>***Syntax:***```curl -H “Content-Type:application/javascript” -X GET http://localhost:8000/employees/```

2) **POST** method: The POST method is used to add employee information inside the database. *“name”*, *“email”* and
*“department”* fields are not necessary, but compose of the employee object.
<br/>***Syntax:***```curl -u username -H “Content-Type:application/json” -X POST http://localhost:8000/employees/ -d  “{\“name\”:\”employee_name\”, \“email\”:\”employee_email\”, \“department\”:\”employee_department\”}”```
<br/><br/>**Note: Will ask for username’s password in prompt**

3) **PUT** method: The PUT method is used to alter already existing information about an employee inside the
database. The *employee_id* is required to specify which employee is being affected. ONLY the owner that
created the POST of the employee has permission to perform a PUT request for the same employee.
<br/>***Syntax:***```curl -u username -H “Content-Type:application/json” -X PUT http://localhost:8000/employees/employee_id/ -d  “{\“name\”:\”employee_name\”, \“email\”:\”employee_email\”, \“department\”:\”employee_department\”}”```
<br/><br/>**Note: Will ask for username’s password in prompt**

4) **DELETE** method: The DELETE method is used to delete a specific employee record from the database. The
*employee_id* is required to specify which employee is being affected. ONLY the owner that created the POST
of the employee has permission to perform a DELETE request for the same employee.
<br/>***Syntax:***```curl -u username -H “Content-Type:application/json” -X DELETE http://localhost:8000/employees/employee_id/```
<br/><br/>**Note: Will ask for username’s password in prompt**
