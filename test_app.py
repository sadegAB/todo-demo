from app import TODOS, add_todo

def test_add_todo():
    TODOS.clear()
    result = add_todo("Study German")
    assert result == "Study German"
    assert TODOS == [{"title": "Study German", "priority": "Medium"}]

def test_add_todo_with_priority():
    TODOS.clear()
    result = add_todo("Fix bug", priority="High")
    assert result == "Fix bug"
    assert TODOS[0]["priority"] == "High"

def test_default_priority_is_medium():
    TODOS.clear()
    add_todo("Read book")
    assert TODOS[0]["priority"] == "Medium"
