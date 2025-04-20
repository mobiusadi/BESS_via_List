import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
from dash import callback_context

# Your generated location coordinates dictionary
location_coordinates = {
    'Japan, Ibaraki Prefecture': {'latitude': 36.2869536, 'longitude': 140.4703384},
    'US, HI, Kahuku': {'latitude': 21.679124, 'longitude': -157.94838},
    'US, AZ, Flagstaff': {'latitude': 35.1987522, 'longitude': -111.651822},
    'US, WA, Port Angeles': {'latitude': 48.118146, 'longitude': -123.430741},
    'US, WI, Franklin': {'latitude': 42.888627, 'longitude': -88.0384183},
    'China, Shanxi': {'latitude': 37.0, 'longitude': 112.0},
    'South Korea, North Jeolla, Gochang': {'latitude': 35.4355, 'longitude': 126.7021},
    'Belgium, Drogenbos': {'latitude': 50.786532, 'longitude': 4.3173542},
    'China, Shanxi': {'latitude': 37.0, 'longitude': 112.0},
    'South Korea, North Gyeongsang, Gyeongsan': {'latitude': 35.825122, 'longitude': 128.741329},
    'South Korea, South Jeolla, Yeongam': {'latitude': 34.800052, 'longitude': 126.6970381},
    'South Korea, North Jeolla, Gunsan': {'latitude': 35.9679984, 'longitude': 126.7369036},
    'South Korea, South Jeolla, Haenam': {'latitude': 34.5734106, 'longitude': 126.5989275},
    'South Korea, South Gyeongsang, Geochang': {'latitude': 35.6872871, 'longitude': 127.9138505},
    'South Korea, Sejong': {'latitude': 36.4799999, 'longitude': 127.289},
    'South Korea, Chungcheongbuk-do, Yeongdong': {'latitude': 36.1747588, 'longitude': 127.7834432},
    'South Korea, Chungcheongnam, Taean': {'latitude': 36.7454236, 'longitude': 126.29836},
    'South Korea, Jeju': {'latitude': 33.4887737, 'longitude': 126.4987083},
    'South Korea, Gyeonggi, Yongin': {'latitude': 37.2405741, 'longitude': 127.1785572},
    'South Korea, North Gyeongsang, Yeongju': {'latitude': 36.805685, 'longitude': 128.624054},
    'South Korea, South Chungcheong, Cheonan': {'latitude': 36.8150283, 'longitude': 127.1140654},
    'South Korea, Gyeongsangbuk-do, Mungyeong': {'latitude': 36.5858541, 'longitude': 128.1870612},
    'South Korea, North Chungcheong, Jecheon': {'latitude': 37.1326042, 'longitude': 128.1913508},
    'South Korea, Gangwon, Samcheok': {'latitude': 37.4498745, 'longitude': 129.1652969},
    'South Korea, South Gyeongsangnam, Yangsan': {'latitude': 35.3349979, 'longitude': 129.0370582},
    'South Korea, South Jeolla, Wando': {'latitude': 34.3110373, 'longitude': 126.7553933},
    'South Korea, North Jeolla, Jangsu': {'latitude': 35.647, 'longitude': 127.5212},
    'South Korea, Ulsan': {'latitude': 35.5391697, 'longitude': 129.3119136},
    'US, OR, Tualatin': {'latitude': 45.3809339, 'longitude': -122.7694369},
    'US, AZ, Surprise': {'latitude': 33.629247, 'longitude': -112.3681428},
    'South Korea, North Gyeongsang, Chilgok': {'latitude': 35.995, 'longitude': 128.4017},
    'South Korea, Yesan': {'latitude': 36.6871147, 'longitude': 126.8284677},
    'France, Vitry-sur-Seine': {'latitude': 48.7876, 'longitude': 2.39164},
    'South Korea, Pyeongchang': {'latitude': 37.3705, 'longitude': 128.3903},
    'South Korea, Gunwi': {'latitude': 36.2425017, 'longitude': 128.5732027},
    'South Korea, Hadong': {'latitude': 35.0670735, 'longitude': 127.7516778},
    'South Korea, Gimhae': {'latitude': 35.2310947, 'longitude': 128.8908228},
    'Australia, Brisbane': {'latitude': -27.4689682, 'longitude': 153.0234991},
    'South Korea, Haenam': {'latitude': 34.5734106, 'longitude': 126.5989275},
    'UK, Liverpool': {'latitude': 53.4071991, 'longitude': -2.99168},
    'France, Ariege, Perles-et-Castelet': {'latitude': 42.7146384, 'longitude': 1.7695911},
    'South Korea, Hongseong': {'latitude': 36.5993365, 'longitude': 126.6812157},
    'Australia, Bohle Plains': {'latitude': -19.288899, 'longitude': 146.6739271},
    'US, MI, Standish': {'latitude': 43.983076, 'longitude': -83.95888},
    'France, New Caledonia, Boulouparis': {'latitude': -21.8629851, 'longitude': 166.0509591},
    'Germany, Neuhardenberg': {'latitude': 52.5965971, 'longitude': 14.2383658},
    'US, IL, LaSalle': {'latitude': 41.3474892, 'longitude': -88.9011861},
    'Australia, Victoria, Moorabool': {'latitude': -38.0666588, 'longitude': 144.2925356},
    'US, CA, Moss Landing': {'latitude': 36.8035938, 'longitude': -121.7862749},
    'South Korea, Nam-gu, Ulsan': {'latitude': 35.535263, 'longitude': 129.2594949},
    'US, CA, Valley Center': {'latitude': 33.2272406, 'longitude': -117.0291893},
    'US, AZ, Chandler': {'latitude': 33.3062031, 'longitude': -111.841185},
    'South Korea, Jangseong-gun': {'latitude': 35.3017065, 'longitude': 126.7844061},
    'US, CA, Rio Dell': {'latitude': 40.499301, 'longitude': -124.106437},
    'South Korea, Incheon': {'latitude': 37.456, 'longitude': 126.7052},
    'USA, Wyoming, Yellowstone National Park': {'latitude': 44.6200885, 'longitude': -110.5606893},
    'China, Hainan': {'latitude': 9.5507929, 'longitude': 112.8906807},
    'South Korea, Jeollanam-do, Yeongam-gun, Geumjeong-myeon': {'latitude': 34.85513, 'longitude': 126.77391},
    'US, PA, Millvale': {'latitude': 40.480069, 'longitude': -79.9783862},
    'France, Saint-Trivier-sur-Moignans': {'latitude': 46.071982, 'longitude': 4.8979906},
    'Sweden, Gothenburg, Vastra Frolunda': {'latitude': 57.6569983, 'longitude': 11.911899},
    'US, NY, East Hampton': {'latitude': 40.9633868, 'longitude': -72.1847598},
    'US, NY, Warwick': {'latitude': 41.256483, 'longitude': -74.3598755},
    'US, NY, Chaumont': {'latitude': 44.066999, 'longitude': -76.130209},
    'France, Saucats, Barban': {'latitude': 44.6223729, 'longitude': -0.6113291},
    'Australia, Queensland, Bouldercombe': {'latitude': -23.53295, 'longitude': 150.4853506},
    'France, Martinique, Saint-Esprit': {'latitude': 14.5622729, 'longitude': -60.9326931},
    'USA, ID, Melba': {'latitude': 43.3732565, 'longitude': -116.5304946},
    'Taiwan, Lanyu': {'latitude': 22.0438499, 'longitude': 121.5422433},
    'USA, CA, San Diego': {'latitude': 32.7174202, 'longitude': -117.162772},
    'Japan, Kagoshima, Isa': {'latitude': 32.0569877, 'longitude': 130.6130906},
    'US, CA, Santa Ana': {'latitude': 33.7494951, 'longitude': -117.873221},
    'US, CA, Escondido': {'latitude': 33.1216751, 'longitude': -117.0814849},
    'Singapore': {'latitude': 1.357107, 'longitude': 103.8194992},
    'South Africa, Table Mountain': {'latitude': -33.9590635, 'longitude': 18.4038716},
    'Canada, ON, Brantford': {'latitude': 43.1408157, 'longitude': -80.2631733},
    'US, CA, Kearny Mesa': {'latitude': 32.8289243, 'longitude': -117.142415},
    'England, Essex, Tilbury': {'latitude': 51.4631174, 'longitude': 0.3643896},
    'Scotland, Aberdeenshire, Rothienorman': {'latitude': 57.4113653, 'longitude': -2.4644314}
}

