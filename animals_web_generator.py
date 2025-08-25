import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'

    if "characteristics" in animal and "diet" in animal["characteristics"]:
        output += f'    <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    if "locations" in animal and len(animal["locations"]) > 0:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    if "characteristics" in animal and "type" in animal["characteristics"]:
        output += f'    <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output

animals_data = load_data("animals_data.json")
output = "".join(serialize_animal(animal) for animal in animals_data)

with open("animals_template.html", "r") as html:
    template = html.read()

new_html = template.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w") as renew:
    renew.write(new_html)
