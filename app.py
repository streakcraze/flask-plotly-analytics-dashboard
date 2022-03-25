from flask import Flask, render_template
import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    return render_template("graph.html")


@app.route('/plotacc')
def plot_acc():
    df = pd.read_csv('./data/imu_data.csv')

    fig = make_subplots()

    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Acc_x"],
        mode="lines",
        name="gx"
    ))
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Acc_y"],
        mode="lines",
        name="gy"
    ))
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Acc_x"],
        mode="lines",
        name="gz"
    ))

    fig.update_layout(title_text="3-Axis Accelerometer")
    fig.update_xaxes(title_text="Time [s]")
    fig.update_yaxes(title_text=f"Acceleration [m/s^2]")

    return plotly.io.to_html(fig)


@app.route('/plotgyro')
def plot_gyro():
    df = pd.read_csv('./data/imu_data.csv')

    fig = make_subplots()

    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Gyro_x"],
        mode="lines",
        name="gx"
    ))
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Gyro_y"],
        mode="lines",
        name="gy"
    ))
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Gyro_x"],
        mode="lines",
        name="gz"
    ))

    fig.update_layout(title_text="3-Axis Gyroscope")
    fig.update_xaxes(title_text="Time [s]")
    fig.update_yaxes(title_text=f"Degrees [{chr(176)}]")

    return plotly.io.to_html(fig)


@app.route('/plotbaro')
def plot_baro():
    df = pd.read_csv('./data/pressure_data.csv')

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Temperature (C)"],
        name="temp"
    ), secondary_y=False)
    fig.add_trace(go.Scatter(
        x=df["Time"],
        y=df["Atmospheric Pressure (mbar)"],
        name="pressure"
    ), secondary_y=True)

    fig.update_layout(title_text="Temperature-pressure")
    fig.update_xaxes(title_text="Time [s]")
    fig.update_yaxes(title_text="Temperature (C)", secondary_y=False)
    fig.update_yaxes(title_text="Atmospheric Pressure (mbar)",
                     secondary_y=True)

    return plotly.io.to_html(fig)


if __name__ == "__main__":
    app.run(debug=True)
