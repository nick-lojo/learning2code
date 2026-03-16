# A news platform stores articles in code.
# Each article has an embedded media component
# that is detailed enough to warrant its own representation.
#
# Build an article that owns its media component.
# Access and interact with the component through the article.

class EmbeddedMedia:
    """A class that can be used as an attribute for an article."""
    def __init__(self, media_type):
        self.media_type = media_type
    
    def share_media(self):
        """A method that states the file embedded in the article."""
        if self.media_type == 'photo':
            print(f"\nThere is a {self.media_type} .jpeg embedded in this article.")
        elif self.media_type == 'video':
            print(f"\nThere is a {self.media_type} .mov embedded in this article.")
        else:
            print("You can only embed photos or videos into articles.")

class Article:
    """A class used to store articles for a news website."""
    def __init__(self, title, author, year_published, embedded_media):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.embedded_media = EmbeddedMedia(embedded_media)
    
    def article_details(self):
        """Prints key details about the article."""
        message = f'\nArticle Title: "{self.title.title()}"'
        message += f'\n\tAuthor: {self.author.title()}'
        message += f'\n\tPublication Year: {self.year_published}'
        print(message)
        self.embedded_media.share_media()

article_0 = Article('patriots win super bowl 51', 'jane doe', 2017, 'video')
article_0.article_details()