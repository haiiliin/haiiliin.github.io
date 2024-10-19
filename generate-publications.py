import mkdocs_gen_files
import yaml
from jinja2 import Template


def generate_publications(
    metadata_file: str = "docs/publications.yml",
    template_file: str = "docs/templates/publications.md",
    output: str = "publications.md",
):
    with open(template_file, "r+", encoding="utf-8") as file:
        template = file.read()

    with open(metadata_file, "r+", encoding="utf-8") as file:
        metadata = yaml.safe_load(file)["publications"]

    # Render the template
    rendered = Template(template).render(publications=metadata)
    with mkdocs_gen_files.open(output, "w+") as file:
        file.write(rendered)


generate_publications()
