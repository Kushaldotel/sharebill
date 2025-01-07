# College Expense Sharing Platform

A Django-based application that helps college students track and split their daily expenses with friends. The platform focuses on managing shared costs for dining, textbooks, travel, and outings, making group expenses easier to handle during college life.

## Features
- Custom User Management:
  - Register with email and password.
  - Profile fields include avatar, phone number, college year, bio, and date of birth.
  - User roles and permissions.

- Expense Sharing:
  - Split group expenses efficiently.
  - Track individual and group spending.

- User-Friendly Interface:
  - Modern UI for managing expenses.
  - Secure authentication and profile management.

## Tech Stack
- Backend: Django
- Database: SQLite (development)
- Frontend: Django Templates (placeholder, extendable to modern frameworks)

## Installation
1. Clone the repository:
   bash
   git clone <repository-url>
   cd <project-directory>


2. Create and activate a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate


3. Install dependencies:
   bash
   pip install -r requirements.txt


4. Apply migrations and run the server:
   bash
   python manage.py migrate
   python manage.py runserver


5. Access the app at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Future Enhancements
- Add real-time notifications for shared expenses.
- Integrate payment gateways for seamless transactions.
- Analytics for expense tracking and budgeting.