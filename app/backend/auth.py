from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    # Fix: Use default hash method (pbkdf2:sha256)
    hashed_password = generate_password_hash(password)
    
    # Auto-admin for specific username or if it's the first user (optional, here just checking username)
    is_admin = (username.lower() == 'admin')
    
    new_user = User(username=username, password=hashed_password, is_admin=is_admin)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid credentials'}), 401

    login_user(user)
    return jsonify({
        'message': 'Logged in successfully', 
        'username': user.username,
        'id': user.id,
        'is_admin': getattr(user, 'is_admin', False)
    })

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({
            'username': current_user.username, 
            'id': current_user.id,
            'is_admin': getattr(current_user, 'is_admin', False)
        })
    return jsonify({'error': 'Not logged in'}), 401

@auth_bp.route('/admin/data', methods=['GET'])
@login_required
def get_admin_data():
    if not getattr(current_user, 'is_admin', False):
        return jsonify({'error': 'Unauthorized'}), 403
    
    users = User.query.all()
    result = []
    for user in users:
        user_history = []
        for h in user.history:
            user_history.append({
                'recipe_name': h.recipe_name,
                'date': h.date.isoformat(),
                'details': h.details
            })
        result.append({
            'id': user.id,
            'username': user.username,
            'history': user_history
        })
    
    return jsonify(result)
