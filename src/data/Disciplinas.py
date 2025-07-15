import random



from .dataTables import dataTables



class Disciplinas(dataTables):
    __curso : str
    __nomes : list
    __cargasHorarias : list
    __modalidades : list

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Disciplinas'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarDisciplina/'
        self.urlMethodFindAll = '/listarDisciplinas/'
        self.urlMethodCreate = '/adicionarDisciplina/'
        self.urlMethodUpdate = '/atualizarDisciplina/'
        self.urlMethodDelete = '/removerDisciplina/'

        self.innerData = {
            'idDisciplina' : []
        }

        self.foreignData = {
            'idCurso' : []
        }

        self.__curso = 'cienciaComputacao'

        self.__nomes = {
            'cienciaComputacao' : [
                'Algorítimos e Programação de Computadores',
                'Programação de Computadores 01',
                'Programação de Computadores 02',
                'Programação de Computadores 03',
                'Banco de Dados 01',
                'Banco de Dados 02',
                'Engenharia de Software 01',
                'Engenharia de Software 02',
                'Redes de Computadores 01',
                'Redes de Computadores 02'
            ]
        }

        self.__cargasHorarias = [
            36,
            48,
            60,
            72
        ]

        self.__modalidades = [
            'EAD',
            'Presencial',
            'Híbrido'
        ]

    def generateMethod(self) -> None:
        methods : dict = {}

        disciplinas : int = self.quantity + 1
        rangeValues : int = disciplinas

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
        disciplina : dict = {}

        disciplinas : int = self.quantity + 1
        nomes : int = len(self.__nomes[self.__curso]) + 1
        rangeValues : int = int(min(disciplinas, nomes))

        for i in range(1, rangeValues):
            disciplina = {}
            userName : str = f'{self.userName}{i}'

            escolhaNome : str = random.choice(self.__nomes[self.__curso])
            indiceNome : int = self.__nomes[self.__curso].index(escolhaNome)
            self.__nomes[self.__curso].pop(indiceNome)

            escolhaIdCurso : int = random.choice(self.foreignData['idCurso'])
            escolhaCargaHoraria : int = random.choice(self.__cargasHorarias)
            escolhaModalidade : str = random.choice(self.__modalidades)

            idDisciplina : int = int(i)
            idCurso : int = int(escolhaIdCurso)
            nome : str = str(escolhaNome)
            cargaHoraria : int = int(escolhaCargaHoraria)
            modalidade : str = str(escolhaModalidade)

            disciplina['id_disciplina'] = idDisciplina
            disciplina['id_curso'] = idCurso
            disciplina['nome'] = nome
            disciplina['carga_horaria'] = cargaHoraria
            disciplina['modalidade'] = modalidade

            self.userbaseList.append({userName : disciplina})
            self.innerData['idDisciplina'].append(idDisciplina)

    @property
    def curso(self) -> dict:
        return self.__curso
    @curso.setter
    def curso(self, curso : dict) -> None:
        self.__curso = curso
    
    @property
    def nomes(self) -> dict:
        return self.__nomes
    @nomes.setter
    def nomes(self, nomes : dict) -> None:
        self.__nomes = nomes

    @property
    def cargasHorarias(self) -> dict:
        return self.__cargasHorarias
    @cargasHorarias.setter
    def cargasHorarias(self, cargasHorarias : dict) -> None:
        self.__cargasHorarias = cargasHorarias

    @property
    def modalidades(self) -> dict:
        return self.__modalidades
    @modalidades.setter
    def modalidades(self, modalidades : dict) -> None:
        self.__modalidades = modalidades
