
# Candidates Dashboard Project

This project demonstrates a full‑stack web application that displays candidate data from a MongoDB Atlas database. The application includes a Flask backend that provides a `/candidates` API endpoint (with filtering support) and a front‑end HTML page that uses Bootstrap and vanilla JavaScript to display, filter, and sort candidate data.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Files Description](#files-description)
- [Installation and Setup](#installation-and-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Dummy Data Generation](#dummy-data-generation)
- [API Details](#api-details)
- [License](#license)

## Project Overview

The Candidates Dashboard project is a full‑stack demo that:
- Uses **Flask** to create a RESTful API that connects to MongoDB Atlas.
- Applies filter parameters (such as candidate name, rank, job ID, and last update date range) on the candidate data.
- Returns candidate data in JSON format, properly converting MongoDB’s ObjectIds and datetime values.
- Uses **Flask-CORS** to allow cross-origin requests from any origin.
- Provides a front‑end HTML page (served via a live server) that:
  - Displays a filter form.
  - Fetches data from the API.
  - Renders a table with candidate information.
  - Highlights the top candidate (first row) in a primary color.
  - Allows sorting on any table header by clicking, with arrow indicators showing ascending (↑) or descending (↓) order.

## Project Structure

```
/project-root
  ├── app.py                 # Flask backend API code
  ├── dummy_data.py          # Script to insert dummy data (jobs and candidates) into MongoDB Atlas
  ├── index.html             # Frontend HTML file with Bootstrap and JavaScript
  ├── requirements.txt       # Python dependencies list
  └── README.md              # Project documentation (this file)
```

## Files Description

### app.py
- **Purpose:**  
  Implements the Flask server which connects to MongoDB Atlas and provides the `/candidates` endpoint.
- **Key Features:**
  - Constructs a filter query from GET parameters (e.g., `name`, `rank`, `job_id`, date ranges).
  - Retrieves candidate records from the `candidates` collection.
  - Converts MongoDB ObjectIds (`_id` and `job_id`) and datetime values (`last_update`) to strings for JSON serialization.
  - Returns the filtered candidate records as a JSON response.
  - Uses Flask-CORS to allow cross-origin requests from any origin.

### dummy_data.py
- **Purpose:**  
  Uses Faker and PyMongo to populate the MongoDB database with dummy job and candidate records.
- **Key Features:**
  - Inserts 5 dummy job records into the `jobs` collection.
  - Inserts 100 dummy candidate records into the `candidates` collection.
  - Each candidate record includes a `name`, `rank`, a timestamp (`last_update`), and a reference to a job (stored as an ObjectId).

### index.html
- **Purpose:**  
  The front‑end page that displays the candidate dashboard.
- **Key Features:**
  - A filter form that accepts parameters like candidate name, exact rank, rank range, job ID, and last update date range.
  - A table that dynamically displays candidate data fetched from the `/candidates` API.
  - Client‑side JavaScript that:
    - Fetches data from the Flask API using the Fetch API.
    - Renders candidate data into the table.
    - Highlights the top candidate (first row) using Bootstrap’s `table-primary` class.
    - Allows sorting by clicking on table headers. Each header shows an arrow (↑ for ascending, ↓ for descending) indicating the current sort order.

### requirements.txt
- **Purpose:**  
  Contains the list of required Python packages and their versions.
- **Example Content:**
  ```
  Flask==2.2.5
  Flask-Cors==3.0.10
  pymongo==4.3.3
  Faker==18.9.0
  ```

## Installation and Setup

1. **Clone the Repository:**  
   Clone the project repository to your local machine.
   ```bash
   git clone https://github.com/Rajakrishnasrivatsav/Dashbaord
   cd Dashboard
   ```

2. **Create a Virtual Environment:**  
   Create and activate a Python virtual environment.
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**  
   Install the required packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB Atlas:**  
   - Create a MongoDB Atlas cluster if you haven’t already.
   - Create a database named **Dashboard**.
   - Create the collections **jobs** and **candidates** (these will be populated using the dummy data script).
   - Update the MongoDB connection string in `app.py` and `dummy_data.py` (if necessary) with your actual credentials and connection details.

## Running the Application

1. **Generate Dummy Data:**  
   Run the dummy data script to populate your database with sample job and candidate records.
   ```bash
   python dummy_data.py
   ```
   You should see confirmation messages indicating that dummy job and candidate records have been inserted.

2. **Start the Flask Server:**  
   Run the Flask application.
   ```bash
   python app.py
   ```
   The server will start (by default on `http://localhost:5000`).

3. **Serve the Frontend:**  
   Open the `index.html` file using your preferred method:
   - If using VSCode’s Live Server extension, right‑click the file and choose "Open with Live Server".
   - Alternatively, open the file directly in your browser (ensure the API endpoint in the JavaScript fetch URL points to `http://localhost:5000/candidates`).

## Usage

- **Filtering:**  
  Use the filter form at the top of the page to search by candidate name, exact rank, rank range, job ID, or last update date range.  
  Click the **Filter** button to fetch and display the filtered data.

- **Sorting:**  
  Click on any table header (ID, Name, Rank, Last Update, or Job ID) to sort the candidate records based on that field.
  - The first click sorts in ascending order (displayed with an up arrow ↑).
  - A subsequent click toggles to descending order (displayed with a down arrow ↓).
  - Arrow indicators update to reflect the current sort direction.

- **Highlighting:**  
  The top candidate (the first row in the table after any sorting/filtering) is highlighted using Bootstrap's `table-primary` class.

- **Reset:**  
  Click the **Reset** button to clear all filter fields and reload the entire candidate dataset.

## API Details

- **Endpoint:** `/candidates`  
  - **Method:** GET  
  - **Query Parameters:**
    - `name`: Case-insensitive substring match for candidate name.
    - `rank`: Exact match for candidate rank.
    - `rank_min` and `rank_max`: Define a rank range.
    - `job_id`: Filter by job ID.
    - `last_update_start` and `last_update_end`: Filter by the last update date range (expects ISO format date strings).
  - **Response:**  
    A JSON array of candidate objects, where each object contains:
    - `_id`: Candidate document ID (string)
    - `name`: Candidate name (string)
    - `rank`: Candidate rank (number)
    - `last_update`: Timestamp in ISO string format
    - `job_id`: Job ID associated with the candidate (string)

## License

This project is provided for demonstration purposes. You are free to modify and use the code as needed.
