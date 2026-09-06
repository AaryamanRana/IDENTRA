import sys
from pathlib import Path
import os

# Add root directory to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

try:
    from ui.app import create_app
    app = create_app()
except Exception as e:
    import traceback
    err_trace = traceback.format_exc()
    from flask import Flask, Response
    app = Flask(__name__)
    
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def handle_error(path):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head><title>Deployment Error</title></head>
        <body style="font-family: monospace; padding: 30px; background: #0f172a; color: #f87171;">
          <h2>⚠️ Serverless Startup Error</h2>
          <pre style="background: #1e293b; padding: 20px; border-radius: 8px; color: #fca5a5; overflow-x: auto;">{err_trace}</pre>
        </body>
        </html>
        """
        return Response(html, mimetype="text/html", status=500)

if __name__ == "__main__":
    app.run()
