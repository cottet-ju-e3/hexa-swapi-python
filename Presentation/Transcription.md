# Présentation du sujet
## Attaque de l'empire
Le temps presse l'Empire intensifie ses attaques contre nos bases et nous avons énormément de mal à aller au secours de
rescapés.

## Resistance => système flotte de sauvetage
Nous devons admettre que nous avons du mal à nous organiser c'est pour cela que le Haut Conseil de la résistance nous
demande et bien de construire un système informatisé qui va nous nous aider à constituer des flottes de sauvetage à
partir et bien des vaisseaux dont on a à notre disposition.


Imaginons qu'on ait 5 personnes à aller secourir on va aller chercher dans notre référentiel de vaisseau existant qui
s'appelle swapy, tous les vaisseaux à notre disposition.
On va s'intéresser à leur capacité de transport de passagers.

On va extraire uniquement les vaisseaux qui transportent plus que le pilote, 
En appliquant un algorithme très poussé basé sur de l'IA on va sélectionner et bien (c'est à dire qu'il n'y aura plus if) 
on va sélectionner les vaisseaux qui permettent d'effectuer la mission de sauvetage 
Le falcon Millennium ayant assez de capacité de transport il est suffisant pour mener cette cette mission de sauvetage.

# Architecture N-Tiers
Il faut pas perdre de temps sur l'architecture à mettre en place pour et bien construire ce logiciel et je vous propose cette architecture là l'architecture n tiers avec un couche contrôleur une couche service qui dépend une couche de persistance.
"tout le monde est OK avec ça ?"

"c'était un piège" => Infiltrés de l'Empire ?

Même si elle est très utile bah elle a tendance un peu à mal vieillir parce que elle a quand même quelques petits problèmes déjà pour vous vous
l'illustrer.

Où est-ce que que se trouve la logique métier là-dedans ?

Comme cette architecture n'a pas été pensée pour avoir une isolation bien faite de cette couche service et bien la logique métier se trouve à leaker partout.

- dans la couche de persistance 
- dans la couche contrôleur 
- jusque dans le frontend 
- Les plus viles des ingénieurs de l'Empire ont tendance à mettre ça dans les procédure stockées

Dans le code d'un projet dont on ne citera pas le nom il y avait beaucoup de couplage et il y avait une forte tendance à mettre la logique métier côté couches de persistance.

Mettre de la logique métier là-dedans bah c'est galère parce que on peut plus faire de test unitaire pour valider
notre métier il va nous falloir une base ce qui est pas fou.

Mais on pourrait croire aussi que bah le seul problème c'est cette histoire la logique métier mais en réalité il y a aussi les responsabilités techniques qui lient partout parce que là on pourrait se dire bah la persistance c'est dans la couche de persistance et non là j'ai un autre exemple sur la même code base où on prépare des requêtes SQL dans le contrôleur.

Ici on est dans un qui représente leur objet métier donc c'est un vrai code que j'ai pris au hasard sur github et là on voit que c'est anoté par des ORM notamment hibernate donc qui permet de dire voilà ce champ là c'est une colonne dans ma base etc.

Dnc au passage c'est du SQL mais il y a aussi des magnifiques @json property et si vous savez pas ce que c'est en fait c'est un autre framework qui
s'appelle Jackson qui va vous aider à sérialiser ça en rest pour dire et ça va s'appeler ExerciceID dans ton contrôleur.

Donc ça veut dire que là on a tout couplé au même endroit ce qui fait que on va avoir énormément de difficultés bah à la fois de faire des tests parce que on va avoir des tests avec plusieurs responsabilités on va avoir aussi des conflits potentiels de de framework qui se collisionnent là-dessus hein parce qu'ils vont avoir potentiellement besoin de même dépendance mais dans des versions différentes mais l'autre truc aussi c'est que ce qu'on voit là c'est qu'il y a carrément des des directives de jointure là il y a des joint colonnes il y a même des directive de un peu plus loin je crois qu'il y a joint table ici en annotation sur les champs en fait de la couche service donc là.

