from flask import Flask,render_template,request,redirect
from instance import db, StudentModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/create' , methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        try:
            user = StudentModel(
                first_name=request.form["firstname"],
                last_name=request.form["lastname"],
                email=request.form["email"],
                password=request.form["password"],
                gender=request.form["gender"],
                hobbies=request.form["hobbies"],
                country=request.form["country"],
            )
            db.session.add(user)
            db.session.commit()
            success = True
        except Exception as e:
            print(e)
            db.session.rollback()
            success = False

        return render_template('create.html', success=success)

    return render_template('create.html')

@app.route('/read' , methods = ['GET'])
def read():
        try:
            user = StudentModel.query.all()
        except Exception as e:
            print(e)

        return render_template('read.html', datas=user)
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)