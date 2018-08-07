from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
	sports = ["football" , "golf" , "basktboll"] 
	return render_template("index.html", sports=sports , like_same_sports=False)

    

if __name__ == '__main__':
   app.run(debug = True)