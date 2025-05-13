import taipy.gui.builder as tgb
from taipy.gui import Gui
import pandas as pd
import plotly.express as px
from utils.constant import DATA_DIRECTORY


df = pd.read_csv( 
     DATA_DIRECTORY / "nordic_ranking_company.csv"
    )

selected_company = []
selected_industry = []
# selected_metric = []

df_sorted = df.sort_values(by="Revenue (billion $)", ascending=False)
 
fig = px.bar(
    df_sorted.head(8),
    x="Company",
    y="Revenue (billion $)",
    title="Revenue by Company (in Billion $)",
    labels={"Revenue (billion $)": "Revenue (Billion $)"},
    height=600
)


with tgb.Page() as page:
    with tgb.part(class_name="card"):
        tgb.text("# Dashboard", mode="md")
        tgb.text("En dashboard för att visa dem rikaste företagen i Norden", mode="md")

    
    with tgb.layout(columns="1 1 1", class_name="card"):
        with tgb.part(class_name= "text-center"):
            tgb.selector(
                label= "Select Industry",
                value="{selected_industry}",
                lov=df["Industry"].unique(),
                dropdown=True,
            )
            
            with tgb.part(class_name="text-start"):
                tgb.selector(
                label= "Select Company",
                value="{selected_company}",
                lov=df["Company"].unique(),
                dropdown=True,
            )
            
            tgb.button("FILTER DATA", class_name="button-color")
            
            # with tgb.part(class_name="text-end"):
            #     tgb.selector(
            #     label= "Select Company",
            #     value="{selected_metric}",
            #     lov=df["Company"].unique(),
            #     dropdown=True,
            # )
                 
        tgb.chart(figure="{fig}")
        
    with tgb.part(class_name="card"):
        tgb.text("## Raw data", mode="md")
        tgb.table("{df}")

Gui(page, css_file="assets/main.css").run(
    dark_mode=False, use_reloader=True, port=8080)