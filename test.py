import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		self.responce.write("Hello World, WE ARE RMDSSOE")

app = webapp2.WSGIApplication([('/',MainPage)], debug=True)