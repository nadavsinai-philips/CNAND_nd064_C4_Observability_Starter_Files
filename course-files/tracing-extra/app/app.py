import os
import time
import requests

from flask import Flask, jsonify

import logging
from jaeger_client import Config
from flask_opentracing import FlaskTracing

import redis
import redis_opentracing

app = Flask(__name__)

rdb = redis.Redis(host="redis-primary.default.svc.cluster.local", port=6379, db=0)


def init_tracer(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    config = Config(
        config={"sampler": {"type": "const", "param": 1,}, "logging": True,
        'reporter_batch_size': 1,},
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()



jagertracer = init_tracer("test-service")
tracer = FlaskTracing(jagertracer,True,app)
redis_opentracing.init_tracing(tracer, trace_all_classes=False)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/alpha")
def alpha():
<<<<<<< .merge_file_dIRsXu
    with tracer.start_span("alpha") as span:
      span.set_tag('http.method',"GET")
      for i in range(100):
        do_heavy_work()  # removed the colon here since it caused a syntax error - not sure about its purpose?
      return "This is the Alpha Endpoint!"

@app.route("/beta")
def beta():
<<<<<<< .merge_file_dIRsXu
    with tracer.start_span("beta") as span:
        span.set_tag('http.method',"GET")
=======
>>>>>>> .merge_file_R9kS1p
        r = requests.get("https://www.google.com/search?q=python")
        dict = {}
        for key, value in r.headers.items():
            print(key, ":", value)
            dict.update({key: value})
        return jsonify(dict)

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
