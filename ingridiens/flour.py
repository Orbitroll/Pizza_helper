from flask import Flask , request, jsonify, Blueprint
flour_bp = Blueprint('flour', __name__)

flours = [("caputo nuvola " , "Type 0") ,
          ("caputo pizzeria " , "Type 00") 
        ]



@flour_bp.route('/', methods=['GET'])
def get_flours():
    return jsonify([{"name": name, "type": type_} for name, type_ in flours])
