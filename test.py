import json
import subprocess
import sys
with open('data.txt') as json_file:
    data=json.load(json_file)
    uninstalled=[]
    print("started installing dependencies")
    for key in data['Dependencies']:
        try :
            subprocess.check_output([sys.executable, '-m', 'pip', 'install', '{}=={}'.format(key,data['Dependencies'][key])],stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            uninstalled.append(key+"=="+data['Dependencies'][key])
    if len(uninstalled)!=0:
        print("unable to install")
        for d in uninstalled:
            print(d)
    else:
        print("succesfully installed all dependencies")
    




