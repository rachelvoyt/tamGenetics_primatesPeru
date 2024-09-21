#!/bin/bash

# definitions
base_url="https://export.uppmax.uu.se/snic2022-6-144/share/tmp_dir_vcfs/"
loci_list="/home/rachelvoyt/Documents/UT-Grad/Development/repos/tamGenetics_primatesPeru/06_tamGenetics_wgs/00_data/lociList_bcftools.txt"
output_dir="/home/rachelvoyt/Documents/UT-Grad/Development/repos/tamGenetics_primatesPeru/06_tamGenetics_wgs/00_data/00_vcfData/"

# loop function
for i in {1..23}
do 
    # define url for individual vcf file
    vcf_url="$base_url/interval_${i}.vcf.gz"

    # define output for individual vcf file
    output_file="$output_dir/interval_${i}_genos.txt"

    # extract genos for loci in list, output to txt file
    bcftools query -H -f '%CHROM\t%POS\t%REF\t%ALT[\t%GT\t%DP\t%GQ]\n' -R "$loci_list" "$vcf_url" > "$output_file"

    # print message indicating file has been processed
    echo "Processed interval_${i}.vcf.gz -> $output_file"
done