## Changement de DB => mongo document
Si demain vous devez changer de techno de base de données et que vous passez à du Mongo
par exemple vous n'êtes plus en forme normale 3 vers des colonnes partout et cetera vous avez juste un document.

## Ca va casser aussi le controller (Et inversement si on change de REST à Graphql)
Vous êtes obligé de le changer et comme c'est couplé à votre contrôleur bah peut-être que ça va péter aussi votre contrôleur et pareil vous passez
de reste à graphql bah peut-être que ça va avoir un impact jusqu'à la base donc.

Il y a énormément de couplage dans la pratique qu'on a de cette architecture et souvent elle est
aussi amené par le fait qu'on a tendance à mettre notre framework structurant partout c'est-à-dire vraiment dans
n'importe quelle couche 

## Retour d'xp => montée de version de S-boot => tout à cassé (sans changer le code métier)
et pour vous donner un petit retour d'expérience sur les problèmes que ça peut vous apporter
quand je travaille chez xpéia on a monté un backend de du springbot 1.3 1.4 il y a plus rien qui compilait ça nous a pris un mois pour toute l'équipe à faire en sorte que le soft remarche.

Mais là-dedans en fait la logique métier n'avait pas changé on peut se poser la question est-ce que changer la version mineure d'un framework est-ce que ça devrait péter on sait tous que non mais est-ce que en plus ça devrait nous amener un doute sur la régression
fonctionnelle bien sûr que non.

Si on va plus loin ce qui arrive souvent quand on redéveloppe et bien des je dirais des legacy souvent c'est les legacy qui font le taf. 
Cad qu'ils rapportent de l'argent et la logique métier est bonne et ils sont sur sur des stacks très vieilles des EJB des servelet.

## Changer les technos pour qqch de plus cool
Enfin des trucs comme ça on se dirait ben ce serait cool de pouvoir prendre ce qui marche ce qui a du sens qui a de la valeur le métier l'extraire développer tout ce qui est autour et faire dans une stack plus neuve comme par exemple quarcus et spring boot est-ce que ça c'est
possible non parce que souvent c'est très couplé au framework 

## trop de couplage et réaction en chaine
plus comme c'est des dépendances en cascade vous avez une petite erreur de compilation dans la persistance la
couche chich ne fonctionne plus le contrôleur non plus compile plus et là c'est une réaction en chaîne donc j'ai
pas forcément le temps de vous tout vous expliquer  => Video topçu

# Framework pour être moins couplé (Architecture hexagonale)
On va voir un pattern pour être moins couplé pour amener moins de fragilité qui s'appelle l'architecture hexagonale.

## Centré sur le métier
On veut sacraliser ce qui apporte de de la valeur au métier donc on va pas mettre ça partout.
On va mettre ça à un seul endroit pour qu'en plus on puisse faire des tests qui n'aient qu'une seule responsabilité : tester le métier.

donc on prend toute cette logique métier et on la centralise dans un endroit qu'on appelle le domaine.

## Quelle différence avec la != avec la couche service ?
différence avec le service de tout à l'heure => "bah le nom"

## Double responsabilité 
la couche service d'avant elle avait une double responsabilité
- Du métier 
- Gérer les couches plus basses de persistance et de client web service
 
## Inverser la dépendance (la persistance dépend de mon domaine)
Donc là ça voudrait dire que si je fais ça mon domaine il dépend de ma couche technique la persistance donc ça je vais faire en sorte que ce soit plus le cas
pour que je puisse avoir un domaine agnostique de la technique et qui dépend d'aucun framework on va inverser la
dépendance ici à gauche pour que ce soit la persistance qui dépend du domaine et pas le contraire 

## Domain indépendant (Technique à l'extérieur)
Un domaine qui ne va dépendre de rien d'autre que de lui-même dans lequel je vais pouvoir et bien centraliser la logique métier et tout ce qui est technique je vais le mettre à l'extérieur.

La logique métier ce qu'on appelle la "complexité essentielle", c'est la raison d'être de votre logiciel ce
qui apporte de la valeur et bien à vos utilisateurs logique métier.

A l'extérieur c'est la "complexité obligatoire" c'est tout ce qui est nécessaire techniquement pour mettre en musique cette logique métier donc là on
fait du découplage comme ça et on va sacraliser les espaces.

