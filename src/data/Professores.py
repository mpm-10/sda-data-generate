import random



from .dataTables import dataTables



class Professores(dataTables):

    __curso : str
    __formacoes : dict

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Professores'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarProfessor/'
        self.urlMethodFindAll = '/listarProfessores/'
        self.urlMethodCreate = '/adicionarProfessor/'
        self.urlMethodUpdate = '/atualizarProfessor/'
        self.urlMethodDelete = '/removerProfessor/'

        self.__curso = 'cienciaComputacao'
        self.__formacoes = {
            'cienciaComputacao' : [
                'Estrutura de Dados',
                'Banco de Dados',
                'Teoria da Computacao',
                'Análise de Algoritimos',
                'Redes de Computadores'
            ],
        }
    
    def generateMethod(self) -> None:
        methods : dict = {}

        professores : int = self.quantity + 1
        rangeValues : int = professores

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
        professor : dict = {}

        data = self.data
        professores : int = self.quantity + 1
        rangeValues : int = professores

        for i in range(1, rangeValues):
            professor = {}
            userName : str = f'{self.userName}{i}'

            escolhaFormacao : str = random.choice(self.__formacoes[self.__curso])

            idProfessor : int = int(i)
            nome : str = str(data.name())
            formacao : str = str(escolhaFormacao)

            primeiroNome : str = nome.split()[0]
            segundoNome : str = nome.split()[1]
            primeiroNome : str = primeiroNome.lower()
            segundoNome : str = segundoNome.lower()

            email : str = str(primeiroNome + segundoNome + '@institucional.email.com')
            endereco : str = data.street_address()
            cidade : str = data.city()
            telefone : str = data.phone_number()

            professor['id_professor'] = idProfessor
            professor['nome'] = nome
            professor['formacao'] = formacao
            professor['email'] = email
            professor['endereco'] = endereco
            professor['cidade'] = cidade
            professor['telefone'] = telefone

            self.userbaseList.append({userName : professor})

    @property
    def curso(self) -> dict:
        return self.__curso
    @curso.setter
    def curso(self, curso : dict) -> None:
        self.__curso = curso

    @property
    def formacoes(self) -> dict:
        return self.__formacoes
    @formacoes.setter
    def formacoes(self, formacoes : dict) -> None:
        self.__formacoes = formacoes