from datetime import date
import random



from .dataTables import dataTables



class Alunos(dataTables):

    def __init__(self) -> None:
        super().__init__()

        self.directoryName = 'Alunos'
        self.userName = 'User'
        self.urls = {
            'getOne' : 'localhost:3000',
            'getAll' : 'localhost:3000',
            'post' : 'localhost:3000',
            'put' : 'localhost:3000',
            'delete' : 'localhost:3000'
        }

        self.urlMethodFindOne = '/buscarAluno/'
        self.urlMethodFindAll = '/listarAlunos/'
        self.urlMethodCreate = '/adicionarAluno/'
        self.urlMethodUpdate = '/atualizarAluno/'
        self.urlMethodDelete = '/removerAluno/'

        self.innerData = {
            'idAluno' : []
        }
    
    def generateMethod(self) -> None:
        methods : dict = {}

        alunos : int = self.quantity + 1
        rangeValues : int = alunos

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
        aluno : dict = {}

        data = self.data
        alunos : int = self.quantity + 1
        rangeValues : int = alunos

        for i in range(1, rangeValues):
            aluno = {}
            userName : str = f'{self.userName}{i}'

            idAluno : int = int(i)
            nome : str = str(data.name())

            idade : int = int(random.randint(18, 25))
            dataNascimento : date = data.date_of_birth(minimum_age=idade, maximum_age=idade)
            dataNascimento : str = str(dataNascimento.strftime('%Y-%m-%d'))

            primeiroNome = nome.split()[0]
            segundoNome = nome.split()[1]
            primeiroNome = primeiroNome.lower()
            segundoNome = segundoNome.lower()

            email : str = str(primeiroNome + segundoNome + '@email.com')
            endereco : str = str(data.street_address())
            cidade : str = str(data.city())
            telefone : str = str(data.phone_number())

            aluno['id_aluno'] = idAluno
            aluno['nome'] = nome
            aluno['idade'] = idade
            aluno['data_nascimento'] = dataNascimento
            aluno['email'] = email
            aluno['endereco'] = endereco
            aluno['cidade'] = cidade
            aluno['telefone'] = telefone

            self.userbaseList.append({userName : aluno})
            self.innerData['idAluno'].append(idAluno)