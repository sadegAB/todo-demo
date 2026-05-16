TODOS = []

def add_todo(title, priority="Medium"):
    todo = {"title": title, "priority": priority}
    TODOS.append(todo)
    return title
