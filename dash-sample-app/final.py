'''
dash app with 2 charts
1. a static table of the open interest for the given futures with a button to update this table as and when the user clicks it.
2. Live chart of the futures prices
'''
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import datetime
import json
import matplotlib.pyplot as plt
import requests
import asyncio
import websockets
import json
import nest_asyncio
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash('Hello World')
app.layout = html.Div([

    dcc.Graph(id='live-graph'),
    dcc.Interval(
        id='graph-update',
        interval=5*1000,  # in milliseconds
        n_intervals=0
    ),
    html.Button('Update Table', id='button'),
    # table with title "Open Interest"
    html.Div(id='table'),

    # dummy div to force the layout to change
    html.Div(id='dummy-div')

])


@app.callback(Output('dummy-div', 'children'), [Input('dummy-div', 'value')])
def update_graph(selected_dropdown_value):
    asyncio.new_event_loop().run_until_complete(call_api(json.dumps(msg)))


async def call_api(msg):
    global futuresprices, future_dict
    async with websockets.connect('wss://test.deribit.com/ws/api/v2') as websocket:
        await websocket.send(msg)
        n = 0
        while websocket.open:
            response = await websocket.recv()
            output1 = json.loads(response)
            if "result" in output1.keys():
                print("Successfully subscribed")
            if "result" not in output1.keys():
                if output1["params"]["channel"] in channelslist:
                    contractdate = GrabDateFromName(
                        output1["params"]["channel"][7:-6])[1]
                    markprice = output1["params"]["data"]["mark_price"]
                    futuresprices.append({contractdate: markprice})

            n = n+1
            if n > 2:
                # list of key value pairs to dict
                future_dict = {
                    k: v for d in futuresprices for k, v in d.items()}
                # for each in futuresprices:
                #     for key, value in each.items():
                #         future_dict[key] = value
            if len(futuresprices) > 10:
                # select only the last 10 entries
                futuresprices = futuresprices[-10:]
            #     return futurespricetable
            #     # plt.show()
            # # This bit stops the code after awhile, while we are in test mode
            # if n > 10:
            #     break


'''
1. Static Table
'''
futureslist = ['BTC-25MAR22', 'BTC-28JAN22', 'BTC-24JUN22',
               'BTC-30SEP22', 'BTC-30DEC22', 'BTC-PERPETUAL']


def DBDataGrabber(method, params):
    # method = Deribit function
    # params = params in dictionary format
    msg = {"method": method, "params": params}
    webdata = requests.get(
        "https://test.deribit.com/api/v2/public/"+method, params)
    print(webdata.json(), params)
    return webdata.json()


@app.callback(
    Output('table', 'children'),
    [Input('button', 'n_clicks')])
def update_table(n_clicks):
    OIList = {}
    for eachfut in futureslist:
        OIList[eachfut] = DBDataGrabber("ticker", {"instrument_name": eachfut})[
            "result"]["open_interest"]
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in futureslist])] +

        # Body
        [html.Tr([
            html.Td(OIList[eachfut]) for eachfut in futureslist
        ])]
    )


'''
2. Live Chart
'''
channelslist = ['ticker.BTC-25MAR22.100ms', 'ticker.BTC-28JAN22.100ms', 'ticker.BTC-24JUN22.100ms',
                'ticker.BTC-30SEP22.100ms', 'ticker.BTC-30DEC22.100ms', 'ticker.BTC-PERPETUAL.100ms']

msg = {"jsonrpc": "2.0",
       "method": "public/subscribe",
       "id": 42,
       "params": {
           "channels": channelslist}
       }
futuresprices = []
future_dict = {}
futurespricetable = []
# helper


def GrabDateFromName(instrumentname):
    if pd.isnull(instrumentname):
        return ("", "", "", "", "", "")

    instrumentname2 = instrumentname[4:]

    posfinder = instrumentname2.find("-")
    if posfinder == -1:
        contractdate = instrumentname2
        if instrumentname2 == "SPOT":
            expirydate = 0
        elif instrumentname2 == "PERPETUAL":
            expirydate = datetime.datetime.today()
        else:
            expirydate = datetime.datetime.strptime(instrumentname2, "%d%b%y")
    if posfinder > -1:
        contractdate = instrumentname2[0:posfinder]
        expirydate = datetime.datetime.strptime(
            instrumentname2[0:posfinder], "%d%b%y")

    return (contractdate, expirydate)


@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update', 'n_intervals')])
def update_graph_scatter(n):
    # asyncio.new_event_loop().run_until_complete(call_api(json.dumps(msg)))
    global future_dict
    # if len(futuresprices) > 10:
    #     # iterate over dict and remove entries except the last 10
    #     for key in list(futuresprices.keys()):
    #         if key not in list(futuresprices.keys())[-10:]:
    #             futuresprices.pop(key)
    futurespricetable = pd.DataFrame.from_dict(
        future_dict, orient="index").sort_index()
    if len(futurespricetable) > 10:
        # select only the last 10 entries
        futurespricetable = futurespricetable[:10]

    print("-------------------------------------------")
    print(futurespricetable)
    return {
        'data': [{
            'x': futurespricetable.index,
            'y': futurespricetable[eachfut],
            'type': 'line',
            'name': eachfut
        } for eachfut in futurespricetable],
        'layout': {
            'title': 'Live Updating Futures curve'
        }
    }


'''
run data collection loop in background and start app
'''


# nest_asyncio.apply()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(call_api(json.dumps(msg)))


# async def main():
#     # run data collection loop in background and start app
#     asyncio.create_task(call_api(json.dumps(msg)))
#     app.run_server(debug=True)

# asyncio.get_event_loop().run_until_complete(main())
app.run_server()
