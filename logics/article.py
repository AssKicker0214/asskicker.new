import data.article as db
import time


class Article:
    def __init__(self, aid=None):
        self._aid = aid

        found = db.find(aid)
        self._data = found if found is not None else Article.create_empty()
        self._exists = True if found is not None else False

    @property
    def exists(self):
        return self._exists

    def get(self) -> dict:
        return self._data

    def update(self, d: dict, and_save=True):
        assert self._aid == self._data['_id']
        self._data = d
        if and_save:
            self.save()

    def save(self):
        if self._aid is None:
            self._data['_id'] = self._aid = db.next_id()
        print(self._data)
        db.save(self._data)

    def validate(self):
        """
        todo `pip install schema` to do validation
        :return:
        """

    def get_meta(self):
        return {
            'html_title': self._data['title'] or "创建",
            'keywords_content': ', '.join(self._data['keywords']),
            'aid': self._aid
        }

    @staticmethod
    def create_empty() -> dict:
        return {
            "title": None,
            'keywords': [],
            'content': "",
            'on_create': int(time.time()),
            'on_update': int(time.time()),
            'public': True
        }
