import subprocess
import os
import sys


print('\n========== AMAZON DATA PIPELINE STARTED ==========' )


print('\nSTEP 1: SCRAPING AMAZON DATA')
subprocess.run([sys.executable, 'scraper/scraper.py'])


print('\nSTEP 2: CLEANING & TRANSFORMING DATA')
subprocess.run([sys.executable, 'transform/transform_data.py'])


print('\nSTEP 3: RUNNING EDA & VISUALIZATIONS')
subprocess.run([sys.executable, 'eda/eda_analysis.py'])


print('\n========== PIPELINE EXECUTION COMPLETED ==========' )

print('\nGenerated Files:')

print('1. data/raw/amazon_raw_products.csv')
print('2. data/processed/amazon_processed_products.csv')
print('3. reports/charts/price_distribution.png')
print('4. reports/charts/rating_distribution.png')
print('5. reports/charts/top_expensive_products.png')
print('6. reports/charts/price_category_average.png')