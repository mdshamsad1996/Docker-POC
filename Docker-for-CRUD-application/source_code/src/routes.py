from src import app
from flask import jsonify,request
from src.Models.modules import Database

db = Database()

@app.route("/")
def hello():
    return "Hello World"
@app.route('/getStudents',methods=['GET'])
def getStudents():
    return jsonify({'student':db.read()})

@app.route('/getStudent/<int:id>', methods= ['GET'])
def getstudent(id):
    return jsonify({'student': db.read_one_record(id)})

@app.route('/insert_record',methods=['POST'])
def post_record():
    details = request.data
    return jsonify({'message': db.insert(details)})

@app.route('/update/<int:id>',methods=['PUT'])
def update_record(id):
    details = request.data
    return jsonify({'message': db.update(id,details)})

@app.route('/delete/<int:id>', methods = ['DELETE'])
def delete_record(id):
    return jsonify({'message': db.delete(id)})