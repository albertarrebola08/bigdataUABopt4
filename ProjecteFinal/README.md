# Estudi sobre la preocupació per la pèrdua del poder adquisitiu a Espanya
Autors: Pau Cardús i Albert Arrebola

# Pèrdua de poder adquisitiu a Espanya i l'impacte a YouTube (2005-2023)

## Introducció
Aquest estudi té com a objectiu analitzar la situació de perdua de poder adquisitiu a Espanya des del 2005 fins al 2023, utilitzant tècniques de big data. S'explorarà l'evolució dels salaris i dels preus, especialment l'Índex de Preus al Consum (IPC), per demostrar si la perdua de poder adquisitiu és un fenomen real. A més, es realitzaran anàlisis comparatives entre Catalunya i Espanya, s'analitzaran els salaris segons el nivell d'estudis i grups d'edat, així com l'IPC per grups de consum. Finalment mirarem l'impacte a YouTube tant desde el punt de vista de les cerques com dels videos penjats. 

## Metodologia
El treball consta de dues parts:

### Part 1: Anàlisi de dades
En aquesta part, es recopilarà informació sobre els salaris i l'IPC des de fonts com l'Institut d'Estadística de Catalunya (Idescat) utilitzant tècniques de web scraping amb BeautifulSoup. Es generarà una comparativa temporal dels salaris i de l'IPC per demostrar l'evolució de la perdua de poder adquisitiu.

### Part 2: Impacte a YouTube
Un cop s'hagi realitzat l'anàlisi inicial, es portarà l'estudi cap a YouTube per avaluar si els resultats afecten les cerques i la creació de vídeos relacionats. Es farà servir Google Trends per analitzar les paraules clau relacionades amb finances personals com "ahorrar", "como ganar dinero", "ahorro", "precio gasolina" i "precio luz". A més, s'utilitzarà l'API de YouTube per obtenir dades sobre la quantitat de vídeos relacionats amb aquests temes i la seva evolució temporal.

## Recopilació de Dades
Per obtenir la informació necessària, s'han utilitzat les següents tècniques:

- Web Scrapping amb BeautifulSoup per recopilar dades de salaris i IPC des de IDESCAT i INE.
- La llibreria _Pytrends_ per accedir a l'API de Google Trends i obtenir dades sobre les cerques de paraules clau
  - "como ganar dinero"
  - "ahorrar"
  - "ahorro"
  - "precio gasolina"
  - "precio luz"
- L'API de YouTube per recopilar informació sobre els vídeos relacionats amb les paraules clau.

## Visualització de Dades
Un cop recopilades les dades, es generarà una visualització clara i concisa utilitzant la plataforma Tableau. Aquesta visualització es publicarà en un lloc web perquè sigui accessible per a tothom interessat en els resultats de l'estudi.

## Conclusió
Aquest estudi proporcionarà una anàlisi detallada de la perdua de poder adquisitiu a Espanya des del 2005 fins al 2023, així com el seu impacte en les cerques i la producció de contingut a YouTube. Els resultats obtiguts ajudaran a comprendre millor aquest fenomen i les seves implicacions en la vida quotidiana dels ciutadans espanyols.

<hr>

**Com està organitzat el repositori?**
- **codis-python/**: Conté els scripts en Python utilitzats per a l'extracció i processament de dades.
- **dades_extretes/**: Conté les dades extretes durant el projecte.
  - **catalunya-espanya/**: Dades específiques de Catalunya i Espanya.
  - **evolucio-cerques/**: Dades sobre l'evolució de les cerques.
- **datasets/**: Conjunt de dades utilitzades i generades durant l'estudi.

Autors: Pau Cardús i Albert Arrebola
