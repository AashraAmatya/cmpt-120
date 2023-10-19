from datetime import datetime 

log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"

def log(message):
    log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"
    with open(log_file,"a") as file: 
        file.write(f"[{datetime.today().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

        #print (("log-file-" + datetime.today().strftime('%Y-%m-%d') + " " + datetime.now().strftime("%H:%M:%S") + ".log " + message))

def dump():
    log_file = "log-file-" + datetime.today().strftime('%Y-%m-%d') + ".log"
    the_file = open(log_file,"r")
    read_out = the_file.read()
    the_file.close()
    print(read_out)


log("yes")
dump()
