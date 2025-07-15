from datetime import date
import random



from .dataTables import dataTables



class Avaliacoes(dataTables):
    __anoMinimo : int
    __anoMaximo : int
    __curso : str
    __assuntos : list

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Avaliacoes'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarAvaliacao/'
        self.urlMethodFindAll = '/listarAvaliacoes/'
        self.urlMethodCreate = '/adicionarAvaliacao/'
        self.urlMethodUpdate = '/atualizarAvaliacao/'
        self.urlMethodDelete = '/removerAvaliacao/'

        self.foreignData = {
            'idMatricula' : [],
        }

        self.__curso = 'cienciaComputacao'

        self.__assuntos = {
            'cienciaComputacao': [
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

        self.__anoMinimo = 2020
        self.__anoMaximo = 2025
        
    def generateMethod(self) -> None:
        methods : dict = {}

        avaliacoes : int = self.quantity + 1
        rangeValues : int = avaliacoes

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
        avaliacao : dict = {}

        data = self.data
        avaliacoes : int = self.quantity + 1
        rangeValues : int = avaliacoes

        for i in range(1, rangeValues):
            avaliacao = {}
            userName : str = f'{self.userName}{i}'

            escolhaIdMatricula = random.choice(self.foreignData['idMatricula'])
            escolhaNota : float = round(random.uniform(8.00, 10.00), 2)
            escolhaAssuntos : str = random.choice(self.__assuntos[self.__curso])

            idAvaliacao : int = int(i)
            idMatricula : int = int(escolhaIdMatricula)
            nota : float = float(escolhaNota)
            assunto : str = str(escolhaAssuntos)

            anoMinimo : date = date(self.__anoMinimo, 1, 1)
            anoMaximo : date = date(self.__anoMaximo, 12, 31)
            dataAvaliacao : date = data.date_between(anoMinimo, anoMaximo)
            dataAvaliacao : str = str(dataAvaliacao.strftime('%Y-%m-%d'))

            avaliacao['id_avaliacao'] = idAvaliacao
            avaliacao['id_matricula'] = idMatricula
            avaliacao['nota'] = nota
            avaliacao['data_avaliacao'] = dataAvaliacao
            avaliacao['assunto'] = assunto

            self.userbaseList.append({userName : avaliacao})

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
    def curso(self) -> dict:
        return self.__curso
    @curso.setter
    def curso(self, curso : dict) -> None:
        self.__curso = curso

    @property
    def assuntos(self) -> dict:
        return self.__assuntos
    @assuntos.setter
    def assuntos(self, assuntos : dict) -> None:
        self.__assuntos = assuntos