## Dans le domaine : pas de framework
On va pouvoir les mettre à l'extérieur.
En revanche on va pas réinventer la roue on peut y mettre des librairies cependant si vous utilisez librairies faites attention à bien mesurer votre surface d'adhérence et que soit pas trop invasif parce que c'est pareil si elle devient obsolette ça va avoir des impacts sur le domaine.

## Hexagone ?
Pourquoi ça s'appelle un hexagone bah il paraît que si tu te mets d'un certain côté ce que dit alice cockburn ça ça ressemble à un hexagone quand tu le regardes sur le schéma j'ai jamais
Le domaine c'est l'Hexagone, l'extérieur c'est l'infrastructure et puis voilà.

## Isoler le domaine (API, SPI)
Comment on arrive à isoler notre domaine ? 
Il est protégé par deux couches internes qui sont l'API et la SPI 

Dans le domaine on a un ensemble d'interface 
### API
d'un côté les API qui est sont les interfaces qui définissent les contrats d'entrée du domaine qui généralement sont les contrats de fonctionnalité et qui vont servir à l'extérieur d'appeler le domaine comme par exemple ici notre controller. 
Il ne va pas pouvoir polluer mon domaine  => il est obligé de se conformer aux objets du domaine qui sont
utilisés dans cette interface et donc je n'aurai pas de d'annotation Jackson de contrôleur ou de concept de ressources REST dans le domaine.

Ca reste à l'extérieur  => plus facile de changere ce contrôleur pour y mettre ici potentiellement un resolver graphql.
Il y a juste ce côté à redévelopper.

### SPI
Cependant mon domaine il va avoir besoin aussi de données extérieures il fonctionne des fois pas tout seul il va avoir besoin d'une persistance ou d'un web service externe et donc là lui
ce qu'il va faire c'est qu'il va définir une autre interface qui s'appelle la SPI Service Providing Interface qui dit "j'ai besoin de service implémenté par
l'extérieur là".

Mais c'est moi qui donne le contrat donc ce contrat dépend que des objets du domaine qui fait qu'à l'extérieur on va avoir une couche de persistance qui va implémenter cet SPI et qui va dépendre que des objets du domaine donc pareil vos annotations ORM vont pas polluer le domaine votre structuration en DAO qui correspond en fait à une table de donné SQL ne va aucun avoir aucun impact sur votre domaine ce qui fait que ce sera plus facile de passer d'une techno de persistance à une autre.

Bien sûr l'API est implémenté par le domaine parce que c'est les fonctionnalités métier et la SPI par l'extérieur.

## Port Adapter
On appelle cette architecture aussi port et adapters
Les interfaces du domaine sont les ports sur lesquels se connectent des adaptateurs qui sont là
pour traduire le monde extérieur vers le monde du domaine mais je vous propose de rendre
ça beaucoup plus concret en en faisant une petite partie de Live code.

# Live coding explication
Faut savoir qu'en architecture hexagonale on commence toujours par implémenter la fonctionnalité dans dans le domaine
avant de faire le reste donc là disons que je pars de zéro.

## On commence par le domaine
J'ai qu'un module domaine et là les seules dépendances que j'ai dans mon domaine c'est JUnit et AssertJ  qui sont en fait des des framework de test donc c'est OK. 

## Structure de flotte (liste de vaisseaux)
j'ai juste une structure qui représente ma flotte une flotte c'est quoi c'est une liste de vaisseaux.

- un nom
- une capacité de transport de passagers

## Méthode de dev (drivé par les test)
L'architecture hexagonale en fait ce n'est pas qu'une architecture c'est aussi une approche cad c'est une méthode de développement enfin surtout en 2024 ça pas forcément été théorisé comme ça en 2000 mais en 2024 c'est comme ça qu'on l'utilise et donc on va driver ça un peu par les tests.

## Test à la place du controller
On va définir un test fonctionnel qui va se mettre en lieu et en place de notre contrôleur et qui va interagir avec notre domaine ce qui va
nous permettre de définir le contrat d'entrée de notre domaine.

