# Opdracht 3
Bij Kungliga Biblioteket in Stockholm bevat het SPARQL-endpoint de metadata over een boek met properties volgens een eigen datamodel (https://libris.kb.se/sparql). Laten we de boeken zoeken die door Mulisch zijn geschreven. Boeken zijn gekoppeld met hun auteur met de property https://id.kb.se/vocab/responsibilityStatement in deze catalogus. Bij de KB identificeren ze Mulisch met de string "Harry Mulisch".

## 3.1 
Geef een overzicht van de URI's van de boeken in de collectie van de KB geschreven door Mulisch.  Kies een prefix, want dat is handig. Onthoud van deze query hoeveel boeken je hebt gevonden.

Spieken in het leerboek? Zie voorbeeld ex008.rq.

Antwoord: [yasgui-link](https://api.triplydb.com/s/E1OqficKQ)

## 3.2
Bij boeken hebben ze in de catalogus ook de druk opgenomen met de property <https://id.kb.se/vocab/editionStatement>. Breidt de query uit zodat ook de editionStatement wordt weergegeven. Onthoud van deze query hoeveel boeken je hebt gevonden.

Spieken in het leerboek? Zie voorbeeld ex013.rq.

Antwoord: [yasgui-link](https://api.triplydb.com/s/klnLke6Lt)

## 3.3. 
De query bij vraag 3.1 levert een ander aantal boeken (41 boeken) op dan de query van opdracht 3.2 (14 boeken). Dat komt omdat niet alle boeken een editionStatement hebben. Pas de query aan zodat van alle 41 boeken alleen de druk wordt weergegeven als deze ook aanwezig is in de data.

Spieken in het leerboek? Zie voorbeeld ex057.rq.

Antwoord: [yasgui-link](https://api.triplydb.com/s/DiCCubZuY)

Einde blok 1.
