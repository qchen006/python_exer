import threading,time

class FileReader(threading.Thread):
    def __init__(self,fileName):  
        threading.Thread.__init__(self,name="fileReader")
        self.__fileName__=fileName;
        
    def run(self):
        for i in range(10):  
            file_object = open(self.__fileName__)
            try:
                all_the_text = file_object.read()
                print(all_the_text)
            finally:
                 file_object.close()
            
            time.sleep(1)