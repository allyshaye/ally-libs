import logging
import configargparse
import main.config as config



class App():


	def get_basic_parser(self):
		return config.get_basic_parser()


	def get_logger(self,log_level=20):
		logging_format = '%(asctime)s - %(filename)s - %(funcName)s (%(levelname)s):  %(message)s'
		date_format = '%m/%d/%Y %I:%M:%S%p'
		logging.basicConfig(
			format=logging_format,
			datefmt=date_format,
			level=log_level)
		logger = logging.getLogger(__name__)
		return logger


	def start(self):
		logger = self.get_logger()
		logger.info("APP START")
		self._run()
		self.cleanup()


	def _run(self):
		pass


	def cleanup(self):
		pass
