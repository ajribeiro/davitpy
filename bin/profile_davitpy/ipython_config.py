# Configuration file for ipython.
# DaViT-py

c = get_config()

c.TerminalIPythonApp.display_banner = True
c.InteractiveShellApp.log_level = 20
# c.InteractiveShellApp.extensions = []
c.InteractiveShellApp.exec_lines = [
	'import numpy',
	'import scipy',
	'import matplotlib as mplot',
	'import pylab',
	'import h5py',
	'import pydarn',
	'import math as *',
	'import string',
	'%load_ext autoreload',
	'%autoreload 2'
]
# c.InteractiveShellApp.exec_files = []
c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False
c.InteractiveShell.deep_reload = True
c.InteractiveShell.editor = 'vi'
c.InteractiveShell.xmode = 'Context'

c.PromptManager.in_template  = 'In [\#]: '
c.PromptManager.in2_template = '   .\D.: '
c.PromptManager.out_template = 'Out[\#]: '
c.PromptManager.justify = True

c.PrefilterManager.multi_line_specials = True

c.AliasManager.user_aliases = [
 ('la', 'ls -al')
]
