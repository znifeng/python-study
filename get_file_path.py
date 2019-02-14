import os
print os.path.realpath(__file__)
print os.path.split(os.path.realpath(__file__))[0]
