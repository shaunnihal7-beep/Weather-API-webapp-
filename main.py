from flask import Flask, render_template
import pandas as pd




#website obj
#is like the main frame/source
#means only when executed directly it opens
app = Flask(__name__)

#to display only tabel of stations.
#below line is when you want only those columns
stations = pd.read_csv("data_small/stations.txt",skiprows = 17)
stations = stations[["STAID","STANAME                                 "]]
print(stations)




#connects html page to obj
#when some one choose home this will route it or load the html page
#"home" can be any path
#has been changed to "/" to make it defualt pg

@app.route("/")
def home():
    #.to_html() converts it to html ver of table
    return render_template("home.html",data = stations.to_html())



#must always create "templates" folder to use render_template
#and must be in same directory




#when someone types this "api/....." the <station> and date are variables that can be interacted with
#they become args for the function which can be accessed.
#func returns dic.

@app.route("/api/v1/<station>/<date>")
def about(station,date):

    # these 2 lines opens up the file with particular staion id
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"

    #creating dataframe which lets us acess csv file
    #skiprows coz first lines are unwanted data and our data starts at row 21
    #we use parse date because otherwise it will be treated like string
    # all dates must be used as datetime obj.
    df = pd.read_csv(filename, skiprows=20, parse_dates =["    DATE"] )

    #df.loc lets us acess rows and columns by names not positions
    #df.loc is only for date coz we use row value ONLY there
    # syntax of it -> df.loc[row_label, column_label]
    #.squeeze() basically gives only the value not the dataframe series (returns only value without key andol)
    temp = df.loc[df["    DATE"] == date] ["   TG"].squeeze()/10
    return {
        "station": station,
        "date": date,
        "temperature": temp
    }


#means only when executed directly it opens
if __name__ == "__main__":
    #shows error on website + auto refresh
    #you can only run 2 flask apps simultaneously by makin them have diff ports
    app.run(debug=True,port=5008)