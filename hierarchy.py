EMPLOYEE_ID = "employee_id"
NAME = "name"
MANAGER_ID = "manager_id"
MANAGER_HIERARCHY = "manager_hierarchy"
LEVEL = "level"

#### Data
from random import shuffle

employees = [
    {EMPLOYEE_ID: 1, NAME: "Head Honcho", MANAGER_ID: None},
    {EMPLOYEE_ID: 2, NAME: "Bob", MANAGER_ID: 1},
    {EMPLOYEE_ID: 3, NAME: "Alice", MANAGER_ID: 1},
    {EMPLOYEE_ID: 4, NAME: "John", MANAGER_ID: 1},
    {EMPLOYEE_ID: 5, NAME: "Frank", MANAGER_ID: 2},
    {EMPLOYEE_ID: 6, NAME: "Steve", MANAGER_ID: 4},
    {EMPLOYEE_ID: 7, NAME: "Mary", MANAGER_ID: 2},
    {EMPLOYEE_ID: 8, NAME: "Joe", MANAGER_ID: 3},
    {EMPLOYEE_ID: 9, NAME: "Chunk", MANAGER_ID: 6},
    {EMPLOYEE_ID: 10, NAME: "Larry", MANAGER_ID: 8},
    {EMPLOYEE_ID: 11, NAME: "Phil", MANAGER_ID: 9},
    {EMPLOYEE_ID: 12, NAME: "David", MANAGER_ID: 4},
    {EMPLOYEE_ID: 13, NAME: "Henry", MANAGER_ID: 5},
    {EMPLOYEE_ID: 14, NAME: "Eve", MANAGER_ID: 12},
    {EMPLOYEE_ID: 15, NAME: "Gracie", MANAGER_ID: 13},
]
# Show that the solution is not order dependent.
shuffle(employees)

### Solution
from collections import deque, defaultdict

# maps managers to their subordinates via ID
hierarchy = defaultdict(list)
for employee in employees:
    if employee[MANAGER_ID] is not None:
        hierarchy[employee[MANAGER_ID]].append(employee[EMPLOYEE_ID])

# maps employee IDs to the corresponding name
names = {employee[EMPLOYEE_ID]: employee[NAME] for employee in employees}

# Do a level order traversal of the hierarchy tree with the help of a queue and
# pass the parent hierarchy string into the queue along with the child.
solution = []
root_id = next(
    employee[EMPLOYEE_ID] for employee in employees if employee[MANAGER_ID] is None
)
queue = deque(((root_id, "[NULL]"),))
level = 1
while queue:
    for _ in range(len(queue)):
        employee_id, hierarchy_string = queue.popleft()
        solution.append(
            {
                EMPLOYEE_ID: employee_id,
                NAME: names[employee_id],
                MANAGER_HIERARCHY: hierarchy_string,
                LEVEL: level,
            }
        )
        hierarchy_string = (
            hierarchy_string + " -> " + names[employee_id]
            if hierarchy_string != "[NULL]"
            else names[employee_id]
        )
        for subordinate in hierarchy[employee_id]:
            queue.append((subordinate, hierarchy_string))
    level += 1

# Sort by level first and then by employee ID.
solution.sort(key=lambda row: (row[LEVEL], row[EMPLOYEE_ID]))

for row in solution:
    print(row)
