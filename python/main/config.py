import configargparse
import configparser

""" Module for adding config options to apps """


def add_config_options(p):
	d = p.add_argument_group(
		title='default config options',
		description='app agnostic configuration options')
	d.add_argument('--config', '-c',
		required=False,
		help='path to config file',
		is_config_file=True,)
	d.add_argument('--env',
		required=False,
		type=str,
		choices=['prod', 'dev', 'staging'],
		help='environment for runtime')
	d.add_argument('--log-level',
		default='INFO',
		type=str,
		choices=['INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'],
		help='log level to use for logging')
	args = p.parse_args()
	return args
