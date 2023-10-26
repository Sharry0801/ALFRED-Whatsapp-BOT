import sys
import importlib
import contextlib
import subprocess
from io import StringIO

@contextlib.contextmanager
def stdoutIO(stdout=None):
	old = sys.stdout
	if stdout is None:
		stdout = StringIO()
	sys.stdout = stdout
	yield stdout
	sys.stdout = old

def execute_python(code):
	with stdoutIO() as c:
		try:
			exec(code)
		except:
			print("there is something wrong with this code sir.")
	return c.getvalue()

def install_package(package):
	try:
		importlib.import_module(package)
		return f'{package} is already installed sir'
	except:
		subprocess.check_call([sys.executable, "-m", "pip", "install", package])
		return f'{package} installed successfully sir'