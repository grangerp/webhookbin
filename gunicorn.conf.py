import os

workers = os.environ["WORKERS"]
bind = f":{os.environ['PORT']}"
accesslog = "-"
errorlog = "-"
