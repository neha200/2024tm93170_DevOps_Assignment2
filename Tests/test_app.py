import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application"""
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    with app.test_client() as client:
        with app.app_context():
            yield client

@pytest.fixture
def init_session(client):
    """Initialize session with test data"""
    with client.session_transaction() as sess:
        sess['workouts'] = []
        sess['user_info'] = {}

class TestHomeRoute:
    """Test cases for home route"""
    
    def test_home_page_loads(self, client):
        """Test that home page loads successfully"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'ACEest Fitness' in response.data
    
    def test_home_page_version(self, client):
        """Test that version is displayed"""
        response = client.get('/')
        assert b'1.0' in response.data

class TestHealthCheck:
    """Test cases for health check endpoint"""
    
    def test_health_endpoint(self, client):
        """Test health check endpoint"""
        response = client.get('/health')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['status'] == 'healthy'
        assert json_data['version'] == '1.0'

class TestWorkoutAPI:
    """Test cases for workout API endpoints"""
    
    def test_get_empty_workouts(self, client, init_session):
        """Test getting workouts when none exist"""
        response = client.get('/api/workouts')
        assert response.status_code == 200
        json_data = response.get_json()
        assert isinstance(json_data, list)
        assert len(json_data) == 0
    
    def test_add_workout_success(self, client, init_session):
        """Test successfully adding a workout"""
        workout_data = {
            'workout': 'Push-ups',
            'duration': 30
        }
        response = client.post('/api/workouts',
                              json=workout_data,
                              content_type='application/json')
        assert response.status_code == 201
        json_data = response.get_json()
        assert json_data['message'] == 'Workout added successfully'
        assert json_data['workout']['workout'] == 'Push-ups'
        assert json_data['workout']['duration'] == 30
    
    def test_add_workout_missing_fields(self, client, init_session):
        """Test adding workout with missing fields"""
        workout_data = {
            'workout': 'Push-ups'
            # Missing duration
        }
        response = client.post('/api/workouts',
                              json=workout_data,
                              content_type='application/json')
        assert response.status_code == 400
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_add_workout_invalid_duration(self, client, init_session):
        """Test adding workout with invalid duration"""
        workout_data = {
            'workout': 'Squats',
            'duration': 'invalid'
        }
        response = client.post('/api/workouts',
                              json=workout_data,
                              content_type='application/json')
        assert response.status_code == 400
        json_data = response.get_json()
        assert 'error' in json_data
    
    def test_add_workout_negative_duration(self, client, init_session):
        """Test adding workout with negative duration"""
        workout_data = {
            'workout': 'Running',
            'duration': -10
        }
        response = client.post('/api/workouts',
                              json=workout_data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_add_workout_zero_duration(self, client, init_session):
        """Test adding workout with zero duration"""
        workout_data = {
            'workout': 'Plank',
            'duration': 0
        }
        response = client.post('/api/workouts',
                              json=workout_data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_get_workouts_after_adding(self, client, init_session):
        """Test getting workouts after adding some"""
        # Add first workout
        client.post('/api/workouts',
                   json={'workout': 'Push-ups', 'duration': 20},
                   content_type='application/json')
        
        # Add second workout
        client.post('/api/workouts',
                   json={'workout': 'Squats', 'duration': 15},
                   content_type='application/json')
        
        # Get all workouts
        response = client.get('/api/workouts')
        assert response.status_code == 200
        json_data = response.get_json()
        assert len(json_data) == 2
        assert json_data[0]['workout'] == 'Push-ups'
        assert json_data[1]['workout'] == 'Squats'

class TestSummaryAPI:
    """Test cases for summary API endpoint"""
    
    def test_summary_empty(self, client, init_session):
        """Test summary with no workouts"""
        response = client.get('/api/workouts/summary')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['total_workouts'] == 0
        assert json_data['total_duration'] == 0
        assert len(json_data['workouts']) == 0
    
    def test_summary_with_workouts(self, client, init_session):
        """Test summary with multiple workouts"""
        # Add workouts
        client.post('/api/workouts',
                   json={'workout': 'Push-ups', 'duration': 20},
                   content_type='application/json')
        client.post('/api/workouts',
                   json={'workout': 'Squats', 'duration': 30},
                   content_type='application/json')
        
        # Get summary
        response = client.get('/api/workouts/summary')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['total_workouts'] == 2
        assert json_data['total_duration'] == 50
        assert len(json_data['workouts']) == 2

class TestUserAPI:
    """Test cases for user API endpoints"""
    
    def test_get_empty_user_info(self, client, init_session):
        """Test getting user info when none exists"""
        response = client.get('/api/user')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data == {}
    
    def test_save_user_info_success(self, client, init_session):
        """Test successfully saving user info"""
        user_data = {
            'name': 'John Doe',
            'age': 25,
            'weight': 70,
            'height': 175
        }
        response = client.post('/api/user',
                              json=user_data,
                              content_type='application/json')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['message'] == 'User info saved'
        assert json_data['user']['name'] == 'John Doe'
        assert json_data['user']['age'] == 25
        assert 'bmi' in json_data['user']
    
    def test_save_user_info_bmi_calculation(self, client, init_session):
        """Test BMI calculation"""
        user_data = {
            'name': 'Jane Doe',
            'age': 30,
            'weight': 60,
            'height': 160
        }
        response = client.post('/api/user',
                              json=user_data,
                              content_type='application/json')
        assert response.status_code == 200
        json_data = response.get_json()
        
        # BMI = weight(kg) / (height(m))^2
        # BMI = 60 / (1.6)^2 = 60 / 2.56 = 23.44
        expected_bmi = round(60 / ((160/100) ** 2), 2)
        assert json_data['user']['bmi'] == expected_bmi
    
    def test_save_user_info_missing_fields(self, client, init_session):
        """Test saving user info with missing fields"""
        user_data = {
            'name': 'John Doe',
            'age': 25
            # Missing weight and height
        }
        response = client.post('/api/user',
                              json=user_data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_save_user_info_invalid_age(self, client, init_session):
        """Test saving user info with invalid age"""
        user_data = {
            'name': 'John Doe',
            'age': -5,
            'weight': 70,
            'height': 175
        }
        response = client.post('/api/user',
                              json=user_data,
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_get_user_info_after_saving(self, client, init_session):
        """Test getting user info after saving"""
        user_data = {
            'name': 'John Doe',
            'age': 25,
            'weight': 70,
            'height': 175
        }
        # Save user info
        client.post('/api/user',
                   json=user_data,
                   content_type='application/json')
        
        # Get user info
        response = client.get('/api/user')
        assert response.status_code == 200
        json_data = response.get_json()
        assert json_data['name'] == 'John Doe'
        assert json_data['age'] == 25

class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_complete_workout_flow(self, client, init_session):
        """Test complete workflow: save user, add workouts, get summary"""
        # 1. Save user info
        user_data = {
            'name': 'Test User',
            'age': 28,
            'weight': 75,
            'height': 180
        }
        user_response = client.post('/api/user',
                                   json=user_data,
                                   content_type='application/json')
        assert user_response.status_code == 200
        
        # 2. Add multiple workouts
        workouts = [
            {'workout': 'Warm-up Jog', 'duration': 10},
            {'workout': 'Push-ups', 'duration': 15},
            {'workout': 'Squats', 'duration': 20},
            {'workout': 'Cool-down Stretch', 'duration': 5}
        ]
        
        for workout in workouts:
            response = client.post('/api/workouts',
                                 json=workout,
                                 content_type='application/json')
            assert response.status_code == 201
        
        # 3. Get summary
        summary_response = client.get('/api/workouts/summary')
        assert summary_response.status_code == 200
        summary_data = summary_response.get_json()
        assert summary_data['total_workouts'] == 4
        assert summary_data['total_duration'] == 50
        
        # 4. Verify user info still exists
        user_get_response = client.get('/api/user')
        assert user_get_response.status_code == 200
        user_get_data = user_get_response.get_json()
        assert user_get_data['name'] == 'Test User'

if __name__ == '__main__':
    pytest.main([__file__, '-v'])