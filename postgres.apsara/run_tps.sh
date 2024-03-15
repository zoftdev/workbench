#!/bin/bash
#  export PGPASSWORD='abcABC***'  before start process

# CSV file to store the results
output_file="tps2.csv"

# Header for the CSV file
echo "threads,tps" > "$output_file"

# Array of thread counts to test
thread_nums=(1 2 5 10)

# Loop through each thread count
for thread_num in "${thread_nums[@]}"
do
    # Run pgbench and capture the output
    output=$(pgbench -c "$thread_num" -j "$thread_num" -t 1000 my_benchmark_test_db -h pgm-tw9ny436chxf1y16.pg.rds.asr-ops.clouds.trueidc.com -U hlex -p 3433)

    # Extract the TPS (including connections establishing) value using grep and awk
    tps=$(echo "$output" | grep "including connections establishing" | awk '{print $3}')

    # Append the thread count and TPS to the CSV file
    echo "$thread_num,$tps" >> "$output_file"
done

echo "Benchmarking completed. Results saved to $output_file."