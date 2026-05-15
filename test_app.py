from app import TODOS, add_todo


def test_add_todo():
    TODOS.clear()

    result = add_todo("Study German")

    assert result == "Study German"
    assert TODOS == ["Study German"]
