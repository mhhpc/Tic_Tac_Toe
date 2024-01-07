from subprocess import Popen 

commands = ['server.py', 'player.py', 'player.py'] 
procs = [ Popen(['python', i]) for i in commands ] 
for p in procs:
   p.wait()