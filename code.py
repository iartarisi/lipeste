import web
from web import form

render = web.template.render('templates/', base='layout')

urls = (
    '/', 'index'
    )
app = web.application(urls, globals())

pasteForm = form.Form(
    form.Textarea('', rows='20', cols='70'),
    form.Textbox('bad_dog'),
    validators = [form.Validator("Hm... are you a bot?",
                                 lambda i: not i.bad_dog)]
    )

class index:
    def GET(self):
        form = pasteForm()
        return render.index(form)

    def POST(self):
        f = pasteForm()
        if f.validates():
            return render.pasted(form)
        
if __name__ == "__main__": app.run()
