# TRGN_Assignment4

*The program called ensg2hugo.py that takes a comma-delimited file as an argument and a column number as an input, and print a file where the Ensembl gene name has become a HUGO name.*

## Download the file

1. Homo_sapiens.GRCh37.75.gtf contains a huge number of datas, thus we would use curl -O http://ftp.ensembl.org/pub/release-75/gtf/homo_sapiens/Homo_sapiens.GRCh37.75.gtf.gz.
2. Using wget or curl to download the file, which need to be motified. Here's a unit test from https://github.com/davcraig75/unit/blob/master/expres.anal.csv.
3. **Make sure two files in the same and correct directory.**

## How to use

1. Using ```git clone https://github.com/ruocensong/TRGN_Assignment4/ ```to download the program.
2. ```cd TRGN_Assignment4``` into the directary.
3. ```mv ensg2hugo.py ~/bin/.``` to save the program in it.
4. Run the programe ```./ensg2hugo.py -f[0-9] Your_file.csv >Your_file.hugo.csv```, an option “-f [0-9]” where -f2 would pick the 2nd column. If there is no “-f” then the first column is used.
