
render = web.template.render('templates/')

urls = ('/', 'searchIndex', "/search", "search", '/formtest', "formtest")
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox("boe"),
    form.Textbox("bax",
                 form.notnull,
                 form.regexp('\d+', 'Must be a digit'),
                 form.Validator('Must be more than 5', lambda x: int(x) > 5)),
    form.Textarea('moe'),
    form.Checkbox('curly'),
    form.Dropdown('french', ['mustard', 'fries', 'wine']))


class formtest:
    def GET(self):
        form = myform()
        # make sure you create a copy of the form by calling it (line above)
        # Otherwise changes will appear globally
        return render.formtest(form)

    def POST(self):
        form = myform()
        if not form.validates():
            return render.formtest(form)
        else:
            # form.d.boe and form['boe'].value are equivalent ways of
            # extracting the validated arguments from the form.
            return "Grrreat success! boe: %s, bax: %s" % (form.d.boe, form['bax'].value)


class searchIndex:
    def GET(self):
        return render.searchIndex()


class search:
    def POST(self):
        inputParameters = web.input()
        for inputParameter in inputParameters:
            print("Key : " + inputParameter + " Value : " + inputParameters.get(inputParameter))

        # todo : the search key "hostname" is hardcoded here, should refine later
        searchKey = inputParameters.get("hostname")

        # pass the value to the function, so in the page "searchResult.html",
        # we can get the variable value and display with the variable
        return render.searchResult(searchKey)


if __name__ == "__main__":
    web.internalerror = web.debugerror
    app.run()
