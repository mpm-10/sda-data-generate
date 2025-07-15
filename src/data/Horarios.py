import random



from .dataTables import dataTables



class Horarios(dataTables):

    __horarios : dict

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Horarios'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarHorario/'
        self.urlMethodFindAll = '/listarHorarios/'
        self.urlMethodCreate = '/adicionarHorario/'
        self.urlMethodUpdate = '/atualizarHorario/'
        self.urlMethodDelete = '/removerHorario/'

        self.foreignData = {
            'idTurma' : []
        }

        self.__horarios = {
            'segunda-feira' : [
                ('08:00', '11:40'),
                ('13:30', '17:10')
            ],
            'terca-feira' : [
                ('08:00', '11:40'),
                ('13:30', '17:10')
            ],
            'quarta-feira' : [
                ('08:00', '11:40'),
                ('13:30', '17:10')
            ],
            'quinta-feira' : [
                ('08:00', '11:40'),
                ('13:30', '17:10')
            ],
            'sexta-feira' : [
                ('08:00', '11:40'),
                ('13:30', '17:10')
            ],
        }
    
    def generateMethod(self) -> None:
        methods : dict = {}

        horarios : int = self.quantity + 1
        rangeValues : int = horarios

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
        horario : dict = {}

        horarios : int = self.quantity + 1

        horariosDisponiveis : list = [grade for grade in self.__horarios.values()]
        gradeHoraria : int = sum(len(grade) for grade in horariosDisponiveis) + 1
        turmas : int = len(self.foreignData['idTurma']) + 1
        rangeValues : int = min(horarios, gradeHoraria, turmas)

        for i in range(1, rangeValues):
            horario = {}
            userName : str = f'{self.userName}{i}'

            escolhaTurma : str = random.choice(self.foreignData['idTurma'])
            indiceTurma : int = self.foreignData['idTurma'].index(escolhaTurma)
            self.foreignData['idTurma'].pop(indiceTurma)

            idHorario : int = int(i)
            idTurma : str = str(escolhaTurma)
            diaSemana : str = ''
            inicio : str = ''
            fim : str = ''

            dias : list = [dia for dia in self.__horarios if self.__horarios[dia] != []]
            if dias:
                escolherHorario : str = random.choice(dias)
                diaSemana : str = str(escolherHorario)
                horariosAula = self.__horarios[diaSemana]

                (inicio, fim)  = random.choice(horariosAula)

                inicio = str(inicio)
                fim = str(fim)

                indiceHorario : int = horariosAula.index((inicio, fim))
                horariosAula.pop(indiceHorario)

            diasOcupados : list = [(k, v) for k, v in self.__horarios.items() if not v]
            for diaOcupado in diasOcupados:
                self.__horarios.pop(diaOcupado[0])

            inicio = f'{inicio}:00'
            fim = f'{fim}:00'

            horario['id_horario'] = idHorario
            horario['id_turma'] = idTurma
            horario['dia_semana'] = diaSemana
            horario['inicio'] = inicio
            horario['fim'] = fim

            self.userbaseList.append({userName : horario})

    @property
    def horarios(self) -> dict:
        return self.__horarios
    @horarios.setter
    def horarios(self, horarios : dict) -> None:
        self.__horarios = horarios