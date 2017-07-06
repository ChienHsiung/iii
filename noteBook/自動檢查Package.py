import subprocess
import importlib

def install(app):
    ckApp = importlib.util.find_spec(app)
    if not ckApp:
        subprocess.call(['pip','install',app])
    else:
        subprocess.call(['pip','uninstall',app,'-y'])

install('tornado')


# print('hello')
# get_ipython().system('pip install lxml')
# get_ipython().system('pip uninstall lxml -y')
# get_ipython().system('pip install lxml')