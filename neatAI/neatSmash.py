""" 2-input AND example """
from __future__ import print_function

from neat import nn, population, statistics, visualize

# Network inputs and expected outputs.
and_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
and_outputs = [0, 0, 0, 1]


"""
    @param1 { NodeGene list} genomes = is a list of class nodeGenes, the file called genome.py (https://github.com/MatKallada/neat-python/blob/master/neat/genome.py), genome is the entire neural network, so this is taking in all the nn's in this generation

    @return nothing

    this function will change the fitness variable for each node which represents how effective it is
"""
def eval_fitness(genomes):
    print("genomes: ", type(genomes));
    print("genoes[0]: ", genomes[0]);
    for g in genomes:
        ### get the neural network
        net = nn.create_feed_forward_phenotype(g)

        sum_square_error = 0.0
        for inputs, expected in zip(and_inputs, and_outputs):
            # Serial activation propagates the inputs through the entire network.
            output = net.serial_activate(inputs)
            sum_square_error += (output[0] - expected) ** 2

        # When the output matches expected for all inputs, fitness will reach
        # its maximum value of 1.0.
        g.fitness = 1 - sum_square_error


pop = population.Population('smash_config')
pop.run(eval_fitness, 300)

print('Number of evaluations: {0}'.format(pop.total_evaluations))

# Display the most fit genome.
winner = pop.statistics.best_genome()
print('\nBest genome:\n{!s}'.format(winner))

# Verify network output against training data.
print('\nOutput:')
winner_net = nn.create_feed_forward_phenotype(winner)
for inputs, expected in zip(and_inputs, and_outputs):
    output = winner_net.serial_activate(inputs)
    print("expected {0:1.5f} got {1:1.5f}".format(expected, output[0]))

# # Visualize the winner network and plot/log statistics.
# visualize.plot_stats(pop.statistics)
# visualize.plot_species(pop.statistics)
# visualize.draw_net(winner, view=True, filename="xor2-all.gv")
# visualize.draw_net(winner, view=True, filename="xor2-enabled.gv", show_disabled=False)
# visualize.draw_net(winner, view=True, filename="xor2-enabled-pruned.gv", show_disabled=False, prune_unused=True)

## save stats, and nn
statistics.save_stats(pop.statistics)
statistics.save_species_count(pop.statistics)
statistics.save_species_fitness(pop.statistics)

"""
outputs = 8
- main stick x val
- main stick y val
- A
- B
- X
- Y
- Block
- grab
- jump

maybe
  - recover (just a script that makes it recover)



Inputs = 40

needed p1 + p2
- action
- actionCounter
- actionFrame
- invulnerable
- hitlagFramesLeft
- hitStunFramesLeft
- isChargingSmash
- jumpsRemaining
- isOnGround
- speedAirX
- speedAirY
- speedXAttack
- speedYAttack
- speedGroundX
- damage
- stocks
- facingLeft
- x
- y


maybe
- character


not needed
- frame
- menuState
- stage
- cursorX
- cursorY




"""
