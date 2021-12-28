from argparse import ArgumentParser

from flask import Flask, request, redirect, render_template, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


@app.route("/", methods=['GET'])
def get_trains():
    from trains_db import TrainTable

    TrainList = db.session.query(TrainTable).all()
    return render_template('index.html', Trainlist=TrainList)


@app.route("/register", methods=['POST'])
def register():
    from trains_db import TrainTable

    train_name = request.form.get('train')
    new_train = TrainTable(TrainName=train_name)
    db.session.add(new_train)
    db.session.commit()
    return redirect(url_for('get_trains'))


@app.route("/delete", methods=['POST'])
def delete():
    from trains_db import TrainTable

    train_name = request.form.get('train')
    db.session.query(TrainTable).filter(TrainTable.TrainName == train_name).delete()
    db.session.commit()
    return redirect(url_for('get_trains'))

@app.route("/deleteitem/<string:train_name>")
def delete_item(train_name):
    from trains_db import TrainTable
    
    db.session.query(TrainTable).filter(TrainTable.TrainName == train_name).delete()
    db.session.commit()
    return redirect(url_for('get_trains'))

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port ] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=5000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(host='0.0.0.0', debug=options.debug, port=options.port)
