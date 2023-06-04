from flask import Flask,render_template,request
import pymongo

app=Flask(__name__)
client=pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db=client['users']
coll=db['data']
@app.route('/', methods=["GET","POST"])
def home():
    if request.method=="POST":
        global name,email,degree,university,yrs,skills,exp
        name=request.form.get("name")
        email=request.form.get("email")
        degree=request.form.get("degree")
        university=request.form.get("university")
        yrs=request.form.get("yrs")
        exp=request.form.get("exp")
        skills=request.form.getlist("options")
        data={"name":name,"email":email,"education":{"degree":degree,"university":university,"yrs":yrs},"skills":skills}
       # coll.insert_one(data)
        print(f"name :{name} and skills :{skills}")
    
    return render_template("index.html")

@app.route("/print")
def result():
    '''alldata=coll.find({"name":name})
    for data in alldata:
        return render_template("result.html",data=data)'''
    return render_template("result.html", name=name)#name=name,email=email,degree=degree,university=university,exp=exp,skills=skills,result=result)

if __name__=="__main__":
    app.run(debug=True)