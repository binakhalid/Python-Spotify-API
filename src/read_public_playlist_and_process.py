# import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#import json

clientId = "xxx"
clientSecret = "xx"
spotify_user_name_first_playlist = "spotify"
spotify_user_name_second_playlist = "onerepublicofficial"
first_playlist_id = "37i9dQZF1DXbZBKpgxsyXU"
second_playlist_id = "0V4WND9P7IDEdtZjOJomHi"
track_list_1 = []
track_list_2 = []

client_credentials_manager = SpotifyClientCredentials(clientId, clientSecret)
spotify_manager = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_tracks_for_first_playlist(first_playlist_id):
    results = spotify_manager.user_playlist(spotify_user_name_first_playlist,
                                                   first_playlist_id,
                                                   fields="tracks,next")
    tracks = results['tracks']
    for item in tracks['items']:
        track = item['track']
        track_list_1.append(track['name'])
    return track_list_1

def get_tracks_for_second_playlist(second_playlist_id):
    results = spotify_manager.user_playlist(spotify_user_name_second_playlist,
                                                   second_playlist_id,
                                                   fields="tracks,next")
    tracks = results['tracks']
    for item in tracks['items']:
        track = item['track']
        track_list_2.append(track['name'])
    return track_list_2

track_list_1 = get_tracks_for_first_playlist(first_playlist_id)
print('Track List # 1')
print('---------------')
print(track_list_1)
track_list_2 = get_tracks_for_second_playlist(second_playlist_id)
print('Track List # 2')
print('---------------')
print(track_list_2)
print('=======================================================')

def compare_lists_and_generate_common_name_list(track_list_1, track_list_2):
    common_name_list = list(set(track_list_1).intersection(track_list_2))
    print('Track List Common Track Names')
    print('-----------------------------')
    print(common_name_list)

def combine_track_names_and_generate_list(track_list_1, track_list_2):
    combined_list_names = list(track_list_1)
    combined_list_names.extend(x for x in track_list_2 if x not in combined_list_names)
    print('Track List Combined Track Names')
    print('-------------------------------')
    print(combined_list_names)

compare_lists_and_generate_common_name_list(track_list_1, track_list_2)
combine_track_names_and_generate_list(track_list_1, track_list_2)
