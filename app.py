import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

DATA_FILE = os.path.abspath("courses.json")

def load_courses():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_courses(courses):
    with open(DATA_FILE, "w") as f:
        json.dump(courses, f, indent=2)

# 1. GET ALL COURSES
@app.route('/api/courses', methods=['GET'])
def get_all_courses():
    courses = load_courses()
    return jsonify(courses), 200

# 2. GET COURSE STATISTICS (Placed before <int:course_id> route)
@app.route('/api/courses/stats', methods=['GET'])
def get_course_stats():
    courses = load_courses()
    total_courses = len(courses)
    status_counts = {}
    
    for course in courses:
        status = course.get("status", "Unknown")
        status_counts[status] = status_counts.get(status, 0) + 1

    return jsonify({
        "total_courses": total_courses,
        "by_status": status_counts
    }), 200

# 3. GET SINGLE COURSE BY ID
@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    courses = load_courses()
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": f"Course with ID {course_id} not found"}), 404
    return jsonify(course), 200

# 4. ADD A COURSE (POST)
@app.route('/api/courses', methods=['POST'])
def add_course():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Field 'name' is required"}), 400

    courses = load_courses()
    new_id = max([c["id"] for c in courses], default=0) + 1
    
    new_course = {
        "id": new_id,
        "name": data.get("name"),
        "description": data.get("description", ""),
        "target_date": data.get("target_date", ""),
        "status": data.get("status", "Not Started")
    }
    
    courses.append(new_course)
    save_courses(courses)
    return jsonify(new_course), 201

# 5. UPDATE A COURSE (PUT)
@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    courses = load_courses()
    course = next((c for c in courses if c["id"] == course_id), None)
    if not course:
        return jsonify({"error": f"Course with ID {course_id} not found"}), 404

    course["name"] = data.get("name", course["name"])
    course["description"] = data.get("description", course["description"])
    course["target_date"] = data.get("target_date", course["target_date"])
    course["status"] = data.get("status", course["status"])

    save_courses(courses)
    return jsonify(course), 200

# 6. DELETE A COURSE (DELETE)
@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    courses = load_courses()
    updated_courses = [c for c in courses if c["id"] != course_id]

    if len(updated_courses) == len(courses):
        return jsonify({"error": f"Course with ID {course_id} not found"}), 404

    save_courses(updated_courses)
    return jsonify({"message": f"Course {course_id} successfully deleted"}), 200

if __name__ == '__main__':
    print("CodeCraftHub API is starting...")
    print(f"- Data will be stored in: {DATA_FILE}")
    print("- API will be available at: http://localhost:5000\n")
    app.run(debug=True, host='127.0.0.1', port=5000)
