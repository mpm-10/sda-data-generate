import random



from .dataTables import dataTables



class Matriculas(dataTables):
    __anoMinimo : int
    __anoMaximo : int
    __anos : list
    __semestres : list

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Matriculas'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarMatricula/'
        self.urlMethodFindAll = '/listarMatriculas/'
        self.urlMethodCreate = '/adicionarMatricula/'
        self.urlMethodUpdate = '/atualizarMatricula/'
        self.urlMethodDelete = '/removerMatricula/'

        self.innerData = {
            'idMatricula' : [],
        }

        self.foreignData = {
            'idAluno' : [],
        }

        self.__anoMinimo = 2020
        self.__anoMaximo = 2025

        self.__anos = [ano for ano in range(self.__anoMinimo,self.__anoMaximo + 1)]
        self.__semestres = [semestre for semestre in range(1, 9)]

    def generateMethod(self) -> None:
        methods : dict = {}

        matriculas : int = self.quantity + 1
        rangeValues : int = matriculas

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
        matricula : dict = {}

        matriculas : int = self.quantity + 1
        rangeValues : int = matriculas

        for i in range(1, rangeValues):
            matricula = {}
            userName : str = f'{self.userName}{i}'

            escolhaIdAluno : int = random.choice(self.foreignData['idAluno'])
            escolhaIdDisciplina : int = random.choice(self.foreignData['idDisciplina'])
            escolhaAno : int = random.choice(self.__anos)
            escolhaSemestre : int = random.choice(self.__semestres)
            
            idMatricula : int = int(i)
            idAluno : int = int(escolhaIdAluno)
            idDisciplina : int = int(escolhaIdDisciplina)
            ano : int = int(escolhaAno)
            semestre : int = int(escolhaSemestre)
            
            matricula['id_matricula'] = idMatricula
            matricula['id_aluno'] = idAluno
            matricula['id_disciplina'] = idDisciplina
            matricula['ano'] = ano
            matricula['semestre'] = semestre

            self.userbaseList.append({userName : matricula})
            self.innerData['idMatricula'].append(idMatricula)

    @property
    def anoMinimo(self) -> dict:
        return self.__anoMinimo
    @anoMinimo.setter
    def anoMinimo(self, anoMinimo : dict) -> None:
        self.__anoMinimo = anoMinimo

    @property
    def anoMaximo(self) -> dict:
        return self.__anoMaximo
    @anoMaximo.setter
    def anoMaximo(self, anoMaximo : dict) -> None:
        self.__anoMaximo = anoMaximo

    @property
    def anos(self) -> dict:
        return self.__anos
    @anos.setter
    def anos(self, anos : dict) -> None:
        self.__anos = anos
    
    @property
    def semestres(self) -> dict:
        return self.__semestres
    @semestres.setter
    def semestres(self, semestres : dict) -> None:
        self.__semestres = semestres