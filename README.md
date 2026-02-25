# ORMery Python Demo — Flask + sqlite3

A retro-styled todo list app built with Flask, Jinja2, and Python's stdlib `sqlite3`, using the **Temper-compiled ORMery query builder** for schema definition, SELECT queries, and INSERT operations.

Port: **5001**

## How ORMery Is Vendored

The compiled ORMery library lives in `vendor/` with three subdirectories:

```
vendor/
  ormery/          ← the query builder
  std/             ← Temper standard library
  temper-core/     ← Temper runtime
```

These are added to `sys.path` at the top of `app.py`:

```python
import sys, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "temper-core"))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "std"))
sys.path.insert(0, os.path.join(BASE_DIR, "vendor", "ormery"))
```

No SQLAlchemy, no third-party ORM — just Flask and the stdlib `sqlite3` module.

```
# requirements.txt
Flask==3.1.0
```

## How ORMery Is Used

### Schema Definition

From `app.py` — both schemas defined at module level. ORMery's Python API uses snake_case.

```python
from ormery.ormery import schema, field, Query, InMemoryStore, to_insert_sql
from temper_core import Pair, map_constructor

store = InMemoryStore()

list_schema = schema("lists", [
    field("name", "String", False, False),
    field("created_at", "String", False, True),
])

todo_schema = schema("todos", [
    field("title", "String", False, False),
    field("completed", "Int", False, False),
    field("list_id", "Int", False, False),
    field("created_at", "String", False, True),
])
```

### SELECT Queries (ORMery)

ORMery builds the SQL string, then `sqlite3` executes it:

```python
# GET / — fetch all lists ordered by created_at
sql = (Query(list_schema, store)
    .order_by("created_at", "asc")
    .to_sql()
    .to_string())
lists = db.execute(sql).fetchall()

# GET /lists/<id> — fetch todos for a list, sorted
sql = (Query(todo_schema, store)
    .where("list_id", "=", str(list_id))
    .order_by("completed", "asc")
    .order_by("created_at", "desc")
    .to_sql().to_string())
todos = db.execute(sql).fetchall()
```

### INSERT Operations (ORMery)

Values are passed as a Temper map built from a Python dict using `Pair` and `map_constructor`:

```python
def _make_map(d):
    """Build a Temper Map from a plain Python dict."""
    return map_constructor(tuple(Pair(k, v) for k, v in d.items()))

# POST /lists — create a new list
values = _make_map({"name": name, "created_at": _now_iso()})
sql = to_insert_sql(list_schema, values).to_string()
db.execute(sql)
db.commit()

# POST /lists/<id>/todos — create a new todo
values = _make_map({
    "title": title,
    "completed": "0",
    "list_id": str(list_id),
    "created_at": _now_iso(),
})
sql = to_insert_sql(todo_schema, values).to_string()
db.execute(sql)
db.commit()
```

### Raw SQL (not supported by ORMery)

UPDATE, DELETE, and aggregate COUNT queries use parameterized SQL:

```python
# Toggle completed status (ORMery doesn't generate UPDATE)
db.execute(
    "UPDATE todos SET completed = ? WHERE id = ?",
    (new_val, todo_id),
)

# Delete a list and its todos (ORMery doesn't generate DELETE)
db.execute("DELETE FROM todos WHERE list_id = ?", (list_id,))
db.execute("DELETE FROM lists WHERE id = ?", (list_id,))

# Aggregate count (ORMery doesn't support COUNT)
total = db.execute(
    "SELECT COUNT(*) FROM todos WHERE list_id = ?", (list_id,)
).fetchone()[0]
```

## Running

```bash
pip install -r requirements.txt
python app.py
# → Todo app running at http://localhost:5001
```
