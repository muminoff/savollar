from cqlengine import columns
from cqlengine.connection import setup
from scrapy.conf import settings
from models import SavolModel


def main():
    setup(settings["CASSANDRA_CLUSTER"], settings["CASSANDRA_KEYSPACE"])
    print "Gettings first 100 models from DB:"
    for model in SavolModel.objects.all()[:100]:
        print model.savol_id
        print "---------------------"
        print model.title
        print model.question
        print model.answer
        print model.year
        print model.month
        print model.date
        # print "{year}/{month}/{date}".format(
        #     year=model.year,
        #     month=model.month,
        #     date=model.date
        # )
        print "---------------------" 


if __name__ == '__main__':
    main()
