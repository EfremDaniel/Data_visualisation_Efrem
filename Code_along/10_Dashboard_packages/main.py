import taipy.gui.builder as tgb
from taipy.gui import Gui
from utils.constant import DATA_DIRECTORY
from frontend.chart import create_municipality_bar
import pandas as pd

# Läs in Excel-data
df = pd.read_excel(
    DATA_DIRECTORY / "resultat-ansokningsomgang-2024.xlsx",
    sheet_name="Tabell 3",
    skiprows=5,
)

# Funktion för att filtrera på utbildningsområde och summera per kommun
def filter_df_municipality(df, educational_area="Data/IT"):
    return (
        df.query("Utbildningsområde == @educational_area")["Kommun"]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "Kommun", "count": "Ansökta utbildningar"})
    )

# Funktion som körs vid filterändringar
def filter_data(state):
    df_municipality = filter_df_municipality(
        state.df, educational_area=state.selected_educational_area
    )
    
    if df_municipality.empty:
        state.municipality_chart = None
        state.municipalities_title = "Inga data"
    else:
        state.municipality_chart = create_municipality_bar(
            df_municipality.head(state.number_municipalities),
            ylabel="KOMMUN",
            xlabel="# ANSÖKTA UTBILDNINGAR",
        )
        state.municipalities_title = state.number_municipalities
    
    state.educational_area_title = state.selected_educational_area

# Initiera grunddata och tillståndsvariabler
df_municipality = filter_df_municipality(df)

municipality_chart = create_municipality_bar(
    df_municipality.head(), ylabel="KOMMUN", xlabel="# ANSÖKTA UTBILDNINGAR"
)

number_municipalities = 5
municipalities_title = number_municipalities
selected_educational_area = "Data/IT"
educational_area_title = selected_educational_area

# Bygg GUI
with tgb.Page() as page1:
    with tgb.part(class_name="container card stack-large"):
        # Rubrik
        with tgb.part(class_name="card"):
            tgb.text("# MYH dashboard 2024", mode="md")
            tgb.text(
                "En dashboard för att visa statistik och information om ansökningsomgång 2024",
                mode="md",
            )

        # Layout med diagram och filter
        with tgb.layout(columns="2 1"):
            with tgb.part(class_name="card"):
                tgb.text(
                    "## Antalet ansökta YH utbildningar per kommun (topp {municipalities_title}) för {educational_area_title}",
                    class_name="title-chart",
                    mode="md",
                )
                tgb.chart(figure="{municipality_chart}")

            with tgb.part(class_name="card left-margin-md"):
                tgb.text("## Inställningar", mode="md")

                # Filtrering
                tgb.text("Filtrera antalet kommuner", mode="md")
                tgb.slider(
                    value="{number_municipalities}",
                    min=5,
                    max=len(df_municipality),
                    continuous=False,
                    on_change=filter_data
                )

                tgb.text("Välj utbildningsområde", mode="md")
                tgb.selector(
                    value="{selected_educational_area}",
                    lov=df["Utbildningsområde"].unique(),
                    dropdown=True,
                    on_change=filter_data
                )

        # Tabell med rådata
        with tgb.part(class_name="card"):
            tgb.text("### Rådata", mode="md")
            tgb.table("{df}")

# Kör GUI
Gui(page1, css_file="assets/main.css").run(
    dark_mode=False,
    use_reloader=True,
    port=8080
)