import redis
import datetime
import random

redisClient = redis.Redis(host='localhost', port=6379, db=0)

def add_hit(id, date=datetime.date.today()):
    redisClient.sadd("clients",id)
    redisClient.hincrby("stats/client:"+id, "total", 1)
    redisClient.hincrby("stats/client:"+id, datetime.date.strftime(date, '%Y-%m-%d'), 1)


def gnerateData(year):

    yearStart = datetime.datetime.strptime(str(year)+'-01-01', '%Y-%m-%d').date()
    yearEnd = datetime.datetime.strptime(str(year)+'-12-31', '%Y-%m-%d').date()

    ids = ("001","002","003","004","005","006")

    while yearStart<yearEnd:
        for i in range(1, random.randint(100, 200)):
            add_hit(random.choice(ids), yearStart)

        yearStart = yearStart + datetime.timedelta(days=1)

    print "data generated"


def get_total_hit(id):
    return redisClient.hget("stats/client:"+id,"total")

def get_hit_between(id, start, end):
    begin_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()

    return redisClient.hmget("stats/client:"+id, keys(begin_date,end_date))

def keys(start,end):
    while start < end:
        yield start
        start = start + datetime.timedelta(days=1)

def top_clients(period="total", limit=3):
    return redisClient.sort("clients",by="stats/client:*->"+period,get=["#","stats/client:*->"+period],start=0,num=limit,desc=True)




if __name__ == '__main__':
    #gnerateData(2016)

    print get_hit_between('001', '2016-02-01','2016-03-01')
    print top_clients(limit=6)
