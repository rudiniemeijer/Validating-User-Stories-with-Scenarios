import logging

logformat = "%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logfile = "./example.log"
loglevel = logging.INFO

my_formatter = logging.Formatter(logformat)
my_handler = logging.FileHandler(logfile)
my_handler.setFormatter(my_formatter)
my_handler.setLevel(loglevel)

my_logger = logging.getLogger('root_name')
my_logger.addHandler(my_handler)

my_logger.info("We're on!")
