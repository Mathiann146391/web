import cherrypy

class MonSiteWeb(object):
    def index(self):
        return '''
            <form action="salutations" method="GET">
            Bonjour. Quel est votre nom ? 
            <input type="text" name="nom"/>
            <input type="submit" value="OK"/>
            </form>
        '''
    index.exposed = True 

    def salutations(self, nom =None):
        if nom: 
            return "Bonjour, {0}, comment allez-vous?".format(nom)
        else:
            return 'Veuillez svp fournir votre nom <a href="/">ici</a>.'
    salutations.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 10000})
cherrypy.quickstart(MonSiteWeb())
