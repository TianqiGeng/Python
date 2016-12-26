import os
import time
source=[r'C:\Python27\example\for.py', r'C:\Python27\example']
target_dir=r'D:\Python27\example\d'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command="zip -qr '%s' %s" %(target,''.join(source))
if os.system(zip_command)==0:
    print 'successful',target
else:
    print 'back falled'

