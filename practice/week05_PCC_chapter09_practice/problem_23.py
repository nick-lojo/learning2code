# A streaming platform has a general content type in their system.
# Podcast episodes are a specific kind of content.
# The way podcast episodes are previewed is completely different
# from how general content handles previews.
#
# Build this out and show that the child's preview behavior
# replaces the parent's entirely.

class GeneralContent:
    """Models general content for a streaming platform."""
    def __init__(self, content_form):
        self.content_form = content_form
    
    def preview(self):
        """Prints instructions for content preview."""
        print(f"Release the {self.content_form} trailer to YouTube.")

class Podcast(GeneralContent):
    """A special kind of content to model."""
    def __init__(self, av_mix, content_form='podcast'):
        """Attributes from parent class and new attributes for podcast."""
        super().__init__(content_form)
        self.av_mix = av_mix
    
    def preview(self):
        """Prints instructions for podcast content preview."""
        print(f"Post a clip of the {self.content_form} to TikTok.")

tv_0 = GeneralContent('TV show')
tv_0.preview()

podcast_0 = Podcast('audio and video')
podcast_0.preview()