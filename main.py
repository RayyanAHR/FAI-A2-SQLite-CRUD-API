from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from database import get_db_connection, init_db

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    title: str
    done: bool

def format_task(row):
    return {"id": row["id"], "title": row["title"], "done": bool(row["done"])}

@app.get("/tasks")
def get_tasks():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return [format_task(row) for row in rows]

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    return format_task(row)

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    title = task.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, 0)", (title,))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return {"id": new_id, "title": title, "done": False}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    title = task.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail={"error": "Title cannot be empty"})
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    cursor.execute("UPDATE tasks SET title = ?, done = ? WHERE id = ?", (title, int(task.done), task_id))
    conn.commit()
    conn.close()
    return {"id": task_id, "title": title, "done": task.done}

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    if not cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail={"error": "Task not found"})
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    return None