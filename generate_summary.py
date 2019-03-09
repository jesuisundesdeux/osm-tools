import os
import csv
import shutil
import overpass
from collections import OrderedDict

DATAS_DIR="datas"
DATAS_ALL_DEPARTEMENTS="{DATAS_DIR}/departements.csv"
DATAS_ALL_VILLES="{DATAS_DIR}/villes.csv"

REPLACE_WORDS = {
    ' ':['D ','DE ', 'DES ', 'LA ','LES ','DU '],
    }

# Remove accents
REMOVE_SYMBOLS_ACCENTS = {
    'A':[u'Â',u'À'],
    'C':[u'Ç'],
    'E':[u'È',u'Ê',u'É',u'Ë'],
    'I':[u'Ï',u'Î'],
    'O':[u'Ö',u'Ô'],
    'U':[u'Û',u'Ü'],
    ' ': ['-','\'','"','/','.']
    }

TYPE_VOIE = (
    "ANCIEN CHEMIN",
    "AERODROME",
    "AEROGARE",
    "AGGLOMERATION",
    "AIRE",
    "ALLEE",
    "ANGLE",
    "ARCADE",
    "ANCIENNE ROUTE",
    "AUTOROUTE",
    "AVENUE",
    "BASE",
    "BOULEVARD",
    "BERGE",
    "BORD",
    "BARRIERE",
    "BOURG",
    "BRETELLE",
    "BASSIN",
    "CARRIERA",
    "CALLE,CALLADA",
    "CAMIN",
    "CAMP",
    "CANAL",
    "CARREFOUR",
    "CARRIERE",
    "CASERNE",
    "CHEMIN COMMUNAL",
    "CHEMIN DEPARTEMENTAL",
    "CHEMIN FORESTIER",
    "CHASSE",
    "CHEMIN",
    "CHEMINEMENT",
    "CHALET",
    "CHAMP",
    "CHAUSSEE",
    "CHATEAU",
    "CHEMIN VICINAL",
    "CITE",
    "COURSIVE",
    "CLOS",
    "COULOIR",
    "COIN",
    "COL",
    "CORNICHE",
    "CORON",
    "COTE",
    "COUR",
    "CAMPING",
    "CHEMIN RURAL",
    "COURS",
    "CROIX",
    "CONTOUR",
    "CENTRE",
    "DARSE,DARCE",
    "DEVIATION",
    "DIGUE",
    "DOMAINE",
    "DRAILLE",
    "DESCENTE",
    "ECART",
    "ECLUSE",
    "EMBRANCHEMENT",
    "EMPLACEMENT",
    "ENCLOS",
    "ENCLAVE",
    "ESCALIER",
    "ESPLANADE",
    "ESPACE",
    "ETANG",
    "FOND",
    "FAUBOURG",
    "FONTAINE",
    "FORET",
    "FORT",
    "FOSSE",
    "FERME",
    "GALERIE",
    "GARE",
    "GRAND BOULEVARD",
    "GRANDE PLACE",
    "GRANDE RUE",
    "GREVE",
    "HABITATION",
    "HAMEAU",
    "HIPPODROME",
    "HALLE",
    "HALAGE",
    "HLM",
    "HAUTEUR",
    "ILE",
    "ILOT",
    "IMPASSE",
    "JARDIN",
    "JETEE",
    "LAC",
    "LEVEE",
    "LICES",
    "LIGNE",
    "LOTISSEMENT",
    "MAIL",
    "MAISON",
    "MARCHE",
    "MARE",
    "MAS",
    "MORNE",
    "MARINA",
    "MONTEE",
    "NOUVELLE ROUTE",
    "PETITE AVENUE",
    "PARC",
    "PASSAGE",
    "PASSE",
    "PETIT CHEMIN",
    "PORCHE",
    "PHARE",
    "PISTE",
    "PARKING",
    "PLACE",
    "PLACA",
    "PLAGE",
    "PLAN",
    "PLACIS",
    "PASSERELLE",
    "PLAINE",
    "PLATEAU",
    "POINTE",
    "PONT",
    "PORTIQUE",
    "PORT",
    "POSTE",
    "POTERNE",
    "PROMENADE",
    "PETITE ROUTE",
    "PARVIS",
    "PETITE ALLEE",
    "PORTE",
    "PETITE RUE",
    "PLACETTE",
    "QUARTIER",
    "QUAI",
    "RACCOURCI",
    "REMPART",
    "RESIDENCE",
    "RIVE",
    "RUELLE",
    "ROCADE",
    "RAMPE",
    "ROND POINT",
    "ROTONDE",
    "ROUTE",
    "RUE",
    "RUETTE",
    "RUISSEAU",
    "RUELLETTE",
    "RAVINE",
    "SAS",
    "SENTIER",
    "SQUARE",
    "STADE",
    "TERRE",
    "TOUR",
    "TERRE PLEIN",
    "TRAVERSE",
    "TRABOULE",
    "TERRAIN",
    "TERTRE",
    "TERRASSE",
    "TUNNEL",
    "VAL",
    "VALLON,VALLEE",
    "VOIE COMMUNALE",
    "VIEUX CHEMIN",
    "VENELLE",
    "VILLAGE",
    "VIA",
    "VIADUC",
    "VILLE",
    "VILLA",
    "VOIE",
    "VOIRIE",
    "VOUTE",
    "VOYEUL",
    "VIEILLE ROUTE",
    "ZA",
    "ZAC",
    "ZAD",
    "ZI",
    "ZONE",
    "ZUP",
)

