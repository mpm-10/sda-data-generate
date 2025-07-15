from faker import Faker




class dataTables():
    __folderName : str
    __userName : str
    __urls : dict
    __urlMethodFindOne : str
    __urlMethodFindAll : str
    __urlMethodCreate : str
    __urlMethodUpdate : str
    __urlMethodDelete : str
    __quantity : int
    __interval : int
    __userbaseList : list
    __methodList : list
    __data : Faker
    __innerData : dict
    __foreignData : dict

    def __init__(self) -> None:
        self.__folderName = ''
        self.__userName = ''
        self.__urls = {}
        self.__urlMethodFindOne = ''
        self.__urlMethodFindAll = ''
        self.__urlMethodCreate = ''
        self.__urlMethodUpdate = ''
        self.__urlMethodDelete = ''
        self.__quantity = 0
        self.__interval = 0
        self.__userbaseList = []
        self.__methodList = []
        self.__data = Faker('pt_BR')
        self.__innerData = {}
        self.__foreignData = {}

    @property
    def folderName(self) -> str:
        return self.__folderName
    
    @folderName.setter
    def folderName(self, folderName) -> None:
        self.__folderName = folderName

    @property
    def userName(self) -> str:
        return self.__userName
    
    @userName.setter
    def userName(self, userName) -> None:
        self.__userName = userName
    
    @property
    def urls(self) -> dict:
        return self.__urls
    
    @urls.setter
    def urls(self, urls) -> None:
        self.__urls = urls
    
    @property
    def urlMethodFindOne(self) -> str:
        return self.__urlMethodFindOne
    
    @urlMethodFindOne.setter
    def urlMethodFindOne(self, urlMethodFindOne) -> None:
        self.__urlMethodFindOne = urlMethodFindOne

    @property
    def urlMethodFindAll(self) -> str:
        return self.__urlMethodFindAll
    
    @urlMethodFindAll.setter
    def urlMethodFindAll(self, urlMethodFindAll) -> None:
        self.__urlMethodFindAll = urlMethodFindAll

    @property
    def urlMethodCreate(self) -> str:
        return self.__urlMethodCreate
    
    @urlMethodCreate.setter
    def urlMethodCreate(self, urlMethodCreate) -> None:
        self.__urlMethodCreate = urlMethodCreate

    @property
    def urlMethodUpdate(self) -> str:
        return self.__urlMethodUpdate
    
    @urlMethodUpdate.setter
    def urlMethodUpdate(self, urlMethodUpdate) -> None:
        self.__urlMethodUpdate = urlMethodUpdate

    @property
    def urlMethodDelete(self) -> str:
        return self.__urlMethodDelete
    
    @urlMethodDelete.setter
    def urlMethodDelete(self, urlMethodDelete) -> None:
        self.__urlMethodDelete = urlMethodDelete

    @property
    def quantity(self) -> int:
        return self.__quantity
    
    @quantity.setter
    def quantity(self, quantity) -> None:
        self.__quantity = quantity

    @property
    def interval(self) -> int:
        return self.__interval
    
    @interval.setter
    def interval(self, interval) -> None:
        self.__interval = interval

    @property
    def userbaseList(self) -> list:
        return self.__userbaseList
    
    @userbaseList.setter
    def userbaseList(self, userbaseList) -> None:
        self.__userbaseList = userbaseList

    @property
    def methodList(self) -> list:
        return self.__methodList
    
    @methodList.setter
    def methodList(self, methodList) -> None:
        self.__methodList = methodList

    @property
    def data(self) -> Faker:
        return self.__data
    
    @data.setter
    def data(self, data) -> None:
        self.__data = data

    @property
    def innerData(self) -> dict:
        return self.__innerData
    
    @innerData.setter
    def innerData(self, innerData) -> None:
        self.__innerData = innerData

    @property
    def foreignData(self) -> dict:
        return self.__foreignData
    
    @foreignData.setter
    def foreignData(self, foreignData) -> None:
        self.__foreignData = foreignData

    