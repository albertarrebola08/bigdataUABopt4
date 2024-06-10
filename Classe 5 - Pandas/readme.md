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
- Columna: Nota "en text" per a cada alumne:
  - Si la nota final és inferior a 5, s'afegeix el text "suspendido".
  - Si la nota es troba entre 5 i 6 (ambdós inclosos), s'afegeix el text "aprovat".
  - Si la nota és superior a 6 i inferior a 7, s'afegeix el text "bé".
  - Si la nota és igual o superior a 7, s'afegeix el text "notable".
  - Si la nota supera el 9, s'afegeix el text "Excelente".
  - Si la nota és equivalent a un 10, s'afegeix el text "matrícula d'honor".
- Columna: Diferència de nota respecte a la mediana del grup.
- Columna: Diferència de nota (expressada en percentatge) respecte a la mediana del grup.
Condicions especials:
- Abans de realitzar els càlculs, s'ha de sumar UN punt a cada alumne, però la nota màxima mai pot superar el 10.
  
![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/1dd00c76-127a-4809-b4cb-d663b0b7445f)

**Exercici 1.2**: Aquest dataset conté dades del canal de YouTube "KEXP" fins al 11/03/2024. Volem saber:

- Volum general: ¿Quantes files i columnes té el conjunt de dades complet?
- Composició del conjunt de dades: Quines columnes componen el conjunt de dades?
- Calcula la desviació (absoluta i percentual) de cada vídeo sobre la mitjana d'espectadors/comentaris/m'agrada del canal.
- Localitza el vídeo més vist.
- Localitza el vídeo més comentat.
- Crea una nova columna per a cadascun dels valors calculats anteriorment i crea un nou conjunt de dades final que incorpori tota la nova informació.
- Calcula la durada en segons de cada vídeo i indica la seva desviació percentual sobre la mitjana de durada dels vídeos del canal. (Pendent de comprovació del docent) 

![image](https://github.com/albertarrebola08/bigdataUABopt4/assets/104431726/afeacaea-1e38-4b3c-904b-2383011ea1fd)


### Tasques 
#### 1) Visualitza totes les estadístiques calculades anteriorment en un gràfic de Tableau.
#### 2) Realitzar l'exercici 2 
Pendent de fer a classe






