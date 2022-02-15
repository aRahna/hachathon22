from flask import Flask, render_template, request
import pandas as pd
import modules

app = Flask(__name__)
data = pd.read_csv('ingredients_from_eda.ru.csv')
data['recipe_id'] = data['name'].apply(lambda x: int(x.split('-')[-1]))

def find1(ingr):
    my_ingredients = ingr
    x = modules.search_by_ingredients(set(my_ingredients), data)
    print(x)
    return res("res.html", x)

def find2(dish):
    return "done"

@app.route('/', methods=['POST', 'GET'])
def f_b_i():
    if request.method == "POST":
        f = request.form['ing']
        f = f.split(",")
        find1(f)
    return render_template("find_by_ingr.html")

@app.route('/find_by_dish', methods=['POST', 'GET'])
def f_b_d():
    if request.method == "POST":
        f = request.form['dish']
        print(f)
    return render_template("find_by_dish.html")

@app.route("/res")
def res(page, x):
    return render_template("res.html", x)

if __name__ == "__main__":
    app.run(debug=True)


