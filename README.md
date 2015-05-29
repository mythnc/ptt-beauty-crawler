Special thanks to [c3h3](https://github.com/c3h3) for his great [course materials](https://github.com/c3h3/NCCU-PyData-Courses-2013Spring) and [tzangms](https://github.com/tzangms) for his great [talk](https://speakerdeck.com/tzangms/xiao-hai-yan-xuan) in PyCon APAC 2014.

# Introduction


[PTT](http://en.wikipedia.org/wiki/PTT_Bulletin_Board_System) is the largest terminal-based bulletin board system (BBS) based in Taiwan. [Beauty Board](https://www.ptt.cc/bbs/Beauty/index.html) is one of the most popular board on it. There are a lot of users post images in it.

This application try to crawl all available images URLs from Beauty Board, store them in database, and you can make your own thing by this dataset. For example, you can make a [website](http://minstrel.tw/beauty) show images.



# Prerequisites

1. Download [MongoDB](https://www.mongodb.org/) and install it.

2. Install packages in the `requirements.txt`

```
$ pip install -r requirements.txt
```

# Usage

There are 2 files: `beauty_crawler.py` and `beauty_query.py`. One for create or update dataset, and the other for query dataset and output html format result.

## Create dataset

You can crawl your own dataset by `$ python beauty_crawler.py` 

or restore the existing dataset in `dump/` directory by `$ mongorestore`

## Update dataset

Change the `update` parameter of `save_all_articles_to_db(update=False)` to `True` in the main section, and then execute it.

```
$ python beauty_crawler.py
```

It will update the dataset of latest articles within one month.

## Query dataset
Execute `beauty_query.py` will try to output html format result. You can redirect it to a file, then open it by browser. 

```
$ python beauty_query.py > test.html
```

# Dataset Parameter
* date: the post date of article
* title: title of article
* author: author of article
* push: commendation number
* pic: Image URLs
* url: Article URL
