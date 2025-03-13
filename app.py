from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Koyeb'


if __name__ == "__main__":
    while True:
        try:
            print("🚀 Starting Flask application...")
            app.run(host="0.0.0.0", port=5000)  # Adjust host and port as needed
        except Exception as e:
            print(f"⚠️ Flask application crashed: {e}")
            print("🔄 Restarting the application in 5 seconds...")
            time.sleep(5)  # Wait for 5 seconds before restarting
