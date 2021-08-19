from flash import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATANASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class videomodel(db.model):
    id = db.columm(db.integer, primary_key=True)
    name = db.column(db.String(100), nullable=False)
    views = db.column(db,Integer, nullable=False)
    likes = db.column(db,Integer, nullable=False)

    def __repr__(self):
        return f"video(name= {name}, views= {views}, likes= {likes})

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("name", type=int, help="views of the video")

resource_fields = {
    'id' : fields.integer,
    'name' : fields string,
    'views' :fields.integer,
}

class video(Resource):
    def get(self, video_id, ):
        Result = videomode.query.get(id=video_id)
        return Result

    def put(self, video_id):
            args = video_put_args.parse_args()
            video[video_id] = args
            return video[video_id], 201

    def delete(self, video_id):
        abort_if_video_id_doesnt_exists(video_id)
        del video[video_id]
        return '', 204  

api.add_resource(Video, "/video/<int:video_it>")

if __name__ == "__main__":
    app.run(debug=True)
