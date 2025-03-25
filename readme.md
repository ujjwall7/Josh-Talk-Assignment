# Josh Talk Assignment - Task Management API

## Overview
This is a Django Rest Framework (DRF) based Task Management API for Josh Talk Assignment. The API allows users to create tasks, assign them to users, and retrieve user-specific tasks.

## Features
- Create tasks with name, description, and type.
- Assign tasks to one or multiple users.
- Retrieve tasks assigned to a specific user.
- Django Admin panel for task and user management.

## Installation & Setup
### Prerequisites
- Python 3.x
- Django & Django Rest Framework
- Virtual Environment (Recommended)

### Setup Instructions
```bash
# Clone the repository
git clone https://github.com/ujjwall7/Josh-Talk-Assignment.git
cd Josh-Talk-Assignment

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## API Endpoints
### 1. Create a Task
**Endpoint:** `POST /task/`
```json
{
  "name": "New Task",
  "description": "This is a sample task",
  "task_type": "feature"
}
```
**Response:**
```json
{
  "msg": "Task Created Successfully",
  "success": true
}
```

### 2. Assign Task to User(s)
**Endpoint:** `POST /assign_task/`
```json
{
  "user_id": "[1,2]",
  "task_id": "5"
}
```
**Response:**
```json
{
  "msg": "Assigned Task Successfully",
  "success": true
}
```

### 3. Get User Tasks
**Endpoint:** `GET /user_task/?user_id=1`
**Response:**
```json
{
  "data": {
    "id": 1,
    "name": "John Doe",
    "mobile": "9876543210",
    "username": "johndoe",
    "email": "john@example.com",
    "tasks": [
      {
        "id": 5,
        "name": "New Task",
        "description": "This is a sample task",
        "task_type": "feature",
        "completed_at": null,
        "status": "pending",
        "assigned_users": [1]
      }
    ]
  }
}
```

## Admin Panel
- Access the Django admin panel at: `http://127.0.0.1:8000/admin/`
- Login using the superuser credentials created earlier.

## Testing
To run tests, execute the following command:
```bash
python manage.py test
```

## Notes
- Ensure Django and DRF are installed before running the API.
- Always apply migrations before running the server.
- Modify settings as per the environment (development/production).

## Repository
[Josh Talk Assignment Repo](https://github.com/ujjwall7/Josh-Talk-Assignment)

