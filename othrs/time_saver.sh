


#!/bin/bash
rm wyniki.txt
S=" "
for v in 10  1000 10000 25000 50000 75000 100000 300000 600000 700000 800000 1000000 1200000 1500000 1600000 2000000 10000000
				do
					
					echo -n "$v " >> wyniki.txt;
					python -m timeit -s "import random; s = [random.randint(0,100000000) for r in xrange($v)]" "sorted(s)" | awk '{print $6 " "  $7}' >> wyniki.txt
						
				done
