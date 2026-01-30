from website import create_app
import os
app = create_app()

print("-----", __name__)

if __name__== "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
