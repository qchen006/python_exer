import threading,time

class FileWriter(threading.Thread):
    def __init__(self,fileName, num):  
        threading.Thread.__init__(self,name="fileWriter"+bytes(num))
        self.__fileName__=fileName;
        self.__num__=num
        
    def run(self):
        for i in range(10):  
            output = open(self.__fileName__, 'a')
            output.write("teststr"+bytes(self.__num__))
            output.flush()
            output.close()
            
            time.sleep(1)