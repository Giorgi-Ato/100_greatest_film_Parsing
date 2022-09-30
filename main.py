from bs4 import BeautifulSoup
import requests

# Taking HTML for parsing
resource_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url=resource_url).text

# Create BeautifulSoup Object
soup = BeautifulSoup(response, "html.parser")

# Taking all gallery items
gallery_items = soup.find_all("h3", class_="title")

# Extract movie names
movie_names = [movie.text for movie in gallery_items][::-1]

# Write to movies.txt file
with open("movies.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(movie_names))
