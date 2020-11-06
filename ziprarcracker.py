import zipfile

banner = print( '''
 _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
 _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
              _______          _______                _____                _                 
             |___  (_)        / /  __ \              / ____|              | |                 
                / / _ _ __   / /| |__) |__ _ _ __   | |     _ __ __ _  ___| | _____ _ __      
               / / | | '_ \ / / |  _  // _` | '__|  | |    | '__/ _` |/ __| |/ / _ \ '__|     
              / /__| | |_) / /  | | \ \ (_| | |     | |____| | | (_| | (__|   <  __/ |        
             /_____|_| .__/_/   |_|  \_\__,_|_|      \_____|_|  \__,_|\___|_|\_\___|_|  v1.0  
                     |_|        |_|         |_|            |_|            |_|      |_|                 
 _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
 _+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_By: Faisal_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+

''')

txtfile = input("Password List Location (example: Rockyou.txt): ")
filename = input("Zip/Rar File Location (example: locked.zip): ")
count = 1

with open(txtfile,'rb') as text:
    for entry in text.readlines():
        password = entry.strip()
        try:
            with zipfile.ZipFile(filename,'r') as zf:
                zf.extractall(pwd=password)

                data = zf.namelist()[0]

                data_size = zf.getinfo(data).file_size

                print('''\n[+] Password found! - %s\n ~%s\n ~%s\n''' 
                    % (password.decode('utf8'), data, data_size))
                break

        except:
            number = count
            print('[%s] [-] Password failed! - %s' % (number,password.decode('utf8')))
            count += 1
            pass