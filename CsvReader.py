import os
import configparser
import logging
import datetime
import csv

#Getting the current working directory and checking the file which ends with .csv (Assuming only one file is present in the directory)
#write a function to
class csvreader(object):

    def __init__(self):
        config = configparser.ConfigParser()
        config.read("info.cfg")
        self.directory= config.get('client','directory')

    def reader(self):
        name = str(datetime.date.today()) + ".log"
        logging.basicConfig(filename=name, level=logging.DEBUG)

        ofile=''
        for file in os.listdir(self.directory):
            if file.endswith(".csv"):
                ofile=file
        if ofile=="":
            logging.error("There is no csv file")
        c.validation(ofile)
        return ofile

    def validation(self,file):
        f = open(file)
        reader = csv.reader(f)
        for each in reader:
            if each[23] =="Building":
                if each[24]=="Room":
                    if each[25]=="Rack":
                        logging.info("The csv file is verified")
                        return
            else:
                logging.error("Please check the CSV file")
                exit()



c=csvreader()

