import os
import requests
import yaml
import xml.etree.ElementTree as ET

# ── Hardcover ──────────────────────────────────────────────────────────────────

API_KEY = os.environ.get("HARDCOVER_API_KEY")

query = """
{
  me {
    user_books(where: {status_id: {_eq: 2}}) {
      book {
        title
        slug
        cached_contributors
        image {
          url
        }
      }
    }
  }
}
"""

response = requests.post(
    "https://api.hardcover.app/v1/graphql",
    json={"query": query},
    headers={
        "Authorization": API_KEY,
        "Content-Type": "application/json",
        "User-Agent": "jekyll-blog-currently-reading/1.0"
    }
)

print("Hardcover status:", response.status_code)
data = response.json()

user_books = data["data"]["me"][0]["user_books"]

books = []
for ub in user_books:
    book = ub["book"]
    contributors = book.get("cached_contributors", [])
    author = contributors[0]["author"]["name"] if contributors else "Unknown"
    books.append({
        "title": book["title"],
        "author": author,
        "url": f"https://hardcover.app/books/{book['slug']}",
    })

os.makedirs("_data", exist_ok=True)
with open("_data/currently_reading.yml", "w") as f:
    yaml.dump(books, f, allow_unicode=True)

print(f"Wrote {len(books)} book(s) to _data/currently_reading.yml")

# ── imood ──────────────────────────────────────────────────────────────────────

IMOOD_EMAIL = os.environ.get("IMOOD_EMAIL")

imood_response = requests.get(
    f"https://xml.imood.org/query.cgi?email={IMOOD_EMAIL}",
    headers={"User-Agent": "jekyll-blog-mood/1.0"}
)

print("imood status:", imood_response.status_code)

mood: dict[str, str | None] = {"current": None, "personal": None, "face": None}

try:
    root = ET.fromstring(imood_response.text)
    mood["current"] = root.findtext("bundle/mood/base")
    mood["personal"] = root.findtext("bundle/mood/personal")
    # raw id (a string like "12") keys _data/kaomoji.yml
    mood["face"] = root.findtext("bundle/mood/face")
except ET.ParseError as e:
    print("imood XML parse error:", e)

with open("_data/mood.yml", "w") as f:
    yaml.dump(mood, f, allow_unicode=True)

print(f"Wrote mood to _data/mood.yml: {mood}")