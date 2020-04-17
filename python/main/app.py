import logging
import configargparse
import main.config as config
from abc import ABC, abstractmethod 



class App(ABC):

	parser = configargparse.ArgParser(description='config parser')


	def add_config_options(self, p):
		self.args = config.add_config_options(p)


	def eval_log_level(self,args):
		pass


	def get_logger(self):
		logging_format = '%(asctime)s - %(filename)s - %(funcName)s (%(levelname)s):  %(message)s'
		date_format = '%m/%d/%Y %I:%M:%S %p'
		logging.basicConfig(
			format=logging_format,
			datefmt=date_format,
			level=logging.DEBUG)
		logger = logging.getLogger(__name__)
		return logger


	def start(self):
		LOG = self.get_logger()
		self._run()



	def _run(self):
		pass


if __name__=="__main__":
	App.start()
