import environment
import sampleAgent

x = int(raw_input('input x: ')or 3)
y = int(raw_input('input y: ')or 3)

v = environment.NbyMVacuumEnvironment(x,y)
ag = sampleAgent.ModelBasedAgent()
v.add_agent(ag)
v.run()

raw_input('press enter to exit')
