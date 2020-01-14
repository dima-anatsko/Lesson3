import web
import json

import calories


render = web.template.render('templates/')
urls = ("/(.*)", "index")


class index:
    def GET(self, name):
        if "application/json" in web.ctx.env.get('HTTP_ACCEPT'):
            eats = json.loads(web.data())
            web.header('Content-Type', 'application/json')
            return json.dumps(calories.sum_cal(eats))
        else:
            web.header('Content-Type', 'text/html')
            return render.eat()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
