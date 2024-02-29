from flask import Flask
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    character_dict = json.loads(data)

    characters = []
    for character in character_dict["results"]:
        character_data = {
            "name": character["name"],
            "status": character["status"]
        }
        characters.append(character_data)

    return {"characters": characters}

if __name__ == "__main__":
    app.run(debug=True)
