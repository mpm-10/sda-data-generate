from src.io.config import Config
from src.io.output import Output





if __name__ == '__main__':
    config : Config = Config()
    outputData : Output = Output()

    dataTables : dict = config.dataTables
    dataDependencies : dict = config.dataDependencies
    quantities : dict = config.quantities
    intervals : dict = config.intervals

    for dataTable in dataTables:
        for dependencyTable in dataDependencies[dataTable]:
            for attributeDependency in dataDependencies[dataTable][dependencyTable]:
                table = dataTables[dataTable]
                dependency = dataTables[dependencyTable]

                table.foreignData[attributeDependency] = dependency.innerData[attributeDependency]
        
        dataTables[dataTable].quantity = quantities[dataTable]
        dataTables[dataTable].interval = intervals[dataTable]
        
        dataTables[dataTable].generateMethod()
        dataTables[dataTable].generateUser()

        outputData.methodList = dataTables[dataTable].methodList
        outputData.userbaseList = dataTables[dataTable].userbaseList
        outputData.generateDirectories()

        outputData.writeMethods()
        outputData.writeUserbase()