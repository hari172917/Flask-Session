from flask import Flask,render_template,request,session,redirect,url_for
app=Flask(__name__)
app.secret_key="harikrishnan"
@app.route("/")
def index():
    user_data=session.get('user_data',{})
    return render_template('indexs.html',user_data=user_data)

@app.route("/set_data",methods=["POST","GET"])
def set():
    if request.method=="POST":
        key=request.form.get("key")
        value=request.form.get("value")
        if 'user_data' not in session:
            session['user_data']={}
        session['user_data'][key]=value
        return redirect(url_for("index"))
    return render_template("set_data.html")


@app.route("/clear_data")
def clear():
    if session:
        session.pop('user_data',None)
    return redirect(url_for("index"))

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
        