# plex2m3u

Export Plex playlists to m3u

## Usage

Configuration is passed to this script via environment variables. The following
variables are required:

- `PLEX_URL`: The URL of the Plex server
- `PLEX_TOKEN`: The token to use to authenticate with the Plex server. (See
  [Getting a token](#getting-a-token) for more information)

The following are optional:

- `PLEX_LIBRARY_NAME`: The name of the library to export playlists from. Defaults to "Music".
- `PLEX_PLAYLIST_EXCLUDE`: A comma-separated list of playlist names to exclude from the export. Defaults to "All Music".
- `OUTPUT_DIR`: The directory to write the m3u files to. Defaults to the current directory.
- `PATH_REPLACE`: If you're using docker, you may want to set up path replacement. This is done by setting this to a comma separated list of `from_path:to_path` pairs. For example, if you're using docker and your music is stored in `/mnt/music`, you would set this to `/mnt/music:/music`. This will replace `/mnt/music` with `/music` in the paths in the m3u files.

## Getting a token

A helper script is provided to get a token from a Plex server. To use it, run `./pin-login.py`. Pass the resulting token as the `PLEX_TOKEN` environment variable.
