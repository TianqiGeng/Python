import os
import time
source=[r'C:\Python27\example\cat.py',r'C:\Python27\example\for.py']

target_dir=r'C:\Python27\example\d'
today=target_dir+os.sep+time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')

comment=raw_input('Enter a comment-->')
if len(comment)==0:
    target=today+os.sep+now+'.rar'
else:
     target=today+os.sep+now+'_'+comment.replace('','_')+'.rar'
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today

print source
print target
 
rar_command= '"C:\Python27\example\WinRAR.exe" a %s %s' %(target,' '.join(source))
print(rar_command)
print(os.system(rar_command))
if os.system(rar_command)==0:
    print 'Successful ',target
else:
    print 'fail'
