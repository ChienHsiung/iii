import os
import sys
import codecs
sys.stdout = codecs.getwriter('cp950')(sys.stdout)
# sys.stdout = codecs.getwriter('utf8')(sys.stdout)
env = os.environ
# for myos in env:
#     print(myos)
#     print("")
# print(sys.stdout.encoding)
# print(sys.stdout.isatty())
# print(sys.getfilesystemencoding())

