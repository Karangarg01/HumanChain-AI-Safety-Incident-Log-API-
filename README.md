# AI Safety Incident Log Service

This is a simple RESTful API service built with **Python** and **Django** to log and manage hypothetical AI safety incidents.

---

## 🚀 Tech Stack

- **Language:** Python 3.x
- **Framework:** Django 5.x
- **Database:** SQLite (default with Django)
- **Other Libraries:** Django REST Framework (for building APIs)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Karangarg01/HumanChain-AI-Safety-Incident-Log-API-.git
cd HumanChain-AI-Safety-Incident-Log-API-
``` 
If you have the project as a ZIP, unzip it and navigate inside the folder.

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```bash
python manage.py migrate
```

### 5. (Optional) Create Superuser for Admin Panel
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 6. Run the Development Server
```bash
python manage.py runserver
```
Server will start at: http://127.0.0.1:8000/

### 7. (Optional) Pre-populate Sample Incidents
You can add 2-3 sample incidents manually through:
  
- Django Admin Panel (http://127.0.0.1:8000/admin) OR
- Using the API (explained below).

---
# 📚 API Endpoints
All requests and responses are in JSON.

### 1. Get All Incidents
URL: GET /incidents/
- Description: Fetch all logged incidents.
- Example using curl:

```bash
curl -X GET http://127.0.0.1:8000/incidents/
```

### 2. Create a New Incident
URL: POST /incidents/
- Description: Log a new incident.
- Request Body Example:

```json
{
  "title": "AI Malfunction",
  "description": "AI model generated unsafe output",
  "severity": "High"
}
``` 
Example using curl:

``` bash
curl -X POST http://127.0.0.1:8000/incidents/ \
-H "Content-Type: application/json" \
-d '{"title":"AI Malfunction", "description":"AI model generated unsafe output", "severity":"High"}'
```

### 3. Get a Specific Incident by ID
URL: GET /incidents/{id}/
- Description: Fetch a specific incident by its ID.

Example:

```bash
curl -X GET http://127.0.0.1:8000/incidents/1/
```

### 4. Delete a Specific Incident by ID
URL: DELETE /incidents/{id}/
- Description: Delete a specific incident by its ID.

Example:

```bash
curl -X DELETE http://127.0.0.1:8000/incidents/1/
```

---
# ⚠️ Notes
- Valid severity values: "Low", "Medium", "High".
- reported_at timestamp is automatically set when an incident is created.
- Proper error handling is implemented (e.g., 400 Bad Request, 404 Not Found).

# 👨‍💻 Admin Panel Access
After creating a superuser, login at:

``` arduino
http://127.0.0.1:8000/admin
```
You can create, view, update, and delete incidents easily via the admin dashboard.

---
# 🏁 Final Notes
- All dependencies are listed in requirements.txt.
- Project is built with clean code principles and Django best practices.
- Fully RESTful API structure.
