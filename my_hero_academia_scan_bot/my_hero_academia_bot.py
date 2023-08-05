import telegram
import time

from my_hero_academia_scan_bot.constants import DROPBOX_BOT_DIR_PATH
from my_hero_academia_scan_bot.dropbox_service import DropboxService
from my_hero_academia_scan_bot.extractors import teams
from my_hero_academia_scan_bot.logger import get_application_logger
from my_hero_academia_scan_bot.credentials import MHA_BOT_TOKEN, TELEGRAM_CHAT_ID

log = get_application_logger()
releases_to_check = ['My Hero Academia']


class ContentChecker:

    def __init__(self):
        self.storage_service = DropboxService()
        self.team_items = {}

    def check_releases(self):
        log.info(f"Checking releases at {str(time.strftime('%c'))}")
        for team in teams:
            log.info(f"Fetching releases from {team.name}...")
            try:
                releases, messages = team.fetch_f()
                for release, message in zip(releases, messages):
                    if is_monitored(message):
                        self.send_notification_if_needed(team, release, message)
            except Exception as exc:
                log.warning(f"Unable to fetch releases from {team.name}. Going to skip it.")
                log.warning(f"Okay, hero, we've had a problem here.\n{type(exc).__name__}: {str(exc)}")

    def send_notification_if_needed(self, team, release_code, release_message):
        file_dir = f"{DROPBOX_BOT_DIR_PATH}/{team.name}"
        try:
            if self._is_old_content(file_dir, release_code):
                return
            try:
                mha_bot = telegram.Bot(token=MHA_BOT_TOKEN)
                message = "Hey, eroi! Nuovo capitolo disponibile!"
                message += f"\n\n{team.name}: {release_message}\n\nBuona lettura!"
                self.storage_service.create_file(f"{file_dir}/{release_code}")
                mha_bot.sendMessage(chat_id=TELEGRAM_CHAT_ID, text=message, disable_web_page_preview=True)
            except Exception as exc:
                log.warning("Unable to send Telegram notification.")
                log.warning(f"Okay, hero, we've had a problem here.\n{type(exc).__name__}: {str(exc)}")
        except Exception as exc:
            log.warning("Unable to store data.")
            log.warning(f"Okay, hero, we've had a problem here.\n{type(exc).__name__}: {str(exc)}")

    def _is_old_content(self, file_dir, file_name):
        if file_dir not in self.team_items:
            self.team_items[file_dir] = self.storage_service.list_files(file_dir)
        return any(item.name == file_name for item in self.team_items[file_dir])

def is_monitored(manga):
    for release in releases_to_check:
        if release.lower() in manga.lower():
            return True
    return False
