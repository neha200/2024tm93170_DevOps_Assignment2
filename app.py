from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize session data
def init_session():
    if 'workouts' not in session:
        session['workouts'] = []
    if 'user_info' not in session:
        session['user_info'] = {}

@app.route('/')
def index():
    init_session()
    return render_template('index.html', version='1.0')

@app.route('/api/workouts', methods=['GET'])
def get_workouts():
    init_session()
    return jsonify(session.get('workouts', []))

@app.route('/api/workouts', methods=['POST'])
def add_workout():
    init_session()
    data = request.get_json()
    
    workout = data.get('workout', '').strip()
    duration = data.get('duration', '')
    
    if not workout or not duration:
        return jsonify({'error': 'Please provide both workout and duration'}), 400
    
    try:
        duration = int(duration)
        if duration <= 0:
            raise ValueError('Duration must be positive')
    except ValueError:
        return jsonify({'error': 'Duration must be a positive number'}), 400
    
    entry = {
        'workout': workout,
        'duration': duration,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    workouts = session.get('workouts', [])
    workouts.append(entry)
    session['workouts'] = workouts
    session.modified = True
    
    return jsonify({'message': 'Workout added successfully', 'workout': entry}), 201

@app.route('/api/workouts/summary', methods=['GET'])
def get_summary():
    init_session()
    workouts = session.get('workouts', [])
    
    total_duration = sum(w['duration'] for w in workouts)
    total_workouts = len(workouts)
    
    return jsonify({
        'total_workouts': total_workouts,
        'total_duration': total_duration,
        'workouts': workouts
    })

@app.route('/api/user', methods=['GET'])
def get_user():
    init_session()
    return jsonify(session.get('user_info', {}))

@app.route('/api/user', methods=['POST'])
def save_user():
    init_session()
    data = request.get_json()
    
    try:
        name = data.get('name', '').strip()
        age = int(data.get('age', 0))
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        
        if not name or age <= 0 or weight <= 0 or height <= 0:
            raise ValueError('Invalid user data')
        
        # Calculate BMI
        bmi = weight / ((height / 100) ** 2)
        
        user_info = {
            'name': name,
            'age': age,
            'weight': weight,
            'height': height,
            'bmi': round(bmi, 2)
        }
        
        session['user_info'] = user_info
        session.modified = True
        
        return jsonify({'message': 'User info saved', 'user': user_info}), 200
    except (ValueError, KeyError) as e:
        return jsonify({'error': 'Invalid user data provided'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'version': '1.0'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)