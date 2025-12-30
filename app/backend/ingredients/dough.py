import json
from flask import Blueprint, jsonify, request
from classes.dough import DoughStarters

dough_bp = Blueprint('dough', __name__)

@dough_bp.route("/starter", methods=["GET"])
def calc_starter():
    starter_type = request.args.get("type", "biga")
    total_flour = float(request.args.get("total_flour", 1000))
    preferment_pct = float(request.args.get("preferment_flour_pct", 0.4))

    if starter_type == "biga":
        starter = DoughStarters.biga()
    elif starter_type == "poolish":
        starter = DoughStarters.poolish()
    elif starter_type == "levain":
        starter = DoughStarters.levain()
    else:
        return jsonify({"error": "invalid starter type"}), 400

    result = starter.to_weights_json(
        total_flour_g=total_flour,
        preferment_flour_pct=preferment_pct
    )

    if isinstance(result, str):
        result = json.loads(result)

    return jsonify(result)

@dough_bp.route("/calculate_yeast", methods=["GET"])
def calculate_yeast():
    try:
        hours = float(request.args.get("hours", 24))
        temperature = float(request.args.get("temperature", 20))
        
        
        yeast_pct = 150 / (hours * (temperature ** 1.5))
        
        return jsonify({
            "hours": hours,
            "temperature": temperature,
            "yeast_percentage": round(yeast_pct, 4),
            "note": "Calculated for Instant Dry Yeast (IDY)"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400
