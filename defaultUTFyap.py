#-*-coding:utf-8-*-
#python2.x encode olarak ascii ayarlı gelir 
#bunun default olarak değiştirilmesini isterseniz
#bunu aşağıdaki şekilde yapabilirsiniz. 

import sys
sys.getdefaultencoding()
sys.setdefaultencoding('utf-8')
# bu kısımda hata alırsanız aşağıdaki kodları açın
#reload(sys)
#sys.setdefaultencoding('utf-8')