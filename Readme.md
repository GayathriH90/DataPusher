# Data Pusher Django Web Application 

## Overview This Django web application is designed to receive data into the app server for an account and send it across different platforms (destinations) using webhook URLs. 

## Modules 

### Account Module 
	- Each account has: 
		- Email ID (mandatory and unique) 
		- Account ID (unique to each account) 
		- Account Name (mandatory) 
		- App Secret Token (automatically generated) 
		- Website (optional) 

### Destination Module 
	- Each destination belongs to an account and includes: 
		- URL (mandatory) 
		- HTTP Method (mandatory) 
		- Headers (mandatory with multiple values) 

### Data Handler 
	- Receives JSON data via POST method. 
	- Validates data using 'APP_SECRET_TOKEN' header. 
	- Routes data to appropriate destinations based on account. 

## Features 

**CRUD Operations:** Create, read, update, and delete operations for both accounts and destinations. 

**Dynamic Routing:** Sends data to destinations based on configured HTTP methods. 

**Secure Communication:** Validates requests using secret tokens. 

**Data Integrity:** Ensures data integrity and format compliance. 

## Installation and Setup 

1. **Clone Repository:** "git clone <repository-url> cd project-directory" 

2. **Setup Virtual Environment:** "python -m venv env source env/bin/activate"
# On Windows use "env\Scripts\activate" 

3. **Install Dependencies:** "pip install -r requirements.txt" 

4. **Run Migrations:** "python manage.py migrate" 

5. **Create Superuser (Optional):** "python manage.py createsuperuser" 

6. **Run Development Server:** "python manage.py runserver" 

7. **API Endpoints:** 
	- Accounts API: '/api/accounts/' 
	- Destinations API: '/api/destinations/' 
	- Retrieve Destinations for an Account: '/api/accounts/<account_id>/destinations/' 
	- Incoming Data API: '/server/incoming_data/' 

## Usage 

**Creating Accounts and Destinations:** Use the provided APIs or Django admin interface. 

**Sending Data:**  POST JSON data to '/server/incoming_data/' with 'CL-X-TOKEN' header containing the 'APP_SECRET_TOKEN'.

**Managing Data Destinations:**  Associate destinations with accounts to route data based on HTTP methods.