# Convert the dictionary to a Pandas DataFrame
df_locations = pd.DataFrame.from_dict(location_coordinates, orient='index').reset_index().rename(columns={'index': 'location'})

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'display': 'flex', 'height': '100vh'},
    children=[
        html.Div(
            id='location-list',
            style={'width': '30%', 'overflowY': 'auto', 'padding': '20px'},
            children=[
                html.Div(
                    id={'type': 'location-item', 'index': i},
                    children=[html.H3(location)],
                    style={'marginBottom': '10px', 'border': '1px solid #ddd', 'padding': '10px'}
                )
                for i, location in enumerate(df_locations['location'])
            ]
        ),
        html.Div(
            style={'width': '70%'},
            children=[
                dcc.Graph(
                    id='location-map',
                    figure=px.scatter_mapbox(
                        df_locations,
                        lat="latitude",
                        lon="longitude",
                        hover_name="location",
                        zoom=3,
                        height=800
                    ).update_layout(mapbox_style="open-street-map")
                )
            ]
        ),
    ]
)

@app.callback(
    Output('location-map', 'figure'),
    Output('location-list', 'children'),
    Input({'type': 'location-item', 'index': dash.ALL}, 'n_clicks'),
    State('location-map', 'figure'),
    State('location-list', 'children'),
    State({'type': 'location-item', 'index': dash.ALL}, 'id')
)
def update_map_on_click(n_clicks, current_figure, current_items, item_ids):
    ctx = callback_context
    if ctx.triggered_id:
        clicked_index = int(ctx.triggered_id['index'])
        clicked_row = df_locations.iloc[clicked_index]
        updated_figure = dict(current_figure)
        updated_figure['layout']['mapbox']['center'] = {
            'lat': clicked_row['latitude'],
            'lon': clicked_row['longitude']
        }

        updated_items = []
        for i, item in enumerate(current_items):
            new_item = dict(item)
            default_style = {'marginBottom': '10px', 'border': '1px solid #ddd', 'padding': '10px'}
            new_item['props']['style'] = default_style
            if i == clicked_index:
                new_item['props']['style'] = {'marginBottom': '10px', 'border': '2px solid red', 'padding': '10px'}
            updated_items.append(new_item)

        if 'data' in updated_figure and len(updated_figure['data']) > 0:
            updated_figure['data'][0]['marker']['color'] = ['blue'] * len(df_locations)
            updated_figure['data'][0]['marker']['color'][clicked_index] = 'red'

        return updated_figure, updated_items
    return current_figure, current_items

