# ASE_stats

[![DOI](https://zenodo.org/badge/613491565.svg)](https://zenodo.org/badge/latestdoi/613491565)


### Contributors

- Pathey Shah
- Prit Modi
- Nikhil Mehra


## Instructions


- To view all command line options run 
    ```python3 Main.py --help True ```

- To Run test cases 
    ```python3 Main.py --go <test-name>```

```python3 Main.py --go tiles```
 

```
Here are the list of options

  
OPTIONS:
  -b  --bootstrap     bootstrap value                       = 512
  -c  --cliff         cliff's delta threshold               = .4
  -cf  --conf         conf value                            = 0.05
  -co  --cohen        cohen value                           = .35
  -F  --Fmt           float string formatting value         = "{:2.2f}"
  -w  --width         width value                           = 40
  -g  --go            start-up action                       = nothing
  -h  --help          show help                             = False
  -s  --seed          random number seed                    = 937162211
ACTIONS:


  

```

## To run all test cases

```python3 Main.py --go  all ```

## Output

```

		true True True
		false False False
		false False False
✅PASS : eg_basic
mu sd cliffs boot both
-- -- ------ ---- ----
10.0 1 True True True
10.1 1 True True True
10.2 1 True False False
10.3 1 True False False
10.4 1 True False False
10.5 1 True False False
10.6 1 True False False
10.7 1 False False False
10.8 1 False False False
10.9 1 False False False
11.0 1 False False False
✅PASS : eg_bootmu
rx5 0  -----   *------    |                    {"0.10", "0.20", "0.30", "0.30", "0.40"}
rx3 0   ------    *---    |                    {"0.15", "0.25", "0.35", "0.35", "0.40"}
rx1 0             --------*-----               {"0.34", "0.49", "0.51", "0.51", "0.60"}
rx2 3                     |    ------    *-----{"0.60", "0.70", "0.80", "0.80", "0.90"}
rx4 0                     |    ------    *-----{"0.60", "0.70", "0.80", "0.80", "0.90"}
✅PASS : eg_five
10000 9.970244417873827 2.0195675464478313
✅PASS : eg_gauss
10 5.5 3.0276503540974917
✅PASS : eg_num
✅PASS : eg_ok

eg3
	 1 True True True
	 1.05 True True True
	 1.1 False False True
	 1.15 False False True
	 1.2 False False True
	 1.25 False False True
	 1.3 False False True
	 1.35 False False True
	 1.4 False False True
	 1.45 False False True
✅PASS : eg_pre
dbbaa
cdbce
ccaec
bdcca
acdae
ddcaa
accbe
ebbae
bcddd
ccaee
✅PASS : eg_sample
rx1 0  ----------         *                   -{"99.00", "99.50", "100.00", "101.00", "101.00"}
rx2 1  -------------------*                   -{"99.00", "100.00", "100.00", "101.00", "101.00"}
rx3 1  ----------         *                   -{"99.00", "99.50", "100.00", "101.00", "101.00"}
rx4 0  -------------------*                   -{"99.00", "100.00", "100.00", "101.00", "101.00"}
✅PASS : eg_six
 rx1   -*-               |                    {"8.68", "9.46", "9.94", "10.45", "11.33"}
 rx6   -*-               |                    {"8.71", "9.44", "9.96", "10.50", "11.25"}
 rx7   -*-               |                    {"8.70", "9.46", "10.01", "10.53", "11.28"}
 rx10   -*-               |                    {"8.65", "9.47", "10.02", "10.52", "11.35"}
 rx2   -*-               |                    {"8.81", "9.57", "10.11", "10.62", "11.33"}
 rx3            -*--     |                    {"18.72", "19.43", "19.95", "20.50", "21.28"}
 rx4                     |-*-                 {"28.73", "29.48", "30.00", "30.56", "31.33"}
 rx5                     |-*-                 {"28.89", "29.59", "30.11", "30.63", "31.36"}
 rx8                     |         -*--       {"38.71", "39.44", "40.03", "40.53", "41.26"}
 rx9                     |       --- *---     {"36.15", "38.63", "40.25", "41.66", "43.90"}
✅PASS : eg_sk
 rx1  --*-               |                    {"8.81", "9.51", "9.95", "10.52", "11.31"}
 rx7  --*-               |                    {"8.67", "9.45", "10.03", "10.56", "11.31"}
 rx10  --*-               |                    {"8.73", "9.50", "10.04", "10.61", "11.35"}
 rx6  --*-               |                    {"8.71", "9.55", "10.04", "10.55", "11.36"}
 rx2   -*-               |                    {"8.84", "9.59", "10.11", "10.64", "11.40"}
 rx3            -*-      |                    {"18.66", "19.38", "19.88", "20.46", "21.32"}
 rx4                     |*-                  {"28.64", "29.47", "29.95", "30.51", "31.30"}
 rx5                     |*-                  {"28.87", "29.55", "30.06", "30.54", "31.35"}
 rx8                     |        --*-        {"38.78", "39.52", "40.04", "40.57", "41.22"}
 rx9                     |      --- *---      {"36.31", "38.48", "40.07", "41.81", "44.07"}
✅PASS : eg_tiles

```
