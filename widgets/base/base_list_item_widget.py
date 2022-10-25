from PyQt5.QtWidgets import QListWidgetItem


class BaseListItemWidget(QListWidgetItem):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
