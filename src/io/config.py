from src.data.Alunos import Alunos
from src.data.Professores import Professores
from src.data.Cursos import Cursos
from src.data.Disciplinas import Disciplinas
from src.data.Matriculas import Matriculas
from src.data.Avaliacoes import Avaliacoes
from src.data.Turmas import Turmas
from src.data.Horarios import Horarios



class Config():
    __dataTables : dict
    __quantities : dict
    __dataDependencies : dict
    __intervals : dict

    def __init__(self):
        self.__dataTables = {
            'alunos' : Alunos(),
            'professores' : Professores(),
            'cursos' : Cursos(),
            'disciplinas' : Disciplinas(),
            'matriculas' : Matriculas(),
            'avaliacoes' : Avaliacoes(),
            'turmas' : Turmas(),
            'horarios' : Horarios()
        }

        self.__dataDependencies = {
            'alunos' : {},
            'professores' : {},
            'cursos' : {},
            'disciplinas' : {
                'cursos' : [
                    'idCurso'
                ]
            },
            'matriculas' : {
                'alunos' : [
                    'idAluno'
                ],
                'disciplinas' : [
                    'idDisciplina'
                ]
            },
            'avaliacoes' : {
                'matriculas' : [
                    'idMatricula',
                ]
            },
            'turmas' : {
                'disciplinas' : [
                    'idDisciplina',
                ]
            },
            'horarios' : {
                'turmas' : [
                    'idTurma'
                ]
            }
        }

        self.__quantities = {
            'alunos' : 100,
            'professores' : 25,
            'cursos' : 1,
            'disciplinas' : 10,
            'matriculas' : 100,
            'avaliacoes' : 300,
            'turmas' : 12,
            'horarios' : 10,
        }

        self.__intervals = {
            'alunos' : 10,
            'professores' : 5,
            'cursos' : 1,
            'disciplinas' : 2,
            'matriculas' : 10,
            'avaliacoes' : 30,
            'turmas' : 2,
            'horarios' : 2,
        }

    @property
    def dataTables(self) -> dict:
        return self.__dataTables
    @dataTables.setter
    def dataTables(self, dataTables : dict) -> None:
        self.__dataTables = dataTables

    @property
    def dataDependencies(self) -> dict:
        return self.__dataDependencies
    @dataDependencies.setter
    def dataDependencies(self, dataDependencies : dict) -> None:
        self.__dataDependencies = dataDependencies

    @property
    def quantities(self) -> dict:
        return self.__quantities
    @quantities.setter
    def quantities(self, quantities : dict) -> None:
        self.__quantities = quantities

    @property
    def intervals(self) -> dict:
        return self.__intervals
    @intervals.setter
    def intervals(self, intervals : dict) -> None:
        self.__intervals = intervals