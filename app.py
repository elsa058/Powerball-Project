from Classes import Lotto


def app():
   pball= Lotto()
   pball.genrerate()
   pball.user()
   pball.test(pball.rand())


app()