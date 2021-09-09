from flask import Flask
import json

app = Flask(__name__)

#app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
#app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
#app.config['MYSQL_PASSWORD'] = os.environ['MYSQL_PASSWORD']
#app.config['MYSQL_DB'] = os.environ['MYSQL_DB']

@app.route("/health")
def healthCheck():
    return json.dumps({"message": "is ok"})


app.run(host='0.0.0.0', debug=True, port=5000)