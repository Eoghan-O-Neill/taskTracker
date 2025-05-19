# taskTracker
This is a basic task tracker command line interface (CLI) app I made as a part of the roadmap.sh backend developer roadmap. You can find the specification for the project [here](https://roadmap.sh/projects/task-tracker).

The task tracker does not require any modules external to the Python standard library.  

Run the task tracker by running the task-cli.py file in the command line.  
```python task-cli.py```  

The task tracker has the following functionality...
To add a task use the add argument. The following argument adds a to do item called "Wash the dishes".  
```python task-cli.py add "Wash the dishes"```  

Each item gets a unique ID that is displayed after the todo item is added. Each item is also set with a status of 'to-do'.  
```# Output: Task added successfully (ID: 1)```  

You can use this unique ID to update, delete or mark the status of todos. Todos can be 'in-progress' or 'done'.
```python task-cli.py update 1 "Wash the dishes and clean the car"```  
```python task-cli.py delete 1```  
```python task-cli.py mark-in-progress 1```  
```python task-cli.py mark-done 1```  

You can list all todos...  
```python task-cli.py list```  

Or todos with a specific status...  
```python task-cli.py list in-progress```


