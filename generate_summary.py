import os
import overpass
from collections import OrderedDict

DATAS_DIR="datas"
DATAS_ALL_DEPARTEMENTS="{DATAS_DIR}/departements.csv"
DATAS_ALL_VILLES="{DATAS_DIR}/villes.csv"

REPLACE_WORDS = {
    ' ':['D ','DE ', 'LA ','DU '],
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


endpoint = "http://localhost/api/interpreter"
timeout=600
api = overpass.API(endpoint=endpoint,timeout=600,debug=True)

departements = api.get(
    'area["name"="France"];relation["ref:INSEE"]["type"="boundary"]["boundary"="administrative"]["admin_level"="6"](area);',
    responseformat='csv(::"id","ref:INSEE","name","name_norm")'
)
# departements = api.get(
#     'area["name"="France"];(relation["ref:INSEE"="34"];relation["ref:INSEE"="30"];);',
#     responseformat='csv(::"id","ref:INSEE","name","name_norm")'
# )

ddpartements = OrderedDict()
for departement in departements[1:]:
    did,dinsee,dname,dname_norm = departement
    dname_norm = normalize(dname)
    
    
    ville_nodes = api.get(
        f'area["name"="{dname}"] -> .departement;(node(area.departement)[place=city]; node(area.departement)[place=town];node(area.departement)[place=village];);',
        responseformat='csv(::"id","ref:INSEE","name","name_norm","population","source:population")'
    )

    ville_relations = api.get(
        f'area["name"="{dname}"] -> .departement;(node(area.departement)[place=city]; node(area.departement)[place=town];node(area.departement)[place=village];);rel(bn:"admin_centre");',
        responseformat='csv(::"id","ref:INSEE","name","name_norm","population","source:population")'
    )


    if dinsee != "":
        ddpartements[dinsee] = {
            'id': did,
            'insee': dinsee,
            'name': dname,
            'name_norm': dname_norm ,
            'villes': OrderedDict(),
            'population': 0
        }

        # Parse Nodes
        for ville in ville_nodes[1:]:
            vid_node,vinsee,vname,vname_norm,population,source_population = ville

            vname_norm = normalize(vname)
            if vinsee != "":
                ddpartements[dinsee]['villes'][vinsee] = {
                    'did': did,
                    'dinsee': dinsee,
                    'dname': dname,
                    'dname_norm': dname_norm ,
                    'id_node': vid_node,
                    'id_relation':-1,
                    'insee': vinsee,
                    'name': vname,
                    'name_norm': vname_norm ,
                    'population': population,
                    'source_population': source_population
                }
                
                try:
                    population = int(population)
                    ddpartements[dinsee]['population'] += population
                except:
                    pass

        # Parse Relations
        for ville in ville_relations[1:]:
            vid_relation,vinsee,vname,vname_norm,population,source_population = ville

            vname_norm = normalize(vname)
            if vinsee != "":
                if vinsee in ddpartements[dinsee]['villes']:
                    ddpartements[dinsee]['villes'][vinsee]['id_relation'] = vid_relation


# Write datas
os.makedirs(DATAS_DIR,exist_ok=True)
with open(f'{DATAS_DIR}/departements.csv','w') as alldeps,open(f'{DATAS_DIR}/villes.csv','w') as allvilles:
    alldeps.write("insee;osm_relation;name;name_norm;population\n")
    allvilles.write("did,insee;osm_relation;osm_node;name;name_norm;population\n")

    sdepartements = OrderedDict(sorted(ddpartements.items()))
    for d in sdepartements:
        id = sdepartements[d]['id']
        insee = sdepartements[d]['insee']
        name = sdepartements[d]['name']
        name_norm = sdepartements[d]['name_norm']
        population = sdepartements[d]['population']
        alldeps.write(f"{insee};{id};{name};{name_norm};{population}\n")

        svilles = OrderedDict(sorted(sdepartements[d]['villes'].items()))
        for v in svilles:
            did = sdepartements[d]['villes'][v]['did']
            id_node = sdepartements[d]['villes'][v]['id_node']
            id_relation = sdepartements[d]['villes'][v]['id_relation']
            insee = sdepartements[d]['villes'][v]['insee']
            name = sdepartements[d]['villes'][v]['name']
            name_norm = sdepartements[d]['villes'][v]['name_norm']
            population = sdepartements[d]['villes'][v]['population']
            source_population = sdepartements[d]['villes'][v]['source_population']
            allvilles.write(f"{did};{insee};{id_relation};{id_node};{name};{name_norm};{population};{source_population}\n")