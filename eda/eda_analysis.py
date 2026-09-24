import pandas as pd
import matplotlib.pyplot as plt
import os


def perform_eda():
    input_file = 'data/processed/amazon_processed_products.csv'
    df = pd.read_csv(input_file)

    print('\n===== DATA INFORMATION =====')
    print(df.info())

    print('\n===== SUMMARY STATISTICS =====')
    print(df.describe())

    print('\n===== MISSING VALUES =====')
    print(df.isnull().sum())

    print('\n===== TOP 10 PRODUCTS =====')
    print(df[['title', 'price', 'rating']].head(10))

    os.makedirs('reports/charts', exist_ok=True)

    plt.figure(figsize=(10, 6))
    df['price'].dropna().hist(bins=20)
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.title('Product Price Distribution')
    plt.savefig('reports/charts/price_distribution.png')
    plt.close()

    plt.figure(figsize=(8, 5))
    df['rating'].dropna().hist(bins=10)
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.title('Ratings Distribution')
    plt.savefig('reports/charts/rating_distribution.png')
    plt.close()

    top_products = df.sort_values('price', ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    plt.bar(top_products['title'], top_products['price'])
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Product Title')
    plt.ylabel('Price')
    plt.title('Top 10 Most Expensive Products')
    plt.tight_layout()
    plt.savefig('reports/charts/top_expensive_products.png')
    plt.close()

    if 'price' in df.columns and 'rating' in df.columns:
        avg_by_rating = df.groupby(df['rating'].round(0))['price'].mean().dropna()
        plt.figure(figsize=(8, 5))
        avg_by_rating.plot(kind='bar')
        plt.xlabel('Rounded Rating')
        plt.ylabel('Average Price')
        plt.title('Average Price by Rating')
        plt.tight_layout()
        plt.savefig('reports/charts/price_category_average.png')
        plt.close()

    print('\nEDA charts saved to reports/charts/')


if __name__ == '__main__':
    perform_eda()