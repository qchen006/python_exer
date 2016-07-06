'''
Delete all keys using wild char expression
'''
import redis

if __name__ == '__main__':
    redisClient = redis.Redis(host='localhost', port=6379, db=0)
    expressions = ("words*","documents","next_document_id")
    for expression in expressions:
        for key in redisClient.keys(expression):
            redisClient.delete(key)
            print "deleted key "+key
