import os

from plexapi.server import PlexServer

# Plex server connection details
PLEX_URL = os.getenv("PLEX_URL", "http://192.168.2.10:32400")
PLEX_TOKEN = os.getenv("PLEX_TOKEN")
# Name of Music library to get playlists from
PLEX_LIBRARY_NAME = os.getenv("PLEX_LIBRARY", "Music")
# Comma separated list of playlist names to exclude
PLEX_PLAYLIST_EXCLUDE = os.getenv("PLEX_PLAYLIST_EXCLUDE", "All Music")
# Directory to save M3U files
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./")


def translate_path(origin_path: str) -> str:
    if origin_path.startswith("/data/"):
        origin_path = "/share/Media" + origin_path[5:]

    return origin_path


def create_m3u_playlist(playlist, output_dir):
    # M3U header
    m3u_content = "#EXTM3U\n"

    for item in playlist.items():
        # Add each media file's location to the M3U content
        m3u_content += f"#EXTINF:-1,{item.title}\n"
        m3u_content += f"{translate_path(item.media[0].parts[0].file)}\n"

    # File name for the M3U file
    m3u_file = os.path.join(output_dir, f"{playlist.title}.m3u")

    # Write the M3U content to the file
    with open(m3u_file, "w", encoding="utf-8") as file:
        file.write(m3u_content)
    print(f"Created playlist: {m3u_file}")


def main():
    # Connect to Plex server
    plex = PlexServer(PLEX_URL, PLEX_TOKEN)

    # Specify the library name to fetch playlists from
    library_name = PLEX_LIBRARY_NAME

    # Fetch the library
    music_library = plex.library.section(library_name)

    # Fetch all playlists in the library
    playlists = music_library.playlists()

    # Create output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    exclude = {title.strip() for title in PLEX_PLAYLIST_EXCLUDE.split(",")}

    # Create M3U playlists for each Plex playlist
    for playlist in playlists:
        if playlist.title in exclude:
            continue
        create_m3u_playlist(playlist, OUTPUT_DIR)


if __name__ == "__main__":
    main()
