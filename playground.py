import cmptcomplexity.aprox as aproximator
import sys
setup = sys.argv[1]
proper = sys.argv[2]


a,t = aproximator.count_it(proper,setup)
a.show(t)

