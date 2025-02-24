from pymongo import MongoClient
from faker import Faker
import random
from datetime import datetime

fake = Faker()

client = MongoClient("mongodb+srv://raja:raja@cluster0.h2swe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['Dashboard']

# Define the two collections
jobs_col = db['jobs']
candidates_col = db['candidates']

job_titles = [
    "Software Engineer", "Data Scientist", "DevOps Engineer",
    "Product Manager", "QA Engineer"
]
skills_pool = [
    "Python", "JavaScript", "SQL", "Docker", "Kubernetes",
    "Machine Learning", "Data Analysis", "Java", "C#", "Ruby"
]

# Insert 5 job records
job_ids = []
for _ in range(5):
    job = {
        "job_title": random.choice(job_titles),
        "skills": random.sample(skills_pool, k=random.randint(2, 5)),
        "responsibilities": fake.paragraph(nb_sentences=5),
        "companyName": fake.company(),
        "Location": fake.city()
    }
    result = jobs_col.insert_one(job)
    job_ids.append(result.inserted_id)

print(f"Inserted {len(job_ids)} job records.")

# --- Create Dummy Candidate Records ---
for _ in range(100):
    candidate = {
        "name": fake.name(),
        "rank": random.randint(1, 100),
        "last_update": datetime.now(),  # You can also use fake.date_time_this_year() for random timestamps
        "job_id": random.choice(job_ids)
    }
    candidates_col.insert_one(candidate)

print("Inserted 100 candidate records.")
