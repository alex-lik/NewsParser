from parser.rss import get_feed_data, parse_feed

from config import read_config

if __name__ == '__main__':
    config = read_config()
    all_data = []
    for url in config.get('rss', []):
        print(url)
        feed_data = get_feed_data(url)
        data = parse_feed(feed_data)
        all_data.append(data)
    print(all_data)
        # print(feed_data)
        # print('-'*100)
        # # a = parse_feed(feed_data)
        # entries = feed_data.get('entries', [])

        # for entry in entries:
            # news = get_news(entry)
        # print(a)
        # print('-'*100)
        
