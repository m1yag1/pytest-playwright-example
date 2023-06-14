class Inicio(object):
    def __init__(self, pajina):
        self.pajina = pajina
        
    
    @property
    def texto_de_ejercisio(self):
        # https://playwright.dev/python/docs/api/class-page#page-locator
        return self.pajina.locator(".exercise-text")
    
    
    @property
    def opciones(self):
        # https://playwright.dev/python/docs/api/class-page#page-locator
        return self.pajina.locator(".answer-text > ol li")
    
    @property 
    def ejercisio_id(self):
        return self.pajina.locator(".badge")
