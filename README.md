# drama

list = ['drama' ,'food','romance' ]
df.loc[(df['Genres'].str.contains('drama'))&(df['Genres'].str.contains('food'))&(df['Genres'].str.contains('romance')), ]
