from flask import Flask, render_template, request, redirect
from models import Admin

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def index():
    modelAdmin = Admin()

    if request.method =='POST':
        nama = request.form['username']
        password = request.form['password']
        modelAdmin.setAdmin(nama,password)
        if modelAdmin.cek():
            return redirect(mainform())
        else:
            return render_template('login.html')
        # return 'selamat ' + nama +' dan ' + password
    else:
        return render_template('login.html',modelAdmin=modelAdmin)

@app.route('/Warehouse',methods=['GET','POST'])
def mainform():
    return render_template('Mainform.html')

if __name__ == "__main__":
    app.run(debug=True)