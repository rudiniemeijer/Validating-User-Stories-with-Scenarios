import logging

logformat = "%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logfile = "./example.log"
loglevel = logging.INFO
#loglevel = logging.DEBUG

my_formatter = logging.Formatter(logformat)
my_handler = logging.FileHandler(logfile)
my_handler.setFormatter(my_formatter)

my_logger = logging.getLogger('root_name')
my_logger.addHandler(my_handler)
my_logger.setLevel(loglevel)

my_logger.info("We're on info!")
my_logger.debug("And on debug!")
