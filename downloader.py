import yt_dlp

def choose_format():
    print("\nPilih format audio:")
    print("1. MP3")
    print("2. M4A (AAC)")
    print("3. OPUS")
    print("4. FLAC (Lossless)")

    return {
        "1": "mp3",
        "2": "m4a",
        "3": "opus",
        "4": "flac"
    }.get(input("Masukkan pilihan (1-4): ").strip(), "mp3")


def choose_quality():
    print("\nPilih kualitas audio:")
    print("1. 128 kbps")
    print("2. 192 kbps")
    print("3. 256 kbps")
    print("4. 320 kbps")

    return {
        "1": "128",
        "2": "192",
        "3": "256",
        "4": "320"
    }.get(input("Masukkan pilihan (1-4): ").strip(), "192")


def extract_metadata(url):
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    artist = info.get("artist") or info.get("uploader") or ""
    title = info.get("title") or ""

    if not title:
        raise Exception("Gagal mengambil metadata")

    return artist, title


def download_music(url, audio_format, quality, output_path="downloads"):
    print("\nMengambil metadata...")
    artist, title = extract_metadata(url)

    # 🔥 PAKAI SEARCH, BUKAN LINK LANGSUNG
    search_query = f"ytsearch5:{artist} - {title}"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_path}/%(artist)s - %(title)s.%(ext)s",

        "quiet": False,
        "geo_bypass": True,
        "nocheckcertificate": True,

        # 🔥 FIX ERROR YOUTUBE / YT MUSIC
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        },

        # Metadata & cover
        "addmetadata": True,
        "embedmetadata": True,
        "writethumbnail": True,
        "embedthumbnail": True,
    }

    # Post processing
    if audio_format == "flac":
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "flac",
            }
        ]
    else:
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": quality,
            }
        ]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


if __name__ == "__main__":
    print("=== Music Downloader (YouTube Music FIXED) ===")

    url = input("Masukkan URL lagu / YouTube Music: ").strip()
    audio_format = choose_format()

    if audio_format == "flac":
        quality = None
        print("\nFLAC dipilih (lossless)")
    else:
        quality = choose_quality()
        print(f"\nFormat: {audio_format.upper()} | {quality} kbps")

    print("\nFitur aktif:")
    print("- Metadata artist & title")
    print("- Embed cover album")
    print("- Mode aman YouTube Music\n")

    try:
        download_music(url, audio_format, quality)
        print("\n✅ Download selesai!")
    except Exception as e:
        print("\n❌ Error:", e)        "addmetadata": True,
        "embedmetadata": True,
        "writethumbnail": True,
        "embedthumbnail": True,

        # Lyrics (jika tersedia)
        "writesubtitles": True,
        "writeautomaticsub": True,
        "subtitlesformat": "lrc",
        "subtitleslangs": ["en", "id"],

        # Embed lyric ke audio
        "embedsubtitles": True,

        "quiet": False,
    }

    # Post-processing audio
    if audio_format == "flac":
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "flac",
            }
        ]
    else:
        ydl_opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": quality,
            }
        ]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    print("=== Music Downloader Advanced ===")

    url = input("Masukkan URL musik/video: ").strip()
    audio_format = choose_format()

    if audio_format == "flac":
        quality = None
        print("\nFLAC dipilih (lossless)")
    else:
        quality = choose_quality()
        print(f"\nFormat: {audio_format.upper()} | {quality} kbps")

    print("\nFitur aktif:")
    print("- Embed cover album")
    print("- Metadata artist & album")
    print("- Embed lyric (jika tersedia)\n")

    download_music(url, audio_format, quality)

    print("\nDownload selesai!")
