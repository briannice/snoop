from pages.Page import Page


class CreatePage(Page):

    def __init__(self,  *args, **kwargs):
        super().__init__("blue", *args, **kwargs)
