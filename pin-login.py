#! /usr/bin/env python3
from plexapi.utils import plexOAuth

if __name__ == '__main__':
    plex_account = plexOAuth({"X-Plex-Client-Identifier": "Plex2m3u"})
    if plex_account:
        print("Long lived auth token is: ", plex_account.authenticationToken)
