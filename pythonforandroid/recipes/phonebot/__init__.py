from pythonforandroid.recipe import PythonRecipe


class PhonebotRecipe(PythonRecipe):
    version = "0.2"
    url = 'https://github.com/yycho0108/PhoneBot/archive/0.2.tar.gz'
    depends = ["setuptools"]
    site_packages_name = 'phonebot'


recipe = PhonebotRecipe()
