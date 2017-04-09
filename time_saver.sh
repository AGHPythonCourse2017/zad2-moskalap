


#!/bin/bash
for v in 10 100 1000 10000 100000 100000
				do
					
					echo "problem dla version $v" >> wyniki.txt;
					python -m timeit -s "s = list(range($v ))" "sorted(s)">> wyniki.txt
						
				done
