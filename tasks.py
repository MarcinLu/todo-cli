def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    return tasks

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    return tasks

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks