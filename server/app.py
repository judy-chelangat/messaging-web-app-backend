from flask import Flask, jsonify, make_response,request
from flask_migrate import Migrate
from flask_cors import CORS


from models import db, Message

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/messages',methods=['GET','POST'])
def messages():
    
    if request.method == 'GET':
        messages=Message.query.order_by(Message.created_at.asc()).all()
        all_messages=[]

        for message in messages:
            message_dict=message.to_dict()
            all_messages.append(message_dict)

        response =make_response(jsonify(all_messages),200)
        return response
    
    elif request.method == 'POST':
        data=request.get_json()
        message = Message(body=data['body'], username=data['username'])
        db.session.add(message)
        db.session.commit()

        response = make_response(
            jsonify(message.to_dict()),
            201
        )

    return response
    
@app.route('/messages/<int:id>', methods=['PATCH', 'DELETE'])
def messages_by_id(id):
    message = Message.query.filter(Message.id == id).first()

    if request.method == 'PATCH':
        if message is None:
            response = make_response(
                jsonify({"error": "Message not found"}),
                404
            )
            return response

        data = request.get_json()
        for attr in data:
            setattr(message, attr, data.get(attr))

        db.session.add(message)
        db.session.commit()

        message_dict = message.to_dict()
        response = make_response(jsonify(message_dict), 200)
        return response

    elif request.method == 'DELETE':
        if message is None:
            response = make_response(
                jsonify({"error": "Message not found"}),
                404
            )
            return response

        # Retrieve the message object before deleting it
        message = db.session.get(Message, id)

        # Delete the message
        db.session.delete(message)
        db.session.commit()

        response = make_response(
            jsonify({"message": "Message deleted successfully"}),
            200
        )

        return response

if __name__ == '__main__':
    app.run(port=5555)