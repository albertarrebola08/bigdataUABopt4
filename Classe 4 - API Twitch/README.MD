# Classe 4 - API Twitch

> 05/03/2024

Partint de la classe anterior on ens connectavem a l'API d'Spotify hem afegit dificultat i s'han utilitzat noves tècniques mètodes i llibreries per explotar amb més precisió les dades aportades.
Un dels processos que hem fet ha estat: Crear JSON's de playlist utilitzant **offset** i processar-los després de recopilar-los. Posteriorment també s'haxplicat la llibreria **glob** nativa de Python que ens ha servit per obtneri tots els arxius excel generats al nostre projecte.


<code>import json</code>
<code>import glob</code>


L'última part de la classe ha constat en configurar el nostre accés a l'API de Twitch. Hem creat un nou projecte i hem obtingut la les credencials per poder treballar amb ella. 

__main.py__ utilitza aquesta API per obtenir streams: **get_streams** i agruparlos en diferents JSON's amb un identificador propi. Un nou mètode après i bastant imprescindible en l'obtenció de dades és time.sleep (de la llibreria time nativa de Python). Això el que ens permetrà és donar marge entre captacions de dades per evitar col·lapses i que Twith ens denegui l'accés.
