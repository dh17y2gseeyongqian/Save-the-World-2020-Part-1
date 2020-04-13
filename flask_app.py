from flask import Flask, render_template, request

app = Flask(__name__, template_folder='/home/Hazhax/mysite/templates/')


@app.route('/', methods =["GET", "POST"])
def main_page():
    if request.method == "GET":
      return render_template('index.html')
    else:
       number = request.form.get('number')

       food = request.form.get('food')

       if food in ["Tofu Soup", "Vegetable Dumplings", "Udon"]:
           health = "Less than 400 calories. Not bad. Keep it up!"
       elif food in ["Teriyaki Don", "Cai Fan"]:
           health = "Between 400 and 500 calories. Still okay, but eat these foods in moderation."
       elif food in ["Spaghetti with Meat Sauce", "Chicken Rice", "Roasted Duck Rice", "Fried Rice", "Fish and Chips"]:
           health = "More than 500 calories. That's a bit too heavy, no? Try having a lighter meal later."
       elif food == "Pizza":
           health = "Meme"
       else:
           health = "You think you funny isit. Answer with the food item in the table above."

       if food in ["Tofu Soup", "Vegetable Dumplings", "Udon"]:
           calorie = " <400 calories"
       elif food in ["Teriyaki Don", "Cai Fan"]:
           calorie = " 400-500 calories"
       elif food in ["Spaghetti with Meat Sauce", "Chicken Rice", "Roasted Duck Rice", "Fried Rice", "Fish and Chips"]:
           calorie = " >500 calories"
       else:
           calorie = "You think you funny isit. Answer with the food item in the table above."


       drink= request.form.get('drink')
       if drink in ["Black Coffee", "Warm Soy Bean Milk", "Iced Soy Bean Milk", "Hot Tea"]:
           sugar = "Nice. Sugar content is pretty low. Less than 10g per serving."
       elif drink in ["Hot Milo", "Iced Milo"]:
           sugar = "Hmm. Sugar's between 10-30g. Not bad, but you probably should drink less of it."
       elif drink in ["Fresh Apple Juice", "Fresh Orange Juice"]:
           sugar = "Over 30g of sugar per serving. A bit overboard. You'd probably stay off of the drink for a while."
       elif drink == "Meme":
           sugar = "time"
       else:
           sugar = "Not funny."

       if drink in ["Black Coffee", "Warm Soy Bean Milk", "Iced Soy Bean Milk", "Hot Tea"]:
           level = " <10g"
       elif drink in ["Hot Milo", "Iced Milo"]:
           level = "10-30g"
       elif drink in ["Fresh Apple Juice", "Fresh Orange Juice"]:
           level = " >30g"
       else:
           level = "Not funny."

       fruit= request.form.get('fruit')
       if fruit ==  "Without fruit":
           message = "Eh can be more healthy or not. Fruit is free leh"
       else:
           message = "Nice. At least your diet got a bit balance"

       if health == "Meme" and sugar == "time":
           return render_template('meme.html')
       elif health == "You think you funny isit. Answer with the food item in the table above." and sugar == "Not funny.":
           invalid = "Invalid Input."
           return render_template('index.html', invalid = invalid)
       else:
           fout = open("info[2].txt", "a")
           fout.write("Stall " + number + ", " + food + ", " + calorie + ", " + drink + ", " + level + ", " + fruit + "\n") # \n not /n
           fout.close
           return render_template('index.html', number = number, food = food, health = health, drink = drink, sugar = sugar, fruit = fruit, message = message)



@app.route('/view', methods =["GET", "POST"])
def view():
    if request.method == "GET":
        return render_template('index.html')
    else:
       fin = open("info[2].txt", "r")
       lines = fin.readlines()
       fin.close()
       return render_template('index.html', lines = lines)

