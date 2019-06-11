mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

import mystuff

mystuff.apple()
print(mystuff.tangerine)

class MyStuffs(object):

    def __init__(self):
        self.tangerines = "And now a thousand years between."
        
    def apple(self):
        print("I AM CLASSY APPLES")
        
        
things = MyStuffs()
things.apple()
print(things.tangerines)