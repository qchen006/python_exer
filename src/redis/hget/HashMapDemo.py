__author__ = 'hadoop'

import redis

redisClient = redis.Redis(host='localhost', port=6379, db=0)

redisClient.hset('user:a', 'name', 'namea');
redisClient.hset('user:a', 'age', 22);
redisClient.hset('user:a', 'gender', 'F');

redisClient.hset('user:b', 'name', 'nameFor B');
redisClient.hset('user:b', 'age', 32);
redisClient.hset('user:b', 'gender', 'M');

redisClient.hset('user:c', 'name', 'nameC');
redisClient.hset('user:c', 'age', 40);
redisClient.hset('user:c', 'gender', 'M');

nameA = redisClient.hget('user:a', 'name');

print 'name for user a is ' + nameA;
print 'age for user b is ' + redisClient.hget('user:b', 'age');

userList = list(['user:a','user:b',"user:c"])


'''
Delete all members in the session first
'''

for user in userList:
    redisClient.srem('circle:game:lol',user)
    redisClient.srem('circle:game:dota',user)


redisClient.sadd("circle:game:lol", "user:a")
redisClient.sadd("circle:game:lol", "user:c")

redisClient.sadd("circle:game:dota", "user:b")
redisClient.sadd("circle:game:dota", "user:c")

circleLolSet = redisClient.smembers("circle:game:lol");
print 'member in circle game<LOL> '+ str(circleLolSet)

print 'they are:'

for gameMember in circleLolSet:
    print '     '+ redisClient.hget(gameMember,'name')


print '================================'

circleDotaSet = redisClient.smembers("circle:game:dota");
print 'member in circle game<DOTA> '+ str(circleDotaSet)

print 'they are:'

for gameMember in circleDotaSet:
    print '     '+ redisClient.hget(gameMember,'name')


print '================================'

gameInterSet = redisClient.sinter("circle:game:lol","circle:game:dota")
print 'member in two games '+ str(gameInterSet)

print 'they are:'

for gameMember in gameInterSet:
    print '     '+ redisClient.hget(gameMember,'name')
