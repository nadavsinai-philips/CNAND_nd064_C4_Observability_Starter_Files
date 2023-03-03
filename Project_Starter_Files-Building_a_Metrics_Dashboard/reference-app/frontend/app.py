from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from flask_opentracing import FlaskTracing

app = Flask(__name__)
metrics = PrometheusMetrics(app)
config = Config(config={'sampler': {'type': 'const', 'param': 1},
                                'logging': True, 'service_name':"frontend"})
                        # Service name can be arbitrary string describing this particular web service.
                       
jaeger_tracer = config.initialize_tracer()
tracing = FlaskTracing(jaeger_tracer)

@tracing.trace()
@app.route("/")
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
