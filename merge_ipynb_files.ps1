nbmerge .\1_Loading_Dataset.ipynb .\2_Dataset_Preparation.ipynb > .\merge1.ipynb
nbmerge .\merge1.ipynb .\3_Data_Exploratory_matplot.ipynb > .\merge2.ipynb
nbmerge .\merge2.ipynb .\4_Decision_Tree_Classifier.ipynb > .\merge3.ipynb
nbmerge .\merge3.ipynb .\5_Random_Forest_Classifier.ipynb > 0_merged_ipynb_files_for_google_colab.ipynb