# coding: utf-8
# 爬取 doubantop250 第一页页面
import os
import requests
from pyquery import PyQuery as pq


class Model(object):
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    def __init__(self):
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def movie_from_div(div):
    e = pq(div)
    m = Movie()
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()
    return m


def movies_from_url(url):
    r = requests.get(url)
    page = r.content
    e = pq(page)
    items = e('.item')
    movies = [movie_from_div(i) for i in items]
    return movies


def main():
    url = 'https://movie.douban.com/top250'
    movies = movies_from_url(url)
    print('top250 movies', movies)


if __name__ == '__main__':
    main()
