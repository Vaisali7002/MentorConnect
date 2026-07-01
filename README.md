# MentorConnect — Student Mentor Collaboration Platform


## Overview

MentorConnect is a web-based mentorship platform designed to bridge the gap between students and experienced mentors by creating a structured environment for career guidance and professional development.

The platform enables students to seek mentorship in critical career areas while allowing mentors to review requests and make informed decisions through a role-based workflow system.

Built as a full-stack web application using Python Flask, SQLite, HTML, CSS, and Jinja templating.

---
## Project Outcome

MentorConnect demonstrates the implementation of a scalable mentorship management workflow by combining authentication systems, database-driven request management, role-based access control, session handling, and dynamic dashboard interfaces into a unified web application.

The project focuses on solving real-world mentorship coordination challenges through structured digital interaction between students and mentors.
## Application Preview

### Home Page

![Home](mentorconnect/screenshots/home.png)

### Registration Page

![Register](mentorconnect/screenshots/register.png)

### Login Page

![Login](mentorconnect/screenshots/login.png)

### Student Dashboard

![Student Dashboard](mentorconnect/screenshots/student_dashboard.png)

### Mentor Dashboard

![Mentor Dashboard](mentorconnect/screenshots/mentor_dashboard.png)



## Core Objective

The objective of MentorConnect is to create a centralized mentorship ecosystem where students can request personalized guidance related to internships, placements, resume building, higher studies, and professional development while mentors manage and respond to these requests efficiently.

---

## Key Features

### Authentication System

* Secure user registration system
* Separate login workflow for Students and Mentors
* Duplicate email prevention using database constraints
* Session management for authenticated users
* Logout functionality with session clearing

### Role-Based Access Control

Two distinct user roles:

**Student**

* Register account
* Login securely
* Submit mentorship requests
* Track submitted requests
* View request approval status

**Mentor**

* Register account
* Login securely
* Access mentor dashboard
* View all student mentorship requests
* Accept requests
* Reject requests

### Request Management System

Students can submit mentorship requests under multiple categories:

* Internship Guidance
* Resume Review
* Placement Preparation
* Higher Studies Guidance

Each request stores:

* Student Email
* Request Category
* Priority Level
* Preferred Meeting Date
* Detailed Request Message
* Current Request Status

### Dashboard System

Student Dashboard:

* View all previously submitted requests
* Track request processing status
* Create new mentorship requests

Mentor Dashboard:

* View all incoming student requests
* Review request details
* Accept or reject requests
* Manage mentorship workflow

### Status Tracking

Request lifecycle management:

* Pending
* Accepted
* Rejected

Dynamic status visualization integrated inside dashboards.

---

## Technology Stack

Backend:

* Python
* Flask Framework

Database:

* SQLite3

Frontend:

* HTML5
* CSS3

Templating Engine:

* Jinja2

Architecture:

* Modular Flask Application Structure

---

## Project Architecture

mentorconnect/

├── app.py
├── models.py
├── database.py
├── mentorconnect.db
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── request.html
│   ├── dashboard.html
│   └── student_dashboard.html
│
└── static/
└── style.css

---

## Application Workflow

### Student Flow

Register Account

↓

Login

↓

Access Student Dashboard

↓

Create Mentorship Request

↓

Track Request Status

---

### Mentor Flow

Register Account

↓

Login

↓

Access Mentor Dashboard

↓

Review Student Requests

↓

Accept or Reject Request

---

## Technical Implementation Highlights

* Flask Routing System
* Jinja Template Inheritance
* SQLite Database Integration
* Modular Backend Design
* Role-Based Session Authentication
* Dynamic Navigation Rendering
* Form Handling using POST Requests
* Protected Route Access Validation
* Database CRUD Operations

---

## Installation

Clone repository

```bash
git clone https://github.com/Vaisali7002/MentorConnect.git
```

Move into project folder

```bash
cd MentorConnect
```

Run application

```bash
python app.py
```

Open browser

```text
http://127.0.0.1:5000
```

---

