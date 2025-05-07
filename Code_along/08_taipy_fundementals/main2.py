import taipy.gui.builder as tgb
from taipy.gui import Gui
import plotly.express as px


slider_value = 20
selected_fruit = "avocado"
number1 = 5
number2 = 10
sum_ = number1 + number2
product = number1 * number2
quotient = number1 / number2
difference = number1 - number2

def perform_calculator():
    state.sum_ = int(state.number1) + int(state.number2)
    state.product = int(state.number1) * int(state.number2)
    state.difference = int(state.number1) - int(state.number2)
    state.quotient = int(state.number1) / int(state.number2)


with tgb.Page() as page:
    tgb.text("# Hello there taipy", mode="md")
    tgb.text("Welcome to the world of reactive programming")
    
    # binds to slinder_value variable and makes it dynamic
    tgb.slider(value="{slider_value}", min= 1, max= 50, step= 1)
    tgb.text("Slider value is at {slider_value}")

    tgb.text("Select your favorite fruit", mode="md")
    tgb.selector(
        value="{selected_fruit}", 
        lov=["avocado","apple", "pear", "tomato", "banana"],
        dropdown=True
        )
    
    tgb.text("Yummy **{selected_fruit}**", mode="md")
    tgb.image("assets/{selected_fruit}.jpg")


    tgb.text("Coolu calculator", mode="md")
    tgb.text("Type in number")
    tgb.input("{number1}")

    tgb.text("Type in another number")
    tgb.input("{number2}")

    tgb.text("You have typed {number1} and {number2}")
    tgb.button(label="CALCULATOR", class_name="plain", on_action=perform_calculator)

   






if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)

