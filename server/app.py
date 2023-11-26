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




if __name__ == '__main__':
    app.run(port=5555)