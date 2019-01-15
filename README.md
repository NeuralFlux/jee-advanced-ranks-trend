# JEE Advanced Ranks Trend
A small project to extract and conclude upon the trend of branches in IIT Kanpur

### 1) Getting the data
- Data was extracted from the official JoSAA website
- Data was processed into CSVs using VLOOKUP (to enable automatic script calculation)

### 2) Analyzing the data
(OR - Opening Rank, CR - Closing Rank)

- For every branch in IITK, a factor of preference, 1/(CR-OR), is calculated
  - Why this was implemented? 1/(CR-OR) – Higher the spread of the branch, lesser the value of 1/(CR-OR) and hence it’s a good measure to estimate preference.
- But this had 2 problems, the problem of outliers and the problem of similar rank difference branches.

### 3) Overcoming the problems
- Outliers; A branch which has OR of #6 and CR of #1000 will be greatly undermined
- Similar Rank Difference Branches; Consider 2 branches (#500-#1000 and #3000-#3500) both have a preference of 0.002. Hence this tie has to be broken.
- A factor of competition for each branch was calculated
- For each branch of IITK, the branches which overlap at least 1 rank with it (from other IITs) were taken into account
- P<sub>i</sub> = 1/(CR<sub>i</sub>-OR<sub>i</sub>) and K<sub>i</sub> = (min(CR, CR<sub>i</sub>)-max(OR,OR<sub>i</sub>))/(CR-OR), where P<sub>i</sub> is the preference of i<sup>th</sup> such branch and K<sub>i</sub> is the competition given by it.
- K<sub>i</sub> is basically (number of seats overlapping)/(total seats in particular IITK branch)
- For a particular branch in IITK, total competition by other IIT branches is given by [![Capture.png](https://i.postimg.cc/kg5db5LD/Capture.png)](https://postimg.cc/8jx38TpV)
- A python script was made to calculate all of this for each branch and each year, outputted to a CSV file.

### 4) Result
The results were [![Results](https://i.postimg.cc/02PzhpK3/Capture.png)](https://postimg.cc/3Wfrv0BC)
