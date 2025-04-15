from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# version 1.0
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)

@app.route("/tasks")
@app.route("/")
def home_page():
    active_tasks, completed_tasks = Task.query.filter_by(is_active=True).all(), Task.query.filter_by(is_active=False).all()
    return render_template("index.html", active_tasks=active_tasks, completed_tasks=completed_tasks)

@app.route("/tasks/add_task", methods=["POST"])
def add_task():
    text = request.form.get("task_text")
    db.session.add(
        Task(
            text=text,
            is_active=True
        )
    )
    db.session.commit()
    return redirect(url_for("home_page"))

@app.route("/tasks/delete_task/<int:task_id>", methods=["GET"])
def delete_task(task_id):
    db.session.delete(Task.query.get(task_id))
    db.session.commit()

    return redirect(url_for("home_page"))

@app.route("/tasks/complete_task/<int:task_id>", methods=["GET"])
def complete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task.is_active = False
    db.session.commit()

    return redirect(url_for("home_page"))


with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
