from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

CORS(app)

client = MongoClient("mongodb+srv://raja:raja@cluster0.h2swe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['Dashboard']
collection = db['candidates']

@app.route('/candidates', methods=['GET'])
def get_candidates():
    # Build filter from query parameters
    filter_query = {}

    # Filter by name (case-insensitive search)
    name = request.args.get('name')
    if name:
        filter_query['name'] = {'$regex': name, '$options': 'i'}

    # Filter by exact rank
    rank = request.args.get('rank')
    if rank:
        try:
            filter_query['rank'] = int(rank)
        except ValueError:
            pass

    # Filter by rank range
    rank_min = request.args.get('rank_min')
    rank_max = request.args.get('rank_max')
    if rank_min or rank_max:
        filter_query['rank'] = {}
        if rank_min:
            try:
                filter_query['rank']['$gte'] = int(rank_min)
            except ValueError:
                pass
        if rank_max:
            try:
                filter_query['rank']['$lte'] = int(rank_max)
            except ValueError:
                pass

    # Filter by job_id
    job_id = request.args.get('job_id')
    if job_id:
        filter_query['job_id'] = job_id

    # Filter by last_update date range (expects ISO format dates)
    last_update_start = request.args.get('last_update_start')
    last_update_end = request.args.get('last_update_end')
    if last_update_start or last_update_end:
        filter_query['last_update'] = {}
        if last_update_start:
            try:
                dt_start = datetime.fromisoformat(last_update_start)
                filter_query['last_update']['$gte'] = dt_start
            except ValueError:
                pass
        if last_update_end:
            try:
                dt_end = datetime.fromisoformat(last_update_end)
                filter_query['last_update']['$lte'] = dt_end
            except ValueError:
                pass

    # Retrieve candidates using the built filter
    cursor = collection.find(filter_query)
    candidates = []
    for candidate in cursor:
        # Convert ObjectId to string for JSON serialization
        candidate['_id'] = str(candidate['_id'])
        # Convert job_id to string if present
        if 'job_id' in candidate:
            candidate['job_id'] = str(candidate['job_id'])
        # Convert datetime to ISO string if present
        if 'last_update' in candidate and isinstance(candidate['last_update'], datetime):
            candidate['last_update'] = candidate['last_update'].isoformat()
        candidates.append(candidate)

    return jsonify(candidates)

if __name__ == '__main__':
    app.run(debug=True)
