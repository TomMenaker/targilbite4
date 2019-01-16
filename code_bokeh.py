import pandas as pd
import pyEX
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models.widgets import TextInput, Button
from bokeh.plotting import figure, curdoc
from bokeh.layouts import row, widgetbox


TICKER = "INTC"
TICKER2 = "AAPL"
TICKER3 = "NVDA"
TICKER4 = "IBM"
base = "https://api.iextrading.com/1.0/"
data = ColumnDataSource(dict(time=[], display_time=[], price=[]))
data2 = ColumnDataSource(dict(time=[], display_time=[], price=[]))
data3 = ColumnDataSource(dict(time=[], display_time=[], price=[]))
data4 = ColumnDataSource(dict(time=[], display_time=[], price=[]))


def get_lastest_price(symbol):
    return pd.DataFrame([pyEX.delayedQuote(symbol)])


def update_ticker():
    global TICKER
    TICKER = ticker_textbox.value
    price_plot.title.text = "Real-Time Price: " + ticker_textbox.value
    data.data = dict(time=[], display_time=[], price=[])
    return

def update_ticker2():
    global TICKER2
    TICKER2 = ticker_textbox2.value
    price_plot2.title.text = "Real-Time Price: " + ticker_textbox2.value
    data2.data = dict(time=[], display_time=[], price=[])
    return

def update_ticker3():
    global TICKER3
    TICKER3 = ticker_textbox3.value
    price_plot3.title.text = "Real-Time Price: " + ticker_textbox3.value
    data3.data = dict(time=[], display_time=[], price=[])
    return

def update_ticker4():
    global TICKER4
    TICKER4 = ticker_textbox4.value
    price_plot4.title.text = "Real-Time Price: " + ticker_textbox4.value
    data4.data = dict(time=[], display_time=[], price=[])
    return

def update_price():
    new_price = get_lastest_price(symbol=TICKER)
    data.stream(dict(time=new_price["delayedPriceTime"],
                     display_time=new_price["processedTime"],
                     price=new_price["delayedPrice"]), 10000)
    print('price of {} was updated to {}'.format(TICKER, get_lastest_price(symbol=TICKER)))
    return

def update_price2():
    new_price = get_lastest_price(symbol=TICKER2)
    data2.stream(dict(time=new_price["delayedPriceTime"],
                     display_time=new_price["processedTime"],
                     price=new_price["delayedPrice"]), 10000)
    print('price of {} was updated to {}'.format(TICKER2, get_lastest_price(symbol=TICKER2)))
    return

def update_price3():
    new_price = get_lastest_price(symbol=TICKER3)
    data3.stream(dict(time=new_price["delayedPriceTime"],
                     display_time=new_price["processedTime"],
                     price=new_price["delayedPrice"]), 10000)
    print('price of {} was updated to {}'.format(TICKER3, get_lastest_price(symbol=TICKER3)))
    return

def update_price4():
    new_price = get_lastest_price(symbol=TICKER4)
    data4.stream(dict(time=new_price["delayedPriceTime"],
                     display_time=new_price["processedTime"],
                     price=new_price["delayedPrice"]), 10000)
    print('price of {} was updated to {}'.format(TICKER4, get_lastest_price(symbol=TICKER4)))
    return

hover = HoverTool(tooltips=[
    ("Time", "@display_time"),
    ("Real-Time Price", "@price")
    ])

price_plot = figure(plot_width=700,
                    plot_height=200,
                    x_axis_type='datetime',
                    tools=[hover],
                    title="Real-Time Price Plot")

price_plot.line(source=data, x='time', y='price')
price_plot.xaxis.axis_label = "Time passed since updated"
price_plot.yaxis.axis_label = "Current Price"
price_plot.title.text = "Real Time Price of: " + TICKER

ticker_textbox = TextInput(placeholder="Ticker change for 1st graph")
update = Button(label="Update first graph")
update.on_click(update_ticker)

inputs = widgetbox([ticker_textbox, update], width=200)

price_plot2 = figure(plot_width=700,
                    plot_height=200,
                    x_axis_type='datetime',
                    tools=[hover],
                    title="Real-Time Price Plot")

price_plot2.line(source=data2, x='time', y='price')
price_plot2.xaxis.axis_label = "Time passed since updated"
price_plot2.yaxis.axis_label = "Current Price"
price_plot2.title.text = "Real Time Price of: " + TICKER2

ticker_textbox2 = TextInput(placeholder="Ticker change for 2nd graph")
update2 = Button(label="Update second graph")
update2.on_click(update_ticker2)

inputs2 = widgetbox([ticker_textbox2, update2], width=200)

price_plot3 = figure(plot_width=700,
                    plot_height=200,
                    x_axis_type='datetime',
                    tools=[hover],
                    title="Real-Time Price Plot")

price_plot3.line(source=data3, x='time', y='price')
price_plot3.xaxis.axis_label = "Time passed since updated"
price_plot3.yaxis.axis_label = "Current Price"
price_plot3.title.text = "Real Time Price of: " + TICKER3

ticker_textbox3 = TextInput(placeholder="Ticker change for 3rd graph")
update3 = Button(label="Update third graph")
update3.on_click(update_ticker3)

inputs3 = widgetbox([ticker_textbox3, update3], width=200)

price_plot4 = figure(plot_width=700,
                    plot_height=200,
                    x_axis_type='datetime',
                    tools=[hover],
                    title="Real-Time Price Plot")

price_plot4.line(source=data4, x='time', y='price')
price_plot4.xaxis.axis_label = "Time passed since updated"
price_plot4.yaxis.axis_label = "Current Price"
price_plot4.title.text = "Real Time Price of: " + TICKER4

ticker_textbox4 = TextInput(placeholder="Ticker change for 3rd graph")
update4 = Button(label="Update third graph")
update4.on_click(update_ticker4)

inputs4 = widgetbox([ticker_textbox4, update4], width=200)

curdoc().add_root(row(inputs, price_plot, width=1500))
curdoc().title = "Selected Real-Time Stock Prices from IEX"
curdoc().add_periodic_callback(update_price, 1000)

curdoc().add_root(row(inputs2, price_plot2, width=1500))
curdoc().title = "Selected Real-Time Stock Prices from IEX"
curdoc().add_periodic_callback(update_price2, 1000)

curdoc().add_root(row(inputs3, price_plot3, width=1500))
curdoc().title = "Selected Real-Time Stock Prices from IEX"
curdoc().add_periodic_callback(update_price3, 1000)

curdoc().add_root(row(inputs4, price_plot4, width=1500))
curdoc().title = "Selected Real-Time Stock Prices from IEX"
curdoc().add_periodic_callback(update_price4, 1000)