#!/usr/bin/python
import sys
import fileinput
import re
import json
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('expand_frame_repr', False)

###option -f
my_gene="Homo_sapiens.GRCh37.75.gtf"
if sys.argv[1][:2]=="-f":
    change_column = sys.argv[1][2]
    #my_gene = sys.argv[2]
    your_gene = sys.argv[2]
else:
    change_column = 1
    #my_gene = sys.argv[1]
    your_gene = sys.argv[1]
#print(change_column)
column_need=int(change_column)-1
#print(type(column_need))

###Obtain dictionary of gene_id and gene_name
Replace_gene = {}
for each_line_my_gene in fileinput.input(my_gene):
    Ensembl_name = re.findall(r'gene_id\s\"(\w+)',each_line_my_gene,re.I|re.M)
    HUGO_name = re.findall(r'gene_name\s\"+([\w\.\w-]+)',each_line_my_gene,re.I|re.M)
    my_Columns = re.split('\t',each_line_my_gene)
    #print(Ensembl_name)
    #print(HUGO_name)
    if Ensembl_name:
        if HUGO_name:
            if my_Columns[2] == "gene":
                #Replace_gene[Ensembl_name] = HUGO_name
                for each_line_Ensembl in Ensembl_name: 
                    for each_line_HUGO in HUGO_name:
                        Replace_gene_list = {each_line_Ensembl:each_line_HUGO}
                        Replace_gene.update(Replace_gene_list)

###Change dict into dataframe, and change name
Replace_dict = pd.DataFrame.from_dict(Replace_gene,orient='index',columns=['gene_name'])
Replace_dict = Replace_dict.reset_index().rename(columns={'index':'GENE_ID'})
Change_df = pd.read_csv(your_gene)
Change_df.rename( columns = { Change_df.columns[column_need]: 'gene_ID' }, inplace = True )
Change_df_new = {}
#print(Change_df)


###point problem
for line in Change_df['gene_ID']:##Change_df_new.loc[column_need][i]= delect_point
    delect_point=re.sub(r'\.\w+','',line)
    Delect_point_list = {line:delect_point}
    Change_df_new.update(Delect_point_list)
Change_df_new_dict = pd.DataFrame.from_dict(Change_df_new,orient='index',columns=['GENE_ID'])
Change_df_new_dict = Change_df_new_dict.reset_index().rename(columns={'index':'gene_ID'})
##Change_delect_point=pd.concat([Change_df_new_dict,Change_df],axis=1)
Change_gene = pd.merge(Change_df,Change_df_new_dict,on='gene_ID',how="left")
move_column_ID = Change_gene.pop('GENE_ID')
Change_gene.insert(column_need,'GENE_ID',move_column_ID)
Change_delect_point=Change_gene.drop(['gene_ID'],axis=1)#don't cover
#print(Change_delect_point)            


###Match,move and delect
Save_gene = pd.merge(Change_delect_point,Replace_dict,on='GENE_ID',how="left")
move_column = Save_gene.pop('gene_name')
Save_gene.insert(column_need,'gene_name',move_column)
#print(Save_gene.T)
Result=Save_gene.drop(['GENE_ID'],axis=1)#don't cover

print(Result)


"""
for key in Replace_gene:
    r1=key #ID 
    r2=str(Replace_gene[key]) #Name  
"""

#with open("Result.json","w") as f:
    #json.dump(your_Columns,f) 