@app.callback(
    Output('location-list', 'children', allow_duplicate=True),
    Output('location-map', 'figure', allow_duplicate=True),
    Input('location-map', 'clickData'),
    State('location-list', 'children'),
    State('location-map', 'figure'),
    prevent_initial_call=True
)
def update_list_on_map_click(click_data, current_items, current_figure):
    if click_data:
        clicked_lat = click_data['points'][0]['lat']
        clicked_lon = click_data['points'][0]['lon']
        try:
            clicked_index = df_locations[
                (df_locations['latitude'].round(4) == round(clicked_lat, 4)) &
                (df_locations['longitude'].round(4) == round(clicked_lon, 4))
            ].index[0]

            updated_items = []
            for i, item in enumerate(current_items):
                new_item = dict(item)
                default_style = {'marginBottom': '10px', 'border': '1px solid #ddd', 'padding': '10px'}
                new_item['props']['style'] = default_style
                if i == clicked_index:
                    new_item['props']['style'] = {'marginBottom': '10px', 'border': '2px solid red', 'padding': '10px'}
                updated_items.append(new_item)

            updated_figure_map_click = dict(current_figure)
            if 'data' in updated_figure_map_click and len(updated_figure_map_click['data']) > 0:
                updated_figure_map_click['data'][0]['marker']['color'] = ['blue'] * len(df_locations)
                updated_figure_map_click['data'][0]['marker']['color'][clicked_index] = 'red'

            return updated_items, updated_figure_map_click
        except IndexError:
            return current_items, current_figure
    return current_items, current_figure

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)