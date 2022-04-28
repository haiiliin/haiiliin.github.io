import dataclasses

from .Post import Post, DataClass


@dataclasses.dataclass
class Posts(DataClass):
    """
    Class to generate posts of bibliographies
    """
    posts: dict[str, Post] = dataclasses.field(default_factory=dict)

    @classmethod
    def readPosts(cls, posts: dict[str, dict[str, ...]]):
        """Read posts from a dictionary

        Parameters
        ----------
        posts : dict[dict[str, ...]]
            A dict of dicts of the posts, i.e., posts = {'post-name': {'name': 'A post', 'year': 2021, ...}}

        Returns
        -------
        obj : Posts
            A Posts object
        """
        obj = cls()
        for key, value in posts.items():
            obj.posts[key] = Post.readDictionary(value)
        return obj

    @classmethod
    def readDictionary(cls, data: dict):
        return cls.readPosts(data['posts'])

    def generate(self, fileDir: str = '.'):
        """
        Generate posts

        Parameters
        ----------
        fileDir : str
            File dir of the generated posts
        """
        for generator in self.posts.values():
            generator.generate(fileDir)

    def new(self, name: str, year: int, month: int, day: int, title: str, abstract: str, permalink: str,
            options: dict[str, str] = None, categories: list[str] = None, tags: list[str] = None,
            publisher_link: str = '', google_scholar_link: str = '', pdf_path: str = '', bib_key: str = '') -> \
            Post:
        """Create new post

        Parameters
        ----------
        name : str
            Name of the post
        year : int
            Year
        month : int
            Month
        day : int
            Day
        title : str
            Title of the post
        abstract : str
            Abstract of the post
        permalink : str
             permanent link of the post
        options : dict[str, str]
            Options in the front matter
        categories : list[str]
            Categories of the post
        tags : list[str]
            Tags of the post
        publisher_link : str
            Publisher link of the post
        google_scholar_link : str
            Google Scholar link of the post
        pdf_path : str
            Pdf path of the post
        bib_key : str
            BibTeX key of the post

        Returns
        -------
        generator : Post
            A PostGenerator object
        """
        if options is None:
            options = {}
        if categories is None:
            categories = []
        if tags is None:
            tags = []

        generator = Post(name, year, month, day, title, abstract, permalink, options, categories, tags,
                         publisher_link, google_scholar_link, pdf_path, bib_key)
        self.posts.update({name: generator})
        return generator
