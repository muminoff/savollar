from cqlengine import columns
from cqlengine.connection import setup
from scrapy.conf import settings
from models import SavolModel


def main():
    setup(settings["CASSANDRA_CLUSTER"], settings["CASSANDRA_KEYSPACE"])
    model = SavolModel.objects.all()[0]
    print model.savol_id


if __name__ == '__main__':
    main()