## Description du test 
Il essaye pour 1050 passagers de construire une flotte.
C'est ici qu'on va appeler notre domaine métier et on va s'assurer que tous les vaisseaux de cette flotte ont assez de capacité de transport tous ensemble et
bien pour transporter tous les passagers et s'assurer aussi que chacun des vaissaux ont de la capacité de transport

Les Xwing qui transportent que les pilotes vont pas nous intéresser ok

# Live code start
je vais tout de suite écrire ce que j'attends, la manière dont j'attends d'interagir avec mon domaine.
Quand je suis à l'extérieur de mon domaine, comment j'aimerais appeler les fonctionnalités de mon domaine.

## Assemble a fleet
Mais là j'aimerais bien un truc qui s'appelle "assemble_a_fleet(for_passengers)

Je suis déjà en train par émergence de définir les contrats avec ce truc qui n'existe pas
=> Je vais le créer ici je vais lui donner un type 

## Class ou interface (Avis) ?
on propose soit classe soit interface.
=> Plutôt interface parce ça va vous aider à mieux stubber sans framework le contrôleur.

## Quelle couche d'interface (Vous avez suivi ?)
Oui l'API donc API au sens programmatique du terme  => Pas l'API WEB.
Vous pouvez appeler remplacer API par features c'est peut-être même plus idiomatique.

je vais demander à mon IDE de créer le contrat défini ici par son utilisation

## Contrat, forteresse (aucun concept externe qui rentre dans le domain)

## Implémentation concrète (FleetAssembler)
Je vais appeler FleetAssembleur dans le code de prod et donc là il va implémenter forcément le contrat que fini et devoir avoir une méthode for
passengers qui renvoie une flotte 

## Implementation (Préparation) 
Le code hyper compliqué de ce que fait cet algorithme.
Comment je vais constituer mes flottes d'un point de vue métier
- Premier truc bah les vaisseaux je les ai pas les vaisseaux
- Ils sont dans mon référentiel externe qui s'appelle "swapi" 
- swapy en fait c'est une API Web en REST ok donc il va falloir que je gère l'interconnexion avec ça pour récupérer
ces vaisseaux ensuite une fois que j'ai récupérer les vaisseaux de l'inventaire c'est là dedans que je vais avoir mon IA
qui va me sélectionner mes vaisseaux à partir du nombre de passagers pour constituer ma flotte

## Si vrai swapi => Call HTTP => couplage technique => Demain autre chose que swapi (exemple système de stream)
## => Impact sur mon domain
Donc on va aller créer la fonction qui permet déjà de récupérer et bien les vaisseaux de l'inventaire?
Si j'ai utilisé le vrai swapi je serais obligé de faire appels HTTP mais si je fais ça je serais en train de coupler mon domaine métier avec de la technique
parce que demain je pourrais utiliser autre chose que swap je pourrais utiliser un autre référentiel qui ne fait pas de REST ou qui fait même pas d'HTTP qui streamerait de la donnée par
exemple donc ça voudrait dire que là j'aurai un impact sur mon domaine si je change de partenaire et là je veux que
mon domaine en fait il soit agnostique de ça je veux en fait essentiellement il a besoin d'utiliser un inventaire.

## Si l'inventaire change => logique métier ne change pas
Je vais créer une abstraction qui me permet de représenter le contrat avec mon starship inventory pour requêter l'extérieur de mon domaine.

## Starship inventory
Je vais l'appeler StarshipInventory il va falloir encore une fois que je crée une classe ou une interface comment 

Cette interface je la mets dans quoi ? => SPI

## Par injection => C'est là que se trouvera le vrai client swapi

## Contrat dans la SPI => Méthode starships() -> list[Starship] => Pas de pollution du domain
Ces starships là sont des objets du domaine métier donc c'est pareil de l'extérieur on pourra pas polluer mon
domaine parce qu'ici c'est que des objets du domaine.

