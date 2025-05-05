import taipy.gui.builder as tgb
from taipy.gui import Gui
import plotly.express as px

slider_value = 20
selected_fruit = "avocado"

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
   






if __name__ == "__main__":
    Gui(page).run(dark_mode=False, use_reloader=True, port=8080)

