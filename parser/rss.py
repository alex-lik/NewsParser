import feedparser


def get_feed_data(url):
    """
    Parses the RSS feed from the given URL and returns the parsed data.
    
    :param url: The URL of the RSS feed to parse.
    :return: Parsed RSS feed data.
    """
    try:
        feed = feedparser.parse(url)
        return feed
    except Exception as e:
        print(f"Error parsing RSS feed from {url}: {e}")
        return {"status": 500, "error": str(e)}


def parse_feed(feed):
    if feed.get('status') != 200:
        return {"error": "Failed to fetch feed data"}
    data = []
    for entry in feed.get('entries', []):
        entry_data = {
            "title": entry.get('title'),
            "links": entry.get('links'),
            "tags": entry.get('tags'),
            "summary": entry.get('summary'),
            "summary_detail": entry.get('summary_detail'),
            "fulltext": entry.get('fulltext'),
            "content": entry.get('content'),
        }
        print(f"Title: {entry_data['fulltext']}")
        data.append(entry_data)
    return data