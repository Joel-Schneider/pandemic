# pandemic
Pandemic simulation code

A quickly hacked-together "simulator" for pandemics.
Output in CSV format, for ease of import and graphing

__Caveats__

* Does not predict what will happen with any real pandemic, including COVID-19...
* DO NOT make decisions based on this tool!
* Usage parameters likely to change.

_There's an interesting pattern:_

a lower R leads to lower early infection rate, but higher overall mortality.
I've not worked out why that is, yet!

for example, for 1 year, 1 simulation run:
	
	generic_pandemic.py 0.5 1 365 > data.csv
	generic_pandemic.py 5 1 365 > data.csv
	
for example, for 10 year, 1 simulation run:

	generic_pandemic.py 0.5 1 3650 > data.csv
	generic_pandemic.py 5 1 3650 > data.csv

__TODO__

A lot

Usage: generic_pandemic.py options

Options:	

	R (infectivity rate)
	runs (number of runs)
	days (number of days)

