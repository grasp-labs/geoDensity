import psycopg2
import csv
# relative and fixed imports
from config.db.config import config
from config.db.connect import setup_db
from geodensity.tasks import query_data
from geodensity.querries import geonorge, enhetsreg
# from .models import YOUR_MODEL


def query_data(query, filepath):
    """
    Sample function to collect application layer data and write
    to .csv file taking query and filepath as input. Adjust function to suit your needs.
    """
    conn = setup_db(config(section="DATABASE"))
    sql = query
    cursor = conn.cursor() # cursor_factory=psycopg2.extras.DictCursor
    cursor.execute(sql)
    while True:
        rows = cursor.fetchmany(200)
        if not rows:
            break
        with open(filepath, 'w') as f:
            writer = csv.writer(f, delimiter=',')
            for row in rows:
                writer.writerow(row)
    if cursor:
        cursor.close()
    return True


def example_store_data_to_model(query):
    """
    Example function to store data to project DB
    """
    YOUR_MODEL = "" # replace by proper model with aligned variables
    YOUR_MODEL.objects.all().delete()
    conn = setup_db(config(section="DATABASE"))
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(query)
    while True:
        objs = []
        rows = cursor.fetchmany(200)
        if not rows:
            break

        for row in rows:
            obj = TaxAnomalies(**row)
            objs.append(obj)
        YOUR_MODEL.objects.bulk_create(objs)

    if cursor:
        cursor.close()
    return True


def sample_create_csvs():
    """
    Example function to get some data
    """
    geonorge_filepath = 'geodensity/data/geonorge.csv'
    enhetsreg_filepath = 'geodensity/data/enhetsreg.csv'

    query_data(query=geonorge, filepath=geonorge_filepath)
