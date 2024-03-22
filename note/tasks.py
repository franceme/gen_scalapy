#!/usr/bin/env python3
import os,sys

run = lambda x:os.system(x)
imp = lambda x:run("{0} -m pip install --upgrade {1}".format(sys.executable, x))

imp("pip invoke");from invoke import task

@task
def install(c=None):
	pips, start = [], False
	with open("environment.yml", "r") as reader:
		for line in reader.readlines():
			if start and "#" not in line:
				pips += [
					str(line.split(" - ")[-1]).strip()
				]
			elif "pip:" in line:
				start = True
	imp(' '.join(pips))

@task
def build(c=None):
	run("jupyter-book build lectures/")

@task
def clean(c=None):
	run("yes|rm -r lectures/_build/")

@task
def syncfig(c=None):
	import shutil
	try:
		if os.path.exists("lectures/iframe_figures/"):
			shutil.move(
				"lectures/iframe_figures/",
				"lectures/_build/html/iframe_figures/"
			)
	except:pass

@task
def full(c=None):
	clean(c)
	install(c)
	build(c)
	syncfig(c)

@task
def gitr(c):
	for x in [
		'git config --global user.email "EMAIL"',
		'git config --global user.name "UserName (dev@lite)"'
	]:
		print(x);os.system(x)

@task
def cleanenv(c):
	for x in [
		'CachedExtensions/',
		'CachedExtensionVSIXs/',
		'User/',
		'Machine/',
		'extensions/',
		'logs/',
		'coder.json',
		'machineid',
	]:
		x = "yes|rm -r " + str(x)
		print(x);os.system(x)

@task
def execute(c):
	print("Executing")
