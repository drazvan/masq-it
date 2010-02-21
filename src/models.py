from google.appengine.ext import db

class Space(db.Model):
    ''' Information about a space 
    
    '''
    
    name = db.StringProperty()
        
        
    def __unicode__(self):
        return '[space: %s]' % (self.name)
    
