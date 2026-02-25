import os
from datetime import datetime, timezone

from flask import (
    Flask,
    abort,
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------------------------------------------------
# App configuration
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "todos.db")

app = Flask(__name__, static_folder="static")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "retro-todo-secret-key"

db = SQLAlchemy(app)

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------


class List(db.Model):
    __tablename__ = "lists"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    todos = db.relationship(
        "Todo", backref="list", lazy=True, cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<List {self.name!r}>"


class Todo(db.Model):
    __tablename__ = "todos"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, nullable=False, default=False)
    list_id = db.Column(db.Integer, db.ForeignKey("lists.id"), nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Todo {self.title!r}>"


# ---------------------------------------------------------------------------
# Serve shared retro.css from parent directory
# ---------------------------------------------------------------------------


@app.route("/retro.css")
def retro_css():
    css_path = os.path.join(BASE_DIR, "..", "retro.css")
    return send_file(css_path, mimetype="text/css")


# ---------------------------------------------------------------------------
# Routes -- Lists
# ---------------------------------------------------------------------------


@app.route("/")
def index():
    """Show all lists."""
    lists = List.query.order_by(List.created_at.asc()).all()
    # Attach counts so templates don't need extra queries
    list_data = []
    for lst in lists:
        total = Todo.query.filter_by(list_id=lst.id).count()
        done = Todo.query.filter_by(list_id=lst.id, completed=True).count()
        list_data.append({"list": lst, "total": total, "done": done})
    return render_template("index.html", list_data=list_data)


@app.route("/lists", methods=["POST"])
def create_list():
    """Create a new list."""
    name = request.form.get("name", "").strip()
    if name:
        new_list = List(name=name)
        db.session.add(new_list)
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/lists/<int:list_id>")
def show_list(list_id):
    """Show a single list with its todos."""
    lst = db.get_or_404(List, list_id)
    todos = Todo.query.filter_by(list_id=lst.id).order_by(Todo.created_at.asc()).all()
    total = len(todos)
    done = sum(1 for t in todos if t.completed)
    return render_template("list.html", list=lst, todos=todos, total=total, done=done)


@app.route("/lists/<int:list_id>/edit", methods=["POST"])
def edit_list(list_id):
    """Rename a list."""
    lst = db.get_or_404(List, list_id)
    name = request.form.get("name", "").strip()
    if name:
        lst.name = name
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/lists/<int:list_id>/delete", methods=["POST"])
def delete_list(list_id):
    """Delete a list and all its todos."""
    lst = db.get_or_404(List, list_id)
    db.session.delete(lst)
    db.session.commit()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Routes -- Todos
# ---------------------------------------------------------------------------


@app.route("/lists/<int:list_id>/todos", methods=["POST"])
def create_todo(list_id):
    """Add a todo to a list."""
    lst = db.get_or_404(List, list_id)
    title = request.form.get("title", "").strip()
    if title:
        todo = Todo(title=title, list_id=lst.id)
        db.session.add(todo)
        db.session.commit()
    return redirect(url_for("show_list", list_id=lst.id))


@app.route("/todos/<int:todo_id>/toggle", methods=["POST"])
def toggle_todo(todo_id):
    """Toggle the completed state of a todo."""
    todo = db.get_or_404(Todo, todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for("show_list", list_id=todo.list_id))


@app.route("/todos/<int:todo_id>/edit", methods=["POST"])
def edit_todo(todo_id):
    """Edit a todo's title."""
    todo = db.get_or_404(Todo, todo_id)
    title = request.form.get("title", "").strip()
    if title:
        todo.title = title
        db.session.commit()
    return redirect(url_for("show_list", list_id=todo.list_id))


@app.route("/todos/<int:todo_id>/delete", methods=["POST"])
def delete_todo(todo_id):
    """Delete a todo."""
    todo = db.get_or_404(Todo, todo_id)
    list_id = todo.list_id
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("show_list", list_id=list_id))


# ---------------------------------------------------------------------------
# Database initialisation & seed data
# ---------------------------------------------------------------------------


def seed_database():
    """Populate empty database with sample data."""
    if List.query.first() is not None:
        return  # Already seeded

    personal = List(name="Personal")
    work = List(name="Work")
    db.session.add_all([personal, work])
    db.session.flush()  # Get IDs assigned

    sample_todos = [
        Todo(title="Buy groceries", completed=False, list_id=personal.id),
        Todo(title="Call the dentist", completed=True, list_id=personal.id),
        Todo(title="Read a book", completed=False, list_id=personal.id),
        Todo(title="Go for a walk", completed=False, list_id=personal.id),
        Todo(title="Finish quarterly report", completed=False, list_id=work.id),
        Todo(title="Reply to client emails", completed=True, list_id=work.id),
        Todo(title="Update project roadmap", completed=False, list_id=work.id),
    ]
    db.session.add_all(sample_todos)
    db.session.commit()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        seed_database()
    app.run(debug=True, port=5001)
