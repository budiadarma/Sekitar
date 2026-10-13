import feedparser

def get_trending_news():
    # Menggunakan RSS Feed berita ringan dan tren budaya pop / internet
    rss_url = "https://feeds.arstechnica.com/arstechnica/index"
    
    print("==================================================")
    print(" DAFTAR BERITA & TREN TERBARU UNTUK KONTEN ")
    print("==================================================")
    
    feed = feedparser.parse(rss_url)
    
    for i, entry in enumerate(feed.entries[:5], 1):
        print(f"\n{i}. Judul: {entry.title}")
        print(f"   Ringkasan: {entry.summary[:150]}...")
        print(f"   Link: {entry.link}")

if __name__ == "__main__":
    get_trending_news()
