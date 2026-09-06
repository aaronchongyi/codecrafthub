# CodeCraftHub — RESTful Course Tracker API

CodeCraftHub is a lightweight, beginner-friendly RESTful API built with Python and Flask. It allows developers to track courses they want to learn, update their learning progress, and view simple statistics about their learning goals—all backed by simple, persistent JSON file storage.

This project serves as a practical, hands-on introduction to building web APIs, handling HTTP requests, and understanding full CRUD (Create, Read, Update, Delete) architecture.

---

## Features

- **Full CRUD Support:** Create, read, update, and delete course records.
- **File-Based Persistence:** Automatically saves all course data to a local courses.json file—no complex database configuration required!
- **Dynamic Course Statistics:** Calculate progress totals and breakdowns by status (Not Started, In Progress, Completed).
- **RESTful Best Practices:** Returns standard JSON payloads and proper HTTP status codes (200 OK, 201 Created, 400 Bad Request, 404 Not Found).

---

## Project Structure

The project uses a simple, flat structure:

\\\	ext
codecrafthub/
│
├── app.py          # Main Flask application containing API routes & logic
├── courses.json    # Local JSON storage (automatically generated)
└── README.md       # Project documentation
\\\

### Component Roles

- **pp.py**: Handles incoming HTTP requests, routes them to specific functions, and executes logic to manipulate data.
- **courses.json**: Acts as your database. When data changes via POST, PUT, or DELETE requests, pp.py updates this file immediately.

---

## Prerequisites & Installation

### Step 1: Install Python

Ensure Python 3.8 or higher is installed on your machine. You can check your version in your terminal:

\\\ash
python --version
\\\

### Step 2: Clone or Download the Repository

Clone this repository to your local computer:

\\\ash
git clone https://github.com/aaronchongyi/codecrafthub.git
cd codecrafthub
\\\

### Step 3: Install Flask

Install Flask using Python's package manager (pip):

\\\ash
pip install flask
\\\

---

## How to Run the Application

Start the Flask development server by running:

\\\ash
python app.py
\\\

Upon starting, you will see output similar to this:

\\\	ext
CodeCraftHub API is starting...
Data will be stored in: C:\Users\...\codecrafthub\courses.json
API will be available at: http://localhost:5000
Running on http://127.0.0.1:5000
\\\

Keep this terminal window open while testing your endpoints.

---

## API Endpoints Documentation

All requests interact with http://127.0.0.1:5000.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | /api/courses | Retrieve a list of all courses |
| **GET** | /api/courses/stats | View course statistics summary |
| **GET** | /api/courses/<id> | Retrieve a single course by ID |
| **POST** | /api/courses | Add a new course |
| **PUT** | /api/courses/<id> | Update an existing course |
| **DELETE** | /api/courses/<id> | Delete a course |

---

### Request & Response Examples

#### 1. Retrieve All Courses (GET /api/courses)

**Request:** GET http://127.0.0.1:5000/api/courses

**Response (200 OK):**
\\\json
[
  {
    "id": 1,
    "name": "Python Basics",
    "description": "Learn syntax and data structures",
    "target_date": "2026-10-15",
    "status": "In Progress"
  }
]
\\\

#### 2. Create a Course (POST /api/courses)

**Request:** POST http://127.0.0.1:5000/api/courses  
**Header:** Content-Type: application/json  
**Body:**
\\\json
{
  "name": "Flask REST APIs",
  "description": "Master REST API design with Flask",
  "target_date": "2026-11-01",
  "status": "Not Started"
}
\\\

**Response (201 Created):**
\\\json
{
  "id": 2,
  "name": "Flask REST APIs",
  "description": "Master REST API design with Flask",
  "target_date": "2026-11-01",
  "status": "Not Started"
}
\\\

#### 3. Update a Course (PUT /api/courses/<id>)

**Request:** PUT http://127.0.0.1:5000/api/courses/1  
**Header:** Content-Type: application/json  
**Body:**
\\\json
{
  "status": "Completed"
}
\\\

**Response (200 OK):**
\\\json
{
  "id": 1,
  "name": "Python Basics",
  "description": "Learn syntax and data structures",
  "target_date": "2026-10-15",
  "status": "Completed"
}
\\\

#### 4. Course Statistics (GET /api/courses/stats)

**Request:** GET http://127.0.0.1:5000/api/courses/stats

**Response (200 OK):**
\\\json
{
  "total_courses": 2,
  "by_status": {
    "Completed": 1,
    "Not Started": 1
  }
}
\\\

---

## Testing the API

You can test the running API using PowerShell or cURL.

### Testing in PowerShell (Windows)

\\\powershell
# 1. Get all courses
Invoke-RestMethod -Uri http://localhost:5000/api/courses -Method Get

# 2. Add a new course
$body = @{ name = "Git Fundamentals"; status = "Not Started" } | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/api/courses -Method Post -ContentType "application/json" -Body $body

# 3. View Statistics
(Invoke-RestMethod -Uri http://localhost:5000/api/courses/stats) | ConvertTo-Json
\\\

### Testing with cURL (macOS/Linux/Git Bash)

\\\ash
# 1. Get all courses
curl -X GET http://127.0.0.1:5000/api/courses

# 2. Add a course
curl -X POST http://127.0.0.1:5000/api/courses \
     -H "Content-Type: application/json" \
     -d '{"name": "Git Fundamentals", "status": "Not Started"}'

# 3. Delete a course
curl -X DELETE http://127.0.0.1:5000/api/courses/1
\\\

---

## Troubleshooting Common Issues

### 1. ModuleNotFoundError: No module named 'flask'
- **Cause:** Flask is not installed in your current Python environment.
- **Fix:** Run pip install flask in your terminal.

### 2. Address already in use or Port 5000 Error
- **Cause:** Another process is using port 5000.
- **Fix:** Change the port in pp.py at the bottom of the file:
  \\\python
  app.run(debug=True, host='127.0.0.1', port=5001)
  \\\

### 3. Red Error Text in PowerShell when making GET requests
- **Cause:** Invoke-RestMethod throws standard exceptions when receiving 400 or 404 status codes.
- **Fix:** This is normal behavior for PowerShell when an endpoint responds with an error status code (e.g., trying to fetch a non-existent course ID).

---

## License

This project is open-source and available under the [MIT License](LICENSE).