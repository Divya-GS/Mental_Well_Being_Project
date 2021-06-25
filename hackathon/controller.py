from flask import *   
from flask_mail import *
from random import *
from model.model import First  
app = Flask(__name__) #creating the Flask class object  
app.secret_key="div"

@app.route('/',methods=["POST","GET"])
def Home():
    f=First()
    if request.method=="GET":
        return render_template('home.html')

@app.route('/login',methods=["POST","GET"])
def Login():
    f=First()
    if request.method=="GET":
        return render_template('login.html')
    if request.method=="POST":
        email=request.form["Email"]
        password=request.form["Password"]
        out=f.get_email_user(email)
        if out:
            if out['Password']==password:
                return render_template("home.html",name=out['User_name'],userid=out['UserID'])            
            else:
                flash("Password is wrong.Please enter correct password")
                return render_template("login.html",email=out['Email'])
        else:
            flash("Email you have entered has not been registered. Please register")
            return render_template("login.html")

@app.route('/register',methods=["POST","GET"])
def Register():
    f=First()
    if request.method=="GET":
        return render_template('register.html')
    if request.method=="POST":
            data={
                'User_name':request.form['User_name'],
                'Email':request.form['Email'],
                'Password':request.form['Password'],
            }
            out=f.insert_info_user(data)
            flash("You've been registered successfully!")
            return render_template("home.html")


@app.route('/find',methods=["POST","GET"])
def Find():
    f=First()
    if request.method=="GET":
        return render_template('booking.html')
    if request.method=="POST":
        Area=request.form['Area']
        Gender=request.form['Gender']
        Mode=request.form['Mode']
        Fees=request.form['Fees']
        
        out=f.get_info_therapist(Gender,Area,Mode,Fees)
        
        return render_template("booking.html",out=out)

@app.route('/booking_direct/<area>',methods=["POST","GET"])
def Booking_direct(area):
    f=First()
    if request.method=="GET":
        return render_template('booking.html',area=area)


@app.route('/self_assess',methods=["POST","GET"])
def Self_assess():
    f=First()
    if request.method=="GET":
        return render_template('self_assessment.html')

@app.route('/depression',methods=["POST","GET"])
def Depression():
    f=First()
    if request.method=="GET":
        return render_template('depression.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Depression")


            


@app.route('/ocd',methods=["POST","GET"])
def Ocd():
    f=First()
    if request.method=="GET":
        return render_template('ocd.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="OCD")

    

@app.route('/relationship',methods=["POST","GET"])
def Relationship():
    f=First()
    if request.method=="GET":
        return render_template('relationship.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Relationship")



@app.route('/bipolar_disorder',methods=["POST","GET"])
def Bipolar_disorder():
    f=First()
    if request.method=="GET":
        return render_template('bipolar_disorder.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Bipolar Disorder")


@app.route('/sleep',methods=["POST","GET"])
def Sleep():
    f=First()
    if request.method=="GET":
        return render_template('sleep.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Sleep")



@app.route('/anxiety',methods=["POST","GET"])
def Anxiety():
    f=First()
    if request.method=="GET":
        return render_template('anxiety.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Anxiety")



@app.route('/addiction',methods=["POST","GET"])
def Addiction():
    f=First()
    if request.method=="GET":
        return render_template('addiction.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Addiction")

    

@app.route('/grief_and_loss',methods=["POST","GET"])
def Grief_and_loss():
    f=First()
    if request.method=="GET":
        return render_template('grief_and_loss.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score,area="Grief and Loss")



@app.route('/frontline_workers',methods=["POST","GET"])
def Frontline_workers():
    f=First()
    if request.method=="GET":
        return render_template('frontline_workers.html')
    if request.method=="POST":
        ans=[]
        score=0 
             
        ans.append(request.form['example1'])
        ans.append(request.form['example2'])
        ans.append(request.form['example3'])
        ans.append(request.form['example4'])
        ans.append(request.form['example5'])
        for i in range(0,5):
            if(ans[i]=='Never'):score+=36
            elif(ans[i]=='Sometimes'):score+=27
            elif(ans[i]=='Fairly Often'):score+=18
            else:score+=9
        print(score)
        return render_template('score.html',score=score)



if __name__ =='__main__':  
    app.run(debug = True) 