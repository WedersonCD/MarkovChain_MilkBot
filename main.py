from Simulation     import Simulation
from Util           import Util
from Configuration  import Configuration



util = Util()
configuration=Configuration()
simulation = Simulation(configuration)

simulation.start()


util.generateCSV(simulation.states)
