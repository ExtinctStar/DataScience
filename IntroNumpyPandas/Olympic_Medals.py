import numpy as np
import pandas as pd

countries = pd.Series(['Russian Fed.',
                       'Norway',
                       'Canada',
                       'United States',
                       'Netherlands',
                       'Germany',
                       'Switzerland',
                       'Belarus',
                       'Austria',
                       'France',
                       'Poland',
                       'China',
                       'Korea',
                       'Sweden',
                       'Czech Republic',
                       'Slovenia',
                       'Japan',
                       'Finland',
                       'Great Britain',
                       'Ukraine',
                       'Slovakia',
                       'Italy',
                       'Latvia',
                       'Australia',
                       'Croatia',
                       'Kazakhstan'])

gold = pd.Series([13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])

silver = pd.Series([11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0])

bronze = pd.Series([9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1])

olympic_medal_counts_df = pd.DataFrame({'Countries': countries,
                                        'Golds': gold,
                                        'Silvers': silver,
                                        'Bronzes': bronze})


def solution1():

    print(olympic_medal_counts_df)
    print('\n')
    olympic_medal_counts_df.to_csv('SochiWinter2014.csv')


solution1()


def solution2():
    at_least_one_gold = olympic_medal_counts_df[
        (olympic_medal_counts_df['Golds'] >= 1)
    ]

    print("DataFrame of Countries with at least one gold medal:\n")
    print(at_least_one_gold)

    avg_bronze_at_least_one_gold = np.mean(at_least_one_gold['Bronzes'])

    print("The average number of bronze medals for countries"
          " with at least one gold:\n\t" + str(avg_bronze_at_least_one_gold))
    print("\n")


solution2()


def solution3():

    print("\n")
