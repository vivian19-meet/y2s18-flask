from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home_page():
    fav=["noam","shelly","daria","marah","viva","leen"]
    return render_template("index.html",fav=fav,likes_same_sport=True)
if __name__ == '__main__':
    app.run(debug = True)
