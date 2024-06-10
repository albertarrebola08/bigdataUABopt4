# Classe 5 - Pandas
> 12/03/2024
>
Treballar amb la llibreria Pandas en relació als dataframes. Obtenir dades realitzar operacions per fer transformacions de les dades i després visualitzar-ho en un format llegible i exportable com un .CSV passant abans per els dataframes propis de la llibreria Pandas.
<hr>

S'han realitzat 2 exercicis: 

**Exercici 1.1**: L'objectiu és crear un document CSV amb 5 columnes:

- Columna: Nom i cognoms (en una única cadena de text) de cada alumne.
  ```
  notes = [1, 6, 8, 9, 10, 6, 5]
  alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
  cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]
  
  llista_noms_cognoms = []
  for i in range(len(alumnes)):
      nombre_apellido = alumnes[i] + ' ' + cognoms[i]
      llista_noms_cognoms.append(nombre_apellido)
  ```
- Columna: Nota de cada alumne.
  ```
   "Nota alumne (nº)": notes_arreglades[i],
  ```
- Columna: Nota "en text" per a cada alumne:
  - Si la nota final és inferior a 5, s'afegeix el text "suspendido".
  - Si la nota es troba entre 5 i 6 (ambdós inclosos), s'afegeix el text "aprovat".
  - Si la nota és superior a 6 i inferior a 7, s'afegeix el text "bé".
  - Si la nota és igual o superior a 7, s'afegeix el text "notable".
  - Si la nota supera el 9, s'afegeix el text "Excelente".
  - Si la nota és equivalent a un 10, s'afegeix el text "matrícula d'honor".
  ```
  def to_text(notes_arreglades):
    notes_text = []
    for nota in notes_arreglades:
        if nota < 5:
            nota_texto = "Suspendido"
        elif 5 <= nota <= 6:
            nota_texto = "Aprobado"
        elif 6 < nota < 7:
            nota_texto = "Bien"
        elif 7 <= nota < 9:
            nota_texto = "Notable"
        elif 9 <= nota < 10:
            nota_texto = "Excelente"
        elif nota == 10:
            nota_texto = "Matricula"
        notes_text.append(nota_texto)

    return notes_text
  ```
- Columna: Diferència de nota respecte a la mediana del grup.
  ```
  def diferencia_mitjana(notes_arreglades):
    mitjana_notes = round(sum(notes_arreglades) / len(notes_arreglades))
    diferencia_mitj = []
    for nota in notes_arreglades:
        diferencia = nota - mitjana_notes
        diferencia_mitj.append(diferencia)

    return diferencia_mitj
  ```
- Columna: Diferència de nota (expressada en percentatge) respecte a la mediana del grup.
  ```
  def diferencia_mitjana_percent(notes_arreglades):
    mitjana_notes = round(sum(notes_arreglades) / len(notes_arreglades))
    porcentajes_mitj = []
    for nota in notes_arreglades:
        diferencia = nota - mitjana_notes
        porcentaje = (diferencia / mitjana_notes) * 100
        porcentajes_mitj.append(porcentaje)

    return porcentajes_mitj
  ```
Condicions especials:
- Abans de realitzar els càlculs, s'ha de sumar UN punt a cada alumne, però la nota màxima mai pot superar el 10.
  ```
  def increment(notes):
    notes_arreglades = []
    for nota in notes:
        if nota < 10:
            nota += 1
        notes_arreglades.append(nota)

    return notes_arreglades
  ```

**Resultat final**
  ```
  dicc = {}
  llista_final = []
  
  for i in range(len(alumnes)):
      dicc = {
          "Nom i cognoms ": alumnes[i] + ' ' + cognoms[i],
          "Nota alumne (nº)": notes_arreglades[i],
          "Avaluació ": notes_text[i],
          "Diferencia de nota respecte la mitjana ": diferencia_mitjana[i],
          "Diferencia de nota (%) respecte la mitjana ": diferencia_percent_mitjana[i]
      }
      llista_final.append(dicc)

  df = pd.DataFrame(llista_final)
  df.to_csv('alumnos_final.csv', index=False)
  ```
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/1dd00c76-127a-4809-b4cb-d663b0b7445f)

**Exercici 1.2**: Aquest dataset conté dades del canal de YouTube "KEXP" fins al 11/03/2024. Volem saber:

- Volum general: ¿Quantes files i columnes té el conjunt de dades complet?
  ```
  df = pd.read_csv("dataset.csv")
  print(len(df))
  ```
- Composició del conjunt de dades: Quines columnes componen el conjunt de dades?
  ```
  print(df.columns)
  ```
- Calcula la desviació (absoluta i percentual) de cada vídeo sobre la mitjana d'espectadors/comentaris/m'agrada del canal.
  ```
  average_views = df['viewCount'].mean()
  average_comments = df['commentCount'].mean()
  average_likes = df['likeCount'].mean()
  
  
  df['desviacio_absoluta_likes'] = df['likeCount'] - average_likes
  df['desviacio_absoluta_comments'] = df['commentCount'] - average_comments
  df['desviacio_absoluta_views'] = df['viewCount'] - average_views
  
  df['desviacio_%_likes'] = (df['likeCount'] - average_likes )/ average_likes * 100
  df['desviacio_%_comments'] = (df['commentCount'] - average_comments )/ average_comments * 100
  df['desviacio_%_views'] =(df['viewCount'] - average_views )/ average_views * 100
  ```
- Localitza el vídeo més vist.
  ```
  row_max_view_video = df.iloc[[df['viewCount'].idxmax()]]
  print(row_max_view_video)
  ```
- Localitza el vídeo més comentat.
  ```
  row_max_comment_video = df.iloc[[df['commentCount'].idxmax()]]
  print(row_max_comment_video)
  ```
- Crea una nova columna per a cadascun dels valors calculats anteriorment i crea un nou conjunt de dades final que incorpori tota la nova informació.
  ```
  df = df.drop(['channelId', 'categoryId', 'channelTitle', 'tags', 'publishedAt', 'blocked_at'], axis=1)
  df.to_csv("final.csv")
  ```
- Calcula la durada en segons de cada vídeo i indica la seva desviació percentual sobre la mitjana de durada dels vídeos del canal. (Pendent de comprovació del docent)
  
    Pendent de realitzar amb suport del docent
  
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/afeacaea-1e38-4b3c-904b-2383011ea1fd)


### Tasques 
#### 1) Visualitza totes les estadístiques calculades anteriorment en un gràfic de Tableau.
#### 2) Realitzar l'exercici 2 
Pendent de fer a classe






