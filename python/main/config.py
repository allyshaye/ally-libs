import configargparse
import configparser
import argparse
import logging

""" Module for adding config options to apps """


class SetLogLevel(argparse.Action):
	def __call__(self, parser, namespace, values, option_string=None):
		level = getattr(logging,values.upper())
		setattr(namespace, self.dest, level)


def get_basic_parser():
	p = configargparse.ArgParser(description='config parser')
	d = p.add_argument_group(
		title='default config options',
		description='app agnostic configuration options')
	d.add_argument('--config', '-c',
		required=False,
		help='path to config file',
		is_config_file=True)
	d.add_argument('--env',
		required=False,
		choices=['prod', 'dev', 'staging'],
		help='environment for runtime')
	d.add_argument('--loglevel', 
		default='INFO',
		choices=['INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'],
		help='log level to use for logging',
		type=str,
		action=SetLogLevel)
	return p