## Générer le code qui filre les starships
ok alors j'ai un tout petit truc à faire qui est pas très
utile pour vous qui est de dégager les Starship qui ont pas de capacité de transport voilà c'est pas très important
ça et attention c'est là où je vais vous émerveiller avec ce code qui permet de sélectionner les vaisseaux vous êtes pas prêt c'est un modèle très compliqué je
rajoute les vaisseaux un à un jusqu'à ce que j'ai la capacité de transport voilà j'ai mes deux if là avec un while et puis un ah j'en ai même pas deux c'est pas de l'IA

## Inventory instance => Intellij error (dans le test) => founir un stub
Test dans le domaine => ça ne peut pas être le vrai => Stub => Permet de simuler l'extérieur
ce que je veux ici c'est tester le domain (pas l'intégration).
On la testera plus tard.

## Run test + applause

## Résumé
- un test fonctionnel qui se comporte comme s'il était le contrôleur 
- il appelle le domaine depuis l'extérieur
- le domaine lui il définit son contrat qui est "AssembleAFleet"
    - "c'est comme ça que tu vas devoir interagir avec moi" 
    - si tu veux construire des flottes AssembleAFleet dépend que des objets Starship du domaine 
    - rien va pouvoir polluer mon domaine 
- c'est implémenté par le domaine parce que c'est du métier FleetAssembleur
- Mais lui il a besoin des données de l'inventaire
- L'inventaire c'est techniqu c'est swapi 
    - je crée une abstraction qui dépend que des objets du domaine
    - je pourrais avoir l'implémentation que je veux 
    - la changer n'aura aucun impact sur le domaine 
- pour que mon domaine puisse être testé en standalone
    - Je créé un stub
- L'étape d'après vous en doutez et bien ça va être d'ouvrir à gauche 
- C'est-à-dire que on va implémenter un contrôleur pour exposer cette logique métier sur le réseau

# Génération du controller (à cause du boilerplate) => Avance Rapide

## module d'infrastructure (depend du domain mais pas l'inverse)
Domaine ne dépend toujours pas du framework que j'ai utilisé qui est spring 

En revanche mon infrastructure comme vous voyez ici dépend de mon domaine sinon il pourra pas l'appeler

## TDD controller qui appelle l'url
Le but c'était de créer le contrôleur j'ai créé un test oui parce qu'on fait aussi du tdd donc on commence par le test d'intégration ici on fait un post sur
l'URL RescueFleet et je donne un paramètre qui est number_of_passengers à 5 et je
dis que en retour je dois avoir 
- un statut à Created (201) 
- une reponse json
    - un ID 
    - une liste de vaisseaux 
        - un seul vaisseau 
            - nom : Millennium Falcon
            - La capacités 6 en capacité donc là j'ai défini mon contrat d'API REST

## REST implementation
Je suis mappé sur la bonne URL ça commence bien je peux faire un post et là j'ai mon r request qui est en fait
le payload de la requête sérialisé qui comporte number of_passengers donc vous vous en doutez ici 

## Appel de la méthode métier
C'est l'API donc c'est AssembleAFleet (number_of_passengers ça vient de rescue_fleet)

voilà euh mince qu'est-ce qu' me fait là hop ça vient de rescue flit request et la semb de flit
n'existe pas donc il va falloir que j'en fais je me fasse injecter donc là moi je
vais utiliser l'interface mais comme je dis de ce côté-là si vousutilisez l'implémentation concrète c'est pas très
grave et je vais me le faire injecter par constructeur bon là ça compile pas
parce qu'en fait mon contrôleur il s'attend pas réellement à une flotte du domaine :

Vous avez deux choix 
- soit en fait vous faites vraiment l'implémentation et vous vous lancez sur la partie swapy 
- soit vous faites comme moi et vous allez le stubber ce qui permet de tester en fait le contrôleur et le domaine ensemble 

## Implémentation du stub (Il y a un intéret plus tard)
En gros j'ai créé un truc qui s'appelle StarshipInventoryStub qui va me servir 
- dans mes tests mais pas que
- je l'ai mis dans mon code de prod donc il implémente mon StarshipInventory mais c'est un stub

## Lancement du test avec le stub
Pour l'instant j'ai pas une vraie implémentation j'ai ce truc et je vais le mettre dans mon code de prod et ça va

