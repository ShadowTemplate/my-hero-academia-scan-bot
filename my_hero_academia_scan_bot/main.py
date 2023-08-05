from my_hero_academia_scan_bot.my_hero_academia_bot import ContentChecker


def main():
    print(f"Checking new content...")
    content_checker = ContentChecker()
    content_checker.check_releases()
    print(f"Checked new content.")


if __name__ == '__main__':
    main()
