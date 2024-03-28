from task_package.create_task import create_task
from task_package.edit_task import edit_task
from task_package.categorize_task import categorize_task


#create a task
task1=create_task("complete your Assigment","finish Task Mangement SYSTEM")
#display the task
print("Task 1:,task1")
#edit tha task
edit_task(task1,new_title="update Assigemnet",new_description="review and submit to rashmii mam")
#display the upadte task
print("Update Task 1:",task1)
#categorize  the task
categorize_task(task1,"Zappcode Academy")
#Display the categorized task
print("categorized Task1:",task1)
