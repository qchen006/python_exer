import redis
import datetime
import random

redisClient = redis.Redis(host='localhost', port=6379, db=0)


def add_hit(clientId, date=datetime.date.today()):
    redisClient.sadd("clients", clientId)
    redisClient.zincrby("stats/client:total", clientId, 1)
    redisClient.zincrby("stats/client:" + datetime.date.strftime(date, '%Y-%m-%d'), clientId, 1)


def gnerateData(year):
    yearStart = datetime.datetime.strptime(str(year) + '-01-01', '%Y-%m-%d').date()
    yearEnd = datetime.datetime.strptime(str(year) + '-12-31', '%Y-%m-%d').date()

    ids = ("001", "002", "003", "004", "005", "006")

    while yearStart < yearEnd:
        for i in range(1, random.randint(10, 20)):
            add_hit(random.choice(ids), yearStart)

        yearStart = yearStart + datetime.timedelta(days=1)

    print("data generated")


def get_total_hit(clientId):
    return redisClient.zscore("stats/client:total", clientId)


def get_hit_between(clientId, start, end):
    begin_date = datetime.datetime.strptime(start, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d").date()

    result = []

    for day in keys(begin_date, end_date):
        dayStr = day.strftime('%Y-%m-%d')
        result.append((day, redisClient.zscore("stats/client:" + dayStr, clientId)))

    return result


def keys(start, end):
    while start < end:
        yield start
        start = start + datetime.timedelta(days=1)


def top_clients(period="total", limit=3):
    return redisClient.zrevrange("stats/client:total",start=0, end=limit,withscores=True)


if __name__ == '__main__':
    # gnerateData(2015)

    print(get_hit_between('001', '2015-02-01', '2015-03-01'))
    print(top_clients(limit=3))
