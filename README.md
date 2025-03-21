### Logical Equivalence of Recursive SQL CTE in Python
This repo showcases how the logic of a recursive SQL common table
expression can be achieved in Python. The Python snippet explicitly
shows the level order traversal outside of an SQL context.

## Run SQL Query
You can run the SQL code on [db-fiddle](https://www.db-fiddle.com/) for example:

1. Select **PostgreSQL v15**.
2. Paste the contents of `create_employee_table.sql` into the **Schema SQL** section (left pane).
3. Paste the contents of `hierarchy_query.sql` into the **Query SQL** section (right pane).
4. Click **Run**.

## Run Python Equivalent
To run the Python version of the same logic:

```bash
python3 hierarchy.py
