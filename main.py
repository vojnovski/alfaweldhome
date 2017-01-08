#!/usr/bin/env python
import os
import cgi
from google.appengine.ext import webapp
from google.appengine.api import mail
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get (self, q):
    if q is None:
      q = 'index.html'

    path = os.path.join (os.path.dirname (__file__), q)
    self.response.headers ['Content-Type'] = 'text/html'
    self.response.out.write (template.render (path, {}))
    
class MailSend(webapp.RequestHandler):
  def post(self):
    try:
      mail.send_mail(sender="Viktor Vojnovski <admin@alfaweld.mk>",
              to="Alfa Veld Doo <info@alfaweld.mk>",
              subject="Poraka od Veb",
              body=cgi.escape(self.request.get('cfName')) + " so telefon " + cgi.escape(self.request.get('cfPhone')) + 
              " i mejl" + cgi.escape(self.request.get('cfEmail'))
              + " ti ja isprati slednava poraka:" + cgi.escape(self.request.get('cfComments')))
      self.redirect("/thanks.html")
    except mail.Error:
      self.redirect("/thanksbut.html")
    
def main():
  application = webapp.WSGIApplication([('/(.*html)?', MainHandler),
  										('/mail', MailSend)],
                                         debug=True)
  util.run_wsgi_app(application)


if __name__ == '__main__':
  main()