## Pourquoi dans le domain ?
Ca va me permettre d'aller déployer en réalité cette application potentiellement en prod ou
en préprod.

## Utile pour travailler avec les équipes frontend (ou mobile) alors que l'on n'a pas accès au service final
Bonus: permet de // le travail

# Call réellement l'api SWAPI ?
## Présentation API (swapi.dev)
On va développer notre client swap mais pour ça faut d'abord que je vous présente c'est un vrai truc qui tourne
C'est une api avec un référentiel sur l'univers de Star Wars. 
Plein trucs les planètes les vaissaux les véhicules les personnages moi 

## Url des vaisseaux
Ce qui va m'intéresser ici en fait c'est l'url qui permet de récupérer les vaisseaux de l'univers de Star Wars

Je faire comme si c'était mon référentiel de vaissau donc ça on va l'intégrer

# Saut dans le temps (Génération boilerplate code)

## Que fait le test ?
Ici je suis sur mon test qui va définir mon inventaire dans infrastructure?
Il vérifie que quand j'appelle Starship sur mon swapi_client et bien je vais avoir ces vaisseaux

## Mock client swapi (Pour protéger la CI/CD)
Ca va me simuler le vrai swapy et ça va l'embarquer dans mes tests 

J'ai capturé les Json de swapi et simule swapi dans les tests

## Swapi est paginé
Swapi en fait c'est un truc qui est paginé il y a un "next"
Ils ont fait ce choix mais moi j'ai pas envie 
Mon domaine n'a pas été pensé pour être paginé et qu'il est agnostique en fait de swapy 

## Mapping différent
Il y a un deuxième truc:
- les vaisseau s'appelle "results" je préfère "Starship" 
- il y a plein d'informations dont j'ai pas besoin 
- ce que j'ai besoin c'est "name" ici ça matche avec ce que j'ai défini 
- passengers != capacity 
- passenger c'est un "string" moi ça m'arrange pas parce que j'ai envie de le Sommer moi en fait 
- les capacités de transport de passagers string c'est galère
 
## Hexa à la rescousse
swapi string => dans l'implémentation du client swapi => dans mon domaine "integer" 
C'est pas mon domaine qui a besoin de se prendre la tête avec ça si je changeais de référentiel et que je passais un référentiel qui me le fait en in comme j'ai pas besoin j'ai pas
besoin de changer mon code pour ça donc

## Implementation swapy client
 => Generation de code

Starship qu'est-ce que j'ai dans un swapy Starship j'ai un nom et passengers qui un string donc vous voyez déjà que
le modèle de swapi c'est pas le modèle de mon domaine et là je suis pas pollué par la modélisation de swapi

## Génération de la pagination
"Explication du code"
- Call
- Conversion (Adapter)

## Lancement du test => Rouge
ouais bah je vous rappelle que même en acceptant test driven développement on commence par un truc qui est rouge 

## Parsing de swapi avec "n/a" ou "unknown" ou séparateur de millier
C'est géré dans l'adaptateur : si je change encore une fois d'implémentation et bien je n'auris à changer mon domaine
donc dans le client
jà et prochain truc alors là je faire un petit filtre qui va s'assurer que tous mes vaisseaux on une valide passengers value et ma valide passengers value ce filtre

## Test vert (Ouiii) 

## Lancement de l'application + exécution réelle de bout en bout
Merci et là en fait maintenant si j'exécute bien mon application
effectivement ce qui va se passer c'est que je vais avoir un truc de bout en bout là je vais appeler le vrai
swapy vous voyez les le les vaisseaux ont changé j'en ai plus hein ceux que j'avais mis dans mon stub


