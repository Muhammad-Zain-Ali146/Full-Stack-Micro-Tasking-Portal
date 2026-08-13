# MicroTasker - Dynamic Full-Stack Micro-Task Portal

MicroTasker is a full-stack web application built to connect individuals needing quick micro-services with skilled users looking to complete tasks for rewards. It features complete authentication, task management (CRUD), real-time client-side search filtering, and robust database management.

## Tech Stack & Architecture

* **Backend Framework:** Python / Flask
* **Database:** PostgreSQL (SQLAlchemy ORM)
* **Frontend:** Dynamic HTML5 Templates (Jinja2) & CSS3
* **Client-Side Scripting:** Vanilla JavaScript (DOM Manipulation & Real-Time Filtering)
* **Design Pattern:** Model-View-Controller (MVC)

## Key Features

* **User Authentication:** Secure User Registration, Login, and Session Management with password hashing.
* **Task Lifecycle Management (CRUD):** 
  * Authenticated users can post tasks with custom titles, descriptions, and budget.
  * Real-time status updates (e.g., Open $\rightarrow$ Completed).
* **Instant Client-Side Search:** Real-time task filtering on the `/tasks` page using JavaScript DOM event listeners without page reloads.
* **Responsive Dashboard:** Personalized view for users to monitor their posted tasks and submission statuses.
* **Separation of Concerns:** Clean code structure separating backend routes, database schemas, frontend styles, and JavaScript interactions.

## Project Structure
micro-task-portal/
│
├── app.py                # Main application routes & controller logic
├── config.py             # Database & environment configurations
├── models.py             # PostgreSQL database schemas (User & Task models)
│
├── templates/            # HTML Views rendered via Jinja2
│   ├── base.html         # Base layout template
│   ├── index.html        # Home landing page
│   ├── explore.html      # Browse tasks page with dynamic search bar
│   ├── dashboard.html    # User task control panel
│   ├── task_detail.html  # Detailed task view & status management
│   ├── login.html        # Login interface
│   └── register.html     # User registration form
│
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Custom application styling
    └── js/
        └── main.js       # Real-time search & interactive UI logic
