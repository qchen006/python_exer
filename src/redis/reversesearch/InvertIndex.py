import redis
import os
import pkg_resources
from redis.exceptions import WatchError


class WordCollector(object):
    '''
    Demostrates usage of file, map lamda, redis, WATCH, MULTI
    '''
    STOP_WORDS = list(["the", "is"])
    """
    The class level static stop words
    """

    def __init__(self):
        self.__redisClient = redis.Redis(host='localhost', port=6379, db=0)

    def storeFileWords(self, dirOrFileName):
        try:
            for root, dirs, files in os.walk(dirOrFileName):
                for file in files:
                    absFilePath = os.path.join(root, file)
                    lines = open(absFilePath).readlines()
                    docId = self.__idForDocument(absFilePath)

                    '''
                    Only when the document is not now storing in Redis, we will store the lines
                    '''
                    if docId == '' or docId is None:
                        docId = self.__addFilenameDocMapping(absFilePath)

                        for line in lines:
                            for word in line.split(" "):
                                self.__addWordIfNecc(docId, word)

        except IOError:
            print "file not exists"
            raise IOError("file not exists")

    def __addFilenameDocMapping(self, fileName):
        '''
        add the mapping for Document id and filename mapping, return the new created document id
        '''
        doc_id = self.__redisClient.incr("next_document_id")
        self.__redisClient.hset("documents", fileName, doc_id)
        self.__redisClient.hset("filenames", doc_id, fileName)

        return doc_id

    def __idForDocument(self, fileName):
        doc_id = self.__redisClient.hget("documents", fileName)
        return doc_id

    def __addWordIfNecc(self, docId, word):
        if len(word) > 2 and word not in self.__class__.STOP_WORDS:
            self.__redisClient.zincrby("words:" + word, docId, 1)


class WordSearcher(object):
    def __init__(self):
        self.__redisClient = redis.Redis(host='localhost', port=6379, db=0)

    def _wordTranslate(self, word):
        return "words:" + word

    def search(self, words):
        '''
        do in transaction, using watch and execute,
        '''
        tempset = "temp_set"

        pipe = self.__redisClient.pipeline()
        while 1:
            try:
                pipe.watch(tempset)

                pipe.multi()

                pipe.zinterstore(tempset, map(self._wordTranslate, words))
                pipe.zrevrange(tempset, 0, -1, False)

                multiResults = pipe.execute()
                docIdSet = multiResults[len(multiResults)-1]

                break
            except WatchError:
                print "watcherror happens"
                continue
            finally:
                pipe.reset()


        print "doc id set is "+ str(docIdSet)
        result = self.__redisClient.hmget("filenames", docIdSet)


        return result


if __name__ == '__main__':
    wordCollector = WordCollector()

    abs_file_name = pkg_resources.resource_filename(__name__, "file")
    print abs_file_name
    wordCollector.storeFileWords(abs_file_name)

    searcher = WordSearcher()
    words = list(["how", "are"])
    print "files containing all the words are \n" + str(searcher.search(words))
