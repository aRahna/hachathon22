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
    return x


def find2(dish):
    print("done")


@app.route('/', methods=['POST', 'GET'])
def f_b_i():
    if request.method == "POST":
        f = request.form['ing']
        f = f.split(",")
        URLS = find1(f)
        print(URLS)
        return render_template("res.html", URLS=URLS)
    else:
        return render_template("find_by_ingr.html")


@app.route('/find_by_dish', methods=['POST', 'GET'])
def f_b_d():
    if request.method == "POST":
        f = request.form['dish']
        print(f)
    return render_template("find_by_dish.html")


@app.route("/res")
def res():
    return render_template("res.html")

if __name__ == "__main__":
    app.run(debug=True)


