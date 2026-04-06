# Disaster Management System

## Overview

This project is a full-stack Disaster Management System developed using Python and a relational database. It is designed to help manage disaster-related information, coordinate emergency responses, and efficiently allocate resources during critical situations.

The system provides a centralized platform for reporting disasters, tracking affected areas, and managing rescue operations.

## Objectives

* Provide a structured system for disaster reporting
* Enable efficient resource allocation and tracking
* Maintain a centralized database for disaster-related data
* Improve coordination between authorities and response teams

## Features

* User registration and authentication
* Disaster reporting (location, type, severity)
* Resource management (food, medical aid, shelters)
* Real-time status tracking of incidents
* Admin dashboard for monitoring and control

## Tech Stack

* Backend: Python (Flask / Django – update accordingly)
* Frontend: HTML, CSS, JavaScript
* Database: MySQL / PostgreSQL / SQLite (update accordingly)
* Tools: Git, VS Code

## Database Design

* Relational database structure
* Tables for:

  * Users
  * Disaster Reports
  * Resources
  * Response Teams
* Proper use of:

  * Primary Keys
  * Foreign Keys
  * Normalization (to reduce redundancy)

## Project Structure

```id="dmk381"
├── app/
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   ├── static/
├── database/
├── requirements.txt
├── run.py
├── README.md
```

## Installation

```bash id="zv29xp"
git clone https://github.com/your-username/disaster-management-system.git
cd disaster-management-system
pip install -r requirements.txt
```

## Usage

Run the application:

```bash id="kq91as"
python run.py
```

Access in browser:

```
http://127.0.0.1:5000/
```

## Key Highlights

* Integration of DBMS concepts with real-world application
* Full-stack implementation using Python
* Efficient data handling and query execution
* Scalable structure for future enhancements

## Future Improvements

* Integration with real-time APIs (weather, alerts)
* Mobile application support
* GIS-based location tracking
* Notification system for emergency alerts

## Conclusion

This project demonstrates how database management systems and full-stack development can be combined to build a practical solution for disaster response and management.
