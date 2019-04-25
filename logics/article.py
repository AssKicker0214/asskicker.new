import time
from typing import List

import data.article as db


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

    def update(self, d: dict, and_save=True) -> int:
        assert self._aid == self._data['_id']
        self._data = d
        if and_save:
            self.save()
        return self._aid

    def save(self) -> None:
        if self._aid is None:
            self._data['_id'] = self._aid = db.next_id()
        db.save(self._data)

    def validate(self):
        """
        todo `pip install schema` to do validation
        :return:
        """

    def get_meta(self) -> dict:
        return {
            'aid': self._aid,
            'html_title': self._data['title'] or "创建",
            'keywords_content': ', '.join(self._data['keywords']),
            'keywords': self._data['keywords'],
            'on_create': self._data['on_create'],
            'on_update': self._data['on_update']
        }

    @staticmethod
    def create_empty() -> dict:
        return {
            '_id': None,
            "title": None,
            'keywords': [],
            'content': "",
            'on_create': int(time.time()),
            'on_update': int(time.time()),
            'public': True
        }

    @staticmethod
    def get_all(public_only=True) -> List['Article']:
        articles = []
        for aid in db.find_all(public_only):
            articles.append(Article(aid=aid))
        return articles
