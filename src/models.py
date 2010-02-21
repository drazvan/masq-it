from google.appengine.ext import db

class Space(db.Model):
    ''' Information about a space 
    
        This is stored on Google DataStore. We cand add many types of information here.
    '''
    
    name = db.StringProperty()
        
        
    def __unicode__(self):
        return '[space: %s]' % (self.name)
    
