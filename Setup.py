import logging
import os
import datetime

module =["os","csv","json","logging","requests","datetime"]
# Creating the Log File based on the date, so that each day has a different log file.
name = str(datetime.date.today()) + ".log"
logging.basicConfig(filename=name, level=logging.DEBUG)


for each in module:
    try:
        __import__('imp').find_module(each)
    except ImportError:
        logging.error("The following module"+ each +"is not present in your system")
        sudoPassword = raw_input("Please enter your system password")
        command = 'sudo apt-get install python-'+each
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))