from flask import Flask , blueprint , jsonify , request
from classes.dough import PrefermentSpec, DoughStarters

dough_bp = Blueprint('dough', __name__)

if __name__ == "__main__":
    total_flour = 1000
    starter = DoughStarters.biga()  # מחמצת מסוג ביגה
    json_data = starter.to_weights_json(total_flour_g=total_flour, preferment_flour_pct=0.4)
    print(json_data)


