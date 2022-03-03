from enum import Enum


class SearchMethod(str, Enum):
    bm25 = "bm25"
    keyword = "keyword"
    regex = "regex"
    tf_idf = "tf-idf"
