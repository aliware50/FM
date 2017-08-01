# -*- coding: utf-8 -*-
import pandas as pd
import pymysql


dbconn = pymysql.connect(
    host="10.198.197.158",
    database="featureengine",
    user="root",
    password="123456",
    port=3306,
    charset='utf8'
)


sql = "select fieldname, transform from featuremetadata where modelname='pre_credict_user_fm_new'"
config = pd.read_sql(sql, dbconn)


