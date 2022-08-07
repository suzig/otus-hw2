from app import app
from app.models import Users
from flask import request,jsonify
#import requests
from prometheus_flask_exporter import PrometheusMetrics

metrics = PrometheusMetrics(app)
# static information as metric
metrics.info('app_info', 'Application info', version='1.0.0')

by_path_counter = metrics.counter(
    'by_path_counter', 'Request count by request paths',
    labels={'path': lambda: request.path}
)


@app.route('/get_users', methods=['GET'])
@by_path_counter
def get_users():
    id = request.get_json()['id']
    user = Users.query.filter(Users.id == id).first()
    user_all_atr = [user.id, user.fullname, user.username]
    print (user_all_atr)
    return jsonify(user_all_atr), 200

@app.route('/create_users', methods=['POST'])
@by_path_counter
def create_users():
    if request.method == 'POST':
        user = Users()
        user.update(**{
            "username": request.get_json()["username"],
            "fullname": request.get_json()["fullname"]})
        user.save_to_db()
        return "<p>User created</p>", 200

@app.route('/update_users', methods=['PUT'])
@by_path_counter
def update_users():
    id = request.get_json()['id']
    payload = request.get_json()['payload']
    user = Users.query.filter(Users.id == id).first()
    user.update(**payload)

    user.save_to_db()
    return "<p>User updated</p>", 200

@app.route('/delete_users', methods=['DELETE'])
@by_path_counter
def delete_users():
    id = request.get_json()['id']
    user = Users.query.filter(Users.id == id).first()
    print(user.id)
    user.delete()
    return "<p>User deleted</p>", 200