TYPE_VOIE_BY_SIZE = {}

# Replace word
def replace_words(words, text):
    for word in iter(words):
        for search in words[word]:
            if text.find(search)==0:
                # Begin word
                text = text.replace(search,word)  
            else:
                search = " %(search)s" % locals()
                text = text.replace(search,word)

    text = text.strip()

    return text

def normalize(text, remove_word=False):
    text = text.upper()
    text = " ".join(text.split())
    
    # Remove accent
    for c in iter(REMOVE_SYMBOLS_ACCENTS):
        for r in REMOVE_SYMBOLS_ACCENTS[c]:
            text = text.replace(r,c)    

    if remove_word:
        text = replace_words(REPLACE_WORDS,text)

    return text

def initTypeVoie():
    global TYPE_VOIE_BY_SIZE

    for v in TYPE_VOIE:
        size=len(v)
        if size not in TYPE_VOIE_BY_SIZE:
            TYPE_VOIE_BY_SIZE[len(v)] = list()

        TYPE_VOIE_BY_SIZE[size].append(v)

    TYPE_VOIE_BY_SIZE = OrderedDict(sorted(TYPE_VOIE_BY_SIZE.items(),reverse=True))        
        

def getTypeVoie(text):
    global TYPE_VOIE_BY_SIZE

    text_norm=normalize(text)
    voie = ''
    for s in TYPE_VOIE_BY_SIZE:
        for v in TYPE_VOIE_BY_SIZE[s]:
            if text_norm.find(v)==0:
                voie = v
                break 

        if voie != '':
            break

    return voie


endpoint = "http://localhost/api/interpreter"
timeout=600
api = overpass.API(endpoint=endpoint,timeout=600,debug=True)

def populateDepartementsList(ddpartements):
    csvdepname = f'{DATAS_DIR}/departements.csv'
    if os.path.exists(csvdepname):
        with open(csvdepname,'r') as csvfile:
            departements = csv.DictReader(csvfile, delimiter=';',quotechar='"')
            for d in departements:
                ddpartements[d['insee']] = {
                    'id': d['osm_relation'],
                    'insee': d['insee'],
                    'name': d['name'],
                    'name_norm': d['name_norm'] ,
                    'villes': OrderedDict(),
                    'population': 0,
                    'nb_streets': 0
                }
    else:
        departements = api.get(
            'area["name"="France"];relation["ref:INSEE"]["type"="boundary"]["boundary"="administrative"]["admin_level"="6"](area);',
            responseformat='csv(::"id","ref:INSEE","name","name_norm";false)'
        )
        # departements = api.get(
        #     'area["name"="France"];(relation["ref:INSEE"="34"];relation["ref:INSEE"="30"];);',
        #     responseformat='csv(::"id","ref:INSEE","name","name_norm")'
        # )

        for departement in departements:
            did,dinsee,dname,dname_norm = departement
            dname_norm = normalize(dname)

            if dinsee != "":
                ddpartements[dinsee] = {
                    'id': did,
                    'insee': dinsee,
                    'name': dname,
                    'name_norm': dname_norm ,
                    'villes': OrderedDict(),
                    'population': 0,
                    'nb_streets': 0,
                }
    sdepartements = OrderedDict(sorted(ddpartements.items()))        
    return sdepartements

def writeDepartementsFile(ddpartements):
    os.makedirs(DATAS_DIR,exist_ok=True)

    filename = f'{DATAS_DIR}/departements.csv'
    with open(f"{filename}",'w') as alldeps:
        alldeps.write("insee;osm_relation;name;name_norm;population\n")

        for dinsee in ddpartements:
            id = ddpartements[dinsee]['id']
            insee = ddpartements[dinsee]['insee']
            name = ddpartements[dinsee]['name']
            name_norm = ddpartements[dinsee]['name_norm']
            population = ddpartements[dinsee]['population']
            alldeps.write(f"{insee};{id};{name};{name_norm};{population}\n")

