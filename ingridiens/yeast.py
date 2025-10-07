from flask import Flask , request, jsonify, Blueprint

yeast_bp = Blueprint('yeast', __name__)

yeasts = [("saf-instant", "Instant Yeast"),
          ("fleichmanns", "Active Dry Yeast")
         ]

@yeast_bp.route('/', methods=['GET'] )
def get_yeasts():
    return jsonify([{"name": name, "type": type_} for name, type_ in yeasts]), 200
