import pandas as pd

df = pd.read_excel('query-como ganar dinero ahorrar ahorro.xlsx', index_col=0)

df = df.filter(items=[
   'video_id',
   'video_published_at',
   'video_title',
   'video_description',
   'video_category',
   'video_duration_seconds',
   'video_view_count',
   'video_like_count',
   'video_comment_count',
   'channel_title',
   'channel_id',
   'channel_created_at',
   'channel_location',
   'channel_subscriptors_count',
   'channel_view_count',
   'channel_video_count',
])


# Defineix les paraules clau per a cada categoria
keywords_ahorro = ['ahorro', 'ahorrar', 'ahorros', 'como ahorrar']
keywords_ganar_dinero = ['ganar dinero', 'dinero']
keywords_invertir = ['invertir']

# Filtra les files i assigna la categoria
df['categoria'] = 0  # Inicialitza la columna categoria amb el valor predeterminat

# Filtra les files per paraules clau i assigna la categoria corresponent
df.loc[df['video_title'].str.contains('|'.join(keywords_ahorro), case=False) |
       df['video_description'].str.contains('|'.join(keywords_ahorro), case=False), 'categoria'] = 1

df.loc[df['video_title'].str.contains('|'.join(keywords_ganar_dinero), case=False) |
       df['video_description'].str.contains('|'.join(keywords_ganar_dinero), case=False), 'categoria'] = 2

df.loc[df['video_title'].str.contains('|'.join(keywords_invertir), case=False) |
       df['video_description'].str.contains('|'.join(keywords_invertir), case=False), 'categoria'] = 3

df.to_excel('filtered_results.xlsx', index=False)

print(df)