def populateVillesList(ddpartements):
    dvilles = OrderedDict()
    csvvillename = f'{DATAS_DIR}/villes.csv'
    if os.path.exists(csvvillename):
        with open(csvvillename,'r') as csvfile:
            dvilles = csv.DictReader(csvfile, delimiter=';',quotechar='"')
            for v in dvilles:
                vinsee = v['ville_insee']
                ddpartements[v['dep_insee']]['villes'][vinsee] = {
                    'ville_node':v['ville_node'],
                    'ville_relation':v['ville_relation'],
                    'name':v['name'],
                    'name_norm':v['name_norm'],
                    'population':v['population'],
                    'source_population': v['source_population']
                }


                try:
                    ddpartements[v['dep_insee']]['population'] += int(v['population'])
                except:
                    pass

    else:
        for dinsee in ddpartements:
            did = ddpartements[dinsee]['id']
            dinsee = ddpartements[dinsee]['insee']

            # Get cities node for population informations
            area_id=3600000000+int(did)
            ville_nodes = api.get(
                f'area({area_id}) -> .departement;(node(area.departement)[place=city]; node(area.departement)[place=town];node(area.departement)[place=village];);',
                responseformat='csv(::"id","ref:INSEE","name","name_norm","population","source:population";false)'
            )

            # Get cities relation for border city
            ville_relations = api.get(
                f'area({area_id}) -> .departement;(node(area.departement)[place=city]; node(area.departement)[place=town];node(area.departement)[place=village];);rel(bn:"admin_centre");',
                responseformat='csv(::"id","ref:INSEE","name","name_norm","population","source:population";false)'
            )

            # Parse Nodes
            for ville in ville_nodes:
                ville_node,insee,name,name_norm,population,source_population = ville

                name_norm = normalize(name)
                if insee != "":
                    ddpartements[dinsee]['villes'][insee] = {
                        'ville_node': ville_node,
                        'ville_relation':-1,
                        'name': name,
                        'name_norm': name_norm ,
                        'population': population,
                        'source_population': source_population
                    }
                    
                    try:
                        population = int(population)
                        ddpartements[dinsee]['population'] += population
                    except:
                        pass

            # Parse Relations
            for ville in ville_relations:
                ville_relation,vinsee,vname,vname_norm,population,source_population = ville

                vname_norm = normalize(vname)
                if vinsee != "":
                    if vinsee in ddpartements[dinsee]['villes']:
                        ddpartements[dinsee]['villes'][vinsee]['ville_relation'] = ville_relation


    for dinsee in ddpartements:
        ddpartements[dinsee]['villes'] = OrderedDict(sorted(ddpartements[dinsee]['villes'].items()))

    sdepartements = OrderedDict(sorted(ddpartements.items()))        
    return sdepartements


def writeAllVillesOnFile(ddpartements):
    os.makedirs(DATAS_DIR,exist_ok=True)

    filename = f'{DATAS_DIR}/villes.csv'
    with open(f"{filename}",'w') as allvilles:
        allvilles.write("dep_relation;dep_insee;ville_relation;ville_node;ville_insee;name;name_norm;population;source_population\n")

        for dep_insee in ddpartements:
            dep_relation = ddpartements[dep_insee]['id']

            for ville_insee in ddpartements[dep_insee]['villes']:
                ville_node = ddpartements[dep_insee]['villes'][ville_insee]['id_node']
                ville_relation = ddpartements[dep_insee]['villes'][ville_insee]['id_relation']
                name = ddpartements[dep_insee]['villes'][ville_insee]['name']
                name_norm = ddpartements[dep_insee]['villes'][ville_insee]['name_norm']
                population = ddpartements[dep_insee]['villes'][ville_insee]['population']
                source_population = ddpartements[dep_insee]['villes'][ville_insee]['source_population']
                allvilles.write(f"{dep_relation};{dep_insee};{ville_relation};{ville_node};{ville_insee};{name};{name_norm};{population};{source_population}\n")

    
def writeAllVillesOnFile(ddpartements):
    os.makedirs(DATAS_DIR,exist_ok=True)
    with open(f'{DATAS_DIR}/villes.csv','w') as allvilles:
        allvilles.write("dep_relation;dep_insee;ville_relation;ville_node;ville_insee;name;name_norm;population;source_population\n")

        for dep_insee in ddpartements:
            dep_relation = ddpartements[dep_insee]['id']

            for ville_insee in ddpartements[dep_insee]['villes']:
                ville_node = ddpartements[dep_insee]['villes'][ville_insee]['ville_node']
                ville_relation = ddpartements[dep_insee]['villes'][ville_insee]['ville_relation']
                name = ddpartements[dep_insee]['villes'][ville_insee]['name']
                name_norm = ddpartements[dep_insee]['villes'][ville_insee]['name_norm']
                population = ddpartements[dep_insee]['villes'][ville_insee]['population']
                source_population = ddpartements[dep_insee]['villes'][ville_insee]['source_population']
                allvilles.write(f"{dep_relation};{dep_insee};{ville_relation};{ville_node};{ville_insee};{name};{name_norm};{population};{source_population}\n")

