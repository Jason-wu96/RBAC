import re

ret = re.match('^/delete/(\d+)$','/delete/4')
if ret:
    print(True)
else:
    print(False)