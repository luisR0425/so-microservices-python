from subprocess import Popen, PIPE

def get_all_users():
  grep_process = Popen(["grep","/bin/bash","/etc/passwd"], stdout=PIPE, stderr=PIPE)
  user_list = Popen(["awk",'-F',':','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,user_list)

def add_user(username,password):
  add_process = Popen(["sudo","adduser","--password",password,username], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if username in get_all_users() else False

def remove_user(username):
  vip = ["operativos","jenkins","postgres","root","Daniel"]
  if username in vip:
    return True
  else:
    remove_process = Popen(["sudo","userdel","-r",username], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if username in get_all_users() else True

def get_data_user(username):
 if username in get_all_users():
  grep = Popen(["grep", username, "/etc/passwd"], stdout=PIPE, stderr=PIPE)
  usuario = grep.communicate()[0]
  return usuario
 else:
  return False

def recently_logged():
  grep_process = Popen(["lastlog","-t","1"], stdout=PIPE, stderr=PIPE)
  user_list = Popen(["awk",'-F',' ','{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,user_list)

def commands(username):
   
  if username in get_all_users():
   grep_process = Popen(["cat","/home/"+username+"/.bash_history"], stdout=PIPE, stderr=PIPE)
   user_list = Popen(["awk",'{print $1}'], stdin=grep_process.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
   return filter(None,user_list)
  else:
   return False