def generateStreetsfiles():
    print("Generate streets files ...")
    for dinsee in ddpartements:
        dname = ddpartements[dinsee]['name']

        for vinsee in ddpartements[dinsee]['villes']:
            vid_relation = ddpartements[dinsee]['villes'][vinsee]['ville_relation']
            vname = ddpartements[dinsee]['villes'][vinsee]['name']
            vname_norm = ddpartements[dinsee]['villes'][vinsee]['name_norm']

            vpath = f"{DATAS_DIR}/{dinsee} - {dname}/{vinsee} - {vname}"
            filename = f'{vpath}/streets.csv' 
            os.makedirs(vpath,exist_ok=True)
            if os.path.exists(filename):
                with open(filename) as fcount:
                    nblines = len(fcount.readlines())
                    ddpartements[dinsee]['nb_streets'] += nblines
                continue

            # Get city street ways
            area_id=3600000000+int(vid_relation)
            street_ways = api.get(
                f'area({area_id})->.ville;way["highway"]["name"](area.ville)',
                responseformat='csv(::"id","name";false;";")'
            )

            dstreets = OrderedDict()
            for street in street_ways:
                try:
                    id,name = street[0].split(";")
                    if name not in dstreets:
                        name_norm = normalize(name)
                        voie = getTypeVoie(name)
                        if voie != '':
                            tmp_name_norm = name_norm.replace(voie,'',1).strip()

                            # check if type voie is a real street name
                            if len(tmp_name_norm) != 0:
                                name_norm = tmp_name_norm
                            else:
                                #type voie is a real street name
                                voie = ""

                        last_word = name_norm.split()[-1]
                        dstreets[name] = {
                            'voie': voie,
                            'name': name,
                            'name_norm': name_norm,
                            'last_word': last_word,
                            'ways': list()
                        }

                    dstreets[name]['ways'].append(id)
                except:
                    print(f"########## {street}")


            try:
                with open(filename,'w') as allstreets:
                    allstreets.write("voie;name;name_norm;last_word_norm;ways\n")
                    sstreets = OrderedDict(sorted(dstreets.items()))
                    for streetname in sstreets:
                        ways = ','.join(sstreets[streetname]['ways'])
                        line = f"{sstreets[streetname]['voie']};{streetname};{sstreets[streetname]['name_norm']};{sstreets[streetname]['last_word']};{ways}"
                        allstreets.write(f"{line}\n")
            except:
                print(sstreets[streetname])
                raise

def generateReadmeFile():
    # Generate Readme
    shutil.copyfile("README_template.md", "README.md")
    with open("README.md", 'a') as docfile:
        tot_pop = 0
        tot_cities = 0
        tot_streets = 0

        docfile.write("## Statistique par departement\n\n")
        docfile.write("| Departement | Nb population | Nb villes | nb rues |\n")
        docfile.write("|-------------|---------------|-----------|---------|\n")
        for dinsee in ddpartements:
            depname = ddpartements[dinsee]['name']
            population = ddpartements[dinsee]['population']
            nb_cities = len(ddpartements[dinsee]['villes'])
            nb_streets = ddpartements[dinsee]['nb_streets']
            tot_pop += ddpartements[dinsee]['population']
            tot_cities += len(ddpartements[dinsee]['villes'])
            tot_streets += ddpartements[dinsee]['nb_streets']

            docfile.write(f"| <a href=\"datas/{dinsee} - {depname}\">{dinsee} - {depname}</a> | {population:,} | {nb_cities:,} | {nb_streets:,} |\n")

        docfile.write("\n")
        docfile.write("## Statistique totale\n\n")
        docfile.write(f"  * Total population     : {tot_pop:,}\n")
        docfile.write(f"  * Total villes         : {tot_cities:,}\n")
        docfile.write(f"  * Total rues           : {tot_streets:,}\n")

# Load or generate deparments/cities datas
initTypeVoie()
ddpartements = OrderedDict()
ddpartements = populateDepartementsList(ddpartements)
ddpartements = populateVillesList(ddpartements)

# Write datas
writeDepartementsFile(ddpartements)
writeAllVillesOnFile(ddpartements)
generateStreetsfiles()
generateReadmeFile()