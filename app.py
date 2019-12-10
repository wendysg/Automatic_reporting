import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import base64
import io
import json
import numpy as np
import dash_table
from datetime import datetime
import random
import warnings
warnings.filterwarnings('ignore')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.config.suppress_callback_exceptions = True

colors = {
    "graphBackground": "#F5F5F5",
    "background": "#ffffff",
    "text": "#000000"
}

app.layout = html.Div([
                 html.Div([
                           html.H1(children='Automatic Reporting Dashboard with Insights',
                                   style={
                                        'textAlign':'center'
                                   }),
                           html.P(children='ALY6080 XN Project',
                                   style={
                                        'textAlign':'center'
                                   })
                          ],
                     style = {'padding' : '25px' ,
                             'backgroundColor' : '#42248c',
                             'color': 'white',
                             'float':'center'}),
                html.Hr(),
                html.H4("Step 1: Please select the report type."),
                html.Div([
                    dcc.Dropdown(
                        id='report_dropdown',
                        options=[
                            {'label':'Brand Impact Analysis', 'value':'net_sentiment'},
                            {'label':'Geographic Analysis', 'value':'geographic'},
                            {'label':'User Action Analysis', 'value':'user_action'}
                        ],
                        value=[]
                    )
                ],
                style={'width': '40%', 'display': 'inline-block'}),
                html.Div(id='output_container')
    ])

@app.callback(
        Output('output_container', 'children'),
        [Input('report_dropdown', 'value')]
)
def display_page(value):
    if value == 'net_sentiment':
        return html.Div([
                  html.Hr(),
                  html.H4("Step 2: Please Upload Data for Brand Impact Analysis."),
                  html.Div([
                             dcc.Upload(
                                    id='upload_net_sentiment',
                                    children=html.Div([
                                         'Drag and Drop or ',
                                         html.A('Select Files')
                                    ]),
                                    style={
                                         'width': '100%',
                                         'height': '60px',
                                         'lineHeight': '60px',
                                         'borderWidth': '1px',
                                         'borderStyle': 'dashed',
                                         'borderRadius': '5px',
                                         'textAlign': 'center',
                                         'margin': '10px'
                                    }
                                )
                         ],
                         style={'width':'100%',
                                'display': 'flex',
                                'align-items':'center',
                                'justify-content':'center'
                                }
                        ),
                    html.Div(id='output_net_sentiment')
                 ])
    elif value == 'geographic':
        return html.Div([
                  html.Hr(),
                  html.H4("Step 2: Please Upload Data for Geographic Analysis."),
                  html.Div([
                             dcc.Upload(
                                    id='upload_geographic',
                                    children=html.Div([
                                         'Drag and Drop or ',
                                         html.A('Select Files')
                                    ]),
                                    style={
                                         'width': '100%',
                                         'height': '60px',
                                         'lineHeight': '60px',
                                         'borderWidth': '1px',
                                         'borderStyle': 'dashed',
                                         'borderRadius': '5px',
                                         'textAlign': 'center',
                                         'margin': '10px'
                                    }
                                )
                         ],
                         style={'width':'100%',
                                'display': 'flex',
                                'align-items':'center',
                                'justify-content':'center'
                                }
                        ),
                    html.Div(id='output_geographic')
                 ])
    elif value == 'user_action':
        return html.Div([
                  html.Hr(),
                  html.H4("Step 2: Please Upload Data for User Action Analysis."),
                  html.Div([
                             dcc.Upload(
                                    id='upload_user_action',
                                    children=html.Div([
                                         'Drag and Drop or ',
                                         html.A('Select Files')
                                    ]),
                                    style={
                                         'width': '100%',
                                         'height': '60px',
                                         'lineHeight': '60px',
                                         'borderWidth': '1px',
                                         'borderStyle': 'dashed',
                                         'borderRadius': '5px',
                                         'textAlign': 'center',
                                         'margin': '10px'
                                    }
                                )
                         ],
                         style={'width':'100%',
                                'display': 'flex',
                                'align-items':'center',
                                'justify-content':'center'
                                }
                        ),
                    html.Div(id='output_user_action')
                 ])
    else:
        return html.Div([
                    html.Img(
                                src='https://raw.githubusercontent.com/wendysg/image_folder/master/pic_main2.png',
                                style={
                                      'height' : 350,
                                      'width' : 1350,
                                      'float' : 'center',
                                      'position' : 'relative',
                                      'padding-top' : 20,
                                      'padding-right' : 20
                                   })
                        ],
                          style={
                                 'padding' : '80px',
                                 'float':'center' }
                   )

