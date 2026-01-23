from flask import Flask, render_template

#website obj
#is like the main frame/source
#means only when executed directly it opens
app = Flask(__name__)

#connects html page to obj
#when some one choose home this will route it or load the html page
#"home" can be any path
#has been changed to "/" to make it defualt pg
@app.route("/")
def home():
    return render_template("home.html")

#must always create "templates" folder to use render_template
#and must be in same directory

#when someone types this "api/....." the <station> and date are variables that can be interacted with
#they become args for the function which can be accessed.
#func returns dic.
@app.route("api/v1/<station>/<date>")
def about(station,date):
    temp = 23
    return {
        "station": station,
        "date": date,
        "temperature": temp
    }


#means only when executed directly it opens
if __name__ == "__main__":
    #shows error on website + auto refresh
    app.run(debug=True)