## TODO
donc là j'ai vraiment un truc de bout en bout ce que je vous ai pas
montré là pas avoir le temps de montrer c'est que j'ai aussi un test d'intégration qui va tester ensemble le
contrôleur le domaine et la persistance enfin de bout en bout dans mon test enfin dans mon code de
prod donc là si je résume cette cette étape en
fait donc un test d'intégration sur mon swapi client qui implémente mon Starship
inventory mais swapi a sa propre représentation de ce qui a un vaisseau donc je mets swapi Starship avec mes
passengers au lieu de capacity chez moi qui en plus est un string chez eux et qui est un L chez moi donc là en fait la
responsabilité de l'adaptateur c'est de faire ce qu'on appelle un antiorruption layer qui va convertir le modèle de
swapi vers le modèle du domaine de telle manière ce que les données du domaine soit toujours valide donc on se prend
pas la tête avec est-ce que c'est n pas de code défensif dans le domaine he tout ça est fait dans
l'adaptateur alors admettons que j'ai mis ça en prod et que ça marche bien mais qu'on a
tendance à enfin queon a tendance à remarquer que nos reskp laissent le matériel derrière eux
parce qu'on a pas pensé à avoir de la capacité de transport dans nos vaisseaux donc là on
a fait évoluer notre algorithme pour prendre en compte le fait que il y a une capacité de transport minimale de 100000
M C pour chacun des vaisseaux qu'on sélectionne pour constituer notre flotte
ce qui a amené en fait ici à faire star avec un cargo capacity ok en
revanche cargo capacity c'est de laouille interne donc je le récupère de SW ça me ser sélection je ne veux pas ça
sur tu n parles de ça la fin de T parce fait i truc qui me dérange capacity CARG
capacity pasou conf pourquoi ça je le renommer
pas en fait passengers capacity
pourquoi je fais un refactoring comme ça à la fin du to c'est quoi l'impact de ce que je viens de faire à votre
avis j'ai pété mon consommateur regardez je balance le test du
contrôleur et qu'est-ce que va me dire le test de mon contrôleur et ben il fonctionne pas
pourquoi parce qu'il me dit mais attends je comprends pas je m'attendais à avoir capacité dans le Jon là et ce que tu me
remontes c'est un truc avec passengers capacity et cargo capacity que je sais même pas ce que c'est donc là en fait
j'ai cassé mes consommateurs et la raison pour laquelle je les ai cassé c'est parce que en fait mon contrôleur
n'a pas de représentation directe d'une ressource il il salise directement le domaine donc j'ai couplé mes
consommateurs avec et bien mon domaine métier ce qui fait que si je veux faire des évolutions bah à chaque fois je vais
les casser et je vais devoir gérer en fait la versioning rest dans mon domaine ce qui est pas fou parce que le domaine
c'est pas fait pour ça reste ça doit rester dans le contrôleur donc le versioning rest la déprication de champ
tout ça c'est dans le contrôleur donc ce qui manque ici c'est que de manière implic enfin ce que j'ai fait là c'est
que de manière implicite mes ressources rest sont en fait mes objets du domaine c'est alors des fois on peut s'aligner
ça va mais des fois ça peut vous causer des problèmes donc là en fait il faut créer une
représentation vraiment dans le contrôleur de ce qui est vos ressources REST et là vous allez voir que c'est un
petit peu Chang ch on finit là-dessus ici j'ai mon contrôleur qui va me
renvoyer des flit resources et plus directement des flit donc qui sont des objets en fait de la couche d'infrastructure qui a une liste de
Starship resource et là vous regardez qu'il y a une différence de mapping en fait ici mon Starship il a qu'un nom et
un passengers mais ma Starship resource elle elle la capacity pour être backward compatible avec mes consommateur
passengers capacity qui est le nouveau truc et j'ai un liste de dépréciation ici pour dire à mes utilisateurs
attention ce truc là est déprécié utilise ça à la place donc là j'ai vraiment ma gestion en fait côté
contrôleur donc tout ça pour vous dire qu'en fait il est important aussi d'avoir vos ressources ici à gauche et
faire cette antiorruption layer si vous voyez mon talk qui s'appelle que j' fait ici reste next level écré des appis web
en orienté métier vous verrez que la comment sont structuré mes mes
ressources rest n'ont rien à voir sur les objets métiers de mon domaine mais vraiment rien à
voir donc la Big Picture c'est ça et pour finir je vous remercie vous pouvez
scanner en fait le QR code ici pour avoir accès en fait à mon repository et si des questions bah je suis disponible
après la conférence merci beaucoup

