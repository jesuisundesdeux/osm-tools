# osm-tools
Tools for OSM datas manipulation

# Install app & datas requirements
Update `setup.sh` and execute below command
```
./setup.sh
```

# Analyze cities and streets datas

Generate all streets datas (about 4h)

```
source .virtualenv/bin/activate
./generate_summary.py
```

**<a href="datas/34%20-%20Hérault/34172%20-%20Montpellier/streets.csv">Exemple streets for Montpellier city</a>**


## Statistique par departement

| Departement | Nb population | Nb villes | nb rues |
|-------------|---------------|-----------|---------|
| <a href="datas/01 - Ain">01 - Ain</a> | 585,999 | 409 | 21,776 |
| <a href="datas/02 - Aisne">02 - Aisne</a> | 501,158 | 803 | 21,043 |
| <a href="datas/03 - Allier">03 - Allier</a> | 340,582 | 317 | 10,663 |
| <a href="datas/04 - Alpes-de-Haute-Provence">04 - Alpes-de-Haute-Provence</a> | 160,216 | 199 | 6,226 |
| <a href="datas/05 - Hautes-Alpes">05 - Hautes-Alpes</a> | 136,784 | 165 | 4,438 |
| <a href="datas/06 - Alpes-Maritimes">06 - Alpes-Maritimes</a> | 1,078,863 | 162 | 12,328 |
| <a href="datas/07 - Ardèche">07 - Ardèche</a> | 312,645 | 336 | 11,367 |
| <a href="datas/08 - Ardennes">08 - Ardennes</a> | 279,448 | 458 | 8,846 |
| <a href="datas/09 - Ariège">09 - Ariège</a> | 150,735 | 326 | 5,082 |
| <a href="datas/10 - Aube">10 - Aube</a> | 290,455 | 400 | 9,869 |
| <a href="datas/11 - Aude">11 - Aude</a> | 354,746 | 426 | 18,326 |
| <a href="datas/12 - Aveyron">12 - Aveyron</a> | 272,409 | 300 | 8,877 |
| <a href="datas/13 - Bouches-du-Rhône">13 - Bouches-du-Rhône</a> | 1,976,380 | 119 | 25,328 |
| <a href="datas/14 - Calvados">14 - Calvados</a> | 682,365 | 703 | 21,227 |
| <a href="datas/15 - Cantal">15 - Cantal</a> | 146,778 | 253 | 4,077 |
| <a href="datas/16 - Charente">16 - Charente</a> | 309,217 | 338 | 9,429 |
| <a href="datas/17 - Charente-Maritime">17 - Charente-Maritime</a> | 599,281 | 454 | 24,081 |
| <a href="datas/18 - Cher">18 - Cher</a> | 309,925 | 286 | 10,006 |
| <a href="datas/19 - Corrèze">19 - Corrèze</a> | 224,532 | 239 | 5,738 |
| <a href="datas/21 - Côte-d'Or">21 - Côte-d'Or</a> | 507,198 | 620 | 17,839 |
| <a href="datas/22 - Côtes-d'Armor">22 - Côtes-d'Armor</a> | 449,769 | 206 | 15,126 |
| <a href="datas/23 - Creuse">23 - Creuse</a> | 109,050 | 250 | 4,297 |
| <a href="datas/24 - Dordogne">24 - Dordogne</a> | 385,188 | 514 | 10,561 |
| <a href="datas/25 - Doubs">25 - Doubs</a> | 511,312 | 587 | 16,418 |
| <a href="datas/26 - Drôme">26 - Drôme</a> | 481,663 | 364 | 18,096 |
| <a href="datas/27 - Eure">27 - Eure</a> | 578,312 | 658 | 18,935 |
| <a href="datas/28 - Eure-et-Loir">28 - Eure-et-Loir</a> | 325,396 | 366 | 13,501 |
| <a href="datas/29 - Finistère">29 - Finistère</a> | 790,220 | 179 | 25,950 |
| <a href="datas/2A - Corse-du-Sud">2A - Corse-du-Sud</a> | 107,170 | 99 | 741 |
| <a href="datas/2B - Haute-Corse">2B - Haute-Corse</a> | 127,526 | 194 | 1,077 |
| <a href="datas/30 - Gard">30 - Gard</a> | 703,761 | 350 | 20,674 |
| <a href="datas/31 - Haute-Garonne">31 - Haute-Garonne</a> | 1,246,096 | 589 | 26,359 |
| <a href="datas/32 - Gers">32 - Gers</a> | 189,280 | 463 | 7,225 |
| <a href="datas/33 - Gironde">33 - Gironde</a> | 1,407,336 | 534 | 28,581 |
| <a href="datas/34 - Hérault">34 - Hérault</a> | 1,081,732 | 333 | 31,250 |
| <a href="datas/35 - Ille-et-Vilaine">35 - Ille-et-Vilaine</a> | 849,018 | 233 | 18,877 |
| <a href="datas/36 - Indre">36 - Indre</a> | 176,213 | 161 | 7,084 |
| <a href="datas/37 - Indre-et-Loire">37 - Indre-et-Loire</a> | 656,884 | 268 | 17,366 |
| <a href="datas/38 - Isère">38 - Isère</a> | 1,200,547 | 521 | 37,924 |
| <a href="datas/39 - Jura">39 - Jura</a> | 249,431 | 525 | 13,160 |
| <a href="datas/40 - Landes">40 - Landes</a> | 382,620 | 329 | 16,531 |
| <a href="datas/41 - Loir-et-Cher">41 - Loir-et-Cher</a> | 323,479 | 268 | 12,094 |
| <a href="datas/42 - Loire">42 - Loire</a> | 742,543 | 326 | 16,567 |
| <a href="datas/43 - Haute-Loire">43 - Haute-Loire</a> | 223,903 | 226 | 5,719 |
| <a href="datas/44 - Loire-Atlantique">44 - Loire-Atlantique</a> | 1,364,514 | 221 | 33,246 |
| <a href="datas/45 - Loiret">45 - Loiret</a> | 634,842 | 309 | 16,612 |
| <a href="datas/46 - Lot">46 - Lot</a> | 152,286 | 276 | 3,402 |
| <a href="datas/47 - Lot-et-Garonne">47 - Lot-et-Garonne</a> | 328,457 | 314 | 8,763 |
| <a href="datas/48 - Lozère">48 - Lozère</a> | 69,805 | 172 | 2,238 |
| <a href="datas/49 - Maine-et-Loire">49 - Maine-et-Loire</a> | 787,932 | 362 | 28,206 |
| <a href="datas/50 - Manche">50 - Manche</a> | 420,333 | 506 | 13,775 |
| <a href="datas/51 - Marne">51 - Marne</a> | 544,005 | 572 | 14,987 |
| <a href="datas/52 - Haute-Marne">52 - Haute-Marne</a> | 146,353 | 397 | 6,604 |
| <a href="datas/53 - Mayenne">53 - Mayenne</a> | 306,372 | 261 | 9,926 |
| <a href="datas/54 - Meurthe-et-Moselle">54 - Meurthe-et-Moselle</a> | 725,530 | 576 | 17,490 |
| <a href="datas/55 - Meuse">55 - Meuse</a> | 174,686 | 433 | 8,621 |
| <a href="datas/56 - Morbihan">56 - Morbihan</a> | 683,006 | 232 | 21,176 |
| <a href="datas/57 - Moselle">57 - Moselle</a> | 1,045,147 | 730 | 23,480 |
| <a href="datas/58 - Nièvre">58 - Nièvre</a> | 209,929 | 305 | 7,815 |
| <a href="datas/59 - Nord">59 - Nord</a> | 2,562,102 | 647 | 43,897 |
| <a href="datas/60 - Oise">60 - Oise</a> | 767,325 | 644 | 20,972 |
| <a href="datas/61 - Orne">61 - Orne</a> | 271,915 | 455 | 8,532 |
| <a href="datas/62 - Pas-de-Calais">62 - Pas-de-Calais</a> | 1,449,928 | 888 | 32,985 |
| <a href="datas/63 - Puy-de-Dôme">63 - Puy-de-Dôme</a> | 624,473 | 460 | 20,160 |
| <a href="datas/64 - Pyrénées-Atlantiques">64 - Pyrénées-Atlantiques</a> | 604,015 | 541 | 18,657 |
| <a href="datas/65 - Hautes-Pyrénées">65 - Hautes-Pyrénées</a> | 229,155 | 474 | 11,105 |
| <a href="datas/66 - Pyrénées-Orientales">66 - Pyrénées-Orientales</a> | 394,235 | 139 | 13,479 |
| <a href="datas/67 - Bas-Rhin">67 - Bas-Rhin</a> | 1,095,367 | 530 | 23,640 |
| <a href="datas/68 - Haut-Rhin">68 - Haut-Rhin</a> | 750,496 | 377 | 19,734 |
| <a href="datas/69D - Rhône">69D - Rhône</a> | 453,852 | 228 | 14,038 |
| <a href="datas/69M - Métropole de Lyon">69M - Métropole de Lyon</a> | 1,316,495 | 59 | 11,645 |
| <a href="datas/70 - Haute-Saône">70 - Haute-Saône</a> | 238,296 | 539 | 11,072 |
| <a href="datas/71 - Saône-et-Loire">71 - Saône-et-Loire</a> | 540,306 | 549 | 19,192 |
| <a href="datas/72 - Sarthe">72 - Sarthe</a> | 564,163 | 375 | 17,661 |
| <a href="datas/73 - Savoie">73 - Savoie</a> | 411,683 | 297 | 12,339 |
| <a href="datas/74 - Haute-Savoie">74 - Haute-Savoie</a> | 733,198 | 286 | 21,687 |
| <a href="datas/75 - Paris">75 - Paris</a> | 2,243,833 | 1 | 6,702 |
| <a href="datas/76 - Seine-Maritime">76 - Seine-Maritime</a> | 1,219,158 | 685 | 27,817 |
| <a href="datas/77 - Seine-et-Marne">77 - Seine-et-Marne</a> | 1,305,261 | 507 | 26,048 |
| <a href="datas/78 - Yvelines">78 - Yvelines</a> | 1,399,359 | 260 | 22,528 |
| <a href="datas/79 - Deux-Sèvres">79 - Deux-Sèvres</a> | 290,531 | 186 | 12,316 |
| <a href="datas/80 - Somme">80 - Somme</a> | 565,349 | 771 | 17,013 |
| <a href="datas/81 - Tarn">81 - Tarn</a> | 373,238 | 316 | 11,069 |
| <a href="datas/82 - Tarn-et-Garonne">82 - Tarn-et-Garonne</a> | 241,515 | 194 | 8,364 |
| <a href="datas/83 - Var">83 - Var</a> | 1,009,663 | 153 | 20,066 |
| <a href="datas/84 - Vaucluse">84 - Vaucluse</a> | 531,434 | 149 | 14,228 |
| <a href="datas/85 - Vendée">85 - Vendée</a> | 628,731 | 280 | 30,350 |
| <a href="datas/86 - Vienne">86 - Vienne</a> | 417,510 | 265 | 13,780 |
| <a href="datas/87 - Haute-Vienne">87 - Haute-Vienne</a> | 369,803 | 194 | 11,307 |
| <a href="datas/88 - Vosges">88 - Vosges</a> | 377,914 | 511 | 16,396 |
| <a href="datas/89 - Yonne">89 - Yonne</a> | 337,469 | 447 | 16,194 |
| <a href="datas/90 - Territoire-de-Belfort">90 - Territoire-de-Belfort</a> | 142,931 | 102 | 3,608 |
| <a href="datas/91 - Essonne">91 - Essonne</a> | 1,189,623 | 182 | 19,521 |
| <a href="datas/92 - Hauts-de-Seine">92 - Hauts-de-Seine</a> | 1,573,283 | 36 | 8,702 |
| <a href="datas/93 - Seine-Saint-Denis">93 - Seine-Saint-Denis</a> | 1,523,581 | 40 | 9,699 |
| <a href="datas/94 - Val-de-Marne">94 - Val-de-Marne</a> | 1,326,874 | 47 | 10,101 |
| <a href="datas/95 - Val-d'Oise">95 - Val-d'Oise</a> | 1,168,207 | 183 | 16,653 |

## Statistique totale

  * Total population     : 61,353,633
  * Total villes         : 34,519
  * Total rues           : 1,500,277
