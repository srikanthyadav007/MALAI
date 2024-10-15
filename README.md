# MALAI-ML-based-Attack-on-Learning-With-Error-problem

This **MALAI** repository contains scripts for analyzing secret recovery rates in Learning With Errors (LWE) attacks using various linear models. The analysis focuses on the relationship between the number of samples, Hamming weights, and recovery percentages. In LWE we have `b = a.s + e mod q`, where (a,b) is a public key, and s is the secret(private key) and e is the error. 

## Download Data

Before executing the scripts, download the preprocessed data and create a `modified_A.npy` file. This will enable you to run experiments on data with 
n = 256, log2q = 20 and sparse binary secrets. You can download the data from the following link:

**[Download Data](https://dl.fbaipublicfiles.com/verde/n256_logq20_binary_for_release.tar.gz)**

The data folder contains the following files:
- `orig_A.npy` and `orig_b.npy`: The original 4n LWE samples.
- `params.pkl`: The parameters for the dataset, used by the transformer. This file eliminates the need to specify LWE parameters (N, Q, sigma) manually for this run.
- `secret.npy (n x 380)`: A file containing various secrets.hamming weights [3,40] and each hamming weight has 10 different secrets
- `test.prefix` and `train.prefix`: The preprocessed test and train sets. Each line is a string of `{a} ; {b}`. `a: (m x n)` and `b: (mx1)`.There are 380 `b` vectors for 380 secrets. 

### Refer `Salsa: Verde` preprocess technique for generating 4 Million LWE samples from 4n LWE samples. `train.prefix` + `test.prefix` contains 4 million LWE samples.

The LWE sample pair (a,b), which is a public key and secret s is private key. The LWE sample pair generation and converting the 4n LWE samples to 4 million samples has been done by the SALSA VERDE(open source) authors, which we refered to. THe github link for the data generation is given below:

**[SALSA Verde](https://github.com/facebookresearch/verde)** 

### Note: Please move the following two files from the `verde/n256_logq20_binary_for_release` folder to the `code` folder:
- `train.prefix`
- `secret.npy`

## Create `modified_A.npy`

After downloading the data, execute the `generate_modified_A.py` script to create the `modified_A.npy` file. This script processes the `train.prefix` file by modifying the matrix A, which will be used for further secret recovery analysis.The matrix A got modified where values changed from [0,q) to (-q/2,q/2].

---

## Scripts Overview

Execute the files in the order below:

### 1. Nomod_60%_secret_recovery_results.py (Similar for 65%, 70%, 75%, 80%)

These scripts evaluate the recovery of binary secrets using various linear models such as Linear Regression, ElasticNet, and Orthogonal Matching Pursuit on filtered datasets.

#### Key Features:
- The datasets are filtered based on specific Hamming weights (ranging from 3 to 40) and processed for different percentages of NoMOD data (60%, 65%, 70%, 75%, 80%).
- For each Hamming weight, 10 different secrets are tested to provide a robust evaluation of the recovery process.
- For each specified number of samples, the script attempts secret recovery by:
  - Iterating through the Hamming weights and 10 unique secrets per Hamming weight.
  - Evaluating recovery success using different models.
  - Writing the results to output files in the format: `Secret_recovery_results_for_{num_samples}_samples_with_Nomod_{percentage}%.txt`.
  - Output will be integer from [0,3] which says number of models successfully recovered.

#### Sample Count:
The script analyzes the following sample sizes: 10,000, 20,000, 50,000, 100,000, 200,000, 500,000, 750,000, 1,000,000

#### Output Format:
The results indicate successful recoveries for each combination of samples, NoMOD percentage, and Hamming weight.
- Results are written as files (e.g., Secret_recovery_results_for_100000_samples_with_Nomod_60%.txt) and include information on successful recoveries for each secret tested

### 2. Minimum_samples_required_for_x_Percent_Recovery.py

This script processes recovery results to determine the minimum number of samples required for achieving specified recovery rates (e.g., 80%, 90%, 100%) based on the success of secret recovery across different Hamming weights.
For each Hamming weight, 10 different secrets are tested, so achieving 80% recovery means that 8 out of the 10 secrets were successfully recovered

#### Key Features:
- Analyzes recovery results from multiple files generated in the previous step.
- Identifies the minimum number of samples required to achieve the specified recovery rate for each Hamming weight.
- Outputs the results in a structured text file.

#### Sample Count:
The script analyzes the following sample sizes: 10,000, 20,000, 50,000, 100,000, 200,000, 500,000, 750,000, 1,000,000

#### Output Format:
Each output file indicates the minimum samples required for achieving specified recovery rates.
- Example: `Minimum_samples_required_for_{rate}_Percent_Recovery.txt`.

### 3. Secret_recovery_success_rate_plot.py

This script generates plots of the success rates of secret recovery based on the number of samples across different NoMOD percentages.

#### Key Features:
- Reads and processes recovery data for different NoMOD percentages.
- Plots the success rates against the number of samples for visualization.

#### Output Format:
The output is a graphical representation saved as an image file, typically named:
- `Secret_Recovery_Success_Rate_vs_Number_of_Samples.png`.

### 4. Final_Recovery_Analysis.py

This script consolidates and analyzes recovery data across multiple recovery percentages (e.g., 80%, 90%, 100%) and outputs the results in Excel format.

#### Key Features:
- Processes multiple files to gather minimum NoMOD percentages and corresponding sample sizes for recovery rates.
- Outputs the results in an Excel spreadsheet for easy analysis.

#### Output Format:
The output Excel file contains detailed recovery analysis, including:
- Minimum NoMOD percentages and corresponding sample sizes for each Hamming weight.
- Example: `Final_Recovery_Analysis.xlsx`.

### 5. plot_no_mod_vs_hamming_weight.py

This script plots the percentage of NoMOD data against Hamming weights.

#### Key Features:
- Loads data from an Excel file containing NoMOD data.
- Calculates averages and plots the percentage of NoMOD data for each Hamming weight.

#### Output Format:
The output is a graphical representation saved as an image file, typically named:
- `No_Mod_vs_Hamming_Weight.png`.

---