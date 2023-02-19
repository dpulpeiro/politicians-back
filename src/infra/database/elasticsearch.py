from elasticsearch8 import Elasticsearch

from config import settings

elasticsearch = Elasticsearch(settings.ELASTICSEARCH_URL)
