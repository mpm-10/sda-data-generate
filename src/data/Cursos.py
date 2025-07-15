import random



from .dataTables import dataTables



class Cursos(dataTables):

    __nomes : list
    __duracoes : list
    __tipos : list

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Cursos'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarCurso/'
        self.urlMethodFindAll = '/listarCursos/'
        self.urlMethodCreate = '/adicionarCurso/'
        self.urlMethodUpdate = '/atualizarCurso/'
        self.urlMethodDelete = '/removerCurso/'

        self.innerData = {
            'idCurso' : []
        }

        self.__nomes = [
            'Ciência da Computação'
        ]

        self.__duracoes = [
            3,
            4,
            5
        ]

        self.__tipos = [
            'Bacharelado',
            'Licenciatura'
        ]
    
    def generateMethod(self) -> None:
        methods : dict = {}

        cursos : int = self.quantity + 1
        rangeValues : int = cursos

        directoryName : str = self.directoryName
        interval : int = self.interval

        urlGetOne : str = self.urls['getOne']
        urlGetAll : str = self.urls['getAll']
        urlPost : str = self.urls['post']
        urlPut : str = self.urls['put']
        urlDelete : str = self.urls['delete']

        urlMethodFindOne : str = str(self.urlMethodFindOne)
        urlMethodFindAll : str = str(self.urlMethodFindAll)
        urlMethodCreate : str = str(self.urlMethodCreate)
        urlMethodUpdate : str = str(self.urlMethodUpdate)
        urlMethodDelete : str = str(self.urlMethodDelete)

        getAllMethod : str = f'{urlGetAll}{urlMethodFindAll}'
        methods['directoryName'] = directoryName
        methods['interval'] = interval
        methods['GET'] = getAllMethod
        self.methodList.append(methods)

        for i in range(1, rangeValues):
            methods = {}

            getOneMethod : str = f'{urlGetOne}{urlMethodFindOne}{i}'
            postMethod : str = f'{urlPost}{urlMethodCreate}'
            putMethod : str = f'{urlPut}{urlMethodUpdate}{i}'
            deleteMethod : str = f'{urlDelete}{urlMethodDelete}{i}'

            methods['GET'] = getOneMethod
            methods['POST'] = postMethod
            methods['PUT'] = putMethod
            methods['DELETE'] = deleteMethod

            self.methodList.append(methods)

    def generateUser(self) -> None:
        curso : dict = {}

        cursos : int = self.quantity + 1
        nomes : int = len(self.__nomes) + 1
        rangeValues : int = int(min(cursos, nomes))

        for i in range(1, rangeValues):
            curso = {}
            userName : str = f'{self.userName}{i}'

            escolhaNome : str = random.choice(self.__nomes)
            indiceNome : int = self.__nomes.index(escolhaNome)
            self.__nomes.pop(indiceNome)

            escolhaDuracao : int = random.choice(self.__duracoes)
            escolhaTipo : str = random.choice(self.__tipos)

            idCurso : int = int(i)
            nome : str = str(escolhaNome)
            duracao : int = int(escolhaDuracao)
            tipo : str = str(escolhaTipo)

            curso['id_curso'] = idCurso
            curso['nome'] = nome
            curso['duracao'] = duracao
            curso['tipo'] = tipo

            self.userbaseList.append({userName : curso})
            self.innerData['idCurso'].append(idCurso)

    @property
    def nomes(self) -> dict:
        return self.__nomes
    @nomes.setter
    def nomes(self, nomes : dict) -> None:
        self.__nomes = nomes

    @property
    def duracoes(self) -> dict:
        return self.__duracoes
    @duracoes.setter
    def duracoes(self, duracoes : dict) -> None:
        self.__duracoes = duracoes

    @property
    def tipos(self) -> dict:
        return self.__tipos
    @tipos.setter
    def tipos(self, tipos : dict) -> None:
        self.__tipos = tipos