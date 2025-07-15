from src.io.input import Input
from src.io.connection import Connection





if __name__ == '__main__':
    inputData : Input = Input()
    connection : Connection = Connection()

    inputData.readMethods()
    connection.methodUrlList = inputData.methodUrlList
    connection.loadConnectionData()
