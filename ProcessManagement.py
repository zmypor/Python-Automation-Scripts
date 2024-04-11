import psutil

def get_running_processes():

  return [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]

def kill_process_by_name(process_name):

  for p in psutil.process_iter(['pid', 'name', 'username']):
    if p.info['name'] == process_name:
      p.kill()