@app.callback(
            Output('output_net_sentiment','children'),
            [Input('upload_net_sentiment','contents')]
)
def update_net_sentiment(contents):
    if contents is not None:
        type,data  = contents.split(',')
        decoded = base64.b64decode(data)

        fdata = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        fdata.Date = pd.to_datetime(fdata.Date)

        fdata['Month'] = np.empty((len(fdata), 0)).tolist()

        for i in range(len(fdata)):
          fdata['Month'][i] = fdata.Date[i].month


        for i in range(len(fdata)):
            if fdata.Month[i] == 1: fdata.Month[i] = 'Jan'
            elif fdata.Month[i] == 2: fdata.Month[i] = 'Feb'
            elif fdata.Month[i] == 3: fdata.Month[i] = 'Mar'
            elif fdata.Month[i] == 4: fdata.Month[i] = 'Apr'
            elif fdata.Month[i] == 5: fdata.Month[i] = 'May'
            elif fdata.Month[i] == 6: fdata.Month[i] = 'Jun'
            elif fdata.Month[i] == 7: fdata.Month[i] = 'Jul'
            elif fdata.Month[i] == 8: fdata.Month[i] = 'Aug'
            elif fdata.Month[i] == 9: fdata.Month[i] = 'Sep'
            elif fdata.Month[i] == 10: fdata.Month[i] = 'Oct'
            elif fdata.Month[i] == 11: fdata.Month[i] = 'Nov'
            elif fdata.Month[i] == 12: fdata.Month[i] = 'Dec'

        sum_table = pd.crosstab([fdata.Month, fdata.Source], fdata.Sentiment,
                               rownames = ['Month', 'Source'],
                               colnames = ['Sentiment'])

        month_list = []
        source_list = []
        net_sent_list = []

        month_seq = fdata.Month.unique().tolist()
        source_seq = fdata.Source.unique().tolist()

        for i in month_seq:
            for j in source_seq:
                net_sent = sum_table.loc[i,j]['positive'] - sum_table.loc[i,j]['negative']
                month_list.append(i)
                source_list.append(j)
                net_sent_list.append(int(net_sent))
        df = pd.DataFrame({'Month': month_list, 'Source': source_list, 'Net_sentiment':net_sent_list})

        cat_month = ['Jan', 'Feb', 'Mar', 'Apr','May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        df['Month'] = pd.Categorical(df['Month'], ordered=True, categories=cat_month)
        df = df.sort_values(by='Month')

        source_list = []
        sent_sum = []
        for source_name in df['Source'].unique():
            df_by_source = df[df['Source'] == source_name]
            total_sent = df_by_source['Net_sentiment'].sum()
            sent_sum.append(total_sent)
            source_list.append(source_name)
        summary_df = pd.DataFrame({'Source':source_list, 'Net_sent_sum':sent_sum})
        max_sum_sent = summary_df['Net_sent_sum'].max()
        best_source = summary_df[summary_df['Net_sent_sum']==max_sum_sent]['Source']

        best_source_df = df[df['Source'].values == best_source.values].reset_index(drop=True)
        max_net_sent = best_source_df['Net_sentiment'].max()
        best_month = best_source_df[best_source_df['Net_sentiment']==max_net_sent]['Month']

        traces = []
        for source_name in df['Source'].unique():
            df_by_source = df[df['Source'] == source_name]
            traces.append(go.Scatter(
                        x=df_by_source['Month'],
                        y=df_by_source['Net_sentiment'],
                        text=df_by_source['Net_sentiment'],
                        mode='lines+markers',
                        opacity=0.7,
                        marker={'size': 15},
                        name=source_name
                        ))

        return html.Div([
                html.Div([
                    dcc.Graph(id='graph_net_sentiment',
                        figure={
                            'data': traces,
                            'layout': go.Layout(
                                        title={'text':'Net Sentiment from Different Sources'},
                                        xaxis={'title': 'Time of the Year',
                                               'categoryorder': 'array',
                                               'categoryarray': cat_month,
                                               'type':'category'},
                                        yaxis={'title': 'Net Sentiment Count'},
                                        hovermode='closest',
                                        plot_bgcolor=colors["graphBackground"],
                                        paper_bgcolor=colors["graphBackground"]
                                     )
                                  })
                         ],
                   style={'width':'90%'}
                  ),
                html.Div([
                        html.H4(' {} has the highest impact on the brand.'.format(best_source.to_string(index=False))),
                        html.H4(' The peak is {} net sentiments in {}.'.format(str(max_net_sent),best_month.tolist()[0]))
                        ],
                    style = {
                             'backgroundColor' : '#8f0618',
                             'color': 'white',
                             'padding':'5px'})
        ])
    else:
        return None

@app.callback(
            Output('output_geographic','children'),
            [Input('upload_geographic','contents')]
)
def update_geographic(contents):
    if contents is not None:
        type,data  = contents.split(',')
        decoded = base64.b64decode(data)

        fdata = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        pos_data = fdata[fdata['Sentiment'] == 'positive']
        df2 = pos_data.groupby('State').count().reset_index()[['State','Sentiment']]


        df3 = pd.crosstab(pos_data.Source,pos_data.State)

        source_list = []
        top3_state = []
        top3_count = []

        for source_name in df3.index.to_list():
             order_list = df3.loc[source_name].sort_values(ascending = False)

             for i in range(3):
                 source_list.append(source_name)
                 top3_state.append(order_list.index[i])
                 top3_count.append(int(order_list[i]))

        df_top3 = pd.DataFrame({'Source':source_list,'State':top3_state,'Count':top3_count})

        return html.Div([
                   dcc.Graph(id='graph_geo',
                        figure={
                            'data':[go.Choropleth(
                                        locations=df2['State'], # Spatial coordinates
                                        z = df2['Sentiment'].astype(float), # Data to be color-coded
                                        locationmode = 'USA-states', # set of locations match entries in `locations`
                                        colorscale = 'Reds',
                                        colorbar_title = 'Positive Sentiment Count',
                                        )
                                    ],
                            'layout':{
                                'title':'Geographic Segmentation for Positive Sentiments',
                                'geo':{'scope':'usa'},
                                'width': 1400,
                                'height':650
                                }
                        }),
                    html.Div([
                          html.H4(' Summary of Top 3 States on different platforms: '),
                          html.Div([
                                dash_table.DataTable(
                                            id='table',
                                            data=df_top3.to_dict('records'),
                                            columns=[{"name": i, "id": i} for i in df_top3.columns],
                                            fixed_rows={'headers': True, 'data': 0},
                                            style_cell={'width': '25px',
                                                        'backgroundColor' : '#8f0618',
                                                        'color': 'white',
                                                        'fontSize':16,
                                                        'textAlign': 'center'},
                                            style_table={
                                                    'height': '180px',
                                                    'width':'600px',
                                                    'overflowY': 'scroll',
                                                    'border': 'thin lightgrey solid'
                                                    }
                                                )
                                    ])
                        ],
                        style = {
                                'backgroundColor' : '#8f0618',
                                'color': 'white',
                                'padding':'5px',
                                'height': 250})
        ])
    else:
        return None


@app.callback(Output('output_user_action', 'children'),
              [Input('upload_user_action', 'contents')]
)
def update_user_action(contents):
    if contents is not None:
        type,data  = contents.split(',')
        decoded = base64.b64decode(data)

        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

        return html.Div([
                    html.Div([
                            dcc.Graph(
                                     id='graph_action',
                                     figure={
                                            'data': [
                                                {'x': list(df.Time), 'y': list(df.Views), 'type': 'line', 'name': 'Views'},
                                                {'x': list(df.Time), 'y': list(df.Likes), 'type': 'line', 'name': 'Likes'},
                                                {'x': list(df.Time), 'y': list(df.Shares), 'type': 'line', 'name': 'Shares'},
                                                   ],
                                            'layout': go.Layout(
                                                           title={'text':'Trends of Views, Likes, Shares '}
                                            )
                                        }
                                    )
                              ]
                           ),
                     html.Div([
                            dash_table.DataTable(
                            data=df.to_dict('records'),
                            columns=[{'name': i, 'id': i} for i in df.columns],
                            fixed_rows={'headers': True, 'data': 0},
                            style_cell={'width': '120px'},
                            style_table={
                                    'height': '300px',
                                    'overflowY': 'scroll'
                                    },
                           )
                          ]),
                    html.Hr(),
                    html.Div([
                            html.H4(' Views: Top View is {} on {}. The average views by day is {}.'.format(df.Views.max(), df[df.Views==df.Views.max()]['Time'].to_string(index=False), int(df.Views.mean()))),
                            html.H4(' Likes: Top Like is {} on {}. The average likes by day is {}.'.format(df.Likes.max(), df[df.Likes==df.Likes.max()]['Time'].to_string(index=False), int(df.Likes.mean()))),
                            html.H4(' Shares: Top Share is {} on {}. The average shares by day is {}.'.format(df.Shares.max(), df[df.Shares==df.Shares.max()]['Time'].to_string(index=False), int(df.Shares.mean())))
                        ],
                        style = {
                            'backgroundColor' : '#8f0618',
                            'color': 'white',
                            'padding':'5px'})
                  ],className="row",
                    style={"margin-bottom": "35px"})
    else:
        return None


if __name__ == '__main__':
    app.run_server(debug=True)
