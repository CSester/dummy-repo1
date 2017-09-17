from fabric.api import run, env

def runDeploy():
  print(env)
  run('echo "dummy dump" >> dump.txt')
