import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'www')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = False)

class SudeepBlogTemplate(webapp2.RequestHandler):
  def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

  def render(self, template, **params):
	self.write(self.render_str(template, **params))
