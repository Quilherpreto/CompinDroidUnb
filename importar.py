

from roboflow import Roboflow
rf = Roboflow(api_key="Dc2GBjofvXbaxHM8mqJp")
project = rf.workspace("industrial-murillo").project("cubos-6z0y8")
version = project.version(1)
dataset = version.download("yolov8")



