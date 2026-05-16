# Changed Files

## app.py
- Added `add_todo(title, priority="Medium")` function
- Stores todo as dict with title and priority
- Default priority is Medium
- Supported priorities: Low, Medium, High

## test_app.py
- Updated existing test to match new dict structure
- Added test_add_todo_with_priority
- Added test_default_priority_is_medium
