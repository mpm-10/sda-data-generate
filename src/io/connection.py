import requests
import json



class Connection():
    __methodUrlList : dict
    __methodType : str
    __requestFunctions : dict
    __isUserMethod : bool

    def __init__(self):
        self.__methodUrlList = {}
        self.__methodType = 'GET'
        self.__isUserMethod = False
        self.__requestFunctions = {
            'GET' : requests.get,
            'POST' : requests.post,
            'PUT' : requests.put,
            'DELETE' : requests.delete
        }

    def loadConnectionData(self):
        methodUrlList : dict = {}
        methodType : str = ''
        urls : list = []
        requestFunctions : dict = {}
        userData : dict = {}
        isUserMethod : bool = False

        methodUrlList = self.__methodUrlList
        methodType = self.__methodType
        requestFunctions = self.__requestFunctions
        isUserMethod = self.__isUserMethod

        for methodsUrl in methodUrlList:
            for method in methodUrlList[methodsUrl]:
                if method != methodType:
                    continue
                for url in methodUrlList[methodsUrl][method]:
                    if isinstance(url, tuple):
                        isUserMethod = True
                    urls.append(url)

        if isUserMethod == False:
            for url in urls:
                try:
                    requestFunctions[methodType](url)
                except:
                    print('Conexão Recusada!')
                    exit(0)
        
        elif isUserMethod == True:
            for url, user in urls:
                with open(user, 'r') as userFile:
                    userData = json.load(userFile)
                
                try:
                    requestFunctions[methodType](url, userData)
                except:
                    print('Conexão Recusada!')
                    exit(0)

    @property
    def methodUrlList(self) -> dict:
        return self.__methodUrlList
    @methodUrlList.setter
    def methodUrlList(self, methodUrlList) -> None:
        self.__methodUrlList = methodUrlList

    @property
    def methodType(self) -> str:
        return self.__methodType
    @methodType.setter
    def methodType(self, methodType) -> None:
        self.__methodType = methodType.upper()

    @property
    def requestFunctions(self) -> dict:
        return self.__requestFunctions
    @requestFunctions.setter
    def requestFunctions(self, requestFunctions) -> None:
        self.__requestFunctions = requestFunctions

    @property
    def isUserMethod(self) -> str:
        return self.__isUserMethod
    @isUserMethod.setter
    def isUserMethod(self, isUserMethod) -> None:
        self.__isUserMethod = isUserMethod