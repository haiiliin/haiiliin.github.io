import dataclasses
import json
import os
import typing

markdown = """---
{options}
title: "{title}"
categories:
{categories}
tags: 
{tags}
permalink: {permalink}
---

# Abstract

{abstract}

# Links

[[Publisher]({publisher})], [[Google Scholar]({scholar})]"""

markdown_footer = """, {% cite {bib_key} %}.

{% pdf "{pdf_path}" no_link width=100% height=1000px %}

# References

{% bibliography --cited %}
"""


class ParsedPost:
    year: int
    month: int
    day: int
    name: str

    markdown_text: str = ''

    def __init__(self, text: str, year: int, month: int, day: int, name: str):
        self.markdown_text = text
        self.year, self.month, self.day = year, month, day
        self.name = name

    @property
    def text(self):
        return self.markdown_text

    def save(self, fileDir: str = '.'):
        """
        Save post

        Parameters
        ----------
        fileDir : str
            File dir of the generated posts
        """
        fileName = '{year:04d}-{month:02d}-{day:02d}-{name}.md'.format(year=self.year, month=self.month, day=self.day,
                                                                       name=self.name)
        filePath = os.path.join(fileDir, fileName)
        with open(filePath, 'w+', encoding='utf-8') as file:
            file.write(self.text)


@dataclasses.dataclass
class DataClass:

    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return str(self.toDictionary())

    def toDictionary(self):
        """Save to a dictionary

        Returns
        -------
        dict
            A dictionary
        """
        return dataclasses.asdict(self)

    def toJson(self, filePath: str):
        """Save to a Json file

        Parameters
        ----------
        filePath : str
            File path
        """
        with open(filePath, 'w+', encoding='utf-8') as file:
            json.dump(self.toDictionary(), file, indent=4)

    @classmethod
    def attributeType(cls, name: str) -> typing.Type['DataClass']:
        fields = dataclasses.fields(cls)
        for field in fields:
            if field.name == name:
                return field.type
        raise KeyError('Field {} not found'.format(name))

    @classmethod
    def readDictionary(cls, data: dict):
        """Read a dictionary

        Parameters
        ----------
        data : dict
            A dictionary
        """
        for key, value in data.items():
            subcls = cls.attributeType(key)
            if isinstance(value, dict) and issubclass(subcls, DataClass):
                data.update({key: subcls.readDictionary(value)})
            elif value is not None:
                data.update({key: subcls(value)})
        return cls(**data)

    @classmethod
    def readJson(cls, filePath: str):
        """Read a Json file

        Parameters
        ----------
        filePath : str
            File path
        """
        with open(filePath, 'r+', encoding='utf-8') as file:
            data = json.load(file)
            return cls.readDictionary(data)


@dataclasses.dataclass
class Post(DataClass):
    name: str
    year: int
    month: int
    day: int

    title: str
    abstract: str
    permalink: str

    options: dict[str, str] = dataclasses.field(default_factory=dict)
    categories: list[str] = dataclasses.field(default_factory=list)
    tags: list[str] = dataclasses.field(default_factory=list)
    publisher_link: str = ''
    google_scholar_link: str = ''
    pdf_path: str = ''
    bib_key: str = ''

    def __post_init__(self):
        if len(self.options) == 0:
            self.options = {'classes': 'wide'}

    def parse(self) -> ParsedPost:
        options = '\n'.join(['{key}: {value}'.format(key=key, value=value) for key, value in self.options.items()])
        categories = '\n'.join(['    - {category}'.format(category=category) for category in self.categories])
        tags = '\n'.join(['    - {tag}'.format(tag=tag) for tag in self.tags])
        markdown_text = markdown.format(options=options, title=self.title, categories=categories, tags=tags,
                                        permalink=self.permalink, abstract=self.abstract, publisher=self.publisher_link,
                                        scholar=self.google_scholar_link)
        markdown_text += markdown_footer.replace('{bib_key}', self.bib_key).replace('{pdf_path}', self.pdf_path)
        return ParsedPost(markdown_text, self.year, self.month, self.day, self.name)

    def generate(self, fileDir: str = '.'):
        """
        Generatr posts

        Parameters
        ----------
        fileDir : str
            File dir of the generated posts
        """
        self.parse().save(fileDir)
