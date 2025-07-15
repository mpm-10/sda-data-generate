import os



class Input():
    __inputDirectory : str
    __methodFiles : dict
    __methodUrlList : dict

    def __init__(self) -> None:
        self.__inputDirectory = 'methods/'
        self.__methodFiles = {}
        self.__methodUrlList = {
            'Alunos' : {},
            'Professores' : {},
            'Cursos' : {},
            'Disciplinas' : {},
            'Matriculas' : {},
            'Avaliacoes' : {},
            'Turmas' : {},
            'Horarios' : {}
        }

    def readMethods(self) -> None:
        inputDirectory : str = ''
        methodFiles : dict = {}
        methodUrlList : dict = {}

        methodsPath : str = ''
        methods : list = []
        pathList : list = []

        inputDirectory = self.__inputDirectory
        methodFiles = self.__methodFiles
        methodUrlList = self.__methodUrlList

        if not os.path.exists(inputDirectory):
            os.mkdir(inputDirectory)

        pathList = [path for path in os.listdir(inputDirectory)]
        pathList.sort()
        for path in pathList:
            methodsPath = f'{self.__inputDirectory}{path}'

            methods = [file for file in os.listdir(methodsPath)]
            methods.sort()
            methods.pop()

            methodFiles[path] = {}
            for method in methods:
                methodValue : str = f'{methodsPath}/{method}'
                methodKey : str = method.replace('Methods.txt', '')
                methodKey = methodKey.upper()

                methodFiles[path].update({
                    methodKey : methodValue
                })

        for methodFile in methodFiles:
            methodsPath = f'{self.__inputDirectory}{methodFile}'

            methodUrlList[methodFile] = {
                'GET' : [],
                'POST' : [],
                'PUT' : [],
                'DELETE' : []
            }

            getMethod : str = methodFiles[methodFile]['GET']
            postMethod : str = methodFiles[methodFile]['POST']
            putMethod : str = methodFiles[methodFile]['PUT']
            deleteMethod : str = methodFiles[methodFile]['DELETE']

            with open(getMethod, 'r') as getMethodFile:
                for method in getMethodFile:
                    method = f'http://{method.strip()}'
                    methodUrlList[methodFile]['GET'].append(method)
            
            with open(postMethod, 'r') as postMethodFile:
                for line in postMethodFile:
                    line = line.strip()
                    line = line.split(' ')

                    method : str = f'http://{line.pop(0)}'
                    user : str = f'{methodsPath}/{line.pop(0)}'

                    methodUrlList[methodFile]['POST'].append((method, user))

            with open(putMethod, 'r') as putMethodFile:
                for line in putMethodFile:
                    line = line.strip()
                    line = line.split(' ')

                    method : str = f'http://{line.pop(0)}'
                    user : str = f'{methodsPath}/{line.pop(0)}'

                    methodUrlList[methodFile]['PUT'].append((method, user))
                
            with open(deleteMethod, 'r') as deleteMethodFile:
                for method in deleteMethodFile:
                    method = f'http://{method.strip()}'
                    methodUrlList[methodFile]['DELETE'].append(method)

    @property
    def inputDirectory(self) -> str:
        return self.__inputDirectory
    @inputDirectory.setter
    def inputDirectory(self, inputDirectory) -> None:
        self.__inputDirectory = inputDirectory

    @property
    def methodFiles(self) -> dict:
        return self.__methodFiles
    @methodFiles.setter
    def methodFiles(self, methodFiles) -> None:
        self.__methodFiles = methodFiles

    @property
    def methodUrlList(self) -> dict:
        return self.__methodUrlList
    @methodUrlList.setter
    def methodUrlList(self, methodUrlList) -> None:
        self.__methodUrlList = methodUrlList