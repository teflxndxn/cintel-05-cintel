# --------------------------------------------
# Imports at the top - PyShiny EXPRESS VERSION
# --------------------------------------------

from shiny import reactive, render
from shiny.express import ui

import random
from datetime import datetime
from collections import deque
import pandas as pd
import plotly.express as px
from shinywidgets import render_plotly
from scipy import stats

from faicons import icon_svg


# --------------------------------------------
# Constants & Reactive Values
# --------------------------------------------

UPDATE_INTERVAL_SECS: int = 1
DEQUE_SIZE: int = 5
reactive_value_wrapper = reactive.value(deque(maxlen=DEQUE_SIZE))


# --------------------------------------------
# Simulated Live Data via Reactive Calc
# --------------------------------------------

@reactive.calc()
def reactive_calc_combined():
    reactive.invalidate_later(UPDATE_INTERVAL_SECS)

    temp = round(random.uniform(-18, -16), 1)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_dictionary_entry = {"temp": temp, "timestamp": timestamp}

    reactive_value_wrapper.get().append(new_dictionary_entry)

    deque_snapshot = reactive_value_wrapper.get()
    df = pd.DataFrame(deque_snapshot)
    latest_dictionary_entry = new_dictionary_entry

    return deque_snapshot, df, latest_dictionary_entry


# --------------------------------------------
# UI Page Layout
# --------------------------------------------

ui.page_opts(
    title="Blessing's Live Dashboard",
    fillable=True
)

with ui.sidebar(open="open"):

    ui.h2("Live CI Monitor", class_="text-center")
    ui.p(
        "Blessing's real-time demo: temperature readings in Antarctica.",
        class_="text-center"
    )
    ui.hr()
    ui.h6("Links:")
    ui.a("GitHub Source", href="https://github.com/teflxndxn/cintel-05-intel", target="_blank")
    ui.a("GitHub App", href="https://teflxndxn.github.io/cintel-05-intel/", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")


# --------------------------------------------
# Main Layout: Value Box, Time, Data, Chart
# --------------------------------------------

with ui.layout_columns():

    with ui.value_box(
        showcase=icon_svg("sun"),
        theme="bg-gradient-orange-yellow",
    ):
        "Current Temperature"

        @render.text
        def display_temp():
            _, _, latest = reactive_calc_combined()
            return f"{latest['temp']} °C"

        "warmer than usual"

    with ui.card(full_screen=True):
        ui.card_header("Current Date and Time")

        @render.text
        def display_time():
            _, _, latest = reactive_calc_combined()
            return latest['timestamp']


with ui.layout_columns():
    with ui.card():
        ui.card_header("Most Recent Readings")

        @render.data_frame
        def display_df():
            deque_snapshot, df, _ = reactive_calc_combined()
            return df


with ui.layout_columns():
    with ui.card():
        ui.card_header("Temperature Chart with Trend Line")

        @render_plotly
        def display_plot():
            _, df, _ = reactive_calc_combined()

            if not df.empty:
                df["timestamp"] = pd.to_datetime(df["timestamp"])

                fig = px.scatter(
                    df,
                    x="timestamp",
                    y="temp",
                    title="Temperature Readings with Regression Line",
                    labels={"temp": "Temperature (°C)", "timestamp": "Time"},
                    color_discrete_sequence=["orange"]
                )

                # Linear regression for trend line only if enough data points
                if len(df) >= 3:
                    x_vals = list(range(len(df)))
                    y_vals = df["temp"]

                    slope, intercept, _, _, _ = stats.linregress(x_vals, y_vals)
                    df['trend_line'] = [slope * x + intercept for x in x_vals]

                    fig.add_scatter(
                        x=df["timestamp"],
                        y=df['trend_line'],
                        mode='lines',
                        name='Trend Line',
                        line=dict(color='yellow')
                    )

                fig.update_layout(
                    xaxis_title="Time",
                    yaxis_title="Temperature (°C)"
                )

                return fig

            else:
                return None
