from flask import Flask

app = Flask(__name__)

@app.route("/news/2025/tinubu-ban-on-pepper")

def index(): 
	return render_template("index.html")
	
#if __name__ == "__main__": 
#	app.run()