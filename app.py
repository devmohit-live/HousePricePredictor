from flask import Flask,render_template,request
from sklearn.externals import joblib

app = Flask(__name__)
model=joblib.load('.//static//house.pk1')
print(model)
global price
price=0
cpincome,cpage,cprooms,cpbedrooms,cppopulation='','','','',''
@app.route('/', methods=['GET','POST'])
def index(price=0):
    if request.method == 'POST':

        income = float(request.form['income']) / 100000
        cpincome=str(income*100000)
        age = float(request.form['age']) / 100000
        cpage=str(age*100000)
        rooms = float(request.form['rooms']) / 100000
        cprooms=str(rooms*100000)
        bedrooms =float( request.form['bedrooms']) / 100000
        cpbedrooms=str(bedrooms*100000)
        population = float(request.form['population'])
        cppopulation=population
        # [[1.000, 2.3122, 6.45235, 3.25, 43828.947207]]
        print()
        price = model.predict([[income, age, rooms, bedrooms, population]])
        print(price)
        price = price[0]
        price=round(price,2)
        print(price)
        return render_template('res.html', price=price, cpincome=cpincome,cpage=cpage,cprooms=cprooms,cpbedrooms=cpbedrooms,cppopulation=cppopulation)
    return render_template('index.html')



# @app.route('/ <float:income>/<float:age>/<float:rooms>/<float:bedrooms>/<float:population>/<float:price>', methods=['GET', 'POST'])
# def index(income=0, age=0, rooms=0, bedrooms=0, population=0, price=0):
#     if request.method == 'POST':
#         income=request.form['income']/100000,
#         age=request.form['age']/100000
#         rooms=request.form['rooms']/100000
#         bedrooms=request.form['bedrooms']/100000
#         population=request.form['population']/100000
#         price=model.predict([[income, age, rooms, bedrooms, population]])
#         global price
#         price=price[0]*1000000
#         return render_template('res.html', price=price)
#     if request.method == 'GET':
#         return render_template("index.html",price=price)

#'Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       # 'Avg. Area Number of Bedrooms', 'Area Population'

if __name__ == '__main__':
    app.run()
