from flask import Flask, render_template, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
from flask_pymongo import PyMongo
from jaeger_client import Config
from flask_opentracing import FlaskTracing

app = Flask(__name__)
config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True, 
                                'service_name':"backend"})
                        # Also, provide a hostname of Jaeger instance to send traces to.
                        # Service name can be arbitrary string describing this particular web service.
                     
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer)

app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)
metrics = PrometheusMetrics(app)
@tracing.trace() 
@app.route("/")
def homepage():
    return "Hello World"

@tracing.trace() 
@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)

@tracing.trace() 
@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
