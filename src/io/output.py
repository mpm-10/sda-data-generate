import os
import json



class Output:
    __outputDirectory : str
    __userbaseList : list
    __methodList : list
    __methodFiles : dict
    __userbaseDirectory : str

    def __init__(self) -> None:
        self.__outputDirectory = 'methods/'
        self.__userbaseList = []
        self.__methodList = []

        self.__methodFiles = {
            'GET' : '/getMethods.txt',
            'POST' : '/postMethods.txt',
            'PUT' : '/putMethods.txt',
            'DELETE' : '/deleteMethods.txt'
        }
        self.__userbaseDirectory = 'userbase/'
        
        if not os.path.exists(self.__outputDirectory):
            os.mkdir(self.__outputDirectory)

    def generateDirectories(self) -> None:
        outputInformations : dict = {}
        outputDirectory : str = ''
        methodFile : str = ''

        outputInformations = self.methodList[0]
        directoryName : str = outputInformations['directoryName']
        outputDirectory = f'{self.__outputDirectory}{directoryName}'

        if not os.path.exists(outputDirectory):
            os.mkdir(outputDirectory)

        for (directoryPaths, directoryNames, fileNames) in os.walk(outputDirectory, False):
            for file in fileNames:
                methodFile : str = f'{directoryPaths}/{file}'
                os.remove(methodFile)

            for directory in directoryNames:
                methodDirectory : str = f'{directoryPaths}/{directory}'
                os.rmdir(methodDirectory)

        userbaseDirectory : str = f'{outputDirectory}/{self.__userbaseDirectory}'
        if not os.path.exists(userbaseDirectory):
            os.mkdir(userbaseDirectory)

        methodFile = outputDirectory + self.__methodFiles['GET']
        with open(methodFile, 'a') as getMethodFile:
            getMethodFile.write('')
        
        methodFile = outputDirectory + self.__methodFiles['POST']
        with open(methodFile, 'a') as postMethodFile:
            postMethodFile.write('')
        
        methodFile = outputDirectory + self.__methodFiles['PUT']
        with open(methodFile, 'a') as putMethodFile:
            putMethodFile.write('')
            
        methodFile = outputDirectory + self.__methodFiles['DELETE']
        with open(methodFile, 'a') as deleteMethodFile:
            deleteMethodFile.write('')
        
    def writeMethods(self) -> None:
        outputInformations : dict = {}
        directoryName : str = ''
        interval : int = 0
        outputDirectory : str = ''

        outputInformations = self.methodList.pop(0)
        directoryName = outputInformations['directoryName']
        interval = outputInformations['interval']
        urlGetAll = outputInformations['GET'] + '\n'

        outputDirectory = f'{self.__outputDirectory}{directoryName}'

        for i, method in enumerate(self.methodList):
            urlGetOne : str = method['GET'] + '\n'
            urlDelete : str = method['DELETE'] + '\n'

            methodFile : str = outputDirectory + self.__methodFiles['GET']
            if i % interval == 0:
                with open(methodFile, 'a') as getMethodFile:
                    getMethodFile.write(urlGetAll)
            
            with open(methodFile, 'a') as getMethodFile:
                getMethodFile.write(urlGetOne)
            
            methodFile = outputDirectory + self.__methodFiles['DELETE']
            with open(methodFile, 'a') as deleteMethodFile:
                deleteMethodFile.write(urlDelete)

        self.methodList.insert(0, outputInformations)
    
    def writeUserbase(self) -> None:
        outputInformations : dict = {}
        directoryName : str = ''
        outputDirectory : str = ''
        userbaseDirectory : str = ''

        outputInformations = self.methodList.pop(0)
        directoryName = outputInformations['directoryName']
        outputDirectory = f'{self.__outputDirectory}{directoryName}/'
        userbaseDirectory = f'{outputDirectory}{self.__userbaseDirectory}'

        for method, user in zip(self.methodList, self.userbaseList):
            urlPost : str = method['POST']
            urlPut : str = method['PUT']

            userName : str = list(user.keys())[0]
            userData : dict = list(user.values())[0]
            userbaseFile : str = f'{userbaseDirectory}/{userName}.json'

            with open(userbaseFile, 'w') as userbase:
                json.dump(userData, userbase, ensure_ascii=False, indent=4)

            userFile : str = f'{self.__userbaseDirectory}{userName}.json'
            methodFile : str = outputDirectory + self.__methodFiles['POST']
            urlPostData : str = f'{urlPost} {userFile}\n'
            urlPutData : str = f'{urlPut} {userFile}\n'
            
            with open(methodFile, 'a') as postMethodFile:
                postMethodFile.write(urlPostData)
            
            methodFile = outputDirectory + self.__methodFiles['PUT']
            with open(methodFile, 'a') as putMethodFile:
                putMethodFile.write(urlPutData)

        self.methodList.insert(0, outputInformations)

    @property
    def outputDirectory(self) -> list:
        return self.__outputDirectory
    @outputDirectory.setter
    def outputDirectory(self, outputDirectory) -> None:
        self.__outputDirectory = outputDirectory
    
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
    def methodFiles(self) -> list:
        return self.__methodFiles
    @methodFiles.setter
    def methodFiles(self, methodFiles) -> None:
        self.__methodFiles = methodFiles

    @property
    def userbaseDirectory(self) -> list:
        return self.__userbaseDirectory
    @userbaseDirectory.setter
    def userbaseDirectory(self, userbaseDirectory) -> None:
        self.__userbaseDirectory = userbaseDirectory