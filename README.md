📌 Project Overview

This project is a simple web application developed as part of the VirtuBox “Digitize Your Business” assessment.
The application demonstrates authentication and CRUD operations using a clean and minimal approach.

The focus of this project is on correctness, clarity, and working functionality, not on complex UI design.

🛠️ Technology Stack

-Backend: Python (Flask)

-Frontend: HTML, CSS

-Database: SQLite

-Version Control: Git & GitHub

🔐 Features Implemented
Authentication

-User Sign Up

-User Login

-User Logout

-Basic input validation

-Session-based authentication

-CRUD Operations (After Login)

-Create an item (Task / Note)

-View list of items

-Edit an item (optional / can be extended)

-Delete an item

-Each user can only see and manage their own data.

🧠 Brief Explanation of Approach

-Flask is used as a lightweight backend framework to handle routing, authentication, and database operations.

-HTML templates are rendered using Flask’s render_template.

-SQLite is used as a local database for simplicity and ease of setup.

-Sessions are used to maintain user login state.

-The application follows a simple and readable structure to ensure clarity and maintainability.

⚙️ Setup Instructions
1️⃣ Prerequisites

Python 3.x installed on the system

Git installed

2️⃣ Clone the Repository
git clone https://github.com/anushree1611/Login-webpage.git
cd "Login-webpage"

3️⃣ Install Dependencies
pip install flask

4️⃣ Run the Application
py app.py

5️⃣ Open in Browser
http://127.0.0.1:5000

🧪 Test Cases
Authentication Test Cases
| Test Case                      | Expected Result              |
| ------------------------------ | ---------------------------- |
| Sign up with new user          | User registered successfully |
| Sign up with existing username | Error message                |
| Login with valid credentials   | Redirect to dashboard        |
| Login with invalid credentials | Login fails                  |
| Logout                         | Redirect to login page       |

CRUD Test Cases
| Test Case    | Expected Result     |
| ------------ | ------------------- |
| Create item  | Item added to list  |
| View items   | All items displayed |
| Delete item  | Item removed        |
| Refresh page | Data persists       |


📂 Project Structure
Login-webpage/
├── app.py
├── README.md
├── database.db
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
└── static/
    └── style.css

📌 Notes

-UI is intentionally kept simple as per assessment instructions.

-Focus is on working functionality rather than visual design.

-Code is written clearly and kept easy to understand.

-No external frameworks were used beyond Flask.
