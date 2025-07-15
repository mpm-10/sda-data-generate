import random



from .dataTables import dataTables



class Turmas(dataTables):
    __anoMinimo : int
    __anoMaximo : int
    __anos : list
    __semestres : list

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Turmas'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarTurma/'
        self.urlMethodFindAll = '/listarTurmas/'
        self.urlMethodCreate = '/adicionarTurma/'
        self.urlMethodUpdate = '/atualizarTurma/'
        self.urlMethodDelete = '/removerTurma/'

        self.innerData = {
            'idTurma' : []
        }

        self.foreignData = {
            'idDisciplina' : []
        }

        self.__anoMinimo = 2020
        self.__anoMaximo = 2025
        self.__anos = [ano for ano in range(self.__anoMinimo,self.__anoMaximo + 1)]
        self.__semestres = {ano : [f'{ano}-1', f'{ano}-2'] for ano in self.__anos}

    def generateMethod(self) -> None:
        methods : dict = {}

        turmas : int = self.quantity + 1
        rangeValues : int = turmas

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
        turma : dict = {}

        turmas : int = self.quantity + 1

        semestresDisponiveis : list = [semestre for semestre in self.__semestres.values()]
        semestres : int = sum(len(semestre) for semestre in semestresDisponiveis) + 1
        rangeValues : int = min(turmas, semestres)

        for i in range(1, rangeValues):
            turma = {}
            userName : str = f'{self.userName}{i}'

            escolhaIdDisciplina : int = random.choice(self.foreignData['idDisciplina'])
            escolhaAno : int = random.choice(self.__anos)

            idTurma : int = int(i)
            idDisciplina : int = int(escolhaIdDisciplina)
            ano : int = int(escolhaAno)
            semestreLetivo : str = ''

            anos : list = [ano for ano in self.__semestres if self.__semestres[ano] != []]
            if anos:
                escolherSemestre : str = random.choice(anos)
                anoSemana : str = escolherSemestre

                semestresAula : list = self.__semestres[anoSemana]
                semestreLetivo : str  = str(random.choice(semestresAula))

                indiceSemestre : int = semestresAula.index(semestreLetivo)
                semestresAula.pop(indiceSemestre)

            anosOcupados : list = [(k, v) for k, v in self.__semestres.items() if not v]
            for anoOcupado in anosOcupados:
                self.__semestres.pop(anoOcupado[0])

            turma['id_turma'] = idTurma
            turma['id_disciplina'] = idDisciplina
            turma['semestre_letivo'] = semestreLetivo
            turma['ano'] = ano

            self.userbaseList.append({userName : turma})
            self.innerData['idTurma'].append(idTurma)

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