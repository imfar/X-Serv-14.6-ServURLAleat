import webapp

class URLAleatApp(webapp.webApp):
    def process(self, parsedRequest):  # utilizo un nuevo process
            import random
            return ("200 OK", "<html><body><h1><a href='"+str(random.randint(1,19999999))+"'>Dame otra!</a></h1></body></html>")

if __name__ == "__main__":
    urlAleatApp = URLAleatApp("localhost", 1234)
