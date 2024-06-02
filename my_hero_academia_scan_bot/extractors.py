import urlfetch

import re
import string

from my_hero_academia_scan_bot.logger import get_application_logger

log = get_application_logger()


class Team:
    def __init__(self, name, fetch_f, namespace):
        self.name = name
        self.fetch_f = fetch_f
        self.db_namespace = namespace


def shueisha_fetch():
    # MHA ENG has id 100020
    # web page: https://mangaplus.shueisha.co.jp/titles/100017
    url = "https://jumpg-webapi.tokyo-cdn.com/api/title_detailV3?title_id=100017"
    headers = {
        "User-Agent":
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like "
            "Gecko) Chrome/24.0.1312.27 Safari/537.17"}
    try:
        request = urlfetch.fetch(url, headers=headers)
        raw_text = request.content
        clean_text = ''.join(chr(ch) for ch in raw_text if chr(ch) in string.printable)
        releases = re.findall("#(\d+)", clean_text)[-3:]
        chapter_ids = re.findall("chapter/(\d+)/chapter_thumbnail", clean_text)[3:]
        reader_url = "https://mangaplus.shueisha.co.jp/viewer/{}"
        releases = ["My Hero Academia " + r + " (ENG)" for r in releases]
        messages = [r + "\n" + reader_url.format(ch_id) for r, ch_id in zip(releases, chapter_ids)]
        log.info(releases)
        return releases, messages
    except Exception as exc:
        log.warning("Unable to fetch data.\nPlease check your Internet connection and the availability of the site.")
        log.warning(f"Okay, hero, we've had a problem here.\n{type(exc).__name__}: {str(exc)}")
        raise exc


shueisha = Team("Shueisha", shueisha_fetch, "Shueisha")

teams = [
    shueisha,
]
