from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", row=8, col=8)


@app.route('/<int:row>')
def show_rows(row):
    return render_template("index.html",row=row,col=8)

@app.route('/<int:row>/<int:col>')
def show_rows_columns(row, col):
    return render_template("index.html",row=row,col=col)

@app.route('/<int:row>/<int:col>/<string:color1>/<string:color2>')
def color_rows_columns(row, col, color1, color2):
    return render_template("index.html",row=row,col=col,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True, port=5001)