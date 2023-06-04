from flask import Flask,render_template,request,redirect
app=Flask(__name__)
@app.route('/', methods=["GET","POST"])
def home():
    if request.method=="POST":
        global name,email,degree,university,yrs,skills,exp,phno
        name=request.form.get("name")
        email=request.form.get("email")
        degree=request.form.get("degree")
        university=request.form.get("university")
        yrs=request.form.get("yrs")
        exp=request.form.get("exp")
        skills=request.form.getlist("options")
        phno=request.form.get("phno")
        print("number is :",phno)
        doption=request.form.get("downopts")
        print("your yemp >" , doption)
        if(doption=="simple"):
            return redirect('/simple')
        if(doption=="creative"):
            return redirect('/creative')
        if(doption=="pro"):
            return redirect('/professional')
    return render_template("index.html")

@app.route('/simple')
def simple():
    return render_template("resume1.html",name=name,email=email,degree=degree,yrs=yrs,university=university,exp=exp,skills=skills,phno=phno)

@app.route('/creative')
def creative():
    return render_template("creative.html",name=name,email=email,degree=degree,yrs=yrs,university=university,exp=exp,skills=skills,phno=phno)

@app.route('/professional')
def pro():
    return render_template("resume2.html",name=name,email=email,degree=degree,yrs=yrs,university=university,exp=exp,skills=skills,phno=phno)


if __name__=="__main__":
    app.run(debug=True)