# SQLite CRUD API

A FastAPI application integrated with SQLite for local data persistence.

## 1. Persistence Rationale
SQLite provides zero-configuration, single-file local persistence (`tasks.db`). Data automatically persists across server restarts.

## 2. Storage Location
Database file path: `./tasks.db`

## 3. Local Setup & Execution
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn
