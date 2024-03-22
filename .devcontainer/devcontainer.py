#!/usr/bin/env python3
import os,sys,time,pwd

def get_username():
    return str(pwd.getpwuid(os.getuid())[0])

def run(cmd):
	try:
		print(cmd);os.system(cmd)
	except:pass

def apt(string, use_sudo=False):
	run("{0} apt-get update".format("sudo " if use_sudo else ""))
	run("{0} apt-get install -y {1}".format("sudo " if use_sudo else "",string))

def try_apt(string):
	try:apt(string, use_sudo=True)
	except:pass
	try:apt(string, use_sudo=False)
	except:pass

def pip(string):
	run("{0} -m pip install --upgrade {1}".format(sys.executable, string))

[pip(x) for x in "funbelts when-changed xonsh[full] mystring hugg[all] sdock[all] malloy ruff"];import funbelts as ut
apt("sqlite3")

devcontainer = os.path.join(os.path.dirname(__file__), 'devcontainer.json')
for extension in ut.cmt_json(devcontainer)['customizations']['vscode']['extensions']:
	run(f"code-server --install-extension {extension}")

try_apt("tmux neovim curl wget p7zip-full")

run("docker pull frantzme/scalapy:lite")
for x in "pip mystring[all] hugg[all] sdock xonsh suplemon jupyter-book jupyter-lab when-changed python-minifier pandoc bython".split(" "):
	pip(x)


run("docker pull frantzme/texbuilder:2020")

if False:
	while not os.path.exists("/var/run/docker.sock"):
		print(".",end='',flush=True)
		run("/usr/local/share/docker-init.sh")
		time.sleep(1)
	run("service docker restart")
