# Stock Management System
This project is an Inventory Management System built with Django, designed to help keep track of inventory and manage stock levels.

## Table of Content
### Features
### Installation
### Usage

## Features
User Authentication: Secure login and registration for users.
Inventory Tracking: Add, update, and delete inventory items.
Stock Management: Monitor stock levels and receive alerts for low stock.
Responsive Design: Accessible on both desktop and mobile devices.

## Installation
Clone the Repository:

git clone [https://github.com/calebtetteh2000/Stock-Management-System/tree/main](https://github.com/calebtetteh2000/Stock-Management-System.git)
cd inventory-management-system

### Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate

### Install Dependencies:
pip install -r requirements.txt

### Apply Migrations:
python manage.py migrate

### Create a Superuser:
python manage.py createsuperuser

### Run the Development Server:
python manage.py runserver

## Usage
Login/Registration: Users can register for an account and log in to access the system. Users are prompted to use strong passwords.
Dashboard: After logging in, users are directed to the dashboard, where they can see an overview of the inventory status.
Manage Inventory: Users can add new items, update existing ones, or delete items from the inventory.
Stock Management: Users can monitor stock levels and update stock quantities as needed. If stock reaches a minimum of 3 quantities, it is flagged.

