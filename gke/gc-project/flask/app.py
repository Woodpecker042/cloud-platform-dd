# Ref. https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service#writing

import os, time
import logging

from flask import Flask
from ddtrace import patch, tracer, config, auto

app = Flask(__name__)

# Log trace correlation
# ref. https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/python/
#logging.basicConfig(filename='/mnt/shared-gcs/logs/flask_error.log', level=logging.ERROR)
FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(filename='/mnt/shared-gcs/logs/flask_error.log', level=logging.INFO,format=FORMAT)
log = logging.getLogger(__name__)


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    logging.error("Hello World triggered.")

    #return f"Hello {name}!"

    output =f"Hello {name}!"
    if os.environ.get("MY_LOG_LEVEL") == "SYSTEM":
        log_env_info()

    output += f"<br>{os.popen('which python').read()}"
    output += f"<br>{os.popen('ls -l /mnt/shared-gcs/logs').read()}"
    output += f"<br>{os.popen('which flask').read()}"
    output += f"<br>{os.popen('ls -l /usr/local/bin').read()}"
    #return f"Hello {name}!<br>{os.system("which python")}"
    return output

@tracer.wrap(service="gcrun-flask", resource="log_env_info")
def log_env_info():
    ps_info = os.popen("ps aux").read()
    log.info(f'ps aux: {ps_info}')
    with open('/mnt/shared-gcs/logs/ps_info.log', 'w') as f:
        f.write(str(ps_info))

@app.route("/man_trace")
def manual_trace():
    span = tracer.trace("sandwich.create", resource="resource_name")
    time.sleep(0.5)
    span.finish()  # remember to finish the span
    log.info("/man_trace triggered.")
    return f"ls -l/layers/google.python.pip/pip/bin/: {os.popen('ls -l /layers/google.python.pip/pip/bin/').read()}"

@app.route("/errlog")
def tail_errlog():
    with open('/mnt/shared-gcs/logs/flask_error.log', 'r') as f:
        return f.read()
    return "No error log found."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))