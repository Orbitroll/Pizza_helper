from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from models import db, History

history_bp = Blueprint('history', __name__)

@history_bp.route('/', methods=['GET'])
@login_required
def get_history():
    history_items = History.query.filter_by(user_id=current_user.id).order_by(History.date.desc()).all()
    output = []
    for item in history_items:
        output.append({
            'id': item.id,
            'recipe_name': item.recipe_name,
            'date': item.date.isoformat(),
            'details': item.details
        })
    return jsonify(output)

@history_bp.route('/add', methods=['POST'])
@login_required
def add_history():
    data = request.get_json()
    recipe_name = data.get('recipe_name')
    details = data.get('details')

    if not recipe_name or not details:
        return jsonify({'error': 'Missing data'}), 400

    new_item = History(user_id=current_user.id, recipe_name=recipe_name, details=details)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({'message': 'History saved'})
