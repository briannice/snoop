from pages.Page import Page


class SniffPage(Page):

    def __init__(self,  *args, **kwargs):
        super().__init__("green", *args, **kwargs)
