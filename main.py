from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
import random
import time

dict_sportifs = {
    "Lionel Messi": "Footballeur argentin né en 1987, l'homme aux huit Ballons d'or, considéré comme le plus grand de son sport.",
    "Cristiano Ronaldo": "Footballeur portugais né en 1985, quintuple Ballon d'or, le plus grand buteur de l'histoire.",
    "Neymar": "Footballeur brésilien né en 1992, connu pour sa technique spectaculaire, transféré pour un record de 222 millions d'euros au PSG en 2018.",
    "Kylian Mbappé": "Footballeur français né en 1998, champion du monde à 19 ans et l'un des visages majeurs du football moderne.",
    "Pelé": "Footballeur brésilien (1940-2022), triple champion du monde et légende incontestée du football du XXe siècle.",
    "Diego Maradona": "Footballeur argentin né en 1960, champion du monde en 1986, célèbre pour sa main de Dieu et ses dribbles légendaires.",
    "Ronaldinho": "Magicien brésilien du ballon rond, Ronaldinho (né en 1980) a marqué le football par sa joie de jouer et sa technique spectaculaire.",
    "Johan Cruyff": "Architecte du football total, Cruyff (1947-2016) a marqué les esprits par son élégance et sa vision du jeu avec les Pays-Bas.",
    "Zinedine Zidane": "Footballeur français né en 1972, champion du monde en 1998, connu pour sa maîtrise technique et son influence sur le jeu.",
    "Antoine Griezmann": "Leader créatif de l'équipe de France, Griezmann (né en 1991) s'est illustré par son intelligence de jeu et son rôle majeur lors de la Coupe du monde 2018.",
    "Paolo Maldini": "Défenseur italien emblématique du Milan AC, reconnu pour sa longévité et son élégance sur le terrain.",
    "Francesco Totti": "Icône de l'AS Roma, Totti a consacré toute sa carrière à son club de cœur avec un talent exceptionnel.",
    "Roberto Baggio": "Footballeur italien surnommé le 'Divin Codino', connu pour sa technique et son charisme.",
    "Andrés Iniesta": "Milieu de terrain espagnol, héros de la finale de Coupe du monde 2010, maître du jeu du Barça et de la Roja.",
    "Xavi Hernández": "Architecte du tiki-taka, Xavi a marqué l'histoire du Barça et de l'Espagne avec son intelligence de jeu.",
    "Didier Drogba": "Attaquant ivoirien, légende de Chelsea, connu pour ses buts décisifs et son rôle d'ambassadeur africain.",
    "Samuel Eto'o": "Avant-centre camerounais, triple vainqueur de la Ligue des champions, redoutable buteur.",
    "Thierry Henry": "Meilleur buteur de l'histoire des Bleus, Henry a brillé à Arsenal avec sa vitesse et sa finition.",
    "George Weah": "Seul Ballon d'or africain (1995), l'attaquant libérien est devenu président de son pays après sa carrière.",
    "David Beckham": "Icône mondiale du football anglais, star du Real Madrid, de Manchester United et symbole du glamour sportif.",
    "Serena Williams": "Joueuse américaine née en 1981, 23 fois titrée en Grand Chelem, elle a dominé le tennis féminin pendant deux décennies.",
    "Rafael Nadal": "Guerrier de la terre battue, Rafael Nadal (né en 1986) est célèbre pour ses 14 titres à Roland-Garros et sa combativité hors norme.",
    "Roger Federer": "Icône du tennis par son élégance, Federer (né en 1981) a enchanté les courts avec 20 titres majeurs et un style inimitable.",
    "Novak Djokovic": "Tennisman serbe né en 1987, recordman de titres en Grand Chelem, il a imposé son règne sur toutes les surfaces.",
    "Carlos Alcaraz": "Phénomène espagnol du tennis moderne, Alcaraz (né en 2003) impressionne par sa puissance précoce et ses titres déjà majeurs.",
    "Jannik Sinner": "Né en 2001, Sinner incarne la nouvelle vague italienne avec un jeu explosif et une ascension fulgurante sur le circuit.",
    "Iga Swiatek": "Joueuse polonaise née en 2001, multiple gagnante de Roland-Garros, elle s'impose déjà comme référence du tennis féminin.",
    "Aryna Sabalenka": "Puissance et intensité définissent Sabalenka (née en 1998), Biélorusse victorieuse en Grand Chelem et pilier du top mondial.",
    "André Agassi": "Tennisman américain charismatique, vainqueur des 4 tournois du Grand Chelem.",
    "Pete Sampras": "Légende du tennis américain des années 90, 14 titres majeurs et un service redoutable.",
    "Martina Navratilova": "Joueuse tchèque naturalisée américaine, 18 titres en Grand Chelem en simple et immense carrière.",
    "Chris Evert": "Tenniswoman américaine, 18 titres en Grand Chelem et une rivalité historique avec Navratilova.",
    "Björn Borg": "Suédois au style froid et efficace, Borg a remporté 11 tournois du Grand Chelem dans les années 70.",
    "Steffi Graf": "Joueuse allemande, seule à avoir réalisé le Golden Slam (1988).",
    "Monica Seles": "Tenniswoman d'origine yougoslave, multiple championne, carrière stoppée par une agression.",
    "Naomi Osaka": "Japonnaise née en 1997, quadruple vainqueure en Grand Chelem et figure engagée.",
    "Emma Raducanu": "Jeune britannique, surprise du tennis avec sa victoire à l'US Open 2021.",
    "John McEnroe": "Tennisman américain né en 1959, célèbre pour son talent exceptionnel et son tempérament explosif sur le court.",
    "Jimmy Connors": "Légende américaine du tennis née en 1952, recordman de titres sur le circuit ATP et icône des années 70-80.",
    "Andy Murray": "Tennisman britannique né en 1987, triple vainqueur en Grand Chelem et double champion olympique, symbole de persévérance.",
    "Stan Wawrinka": "Tennisman suisse né en 1985, triple champion du Grand Chelem, réputé pour son revers à une main spectaculaire.",
    "LeBron James": "Joueur américain né en 1984, quadruple champion NBA, considéré comme l'un des plus complets de l'histoire du basketball.",
    "Michael Jordan": "Icône mondiale née en 1963, Jordan a dominé les années 90 avec six titres NBA et un charisme hors pair.",
    "Stephen Curry": "Révolutionnaire du tir à trois points, Curry (né en 1988) a transformé le basketball, remportant au passage 4 titres NBA.",
    "Tony Parker": "Meneur français né en 1982, quadruple champion NBA avec San Antonio, figure majeure du basketball européen.",
    "Shaquille O'Neal": "Colosse du basketball de 2m16 pour 147 kg, né en 1972, Shaq a remporté quatre titres NBA grâce à sa puissance et sa personnalité unique.",
    "Magic Johnson": "Légende américaine de basketball née en 1959, Magic a incarné le jeu collectif avec cinq titres NBA et un charisme inégalé.",
    "Kobe Bryant": "Légende des Lakers, Bryant (1978-2020) fut quintuple champion NBA et une icône mondiale.",
    "Kevin Durant": "Ailier américain né en 1988, double champion NBA et MVP, l'un des meilleurs scoreurs de l'histoire.",
    "Giannis Antetokounmpo": "'Greek Freak', double MVP NBA, connu pour sa puissance et sa polyvalence.",
    "Dirk Nowitzki": "Ailier fort allemand, icône des Mavericks, champion NBA 2011 et pionnier du basketball européen.",
    "Yao Ming": "Pivot chinois de 2m29, star des Rockets et ambassadeur mondial du basketball.",
    "Hakeem Olajuwon": "Basketteur nigérian-américain né en 1963, double champion NBA et maître incontesté du jeu au poste de pivot.",
    "Larry Bird": "Basketteur américain né en 1956, triple champion NBA et rival légendaire de Magic Johnson.",
    "Michael Phelps": "Nageur américain né en 1985, détenteur de 23 médailles d'or olympiques, recordman incontesté de la natation.",
    "Léon Marchand": "Jeune prodige français de la natation né en 2002, Marchand est déjà à 23 ans quadruple champions olympique et septuple champions du monde.",
    "Usain Bolt": "L'éclair jamaïcain né en 1986, détenteur des records du monde du 100 m et 200 m, il a dominé le sprint mondial pendant une décennie.",
    "Eliud Kipchoge": "Marathonien kényan né en 1984, premier homme à courir un marathon en moins de deux heures, symbole d'endurance et de persévérance.",
    "Florence Griffith-Joyner": "Sprinteuse américaine (1959-1998), détentrice des records du 100 m et 200 m, célèbre pour son style et ses performances légendaires.",
    "Jesse Owens": "Athlète américain (1913-1980), quadruple médaillé d'or aux JO de 1936, symbole de lutte contre le racisme.",
    "Tom Brady": "Quarterback américain né en 1977, sept fois champion du Super Bowl, considéré comme le plus grand joueur NFL.",
    "Lewis Hamilton": "Champion du monde de Formule 1 né en 1985, Hamilton a révolutionné la discipline avec ses sept titres et son engagement social.",
    "Alain Prost": "Pilote français né en 1955, quadruple champion du monde de F1, surnommé le « Professeur » pour sa stratégie de course.",
    "Michael Schumacher": "Pilote allemand, septuple champion du monde de F1, icône de Ferrari.",
    "Sebastian Vettel": "Quadruple champion du monde allemand de F1, star des années 2010.",
    "Ayrton Senna": "Pilote brésilien (1960-1994), triple champion du monde et légende tragique de la F1.",
    "Max Verstappen": "Jeune pilote néerlandais, double champion du monde et star montante de la F1.",
    "Fernando Alonso": "Espagnol, double champion du monde de F1, connu pour sa longévité et sa combativité.",
    "Wayne Gretzky": "Légende canadienne du hockey sur glace, Gretzky (né en 1961) détient la plupart des records de points en NHL.",
    "Teddy Riner": "Judoka français né en 1989, onze fois champion du monde et triple champion olympique, dominant incontesté de sa catégorie.",
    "Clarisse Agbégnénou": "Judokate française née en 1992, multiple championne du monde et d'Europe, figure majeure du judo féminin.",
    "Conor McGregor": "Combattant irlandais de MMA né en 1988, célèbre pour son charisme et ses titres en UFC dans deux catégories.",
    "Georges St-Pierre": "Légende canadienne du MMA, St-Pierre a dominé la catégorie poids welters avec un style technique et respecté.",
    "Mike Tyson": "Boxeur américain né en 1966, plus jeune champion du monde des poids lourds, connu pour sa puissance et sa carrière controversée.",
    "Mohammed Ali": "Icône de la boxe (1942-2016), célèbre pour ses exploits sportifs et son engagement social hors du ring.",
    "Tyson Fury": "Boxeur britannique né en 1988, champion du monde des poids lourds reconnu pour son style fluide et sa résilience.",
    "Canelo Álvarez": "Boxeur mexicain né en 1990, champion du monde dans plusieurs catégories.",
    "Georges Foreman": "Boxeur américain né en 1949, double champion du monde poids lourds.",
    "Khabib Nurmagomedov": "Russe invaincu en MMA, champion UFC poids légers, respecté pour sa discipline.",
    "Feliks Zemdegs": "Speedcubeur australien né en 1995, il détient le plus grand nombre de record du monde et de victoires mondiales, considéré comme le plus influent de son sport.",
    "Max Park": "Américain né en 2001, Max Park est un multiple champion du monde de Rubik's Cube, il détient les records du monde du 6x6 et du 7x7.",
    "Tymon Kolasiński": "Polonais né en 1999, Tymon est considéré comme le speedcubeur le plus intelligent au monde, détenant les records du monde en 5x5 et de moyenne en 4x4.",
    "Yiheng Wang": "Jeune speedcuber chinois, Yiheng Wang est le meilleur speedcubeur du monde en 3x3 et le seul à être passé sous la barre des 4s de moyenne.",
    "Faker": "Joueur sud-coréen né en 1996, Faker est une légende du jeu vidéo League of Legends, connu pour sa maîtrise exceptionnelle.",
    "Bugha": "Champion américain de Fortnite né en 2002, Bugha a gagné la Coupe du Monde d'eSport en 2019, symbolisant l'essor des compétitions virtuelles.",
    "Simone Biles": "Gymnaste américaine née en 1997, multiple médaillée olympique, considérée comme l'une des plus grandes athlètes de la gymnastique.",
    "Nadia Comaneci": "Gymnaste roumaine née en 1961, première à obtenir un 10 parfait aux Jeux Olympiques, icône historique de la discipline.",
    "Kelly Slater": "Surfeur américain né en 1972, 11 fois champion du monde, il est une légende incontournable du surf mondial.",
    "Stephanie Gilmore": "Surfeuse australienne née en 1988, sept fois championne du monde, reconnue pour son style fluide et sa régularité.",
    "Charlotte Dujardin": "Cavalière britannique née en 1985, triple championne olympique de dressage, célèbre pour sa précision et son élégance.",
    "Karch Kiraly": "Volleyball américain né en 1960, triple champion olympique, considéré comme l'un des meilleurs joueurs de l'histoire.",
    "Nikola Karabatic": "Handballeur français né en 1984, multiple champion du monde et d'Europe, pilier incontournable de l'équipe de France.",
    "Pauline Ferrand-Prévot": "Cycliste française née en 1992, championne olympique, championne du monde sur route, VTT et cyclocross, vainqueure du Tour de France: polyvalente et talentueuse.",
    "Tadej Pogačar": "Cycliste slovène né en 1998, double vainqueur du Tour de France, prodige du cyclisme moderne.",
    "Sébastien Chabal": "Surnommé 'l'Anesthésiste', joueur français au style rugueux et charismatique.",
    "Antoine Dupont": "Demi de mêlée français, considéré comme le meilleur joueur de rugby actuel.",
    "Mikaela Shiffrin": "Skieuse américaine née en 1995, recordwoman de victoires en Coupe du monde.",
    "Martin Fourcade": "Biathlète français né en 1988, quintuple champion olympique et septuple vainqueur du globe de cristal, il a marqué son sport par sa régularité.",
    "Justin Gatlin": "Sprinteur américain né en 1982, multiple médaillé olympique et champion du monde sur 100 m et 200 m.",
    "Asafa Powell": "Sprinteur jamaïcain né en 1982, ancien recordman du monde du 100 m et figure du sprint mondial.",
    "Tyson Gay": "Sprinteur américain né en 1982, détenteur de plusieurs titres mondiaux sur 100 m et 200 m.",
    "Yohan Blake": "Sprinteur jamaïcain né en 1989, double médaillé olympique et grand rival d'Usain Bolt.",
    "Christophe Lemaitre": "Sprinteur français né en 1990, premier européen à descendre sous les 10 secondes sur 100 m.",
    "Armand Duplantis": "Perchiste suédois né en 1999, détenteur du record du monde de saut à la perche et champion olympique.",
    "Renaud Lavillenie": "Perchiste français né en 1986, ancien recordman du monde et champion olympique.",
    "Caeleb Dressel": "Nageur américain né en 1996, multiple champion olympique et recordman du monde en sprint nage libre.",
    "Katie Ledecky": "Nageuse américaine née en 1997, spécialiste des longues distances, détentrice de multiples records du monde.",
    "Lindsey Vonn": "Skieuse alpine américaine (1984-), détentrice de 82 victoires en Coupe du monde et championne olympique.",
    "Patrick Mahomes": "Quarterback américain né en 1995, MVP et champion du Super Bowl, symbole de la nouvelle génération NFL."
}


dict_chanteurs = {
    "Michael Jackson": "Icône de la pop mondiale surnommé le \"Roi de la Pop\", il a révolutionné la musique avec des albums comme Thriller et des chorégraphies légendaires.",
    "Freddie Mercury": "Chanteur charismatique du groupe Queen, célèbre pour sa voix puissante et ses performances scéniques flamboyantes.",
    "Beyoncé": "Chanteuse américaine née en 1981, superstar internationale et militante engagée, ancienne membre du groupe Destiny's Child.",
    "Rihanna": "Chanteuse barbadienne aux multiples hits, elle est aussi une femme d'affaires influente dans la mode et les cosmétiques.",
    "Taylor Swift": "Autrice-compositrice américaine, elle a conquis la pop mondiale avec ses récits personnels et ses tournées gigantesques.",
    "Billie Eilish": "Révélée très jeune, elle impose un style unique et sombre, combinant pop alternative et introspection.",
    "Adele": "Voix puissante et mélancolique de la soul britannique, elle touche par ses ballades sur l'amour et la rupture.",
    "Elvis Presley": "Légende du rock'n'roll, surnommé le \"King\", il a marqué les années 50 et 60 avec son style et sa voix.",
    "Whitney Houston": "Voix d'or de la musique soul et pop américaine, connue pour I Will Always Love You et son incroyable tessiture.",
    "Frank Sinatra": "Chanteur américain emblématique du 20e siècle, maître du swing et crooner légendaire.",
    "Eminem": "Rappeur américain au flow percutant, connu pour ses textes autobiographiques et son vocabulaire riche.",
    "Drake": "Rappeur et chanteur canadien, figure majeure du rap moderne avec une touche mélodique distinctive.",
    "Kendrick Lamar": "Poète du rap américain, il mêle virtuosité technique et dénonciation sociale, lauréat d'un prix Pulitzer.",
    "The Weeknd": "Chanteur canadien mêlant R&B, pop et synthwave, connu pour sa voix haut perchée et ses univers sombres.",
    "Justin Bieber": "Star mondiale révélée sur YouTube, il évolue de la teen pop à une carrière plus mature.",
    "Bruno Mars": "Showman accompli, il fusionne funk, soul, pop et R&B avec une énergie débordante.",
    "Ed Sheeran": "Chanteur britannique à la guitare acoustique, il séduit par sa simplicité et ses mélodies efficaces.",
    "Harry Styles": "Ancien membre de One Direction, il affirme une carrière solo pop-rock saluée pour son originalité.",
    "Dua Lipa": "Chanteuse anglo-albanaise à la pop électro, elle s'impose comme une figure majeure de la scène actuelle.",
    "Lady Gaga": "Icône de la pop excentrique, elle combine performance, revendication et grand talent vocal.",
    "Madonna": "Reine de la pop depuis les années 80, elle a toujours su se réinventer et bousculer les codes.",
    "Céline Dion": "Chanteuse canadienne à la voix puissante, célèbre pour ses ballades émotionnelles et My Heart Will Go On.",
    "Mariah Carey": "Célèbre pour sa tessiture vocale exceptionnelle et ses tubes R&B-pop, elle règne depuis les années 90.",
    "Shakira": "Chanteuse colombienne mêlant pop, musique latine et danse orientale, artiste internationale aux multiples talents.",
    "ABBA": "Groupe suédois phare des années 70, leurs tubes comme Dancing Queen traversent les générations.",
    "Daniel Balavoine": "Chanteur français engagé, il a marqué la variété des années 80 par sa voix et ses textes poignants.",
    "Dalida": "Star internationale née en Égypte, elle a chanté en plusieurs langues et ému des générations entières.",
    "Avicii": "DJ et producteur suédois, il a modernisé l'EDM avec des tubes comme Wake Me Up avant sa disparition tragique.",
    "The Beatles": "Groupe britannique emblématique, pionnier de la pop-rock, dont l'impact culturel reste inégalé.",
    "Stromae": "Artiste belge mêlant électro, rap et chanson française, connu pour ses textes profonds et originaux.",
    "Angèle": "Chanteuse belge francophone, elle séduit par sa fraîcheur pop et son regard critique sur la société.",
    "Orelsan": "Rappeur français aux textes souvent ironiques ou mélancoliques, il dresse un portrait lucide de sa génération.",
    "Damso": "Rappeur belge à l'univers sombre et poétique, il s'impose comme une plume marquante du rap francophone.",
    "Aya Nakamura": "Chanteuse pop urbaine française, elle explose les charts avec un style vocal reconnaissable et rythmé.",
    "Gims": "Rappeur et chanteur français, ex-membre de Sexion d'Assaut, connu pour sa voix puissante et ses refrains accrocheurs.",
    "Ninho": "Jeune prodige du rap français, il enchaîne les succès avec un style percutant et polyvalent.",
    "Booba": "Figure incontournable du rap français, connu pour son flow, ses clashs et son impact culturel durable.",
    "Big Time Rush": "Groupe pop américain révélé par une série TV, ils ont marqué les années 2010 auprès des adolescents.",
    "Johnny Hallyday": "Monument du rock français, il a traversé les décennies avec passion et un public fidèle.",
    "Nirvana": "Groupe culte du grunge mené par Kurt Cobain, il a marqué les années 90 avec un son brut et désabusé.",
    "Coldplay": "Groupe britannique mêlant rock alternatif et pop mélodique, connu pour ses concerts immersifs.",
    "Imagine Dragons": "Groupe pop-rock américain aux sonorités électro, célèbre pour ses refrains épiques et énergiques.",
    "Eddy Mitchell": "Chanteur français de rock et de variété, figure de la scène depuis les années 60.",
    "Metallica": "Groupe phare du metal américain, ils ont imposé leur puissance sonore depuis les années 80.",
    "AC/DC": "Groupe australien de hard rock, connu pour ses riffs électriques et son énergie scénique légendaire.",
    "Red Hot Chili Peppers": "Groupe californien fusionnant rock, funk et punk, mené par des performances endiablées.",
    "BTS": "Groupe sud-coréen phare de la K-pop, ils séduisent une fanbase mondiale avec leurs messages positifs et leur discipline.",
    "Edith Piaf": "Icône de la chanson française, elle a chanté l'amour et la douleur avec une intensité inégalée.",
    "Bigflo & Oli": "Duo de rappeurs toulousains, ils se distinguent par leur écriture sincère et leur complicité fraternelle.",
    "Daft Punk": "Duo électro français au style iconique et mystérieux, ils ont marqué la musique électronique mondiale.",
    "David Guetta": "DJ français mondialement reconnu, pionnier de la house grand public et des collaborations pop.",
    "The Rolling Stones": "Groupe britannique mythique de rock, actif depuis les années 60 avec une longévité exceptionnelle.",
    "Prince": "Icône de la funk et de la pop, connu pour Purple Rain et son style excentrique.",
    "George Michael": "Chanteur britannique, star des années 80 avec Wham! et en solo.",
    "David Bowie": "Légende du rock britannique, maître de la réinvention artistique.",
    "Elton John": "Chanteur et pianiste britannique, auteur de classiques comme Rocket Man.",
    "Phil Collins": "Chanteur et batteur britannique, star solo et membre de Genesis.",
    "Lionel Richie": "Chanteur américain de soul et pop, connu pour ses ballades intemporelles.",
    "Stevie Wonder": "Prodige de la soul et du R&B, voix mythique de la Motown.",
    "Aretha Franklin": "Reine de la soul, interprète de Respect et Think.",
    "Tina Turner": "Chanteuse légendaire au style puissant, icône du rock et de la soul.",
    "Cher(chanteuse)": "Icône pop américaine, connue pour sa longévité et Believe.",
    "Louis Armstrong": "Figure du jazz mondial, trompettiste et chanteur emblématique.",
    "Ray Charles": "Pionnier de la soul, mêlant gospel, blues et jazz.",
    "Bob Dylan": "Poète du folk américain, Prix Nobel de littérature.",
    "Bruce Springsteen": "Icône du rock américain, surnommé The Boss.",
    "Jimi Hendrix": "Légende de la guitare, aussi chanteur charismatique.",
    "Kurt Cobain": "Leader de Nirvana, voix du grunge des années 90.",
    "Shawn Mendes": "Jeune star canadienne de la pop.",
    "Camila Cabello": "Chanteuse pop cubano-américaine, ex-membre de Fifth Harmony.",
    "Selena Gomez": "Chanteuse pop américaine et actrice.",
    "Miley Cyrus": "Icône pop américaine, connue pour sa polyvalence.",
    "Nicki Minaj": "Rappeuse et chanteuse américaine, icône rap et pop.",
    "Cardi B": "Rappeuse américaine, star mondiale avec Bodak Yellow.",
    "Post Malone": "Rappeur et chanteur américain, mêlant hip-hop et pop.",
    "Travis Scott": "Rappeur américain, connu pour ses shows spectaculaires.",
    "Lil Nas X": "Rappeur américain révélé par Old Town Road.",
    "Charlie Puth": "Chanteur pop américain, connu pour ses ballades romantiques.",
    "Christina Aguilera": "Icône pop américaine, voix puissante révélée dans les années 2000.",
    "Katy Perry": "Chanteuse pop américaine, connue pour Firework et Roar.",
    "Jennifer Lopez": "Icône latino-pop, chanteuse, danseuse et actrice.",
    "Enrique Iglesias": "Chanteur espagnol, star mondiale de la pop latine.",
    "Luis Fonsi": "Chanteur portoricain connu pour Despacito.",
    "J Balvin": "Star mondiale du reggaeton colombien.",
    "Bad Bunny": "Rappeur et chanteur portoricain, icône mondiale.",
    "Marc Anthony": "Icône de la salsa et de la pop latine.",
    "Rosalía": "Chanteuse espagnole, mélange flamenco et pop moderne.",
    "Luciano Pavarotti": "Ténor italien légendaire, star des Trois Ténors.",
    "Michel Sardou": "Chanteur français, icône de la variété.",
    "Francis Cabrel": "Auteur-compositeur français aux ballades poétiques.",
    "Jean-Jacques Goldman": "Chanteur et auteur-compositeur français adoré.",
    "Charles Aznavour": "Icône de la chanson française, poète de l'amour.",
    "Jacques Brel": "Légende belge de la chanson, poète des émotions.",
    "Georges Brassens": "Auteur-compositeur français, maître des mots.",
    "Patrick Bruel": "Chanteur français populaire et acteur.",
    "Florent Pagny": "Chanteur français à la voix puissante.",
    "Mylène Farmer": "Icône de la pop française, univers mystérieux.",
    "Indochine": "Groupe français culte de la new wave.",
    "SCH": "Rappeur marseillais, plume sombre et originale.",
    "Jul": "Rappeur marseillais ultra-prolifique, star des charts.",
    "Nekfeu": "Rappeur parisien, reconnu pour sa plume et son flow.",
    "Vald": "Rappeur français décalé, style absurde et percutant.",
    "Lomepal": "Rappeur-chanteur français à l'univers introspectif.",
    "Soolking": "Chanteur algérien mêlant rap, pop et influences orientales.",
    "Sia": "Chanteuse australienne connue pour Chandelier."
}

dict_evenements_historiques = {
    "Révolution française": "En 1789, la monarchie tombe et naissent les principes de liberté, d'égalité et de souveraineté populaire.",
    "Chute de l'Empire romain": "En 476, l'Empire romain d'Occident s'effondre, marquant le début du Moyen Âge en Europe.",
    "Découverte de l'Amérique": "En 1492, Christophe Colomb atteint le Nouveau Monde, bouleversant l'histoire des continents.",
    "Guerre de Cent Ans": "De 1337 à 1453, l'Angleterre et la France s'affrontent, redéfinissant le pouvoir royal et les nations.",
    "Réforme protestante": "En 1517, Luther conteste l'Église catholique, divisant le christianisme en Europe.",
    "Révolution industrielle": "Dès la fin du XVIIIe siècle, l'essor des machines transforme radicalement sociétés et économies.",
    "Première Guerre mondiale": "De 1914 à 1918, un conflit mondial cause des millions de morts et redessine les frontières.",
    "Seconde Guerre mondiale": "Entre 1939 et 1945, le monde s'embrase à nouveau, jusqu'à la chute du nazisme.",
    "Guerre froide": "Après 1945, les États-Unis et l'URSS s'opposent dans une rivalité idéologique, technologique et nucléaire.",
    "Chute du mur de Berlin": "En 1989, le mur s'effondre, symbolisant la fin de la division Est-Ouest et de la guerre froide.",
    "Attentats du 11 septembre 2001": "Des attaques terroristes frappent les États-Unis, changeant durablement l'ordre mondial.",
    "Printemps arabe": "En 2011, une vague de révoltes populaires secoue le monde arabe, réclamant démocratie et libertés.",
    "Guerre du Vietnam": "Entre 1955 et 1975, les États-Unis échouent à stopper la progression du communisme en Asie.",
    "Abolition de l'esclavage": "Aux XIXe et XXe siècles, les luttes aboutissent à l'interdiction de l'esclavage dans de nombreux pays.",
    "Invention de l'imprimerie": "Vers 1450, Gutenberg révolutionne la diffusion du savoir grâce à la presse typographique.",
    "Conquête spatiale": "En 1969, Apollo 11 permet à l'Homme de marcher sur la Lune, exploit majeur de la guerre froide.",
    "Crise des missiles de Cuba": "En 1962, le monde frôle la guerre nucléaire lors d'un affrontement tendu entre l'URSS et les États-Unis.",
    "Indépendance des États-Unis": "En 1776, les colonies d'Amérique rompent avec l'Angleterre et fondent une nouvelle nation.",
    "Révolution russe": "En 1917, les bolcheviks prennent le pouvoir et instaurent le premier État communiste.",
    "Génocide du Rwanda": "En 1994, environ 800 000 Tutsis sont massacrés en quelques mois dans un contexte de haine ethnique.",
    "Shoah / Holocauste": "Entre 1941 et 1945, six millions de Juifs sont exterminés par le régime nazi.",
    "Guerre d'Algérie": "De 1954 à 1962, la lutte pour l'indépendance oppose violemment la France et le FLN.",
    "Révolution iranienne": "En 1979, le régime du Shah est renversé et une République islamique est instaurée.",
    "Traité de Versailles": "En 1919, la paix est signée avec l'Allemagne, mais les conditions poseront les germes du second conflit mondial.",
    "Pandémie de COVID-19": "En 2020, un virus se propage à l'échelle mondiale, bouleversant les sociétés humaines.",
    "Prise de la Bastille": "Le 14 juillet 1789, un symbole de l'absolutisme est pris d'assaut par le peuple de Paris.",
    "Guerre de Corée": "De 1950 à 1953, Nord et Sud s'affrontent dans un conflit idéologique soutenu par les grandes puissances.",
    "Guerre d'Indépendance de l'Inde": "Après des décennies de lutte non violente, l'Inde devient indépendante en 1947.",
    "Élection de Nelson Mandela": "En 1994, il devient le premier président noir d'Afrique du Sud, tournant historique contre l'apartheid.",
    "Bombes atomiques sur Hiroshima et Nagasaki": "En août 1945, les États-Unis utilisent l'arme nucléaire pour mettre fin à la guerre.",
    "Crise économique de 1929": "Un krach boursier plonge le monde dans une dépression sans précédent.",
    "Attentat contre JFK": "En 1963, le président américain John F. Kennedy est assassiné à Dallas.",
    "Guerre en Ukraine": "En 2022, la Russie envahit l'Ukraine, relançant une guerre sur le sol européen.",
    "Affaire Dreyfus": "À la fin du XIXe siècle, un officier juif est accusé à tort, révélant l'antisémitisme en France.",
    "Éruption du Vésuve et destruction de Pompéi": "En l'an 79, un volcan raye une cité romaine de la carte en quelques heures.",
    "Chute de Constantinople": "En 1453, l'Empire byzantin tombe aux mains des Ottomans, marquant la fin du Moyen Âge.",
    "Déclaration des droits de l'homme": "En 1789, la France proclame des principes universels de liberté et d'égalité.",
    "Décolonisation de l'Afrique": "Après 1945, les colonies africaines accèdent peu à peu à l'indépendance.",
    "Signature de la Magna Carta": "En 1215, le roi d'Angleterre accepte de limiter son pouvoir au profit des barons.",
    "Guerre d'Espagne": "De 1936 à 1939, républicains et nationalistes s'affrontent dans une guerre civile sanglante.",
    "Invention d'Internet": "Dans les années 1980, un réseau mondial voit le jour, révolutionnant les communications.",
    "L'Apartheid": "De 1948 à 1991, un régime ségrégationniste oppresse la majorité noire en Afrique du Sud.",
    "Commune de Paris": "En 1871, les ouvriers prennent le pouvoir à Paris pendant quelques semaines.",
    "Révolution culturelle en Chine": "À partir de 1966, Mao lance une campagne pour purger les idées capitalistes.",
    "Première croisade": "En 1096, les chrétiens d'Occident marchent vers Jérusalem pour reprendre la ville aux musulmans.",
    "Assassinat de Georges Floyd": "En 2020, la mort d'un Afro-Américain provoque une vague mondiale de protestations.",
    "Guerre civile américaine": "De 1861 à 1865, Nord et Sud s'opposent sur la question de l'esclavage.",
    "Couronnement de Charlemagne": "En l'an 800, le roi des Francs est sacré empereur d'Occident à Rome.",
    "Révolte des esclaves de Spartacus": "Au Ier siècle av. J.-C., un gladiateur mène une insurrection contre Rome.",
    "Catastrophe de Tchernobyl": "En 1986, un réacteur nucléaire explose en URSS, causant un désastre écologique majeur.",
    "Déclaration d'indépendance du Brésil": "En 1822, le Brésil se libère du Portugal et devient un empire indépendant.",
    "Traité de Westphalie": "En 1648, ce traité met fin à la guerre de Trente Ans et fonde les bases des États modernes.",
    "Fondation de l'ONU": "En 1945, l'Organisation des Nations unies est créée pour maintenir la paix mondiale.",
    "Guerres napoléoniennes": "De 1803 à 1815, Napoléon étend puis perd son empire à travers l'Europe.",
    "Assassinat de Jules César": "En -44, César est tué à Rome, bouleversant la République romaine.",
    "Indépendance de l'Indonésie": "En 1945, Soekarno proclame l'indépendance après la domination néerlandaise.",
    "Chute de l'Empire aztèque": "En 1521, Hernán Cortés conquiert Tenochtitlán, mettant fin à la civilisation aztèque.",
    "Signature du Bill of Rights": "En 1791, les dix premiers amendements à la Constitution américaine sont adoptés.",
    "Traité de Tordesillas": "En 1494, l'Espagne et le Portugal se partagent le Nouveau Monde.",
    "Révolte des Taiping": "De 1850 à 1864, une guerre civile sanglante secoue la Chine impériale.",
    "Proclamation de la République française": "En 1870, la Troisième République est proclamée après la chute du Second Empire.",
    "Chute de Saïgon": "En 1975, la prise de Saïgon marque la fin de la guerre du Vietnam.",
    "Indépendance de l'Irlande": "En 1922, l'Irlande devient un État libre après un conflit avec le Royaume-Uni.",
    "Assassinat de Martin Luther King": "En 1968, le leader des droits civiques est tué à Memphis.",
    "Révolte de Varsovie": "En 1944, les résistants polonais tentent de libérer Varsovie de l'occupation nazie.",
    "Guerre d'indépendance algérienne": "De 1954 à 1962, le FLN lutte contre la colonisation française.",
    "Indépendance du Pakistan": "En 1947, le Pakistan naît de la partition de l'Inde.",
    "Traité de Maastricht": "En 1992, il fonde l'Union européenne et introduit l'euro.",
    "Assassinat de Gandhi": "En 1948, le leader de l'indépendance indienne est tué à New Delhi.",
    "l'Inquisition": "De 1478 à 1834, l'Espagne met en place un tribunal religieux contre les hérétiques.",
    "Guerre des Malouines": "En 1982, le Royaume-Uni et l'Argentine s'affrontent pour ces îles de l'Atlantique Sud.",
    "Révolte de 1830 en France": "Les 'Trois Glorieuses' renversent Charles X et instaurent la monarchie de Juillet.",
    "Traité de Rome": "En 1957, il fonde la Communauté économique européenne (CEE).",
    "Indépendance du Maroc": "En 1956, le Maroc devient indépendant de la France et de l'Espagne.",
    "Révolution américaine": "De 1775 à 1783, les colonies américaines obtiennent leur indépendance.",
    "Traité de Paris 1763": "Il met fin à la guerre de Sept Ans et redéfinit les empires coloniaux.",
    "Accord de Paris sur le climat": "En 2015, les nations s'engagent à limiter le réchauffement climatique sous 2°C.",
    "Crise financière de 2008": "Une faillite bancaire mondiale déclenche une récession économique majeure.",
    "Attentats de Paris du 13 novembre 2015": "Des attaques terroristes font 130 morts et choquent la France.",
    "Mort de Ben Laden": "En 2011, le leader d'Al-Qaïda est tué lors d'une opération américaine au Pakistan.",
    "Gilets jaunes": "Depuis 2018, un mouvement de protestation français dénonce les inégalités sociales.",
    "Éruption du volcan Eyjafjallajökull": "En 2010, l'Islande provoque un énorme nuage de cendres affectant le trafic aérien européen.",
    "Tsunami au Japon": "En 2011, un séisme de magnitude 9 provoque un tsunami et un accident nucléaire à Fukushima.",
    "Indépendance du Soudan du Sud": "En 2011, il devient le plus jeune État du monde après un référendum.",
    "Attentat de Charlie Hebdo": "En janvier 2015, l'attaque contre le journal satirique fait 12 morts à Paris.",
    "Crise de la zone euro": "À partir de 2009, la dette grecque et la récession européenne menacent la monnaie unique.",
    "Fukushima": "Suite au séisme de 2011, la centrale nucléaire japonaise subit une fusion partielle des réacteurs.",
    "Réforme du mariage pour tous en France": "En 2013, le mariage homosexuel est légal en France après un long débat.",
    "Guerre en Afghanistan": "Depuis 2001, un conflit oppose les forces internationales et les talibans.",
    "Sommet historique Trump-Kim": "En 2018, premier sommet entre un président américain et un leader nord-coréen.",
    "Mouvement #MeToo": "Depuis 2017, ce mouvement mondial dénonce le harcèlement et les violences sexuelles.",
    "Crise en Venezuela": "Depuis 2013, le pays traverse une grave crise économique, politique et humanitaire.",
    "Attentat de Nice": "En 2016, un camion fonce sur la foule du 14 juillet, causant 86 morts.",
    "Réforme du bac en France": "En 2018, la réforme transforme le baccalauréat et le lycée français.",
    "Explosion à Beyrouth": "En 2020, une gigantesque explosion dans le port détruit une partie de la ville et fait des centaines de morts.",
    "Pandémie de grippe H1N1": "En 2009, un virus provoque une pandémie mondiale de grippe.",
    "Crise des subprimes": "En 2007-2008, les prêts immobiliers américains déclenchent la crise financière mondiale.",
    "Réforme des retraites en France 2023": "Provoque un mouvement social massif et des grèves nationales.",
    "Élection de Macron à la présidence": "En 2017, il marque une rupture politique en France avec son mouvement La République En Marche.",
    "Attentats de Bruxelles": "En 2016, des explosions dans l'aéroport et le métro font 32 morts et de nombreux blessés.",
    "Guerre Russie-Ukraine 2022": "Conflit majeur en Europe relançant la tension géopolitique mondiale.",
    "Crise au Liban 2019": "Manifestations massives contre la corruption et la situation économique.",
    "Mort de Michael Jackson": "En 2009, le roi de la pop meurt, provoquant une vague mondiale d'émotion.",
    "Accords d'Oslo": "Depuis 1993, tentatives de paix entre Israéliens et Palestiniens.",
    "Catastrophe de l'ouragan Katrina": "En 2005, la Nouvelle-Orléans est dévastée, provoquant des milliers de morts.",
    "Mort de Jacques Chirac": "En 2019, l'ancien président français disparaît, laissant un héritage politique."
}

dict_metiers = {
    "Médecin": "Le médecin soigne les maladies et veille à la santé des patients grâce à des diagnostics précis et des traitements adaptés.",
    "Enseignant": "Transmettre le savoir, guider les élèves et les aider à grandir, tel est le rôle fondamental de l'enseignant au quotidien.",
    "Ingénieur": "Ingénieur, créateur de solutions techniques, il allie science et innovation pour construire le futur.",
    "Pompier": "Le pompier intervient pour sauver des vies et protéger les biens face aux incendies et autres urgences.",
    "Avocat": "Défendre les droits de ses clients, plaider en justice et conseiller, telle est la mission de l'avocat.",
    "Journaliste": "Le journaliste enquête et informe le public, apportant des récits clairs et précis sur l'actualité.",
    "Policier": "Maintenir l'ordre public, protéger les citoyens et faire respecter la loi font partie des tâches du policier.",
    "Vétérinaire": "Soigner les animaux et veiller à leur bien-être, c'est la vocation du vétérinaire.",
    "Architecte": "L'architecte imagine et conçoit les bâtiments, mêlant créativité et technique pour créer des espaces de vie.",
    "Plombier": "Le plombier installe, répare et entretient les systèmes d'eau et de chauffage dans les bâtiments.",
    "Électricien": "L'électricien assure l'installation et la maintenance des réseaux électriques, garantissant sécurité et confort.",
    "Boulanger": "Artisan du pain, le boulanger pétrit, façonne et cuit des produits savoureux chaque jour.",
    "Musicien": "Le musicien crée et interprète des œuvres sonores pour toucher les émotions du public.",
    "Infirmier": "Aux côtés des médecins, l'infirmier soigne les malades et accompagne les patients avec attention.",
    "Pilote de ligne": "Le pilote de ligne maîtrise l'avion et assure la sécurité des passagers lors de leurs voyages.",
    "Chauffeur routier": "Le chauffeur routier transporte des marchandises sur de longues distances, garantissant leur livraison.",
    "Développeur informatique": "Le développeur conçoit des logiciels et applications pour répondre aux besoins numériques.",
    "Agriculteur": "L'agriculteur cultive la terre et élève les animaux pour nourrir la population.",
    "Psychologue": "Le psychologue écoute et accompagne les personnes pour améliorer leur bien-être mental.",
    "Comédien": "Le comédien incarne des personnages pour raconter des histoires sur scène ou à l'écran.",
    "Mécanicien": "Le mécanicien répare et entretient les véhicules pour garantir leur bon fonctionnement.",
    "Coiffeur": "Le coiffeur coupe et stylise les cheveux pour sublimer l'apparence de ses clients.",
    "Maçon": "Le maçon construit les fondations et les murs des bâtiments avec soin et précision.",
    "Chef cuisinier": "Le chef imagine des plats savoureux et coordonne la cuisine d'un restaurant.",
    "Caissier": "Le caissier gère les paiements et accueille les clients dans les magasins.",
    "Bibliothécaire": "Le bibliothécaire organise et prête des livres, facilitant l'accès au savoir.",
    "Photographe": "Le photographe capture des images pour raconter des histoires ou immortaliser des instants.",
    "Astronaute": "L'astronaute explore l'espace et réalise des missions scientifiques hors de la Terre.",
    "Banquier": "Le banquier conseille et gère les finances des particuliers ou des entreprises.",
    "Dentiste": "Le dentiste soigne les dents et veille à la santé bucco-dentaire.",
    "Sage-femme": "La sage-femme accompagne les femmes lors de la grossesse et de l'accouchement.",
    "Traducteur": "Le traducteur rend accessibles les textes d'une langue à une autre avec fidélité.",
    "Contrôleur aérien": "Le contrôleur aérien guide les avions pour assurer la sécurité dans le ciel.",
    "Graphiste": "Le graphiste crée des visuels pour communiquer des messages attractifs.",
    "Actuaire": "L'actuaire analyse les risques financiers pour aider les entreprises à prendre des décisions.",
    "Géomètre": "Le géomètre mesure et délimite les terrains pour les projets de construction.",
    "Designer d'intérieur": "Le designer aménage les espaces intérieurs pour les rendre fonctionnels et esthétiques.",
    "Restaurateur d'art": "Le restaurateur d'art soigne et préserve les œuvres anciennes pour les générations futures.",
    "Urbaniste": "L'urbaniste planifie l'organisation des villes et des territoires.",
    "Policier scientifique": "Le policier scientifique analyse les indices sur les scènes de crime pour résoudre des enquêtes.",
    "Monteur vidéo": "Le monteur assemble les images pour créer des films ou des vidéos cohérents.",
    "Couturier": "Le couturier conçoit et réalise des vêtements uniques sur mesure.",
    "Ébéniste": "L'ébéniste travaille le bois pour fabriquer des meubles raffinés.",
    "Guide touristique": "Le guide touristique accompagne et informe les visiteurs sur les sites à découvrir.",
    "Data analyst": "Le data analyst interprète des données pour aider à la prise de décisions stratégiques.",
    "Testeur de jeux vidéo": "Le testeur vérifie les jeux pour assurer leur qualité avant leur sortie.",
    "Logisticien": "Le logisticien organise le transport et la distribution des marchandises.",
    "Professeur d'université": "Le professeur d'université enseigne et fait avancer la recherche scientifique.",
    "Responsable des ressources humaines": "Le responsable RH gère le personnel et veille au bien-être des employés.",
    "Entraîneur sportif": "L'entraîneur prépare et motive les athlètes pour atteindre leurs objectifs.",
    "Océanographe": "Scientifique spécialisé dans l'étude des mers et océans, il analyse leur biodiversité et leurs dynamiques.",
    "Climatologue": "Expert du climat, il observe les phénomènes atmosphériques et leurs évolutions pour comprendre le réchauffement global.",
    "Thanatopracteur": "Il prépare et préserve les corps après la mort, offrant un dernier hommage aux défunts.",
    "Horloger": "Artisan de précision, il conçoit, répare et entretient des montres et des horloges.",
    "Charpentier": "Spécialiste du bois, il fabrique et assemble des structures comme les toitures ou les ossatures de bâtiments.",
    "Tailleur de pierre": "Artisan qui façonne la pierre pour les constructions et la restauration de monuments.",
    "Pilote de chasse": "Militaire, il conduit des avions de combat pour défendre l'espace aérien.",
    "Conservateur de musée": "Responsable des collections d'un musée, il assure leur préservation et leur valorisation.",
    "Criminologue": "Spécialiste de l'étude du crime et des comportements criminels pour aider la justice.",
    "Éthologue": "Scientifique qui observe et analyse le comportement des animaux.",
    "Botaniste": "Chercheur en biologie végétale, il étudie les plantes et leur rôle dans les écosystèmes.",
    "Viticulteur": "Producteur de raisins destinés à la vinification, il entretient les vignes avec soin.",
    "Sommelier": "Expert en vins, il conseille les clients dans les restaurants et organise des dégustations.",
    "Chef d'orchestre": "Il dirige les musiciens pour interpréter une œuvre musicale avec harmonie.",
    "Cascadeur": "Artiste qui réalise des scènes dangereuses à la place des acteurs.",
    "Tatoueur": "Artisan et artiste, il réalise des dessins permanents sur la peau de ses clients.",
    "Marin pêcheur": "Il part en mer pour capturer des poissons et approvisionner les marchés.",
    "Kinésithérapeute": "Professionnel de santé qui rééduque les patients par des exercices physiques.",
    "Opticien": "Il corrige les troubles de la vue grâce à des lunettes ou lentilles adaptées.",
    "Diététicien": "Il conseille sur l'alimentation et propose des régimes équilibrés.",
    "Puéricultrice": "Infirmière spécialisée dans les soins et le suivi des enfants en bas âge.",
    "Orthophoniste": "Il rééduque les troubles du langage et de la communication.",
    "Orthoptiste": "Spécialiste de la rééducation visuelle, il aide à corriger certains troubles de la vue.",
    "Prothésiste dentaire": "Artisan qui fabrique les prothèses et implants dentaires.",
    "Chirurgien": "Médecin spécialisé dans les opérations pour soigner ou réparer le corps.",
    "Dermatologue": "Médecin expert de la peau et de ses maladies.",
    "Pharmacien": "Il prépare, délivre et conseille sur les médicaments et traitements.",
    "Garde forestier": "Il protège et entretient les forêts, surveillant la faune et la flore.",
    "Jardinier paysagiste": "Il conçoit et entretient les espaces verts et jardins.",
    "Apiculteur": "Éleveur d'abeilles, il récolte le miel et contribue à la pollinisation.",
    "Fromager": "Artisan qui fabrique différents types de fromages à partir du lait.",
    "Boucher": "Il découpe et prépare la viande pour la vente.",
    "Poissonnier": "Il vend et prépare poissons et fruits de mer pour les clients.",
    "Chocolatier": "Artisan qui crée des confiseries et gourmandises à base de cacao.",
    "Pâtissier": "Il confectionne des gâteaux, desserts et viennoiseries.",
    "Glacier": "Artisan spécialisé dans la fabrication de crèmes glacées et sorbets.",
    "Cordonnier": "Artisan qui répare et fabrique des chaussures.",
    "Bijoutier": "Artisan qui crée et vend des bijoux en métal précieux ou fantaisie.",
    "Orfèvre": "Il façonne des objets précieux en or, argent ou platine.",
    "Serrurier": "Il installe et répare serrures, portes et systèmes de sécurité.",
    "Forgeron": "Artisan qui travaille les métaux en les chauffant et en les martelant.",
    "Moniteur d'auto-école": "Il enseigne la conduite et prépare les élèves au permis.",
    "Steward": "Personnel navigant qui assure la sécurité et le confort des passagers en avion.",
    "Hôtesse de l'air": "Elle accueille et accompagne les passagers durant le vol.",
    "Capitaine de navire": "Commandant d'un bateau, il est responsable de l'équipage et de la navigation.",
    "Maître-nageur": "Il surveille les piscines et plages et enseigne la natation.",
    "Moniteur de ski": "Il enseigne la pratique du ski et encadre les sportifs en montagne.",
    "Paléontologue": "Scientifique qui étudie les fossiles pour comprendre l'histoire de la vie.",
    "Archéologue": "Chercheur qui fouille et analyse les vestiges des civilisations anciennes.",
    "Historien": "Il étudie et interprète les faits passés pour mieux comprendre l'humanité.",
    "Sociologue": "Chercheur qui analyse les sociétés, leurs comportements et leurs évolutions.",
    "Philosophe": "Il réfléchit aux grandes questions de l'existence, de la morale et du savoir.",
    "Écrivain": "Auteur d'œuvres littéraires, il transmet des idées et des histoires par l'écriture.",
    "Poète": "Il exprime émotions et réflexions à travers la poésie.",
    "Peintre": "Artiste qui crée des œuvres visuelles avec couleurs et formes.",
    "Sculpteur": "Il façonne la pierre, le bois ou le métal pour créer des œuvres en volume.",
    "Illustrateur": "Artiste qui réalise des dessins pour des livres, affiches ou magazines.",
    "Caricaturiste": "Dessinateur qui exagère les traits pour créer humour ou critique.",
    "Mangaka": "Dessinateur japonais spécialisé dans les bandes dessinées (mangas).",
    "Scénariste": "Auteur qui écrit les scripts pour films, séries ou BD.",
    "Réalisateur": "Il met en scène des films ou des séries, dirigeant acteurs et techniciens.",
    "Producteur de cinéma": "Il finance et organise la production d'œuvres audiovisuelles.",
    "Chorégraphe": "Créateur de mouvements, il imagine et met en scène des danses.",
    "Danseur": "Artiste qui exprime émotions et récits par le mouvement corporel.",
    "Magicien": "Artiste qui réalise des tours pour émerveiller le public.",
    "Clown": "Comédien qui fait rire grâce à ses gestes, mimiques et spectacles.",
    "Marionnettiste": "Il manipule des marionnettes pour raconter des histoires au public.",
    "Animateur radio": "Il anime des émissions radiophoniques pour informer ou divertir.",
    "Animateur télé": "Présentateur qui anime des programmes télévisés.",
    "Community manager": "Il gère et anime la présence d'une entreprise ou personnalité sur les réseaux sociaux.",
    "Influenceur": "Personnalité active sur Internet qui influence les comportements d'achat ou d'opinion.",
    "Conseiller financier": "Il aide ses clients à optimiser leurs placements et gérer leur patrimoine.",
    "Trader": "Spécialiste des marchés financiers, il achète et vend des actifs pour générer des profits.",
    "Entrepreneur": "Créateur d'entreprise, il développe des projets et prend des risques économiques.",
    "Diplomate": "Représentant d'un pays à l'étranger, il défend ses intérêts et négocie.",
    "Militaire": "Il sert son pays en assurant sa défense et en participant aux opérations.",
    "Député": "Élu politique, il représente les citoyens et participe au vote des lois.",
    "Maire": "Responsable d'une commune, il gère l'administration locale.",
    "Président": "Chef d'État, il incarne et dirige la politique d'une nation."
}

dict_animaux = {
    "Chien": "Compagnon fidèle de l'homme, il est apprécié pour sa loyauté, sa sociabilité et sa diversité de races et de tailles.",
    "Chat": "Animal domestique indépendant, le chat est apprécié pour sa grâce, son calme et son instinct de chasseur.",
    "Cheval": "Utilisé depuis l'Antiquité pour le transport ou les loisirs, il incarne la puissance et la complicité avec l'homme.",
    "Vache": "Ruminant emblématique de l'élevage, elle fournit lait, viande et cuir à de nombreuses sociétés humaines.",
    "Mouton": "Apprécié pour sa laine et sa viande, cet herbivore paisible est souvent élevé en troupeaux.",
    "Chèvre": "Animal agile et curieux, elle produit du lait, du fromage et s'adapte à des terrains difficiles.",
    "Cochon": "Mammifère intelligent et sociable, il est élevé principalement pour sa viande.",
    "Poulet": "Oiseau de basse-cour très répandu, il est une source majeure d'œufs et de viande dans le monde.",
    "Canard": "Oiseau aquatique, il est souvent élevé pour sa chair, son foie gras ou ses œufs.",
    "Oie": "Plus grande que le canard, l'oie est un oiseau domestique connu pour sa vigilance et sa viande.",
    "Lapin": "Animal à reproduction rapide, il est élevé pour sa viande, sa fourrure ou comme animal de compagnie.",
    "Lion": "Félin majestueux surnommé « roi des animaux », il vit en groupe dans la savane africaine.",
    "Tigre": "Grand félin solitaire, il impressionne par sa force, sa discrétion et ses rayures caractéristiques.",
    "Éléphant": "Plus grand mammifère terrestre, il est reconnaissable à sa trompe et ses grandes oreilles.",
    "Girafe": "Avec son long cou, elle broute les feuilles des arbres les plus hauts de la savane africaine.",
    "Zèbre": "Mammifère herbivore à rayures noires et blanches, il vit en troupeaux dans les plaines africaines.",
    "Rhinocéros": "Puissant et massif, ce mammifère est menacé à cause du braconnage de ses cornes.",
    "Hippopotame": "Animal semi-aquatique, il vit dans les rivières d'Afrique et passe la journée dans l'eau.",
    "Singe": "Mammifère primate très intelligent, on le retrouve dans divers milieux tropicaux et forestiers.",
    "Gorille": "Grand singe fort et paisible, il vit en groupes familiaux dans les forêts d'Afrique centrale.",
    "Panda": "Symbole de la protection animale, il se nourrit presque exclusivement de bambou en Chine.",
    "Koala": "Marsupial d'Australie, il passe ses journées dans les eucalyptus dont il se nourrit exclusivement.",
    "Kangourou": "Marsupial sauteur emblématique de l'Australie, il transporte ses petits dans une poche ventrale.",
    "Ours": "Mammifère omnivore, parfois redouté, il hiberne en hiver et vit dans les forêts ou les montagnes.",
    "Loup": "Ancêtre du chien domestique, le loup est un prédateur social vivant en meutes organisées.",
    "Renard": "Petit carnivore rusé et discret, il est présent dans de nombreux contes et écosystèmes.",
    "Cerf": "Grand herbivore forestier aux bois majestueux, symbole de grâce et de force dans la nature.",
    "Sanglier": "Cochon sauvage d'Europe, il vit dans les forêts et se nourrit de racines et de fruits.",
    "Chameau": "Parfaitement adapté au désert, il peut stocker l'eau et transporter de lourdes charges.",
    "Dromadaire": "Avec une seule bosse, il est essentiel aux caravanes dans les déserts chauds.",
    "Dauphin": "Cétacé sociable et joueur, il fascine par son intelligence et ses bonds hors de l'eau.",
    "Baleine": "Plus grand animal vivant, elle se déplace lentement et produit des chants impressionnants.",
    "Requin": "Prédateur marin ancien, il joue un rôle important dans les écosystèmes marins.",
    "Raie": "Poisson plat à nage fluide, elle se cache souvent dans le sable des fonds marins.",
    "Tortue": "Reptile à carapace, terrestre ou marine, elle est réputée pour sa longévité.",
    "Serpent": "Reptile sans pattes, parfois venimeux, il fascine autant qu'il effraie.",
    "Crocodile": "Reptile redoutable des marais tropicaux, il guette ses proies au bord de l'eau.",
    "Aigle": "Rapace majestueux au regard perçant, il plane dans les hauteurs pour repérer ses proies.",
    "Faucon": "Oiseau de proie rapide et précis, il est utilisé en fauconnerie depuis des siècles.",
    "Corbeau": "Oiseau noir intelligent, souvent lié aux légendes, capable d'utiliser des outils.",
    "Perroquet": "Oiseau coloré et bavard, il peut imiter la parole humaine et vit souvent en couple.",
    "Pingouin": "Oiseau marin incapable de voler, il se déplace en groupe sur la glace et nage avec agilité.",
    "Autruche": "Plus grand oiseau du monde, incapable de voler mais très rapide à la course.",
    "Poule": "Oiseau domestique omniprésent, élevé pour ses œufs et sa viande.",
    "Chauve-souris": "Seul mammifère volant, elle utilise l'écholocation pour se déplacer dans le noir.",
    "Grenouille": "Amphibien bondissant, elle vit entre terre et eau et est très sensible à la pollution.",
    "Crabe": "Crustacé aux pinces robustes, il vit dans les fonds marins ou sur les plages.",
    "Pieuvre": "Mollusque à huit bras, elle est réputée pour son intelligence et ses capacités de camouflage.",
    "Étoile de mer": "Animal marin aux formes étoilées, elle se régénère si elle perd un bras.",
    "Méduse": "Organisme gélatineux marin, parfois urticant, qui flotte au gré des courants.",
    "Antilope": "Mammifère herbivore rapide des savanes africaines, reconnaissable à ses cornes fines et recourbées.",
    "Bison": "Grand herbivore puissant d'Amérique du Nord ou d'Europe, autrefois chassé intensivement.",
    "Yak": "Bovin robuste vivant sur les hauts plateaux de l'Himalaya, utilisé pour le lait et le transport.",
    "Buffle": "Grand bovin des zones tropicales, apprécié pour sa force et sa capacité à travailler dans les rizières.",
    "Tapir": "Mammifère forestier au museau allongé, présent en Amérique du Sud et en Asie.",
    "Capybara": "Plus gros rongeur du monde, il vit en groupe près des rivières d'Amérique du Sud.",
    "Chinchilla": "Petit rongeur andin à la fourrure très douce, souvent élevé comme animal de compagnie.",
    "Hamster": "Petit rongeur domestique, connu pour stocker sa nourriture dans ses abajoues.",
    "Rat": "Rongeur très adaptable, souvent associé aux villes mais aussi utilisé en recherche scientifique.",
    "Souris": "Petit rongeur rapide et curieux, présent dans de nombreux environnements.",
    "Écureuil": "Rongeur arboricole, connu pour stocker des noisettes pour l'hiver.",
    "Castor": "Rongeur aquatique bâtisseur, célèbre pour ses barrages en bois.",
    "Loutre": "Mammifère joueur et aquatique, excellent nageur, vivant en rivières ou en mer.",
    "Phoque": "Mammifère marin carnivore, agile dans l'eau mais maladroit sur terre.",
    "Morse": "Grand mammifère marin muni de longues défenses et adapté aux eaux glacées.",
    "Narval": "Cétacé de l'Arctique, surnommé « licorne des mers » grâce à sa longue défense torsadée.",
    "Orque": "Cétacé prédateur, aussi appelé « épaulard », connu pour sa chasse en groupe.",
    "Beluga": "Cétacé blanc de l'Arctique, émettant de nombreux sons pour communiquer.",
    "Lynx": "Félin sauvage aux oreilles ornées de pinceaux noirs, discret et solitaire.",
    "Guépard": "Félin le plus rapide du monde, capable d'atteindre 100 km/h en course.",
    "Panthère": "Grand félin tacheté, symbole d'élégance et de puissance dans la jungle.",
    "Jaguar": "Félin d'Amérique du Sud, puissant prédateur des forêts tropicales.",
    "Puma": "Grand félin d'Amérique, aussi appelé couguar ou lion des montagnes.",
    "Serval": "Félin africain aux grandes oreilles, chasseur habile de petits animaux.",
    "Caracal": "Félin d'Afrique et d'Asie, reconnaissable à ses oreilles pointues noires.",
    "Hyène": "Carnivore africain, connue pour son cri ressemblant à un rire et son rôle de charognard.",
    "Chacal": "Canidé sauvage d'Afrique et d'Asie, opportuniste et souvent charognard.",
    "Coyote": "Canidé d'Amérique du Nord, cousin du loup, réputé pour son hurlement.",
    "Dingo": "Chien sauvage d'Australie, vivant en meute.",
    "Paresseux": "Mammifère arboricole d'Amérique centrale et du Sud, célèbre pour sa lenteur.",
    "Tatou": "Petit mammifère cuirassé, protégé par une carapace rigide.",
    "Ornithorynque": "Mammifère étrange d'Australie, pondant des œufs et doté d'un bec de canard.",
    "Hérisson": "Petit mammifère couvert de piquants, qui se roule en boule pour se protéger.",
    "Taupe": "Petit mammifère fouisseur, vivant sous terre et se nourrissant de vers.",
    "Suricate": "Petit carnivore d'Afrique du Sud, vivant en groupes et observant le danger debout.",
    "Iguane": "Grand lézard herbivore des régions tropicales.",
    "Caméléon": "Reptile capable de changer de couleur et d'attraper ses proies avec sa langue longue.",
    "Gecko": "Petit lézard grimpeur, connu pour ses pattes adhésives.",
    "Varan": "Grand lézard carnivore, dont le varan de Komodo est le plus célèbre.",
    "Anaconda": "Serpent géant d'Amérique du Sud, constricteur redoutable.",
    "Boa": "Grand serpent constricteur, présent en Amérique.",
    "Cobra": "Serpent venimeux d'Asie et d'Afrique, reconnaissable à sa capuche.",
    "Vipère": "Serpent venimeux répandu en Europe et ailleurs.",
    "Python": "Serpent constricteur non venimeux, capable d'avaler de grandes proies.",
    "Alligator": "Reptile proche du crocodile, vivant en Amérique.",
    "Tortue de mer": "Reptile marin migrateur, souvent menacé par la pollution.",
    "Flamant rose": "Oiseau aux plumes roses, vivant en colonies dans les lagunes.",
    "Cygne": "Grand oiseau aquatique élégant, symbole de beauté et de fidélité.",
    "Canari": "Petit oiseau chanteur, longtemps élevé pour sa voix mélodieuse.",
    "Moineau": "Petit oiseau très commun dans les villes et campagnes.",
    "Hirondelle": "Oiseau migrateur au vol agile, annonciateur du printemps.",
    "Albatros": "Grand oiseau marin, capable de parcourir de longues distances.",
    "Pélican": "Grand oiseau aquatique, reconnaissable à sa poche sous le bec.",
    "Manchot": "Oiseau marin de l'hémisphère sud, incapable de voler mais excellent nageur.",
    "Colibri": "Minuscule oiseau capable de voler sur place grâce à ses battements d'ailes rapides.",
    "Toucan": "Oiseau tropical reconnaissable à son énorme bec coloré.",
    "Perdrix": "Petit oiseau terrestre, souvent chassé en Europe.",
    "Dinde": "Grand oiseau d'Amérique du Nord, élevé pour sa chair.",
    "Ane": "Mammifère domestique robuste, utilisé comme animal de bât.",
    "Mule": "Hybride issu d'un âne et d'une jument, utilisée pour le transport.",
    "Lama": "Camélidé domestiqué des Andes, utilisé pour le portage.",
    "Alpaga": "Proche du lama, élevé principalement pour sa laine douce.",
    "Fennec": "Petit renard du désert, reconnaissable à ses grandes oreilles.",
    "Axolotl": "Amphibien mexicain étonnant, capable de régénérer ses membres.",
    "Salamandre": "Amphibien à la peau lisse, souvent nocturne et discret.",
    "Homard": "Crustacé marin apprécié en gastronomie, doté de grandes pinces.",
    "Langouste": "Crustacé marin sans pinces, très prisé culinairement.",
    "Crevette": "Petit crustacé marin ou d'eau douce, vivant en groupes.",
    "Écrevisse": "Crustacé d'eau douce, semblable à un petit homard.",
    "Saumon": "Poisson migrateur, qui remonte les rivières pour se reproduire.",
    "Truite": "Poisson d'eau douce, très apprécié pour la pêche.",
    "Thon": "Poisson marin rapide, important dans l'alimentation mondiale.",
    "Poisson-clown": "Petit poisson coloré vivant en symbiose avec les anémones.",
    "Raie manta": "Grande raie majestueuse, planant dans les océans.",
    "Requin-marteau": "Requin reconnaissable à la forme particulière de sa tête.",
    "Hippocampe": "Petit poisson dont le mâle porte les petits dans une poche ventrale."
}

dict_acteurs = {
    "Robert De Niro": "Acteur américain légendaire, connu pour ses rôles puissants dans 'Taxi Driver' et 'Raging Bull'.",
    "Marlon Brando": "Icône du cinéma, célèbre pour son rôle dans 'Le Parrain' et sa méthode d'interprétation unique.",
    "Al Pacino": "Acteur américain réputé, célèbre pour ses performances intenses dans 'Scarface' et 'Le Parrain'.",
    "Leonardo DiCaprio": "Star hollywoodienne contemporaine, reconnue pour 'Titanic' et 'Inception'.",
    "Jack Nicholson": "Acteur charismatique américain, célèbre pour ses rôles dans 'Shining' et 'Vol au-dessus d'un nid de coucou'.",
    "Tom Hanks": "Acteur américain polyvalent, adoré pour 'Forrest Gump' et 'Il faut sauver le soldat Ryan'.",
    "Denzel Washington": "Acteur américain distingué, connu pour ses rôles dans 'Training Day' et 'Malcolm X'.",
    "Morgan Freeman": "Voix emblématique du cinéma, acteur primé, vu dans 'Les Évadés' et 'Million Dollar Baby'.",
    "Christian Bale": "Acteur britannique célèbre pour ses transformations physiques, notamment dans 'The Dark Knight'.",
    "Brad Pitt": "Star américaine renommée, acteur et producteur, connu pour 'Fight Club' et 'Once Upon a Time in Hollywood'.",
    "Meryl Streep": "Actrice américaine aux multiples Oscars, célèbre pour sa polyvalence dans 'Le Choix de Sophie'.",
    "Cate Blanchett": "Actrice australienne, reconnue pour ses rôles dans 'Elizabeth' et 'Le Seigneur des anneaux'.",
    "Natalie Portman": "Actrice américaine d'origine israélienne, oscarisée pour 'Black Swan'.",
    "Nicole Kidman": "Actrice australienne, célèbre pour 'Moulin Rouge' et 'The Hours'.",
    "Julia Roberts": "Actrice américaine, icône romantique, connue pour 'Pretty Woman'.",
    "Emma Stone": "Actrice américaine au charisme naturel, oscarisée pour 'La La Land'.",
    "Scarlett Johansson": "Actrice américaine, célèbre aussi comme Black Widow dans l'univers Marvel.",
    "Jennifer Lawrence": "Actrice américaine, révélée dans 'Hunger Games' et oscarisée pour 'Winter's Bone'.",
    "Anne Hathaway": "Actrice américaine, connue pour 'Le Diable s'habille en Prada' et 'Les Misérables'.",
    "Audrey Hepburn": "Icône du cinéma classique, célèbre pour 'Breakfast at Tiffany's'.",
    "Angelina Jolie": "Actrice et militante, connue pour 'Tomb Raider' et son engagement humanitaire.",
    "Sandra Bullock": "Actrice américaine populaire, vue dans 'Gravity' et 'Miss Congeniality'.",
    "Kristen Stewart": "Actrice américaine, révélée par 'Twilight', connue pour son jeu intense.",
    "Penélope Cruz": "Actrice espagnole oscarisée, célèbre pour ses rôles dans 'Vicky Cristina Barcelona'.",
    "Marion Cotillard": "Actrice française oscarisée, connue pour 'La Môme' et 'Inception'.",
    "Charlize Theron": "Actrice sud-africaine, oscarisée pour 'Monster'.",
    "Kate Winslet": "Actrice britannique, célèbre pour 'Titanic' et ses rôles dramatiques.",
    "Jodie Foster": "Actrice et réalisatrice américaine, oscarisée pour 'Le Silence des agneaux'.",
    "Glenn Close": "Actrice américaine respectée, connue pour 'Les Liaisons dangereuses'.",
    "Florence Pugh": "Jeune actrice britannique, saluée pour 'Little Women'.",
    "Michelle Yeoh": "Actrice malaisienne, célèbre pour 'Tigre et Dragon' et 'Everything Everywhere All at Once'.",
    "Zendaya": "Actrice et chanteuse américaine, star montante, connue pour 'Euphoria'.",
    "Viola Davis": "Actrice américaine oscarisée, reconnue pour son intensité dans 'Fences'.",
    "Isabelle Huppert": "Actrice française d'exception, célèbre pour 'Elle' et 'La Pianiste'.",
    "Monica Bellucci": "Actrice italienne, connue pour sa beauté et ses rôles dans 'Malèna'.",
    "Harrison Ford": "Acteur américain culte, connu pour ses rôles dans 'Indiana Jones' et 'Star Wars'.",
    "George Clooney": "Acteur et réalisateur américain, célèbre pour 'Ocean's Eleven' et 'Gravity'.",
    "Matt Damon": "Acteur américain, reconnu pour 'Jason Bourne' et 'Will Hunting'.",
    "Ben Affleck": "Acteur et réalisateur américain, oscarisé pour 'Argo'.",
    "Mark Wahlberg": "Acteur américain, passé du rap au cinéma, connu pour 'The Fighter'.",
    "Ryan Gosling": "Acteur canadien, célèbre pour 'Drive' et 'La La Land'.",
    "Ryan Reynolds": "Acteur canadien, connu pour son humour et son rôle de 'Deadpool'.",
    "Chris Hemsworth": "Acteur australien, célèbre pour son rôle de Thor dans Marvel.",
    "Chris Evans": "Acteur américain, reconnu comme Captain America dans Marvel.",
    "Chris Pratt": "Acteur américain, star de 'Jurassic World' et 'Guardians of the Galaxy'.",
    "Tom Hardy": "Acteur britannique intense, tête d'affiche de 'Venom'.",
    "Joaquin Phoenix": "Acteur américain, oscarisé pour 'Joker'.",
    "Heath Ledger": "Acteur australien disparu trop tôt, culte pour son Joker dans 'The Dark Knight'.",
    "Edward Norton": "Acteur américain reconnu pour 'Fight Club' et 'American History X'.",
    "Hugh Jackman": "Acteur australien, célèbre pour son rôle de Wolverine dans X-Men.",
    "Michael Fassbender": "Acteur germano-irlandais, reconnu pour 'Shame' et 'Steve Jobs'.",
    "Javier Bardem": "Acteur espagnol oscarisé, célèbre pour 'No Country for Old Men'.",
    "Antonio Banderas": "Acteur espagnol, connu pour 'Desperado' et 'Le Masque de Zorro'.",
    "Gael García Bernal": "Acteur mexicain, reconnu pour 'Amours chiennes' et 'Babel'.",
    "Diego Luna": "Acteur mexicain, connu pour 'Y Tu Mamá También' et 'Andor'.",
    "Ethan Hawke": "Acteur américain, salué pour 'Before Sunrise' et 'Training Day'.",
    "Kevin Costner": "Acteur et réalisateur américain, célèbre pour 'Danse avec les loups'.",
    "Russell Crowe": "Acteur néo-zélandais, oscarisé pour 'Gladiator'.",
    "Colin Farrell": "Acteur irlandais, reconnu pour 'Phone Booth' et 'The Banshees of Inisherin'.",
    "Brendan Fraser": "Acteur américain, star de 'La Momie' et oscarisé pour 'The Whale'.",
    "Keanu Reeves": "Acteur canadien, culte pour 'Matrix' et 'John Wick'.",
    "Will Smith": "Acteur américain, star de 'Men in Black' et 'Ali'.",
    "Jamie Foxx": "Acteur américain oscarisé, connu pour 'Ray' et 'Django Unchained'.",
    "Samuel L. Jackson": "Acteur américain prolifique, culte dans 'Pulp Fiction' et Marvel.",
    "Idris Elba": "Acteur britannique, connu pour 'Luther' et 'Beasts of No Nation'.",
    "Chadwick Boseman": "Acteur américain regretté, célèbre pour 'Black Panther'.",
    "Don Cheadle": "Acteur américain, reconnu pour 'Hotel Rwanda' et son rôle dans Marvel.",
    "Forest Whitaker": "Acteur oscarisé pour 'Le Dernier Roi d'Écosse'.",
    "Mahershala Ali": "Acteur américain, oscarisé pour 'Moonlight' et 'Green Book'.",
    "Adam Driver": "Acteur américain, star de 'Marriage Story' et de 'Star Wars'.",
    "Bill Murray": "Acteur américain culte, connu pour 'Ghostbusters' et 'Lost in Translation'.",
    "Steve Carell": "Acteur américain, star comique de 'The Office' et 'The Big Short'.",
    "Jim Carrey": "Acteur canadien, célèbre pour 'The Mask' et 'Eternal Sunshine'.",
    "Robin Williams": "Acteur américain regretté, culte pour 'Le Cercle des poètes disparus' et 'Mrs Doubtfire'.",
    "Eddie Murphy": "Acteur américain comique, star de 'Un prince à New York' et 'Beverly Hills Cop'.",
    "Gene Hackman": "Acteur américain oscarisé, connu pour 'French Connection' et 'Impitoyable'.",
    "Sean Connery": "Icône écossaise, célèbre pour avoir incarné James Bond.",
    "Daniel Craig": "Acteur britannique, incarnation moderne de James Bond.",
    "Pierce Brosnan": "Acteur irlandais, connu pour James Bond et 'Mamma Mia!'.",
    "Michael Caine": "Acteur britannique respecté, vu dans 'The Dark Knight' et 'Inception'.",
    "Gary Oldman": "Acteur britannique caméléon, oscarisé pour 'Les Heures sombres'.",
    "Alan Rickman": "Acteur britannique culte, célèbre pour 'Harry Potter' et 'Die Hard'.",
    "Anthony Hopkins": "Acteur britannique oscarisé, connu pour 'Le Silence des agneaux'.",
    "Ian McKellen": "Acteur britannique, célèbre pour Gandalf et Magneto.",
    "Patrick Stewart": "Acteur britannique, culte dans 'Star Trek' et 'X-Men'.",
    "Benedict Cumberbatch": "Acteur britannique, connu pour 'Sherlock' et 'Doctor Strange'.",
    "Tom Holland": "Jeune acteur britannique, célèbre comme Spider-Man de Marvel.",
    "Tobey Maguire": "Acteur américain, premier Spider-Man culte du cinéma moderne.",
    "Andrew Garfield": "Acteur britannique-américain, Spider-Man et oscarisé pour 'Tick, Tick... Boom!'.",
    "Paul Newman": "Acteur américain classique, légendaire pour 'L'Arnaqueur'.",
    "James Dean": "Icône américaine des années 50, disparu tragiquement jeune.",
    "Humphrey Bogart": "Acteur américain mythique, célèbre pour 'Casablanca'.",
    "Clark Gable": "Acteur américain, icône de 'Autant en emporte le vent'.",
    "Cary Grant": "Acteur britannique légendaire, star du cinéma hollywoodien classique.",
    "Gregory Peck": "Acteur américain oscarisé, culte pour 'Du silence et des ombres'.",
    "Spencer Tracy": "Acteur américain, figure majeure de l'âge d'or d'Hollywood.",
    "Kirk Douglas": "Acteur américain mythique, star de 'Spartacus'.",
    "Charlton Heston": "Acteur américain, culte pour 'Ben-Hur'.",
    "Jean-Paul Belmondo": "Icône française du cinéma, star de 'À bout de souffle'.",
    "Alain Delon": "Acteur français mythique, connu pour 'Le Samouraï'.",
    "Gérard Depardieu": "Acteur français prolifique, connu pour 'Cyrano de Bergerac'.",
    "Jean Reno": "Acteur français, star de 'Léon' et 'Les Visiteurs'.",
    "Omar Sy": "Acteur français, célèbre pour 'Intouchables'.",
    "Vincent Cassel": "Acteur français reconnu pour 'La Haine' et 'Black Swan'.",
    "Romain Duris": "Acteur français, connu pour 'L'Auberge Espagnole'.",
    "Jean Dujardin": "Acteur français oscarisé pour 'The Artist'.",
    "Daniel Auteuil": "Acteur français respecté, connu pour 'Jean de Florette'.",
    "Louis de Funès": "Acteur comique français légendaire, culte pour 'La Grande Vadrouille'.",
    "Fernandel": "Acteur comique français, célèbre pour 'Don Camillo'.",
    "Bourvil": "Acteur et comique français, connu pour 'La Traversée de Paris'.",
    "Pierre Richard": "Acteur comique français, culte dans 'La Chèvre'.",
    "Alain Chabat": "Acteur et réalisateur français, connu pour 'Astérix et Obélix: Mission Cléopâtre'.",
    "Jamel Debbouze": "Acteur et humoriste français, vu dans 'Astérix' et 'Indigènes'.",
    "Kad Merad": "Acteur français, connu pour 'Bienvenue chez les Ch'tis'.",
    "Dany Boon": "Acteur et réalisateur français, star de la comédie populaire.",
    "François Cluzet": "Acteur français, connu pour 'Intouchables'.",
    "Lambert Wilson": "Acteur français, vu dans 'Des Hommes et des Dieux' et 'Matrix'.",
    "Tahar Rahim": "Acteur français, reconnu pour 'Un prophète'.",
    "Mathieu Kassovitz": "Acteur et réalisateur français, connu pour 'La Haine'.",
    "Guillaume Canet": "Acteur et réalisateur français, reconnu pour 'Ne le dis à personne'.",
    "Jean-Louis Trintignant": "Acteur français culte, vu dans 'Amour'.",
    "Michel Piccoli": "Acteur français, grande figure du cinéma d'auteur.",
    "Romy Schneider": "Actrice franco-allemande, icône avec 'Sissi' et 'La Piscine'.",
    "Brigitte Bardot": "Icône française des années 60, actrice et symbole de beauté.",
    "Catherine Deneuve": "Actrice française culte, connue pour 'Les Parapluies de Cherbourg'.",
    "Sophie Marceau": "Actrice française, célèbre pour 'La Boum' et 'Braveheart'."
}

dict_films_series = {
    "Le Parrain": "Film culte de Francis Ford Coppola, ce drame mafieux raconte la saga de la famille Corleone et ses luttes de pouvoir.",
    "Titanic": "L'histoire tragique du naufrage du célèbre paquebot, mêlée à une romance intense entre Jack et Rose.",
    "Inception": "Un thriller de science-fiction où les rêves deviennent le terrain d'un casse spectaculaire orchestré par Dom Cobb.",
    "La Liste de Schindler": "Un film poignant sur Oskar Schindler, qui sauva des centaines de Juifs durant l'Holocauste.",
    "Forrest Gump": "Le parcours incroyable d'un homme simple au cœur d'événements historiques majeurs des États-Unis.",
    "Gladiator": "Maximus, général romain devenu gladiateur, cherche vengeance dans une Rome antique impitoyable.",
    "Avatar": "Un film de science-fiction époustouflant où l'homme rencontre la nature et une civilisation extraterrestre sur Pandora.",
    "Le Seigneur des Anneaux : La Communauté de l'Anneau": "Début de l'épopée fantastique où Frodon doit détruire un anneau maléfique pour sauver la Terre du Milieu.",
    "Star Wars : Un Nouvel Espoir": "Le premier volet d'une saga spatiale mythique, où Luke Skywalker se lance dans l'aventure pour combattre l'Empire.",
    "Jurassic Park": "Un parc d'attractions peuplé de dinosaures recréés génétiquement tourne au cauchemar pour ses visiteurs.",
    "Le Roi Lion": "Un dessin animé Disney emblématique sur la vie, la perte et la responsabilité d'un jeune lion dans la savane.",
    "Pulp Fiction": "Film culte de Quentin Tarantino, mêlant plusieurs histoires criminelles dans un style non linéaire.",
    "La La Land": "Une histoire d'amour moderne entre une actrice et un musicien, sur fond de rêves et de jazz à Los Angeles.",
    "The Dark Knight": "Batman affronte le Joker dans ce thriller sombre et intense réalisé par Christopher Nolan.",
    "Interstellar": "Un voyage spatial où un père cherche à sauver l'humanité en explorant des dimensions inconnues.",
    "Les Évadés": "Deux prisonniers forment une amitié indéfectible en cherchant la liberté à travers une évasion audacieuse.",
    "Fight Club": "Un homme découvre un monde souterrain de combats clandestins et remet en question sa propre réalité.",
    "Le Fabuleux Destin d'Amélie Poulain": "Une comédie romantique française sur une jeune femme qui décide de changer la vie des autres.",
    "Parasite": "Un thriller coréen qui explore les inégalités sociales avec une tension et un suspense hors normes.",
    "Mad Max : Fury Road": "Un road movie post-apocalyptique intense, où survie et rébellion s'entremêlent dans un désert infernal.",
    "Blade Runner 2049": "Suite du classique de science-fiction, entre quête d'identité et mystères futuristes.",
    "Le Grand Bleu": "Un film sur la rivalité et l'amitié entre deux plongeurs passionnés dans un univers aquatique.",
    "Moulin Rouge!": "Une comédie musicale flamboyante mêlant amour, passion et tragédie dans le Paris bohème.",
    "Casablanca": "Classique du cinéma romantique pendant la Seconde Guerre mondiale, entre amour et devoir.",
    "Le Silence des Agneaux": "Un thriller psychologique où une jeune agente du FBI doit capturer un tueur en série redoutable.",
    "The Social Network": "L'histoire de la création de Facebook, pleine d'ambition, de rivalités et de conflits juridiques.",
    "The Avengers": "Un groupe de super-héros s'allie pour sauver la Terre d'une menace extraterrestre.",
    "Joker": "L'origine sombre du célèbre ennemi de Batman, explorant folie et marginalité.",
    "The Matrix": "Un hacker découvre que la réalité est une illusion, dans ce film qui a révolutionné la science-fiction.",
    "Amadeus": "La vie tourmentée de Mozart vue à travers les yeux de son rival Salieri.",
    "The Revenant": "Un trappeur lutte pour survivre dans la nature sauvage et se venger de ses ennemis.",
    "Slumdog Millionaire": "Un jeune indien participe à un jeu télévisé et raconte son incroyable parcours de vie.",
    "La Vie est Belle": "Un père utilise l'humour pour protéger son fils dans un camp de concentration nazi.",
    "Shining": "Un film d'horreur psychologique où une famille est piégée dans un hôtel isolé et hanté.",
    "Gravity": "Un thriller spatial haletant où deux astronautes tentent de survivre dans l'espace.",
    "Les Temps Modernes": "Un chef-d'œuvre de Chaplin, satire sociale sur l'industrialisation et la condition humaine.",
    "Black Panther": "Un super-héros africain combat pour son royaume et son peuple dans ce film Marvel révolutionnaire.",
    "Là-haut": "Un film d'animation émouvant où un vieil homme part à l'aventure en attelant sa maison à des ballons.",
    "Coco": "Un voyage coloré et musical dans le monde des morts, célébrant la famille et la mémoire.",
    "Toy Story": "Les jouets prennent vie dans cette saga d'animation pleine d'humour et d'émotion.",
    "Le Loup de Wall Street": "L'ascension et la chute d'un courtier véreux dans le monde de la finance new-yorkaise.",
    "Deadpool": "Un anti-héros sarcastique et irrévérencieux dans un film de super-héros atypique.",
    "Wonder Woman": "Une héroïne mythologique qui lutte pour la paix pendant la Première Guerre mondiale.",
    "Apocalypse Now": "Un voyage hallucinant au cœur de la guerre du Vietnam, réalisé par Francis Ford Coppola.",
    "Les Affranchis": "Un chef-d'œuvre de Martin Scorsese retraçant la vie d'un gangster sur plusieurs décennies.",  # Goodfellas
    "Seven": "Un thriller sombre où deux détectives traquent un tueur en série inspiré des sept péchés capitaux.",
    "American Beauty": "Une critique acerbe de la société américaine à travers la crise existentielle d'un homme.",
    "La Ligne verte": "Un gardien de prison découvre les pouvoirs mystérieux d'un condamné à mort au grand cœur.",
    "Il faut sauver le soldat Ryan": "Un film de guerre marquant sur la mission de sauver un soldat en Normandie.",  # Saving Private Ryan
    "Whiplash": "Un étudiant en musique affronte un professeur tyrannique dans sa quête de perfection.",
    "The Big Lebowski": "Une comédie culte des frères Coen autour d'un quiproquo et d'un anti-héros attachant.",
    "No Country for Old Men": "Un thriller brutal sur la violence et le destin dans le Texas désertique.",
    "Requiem for a Dream": "Un drame poignant sur l'addiction et la destruction qu'elle entraîne.",
    "There Will Be Blood": "La montée au pouvoir impitoyable d'un magnat du pétrole au début du XXe siècle.",
    "Oldboy": "Un thriller coréen violent et captivant sur vengeance et manipulation.",
    "Chinatown": "Un film noir culte où un détective privé plonge dans une affaire de corruption.",
    "Orange mécanique": "Une dystopie de Stanley Kubrick sur la violence, le libre arbitre et le contrôle social.",  # A Clockwork Orange
    "Taxi Driver": "Un vétéran perturbé devient chauffeur de taxi et sombre dans la folie à New York.",
    "Scarface": "L'ascension et la chute d'un trafiquant cubain incarné par Al Pacino.",
    "Heat": "Un duel intense entre un policier et un braqueur dans un Los Angeles sous tension.",
    "The Irishman": "Un récit sur le crime organisé et la loyauté, signé Martin Scorsese.",
    "Les Infiltrés": "Un policier infiltré et une taupe dans la police s'affrontent à Boston.",  # The Departed
    "The Truman Show": "Un homme découvre que sa vie entière est une émission de télévision.",
    "Le Pianiste": "Un musicien juif lutte pour survivre dans le ghetto de Varsovie pendant la guerre.",  # The Pianist
    "L'Odyssée de Pi": "L'odyssée spirituelle d'un jeune naufragé accompagné d'un tigre du Bengale.",  # Life of Pi
    "Edward aux mains d'argent": "Une fable gothique sur un homme aux mains en ciseaux rejeté par la société.",  # Edward Scissorhands
    "Beetlejuice": "Une comédie fantastique délirante où un couple de fantômes engage un exorciste.",
    "Le Prestige": "La rivalité obsessionnelle entre deux magiciens dans l'Angleterre victorienne.",  # The Prestige
    "Memento": "Un homme amnésique enquête sur le meurtre de sa femme dans un récit non linéaire.",
    "Dunkerque": "Un film de guerre intense sur l'évacuation des troupes alliées en 1940.",  # Dunkirk
    "Tenet": "Un thriller de science-fiction autour du temps inversé et d'un complot mondial.",
    "Sixième Sens": "Un enfant affirme voir les morts, bouleversant son psychologue.",  # The Sixth Sense
    "Us": "Un film d'horreur où une famille affronte ses doubles maléfiques.",
    "Hellboy": "Un démon élevé par des humains lutte contre les forces du mal.",
    "Pacific Rim": "Des robots géants affrontent des monstres venus d'un autre monde.",
    "King Kong": "Un singe géant capturé devient l'attraction de New York avant de se rebeller.",
    "Godzilla": "Un monstre gigantesque surgit des océans et menace l'humanité.",
    "Les Dents de la mer": "Un requin tueur sème la terreur dans une station balnéaire.",  # Jaws
    "E.T. l'extra-terrestre": "L'amitié entre un enfant et un extraterrestre égaré bouleverse les cœurs.",  # E.T.
    "Rencontres du troisième type": "Des humains établissent un premier contact avec des extraterrestres.",  # Close Encounters...
    "Les Aventuriers de l'Arche perdue": "L'aventurier part à la recherche de l'Arche d'alliance.",  # Indiana Jones: Raiders of the Lost Ark
    "Indiana Jones et la Dernière Croisade": "Indy recherche le Saint Graal avec son père.",  # Indiana Jones and the Last Crusade
    "Indiana Jones et le Temple maudit": "Une mission périlleuse en Inde avec des cultes obscurs.",  # Indiana Jones and the Temple of Doom
    "Retour vers le futur": "Un adolescent voyage dans le passé grâce à une DeLorean temporelle.",  # Back to the Future
    "Retour vers le futur II": "Retour dans le futur avec des univers alternatifs.",
    "Retour vers le futur III": "Un western futuriste où Marty et Doc voyagent au Far West.",
    "S.O.S. Fantômes": "Une équipe capture des fantômes dans New York avec humour et gadgets.",  # Ghostbusters
    "L'Exorciste": "Un classique de l'horreur sur une jeune fille possédée par le diable.",  # The Exorcist
    "Psychose": "Un thriller d'Hitchcock avec la fameuse scène de la douche.",  # Psycho
    "Sueurs froides": "Un policier sujet au vertige enquête sur une femme mystérieuse.",  # Vertigo
    "Fenêtre sur cour": "Un photographe cloué chez lui observe un meurtre depuis sa fenêtre.",  # Rear Window
    "La Mort aux trousses": "Un homme ordinaire est traqué par des espions dans ce film d'action culte.",  # North by Northwest
    "La Dolce Vita": "Un chef-d'œuvre de Fellini sur la décadence romaine.",
    "Cinema Paradiso": "Un hommage au cinéma et à l'enfance en Italie.",
    "Les Sept Samouraïs": "Un classique d'Akira Kurosawa où des samouraïs protègent un village.",  # Seven Samurai
    "Yojimbo": "Un samouraï manipule deux clans rivaux dans un village.",
    "Memories of Murder": "Un thriller coréen sur une enquête policière non résolue.",
    "Train to Busan": "Un film de zombies intense dans un train en Corée du Sud.",
    "Akira": "Un film d'animation culte sur Tokyo post-apocalyptique et les pouvoirs psychiques.",
    "Game of Thrones": "Série d'intrigues et batailles dans un monde médiéval fantastique marqué par la lutte pour le pouvoir.",
    "Breaking Bad": "Série où un prof de chimie devient fabricant de drogue, plongé dans le crime.",
    "Stranger Things": "Série d'enfants affrontant des phénomènes paranormaux dans une petite ville des années 80.",
    "The Crown": "Série sur la vie et le règne de la reine Élisabeth II, entre drame familial et politique.",
    "Friends": "Série comique culte sur un groupe d'amis vivant à New York.",
    "The Mandalorian": "Série d'un chasseur de primes solitaire parcourant la galaxie dans l'univers Star Wars.",
    "Westworld": "Série où les androïdes d'un parc futuriste prennent conscience d'eux-mêmes.",
    "The Witcher": "Série sur un chasseur de monstres dans un monde sombre et magique.",
    "Black Mirror": "Série d'histoires sombres sur les dérives de la technologie moderne.",
    "Sherlock": "Série sur les enquêtes du célèbre détective dans une version moderne.",
    "The Office": "Série humoristique décalée sur la vie quotidienne dans un bureau américain.",
    "Narcos": "Série sur l'ascension et la chute des barons de la drogue en Colombie.",
    "Better Call Saul": "Série préquelle sur l'avocat Jimmy McGill et sa transformation.",
    "Dexter": "Série d'un expert médico-légal qui tue uniquement les criminels.",
    "Lost": "Série où les survivants d'un crash affrontent mystères sur une île isolée.",
    "Chernobyl": "Série dramatique sur la catastrophe nucléaire de 1986.",
    "True Detective": "Série d'enquêtes sombres avec des détectives torturés.",
    "Peaky Blinders": "Série sur des gangsters britanniques entre pouvoir et violence.",
    "The Handmaid's Tale": "Série dystopique où les femmes sont réduites en esclavage.",
    "Ozark": "Série d'une famille impliquée dans le blanchiment d'argent pour un cartel.",
    "The Boys": "Série sur des super-héros corrompus combattus par des justiciers.",
    "Vikings": "Série sur des guerriers nordiques entre légendes et histoire.",
    "Homeland": "Série où une agente de la CIA lutte contre le terrorisme.",
    "House of Cards": "Série politique sur un politicien manipulateur jouant la course au pouvoir.",
    "The Walking Dead": "Série de survivants d'une apocalypse zombie cherchant à survivre.",
    "La Casa de Papel": "Série d'un braquage audacieux à la Maison de la Monnaie espagnole.",
    "The Big Bang Theory": "Série comique sur un groupe de scientifiques geeks.",
    "Grey's Anatomy": "Série sur la vie et les défis de médecins à l'hôpital.",
    "Suits": "Série où un avocat sans diplôme collabore dans un cabinet prestigieux.",
    "Modern Family": "Série comique sur les hauts et bas d'une grande famille.",
    "How I Met Your Mother": "Série où un homme raconte comment il a rencontré sa femme.",
    "The Flash": "Série sur un jeune homme doté d'une vitesse surhumaine qui combat le crime.",
    "Arrow": "Série où un justicier utilise un arc pour protéger sa ville.",
    "Lucifer": "Série où le diable aide la police à résoudre des crimes.",
    "Sons of Anarchy": "Série sur un club de motards confronté à loyauté et violence.",
    "The Good Place": "Série où une femme découvre l'au-delà et cherche à s'améliorer.",
    "Parks and Recreation": "Série satirique humoristique d'un service municipal.",
    "The Marvelous Mrs. Maisel": "Série où une femme au foyer devient humoriste dans les années 50.",
    "Castle": "Série où un écrivain collabore avec une détective à New York.",
    "Mindhunter": "Série où des agents du FBI interviewent des tueurs en série.",
    "Dead to Me": "Série sur deux femmes liées par le deuil et les secrets.",
    "Black Sails": "Série de pirates pleine de lutte pour le pouvoir.",
    "Hannibal": "Série où un psychiatre cannibale fait face à un agent du FBI.",
    "Community": "Série comique sur un groupe d'étudiants aux caractères variés.",
    "Dr House": "Série sur un médecin génial et cynique qui résout des cas complexes.",
    "Brooklyn Nine-Nine": "Comédie policière déjantée sur une équipe de détectives new-yorkais.",
    "Malcolm": "Série humoristique sur un adolescent surdoué et sa famille chaotique.",
    "Scrubs": "Comédie dramatique sur la vie de jeunes médecins internes.",
    "Desperate Housewives": "Série dramatique sur des voisines et leurs secrets à Wisteria Lane.",
    "Prison Break": "Série culte où un homme s'évade de prison pour sauver son frère.",
    "The Umbrella Academy": "Famille de super-héros dysfonctionnelle luttant contre l'apocalypse.",
    "Sense8": "Huit inconnus connectés mentalement à travers le monde.",
    "Penny Dreadful": "Série gothique où monstres et figures littéraires se croisent.",
    "True Blood": "Série de vampires et humains cohabitant dans un climat tendu.",
    "The Originals": "Spin-off de Vampire Diaries centré sur la famille des vampires originels.",
    "Teen Wolf": "Un adolescent devient loup-garou et doit gérer sa nouvelle vie.",
    "Riverdale": "Relecture sombre des comics Archie, entre drame et mystère.",
    "13 Reasons Why": "Série dramatique sur le suicide d'une adolescente et ses raisons.",
    "Elite": "Thriller espagnol sur un lycée prestigieux et ses sombres secrets.",
    "Euphoria": "Série crue et stylisée sur des ados marqués par drogues, sexe et identité.",
    "Big Little Lies": "Série dramatique sur des mères riches cachant des secrets sombres.",
    "Spartacus": "Série violente et spectaculaire sur la rébellion d'esclaves gladiateurs.",
    "The Last Kingdom": "Série médiévale sur les luttes entre Vikings et Anglo-Saxons.",
    "Knightfall": "Série sur les chevaliers templiers et leurs intrigues.",
    "Outlander": "Histoire d'amour et de voyage dans le temps en Écosse et au-delà.",
    "Doctor Who": "Série culte britannique sur le Seigneur du Temps voyageant dans le TARDIS.",
    "Stargate Universe": "Équipe bloquée dans un vaisseau ancien voyageant loin dans la galaxie.",
    "The 100": "Jeunes envoyés sur Terre pour tester si elle est de nouveau habitable.",
    "Colony": "Série dystopique où la Terre est occupée par des forces extraterrestres.",
    "The Man in the High Castle": "Uchronie où l'Allemagne et le Japon ont gagné la Seconde Guerre mondiale.",
    "The Sopranos": "Série culte sur un parrain mafieux entre affaires et thérapie.",
    "Billions": "Série sur la rivalité entre un procureur et un magnat de la finance.",
    "Mr. Robot": "Hacker engagé dans une lutte contre les multinationales.",
    "Utopia": "Série conspirationniste sur un manuscrit prédisant des catastrophes.",
    "Bodyguard": "Série britannique sur un vétéran chargé de protéger une politicienne.",
    "Luther": "Inspecteur charismatique et tourmenté dans des enquêtes violentes.",
    "Top Boy": "Série britannique sur la vie dans les quartiers difficiles de Londres.",
    "Alice in Borderland": "Série japonaise où des jeunes doivent survivre à des jeux mortels.",
    "Fauda": "Série israélienne sur un agent infiltré dans des réseaux terroristes.",
    "Engrenages": "Série policière française réaliste sur les affaires criminelles.",
    "Le Bureau des Légendes": "Série française sur le renseignement et les agents sous couverture.",
    "Plus belle la vie": "Soap français emblématique situé à Marseille.",
    "Kaamelott": "Comédie française culte parodiant la légende arthurienne.",
    "H": "Comédie française absurde dans un hôpital."
}

dict_livres_bd = {
    "Les Misérables": "Un livre de Victor Hugo, une épopée sociale et historique qui explore la condition humaine en France au XIXe siècle.",
    "1984": "Ce roman de George Orwell dépeint une dystopie où la surveillance et la manipulation sont omniprésentes.",
    "Harry Potter à l'école des sorciers": "Premier tome de la célèbre série de J.K. Rowling, un livre jeunesse magique et aventureux.",
    "Le Petit Prince": "Une œuvre poétique et philosophique d'Antoine de Saint-Exupéry, racontant l'histoire d'un petit garçon venu d'une autre planète.",
    "Le Seigneur des Anneaux": "Épopée fantastique écrite par J.R.R. Tolkien, ce livre raconte la quête d'un anneau magique.",
    "Moby Dick": "Un classique d'Herman Melville, ce livre relate la chasse obsessionnelle à une baleine blanche.",
    "Pride and Prejudice": "Roman de Jane Austen, ce livre explore les moeurs sociales et les relations amoureuses en Angleterre au XVIIIe siècle.",
    "Le Comte de Monte-Cristo": "Ce livre d'Alexandre Dumas raconte l'histoire d'une vengeance spectaculaire.",
    "La Peste": "Un livre d'Albert Camus, allégorie de la lutte humaine face à une épidémie.",
    "To Kill a Mockingbird": "Roman de Harper Lee sur le racisme et l'injustice dans le Sud des États-Unis.",
    "Don Quichotte": "Un livre de Miguel de Cervantes, mêlant humour et critique sociale à travers les aventures d'un chevalier fantasque.",
    "Jane Eyre": "Ce roman de Charlotte Brontë raconte le parcours d'une héroïne forte et indépendante.",
    "Les Fleurs du Mal": "Recueil de poèmes de Charles Baudelaire, ce livre explore la beauté et le mal.",
    "Le Nom de la Rose": "Un roman policier historique d'Umberto Eco, mêlant enquête et réflexion philosophique.",
    "Germinal": "Livre d'Émile Zola décrivant la vie difficile des mineurs au XIXe siècle.",
    "Les Chroniques de Narnia": "Série de livres de C.S. Lewis, un univers fantastique pour la jeunesse.",
    "Crime et Châtiment": "Un roman de Fiodor Dostoïevski sur la culpabilité et la rédemption.",
    "L'Étranger": "Un livre d'Albert Camus, une réflexion sur l'absurde et l'aliénation.",
    "Le Hobbit": "Roman de J.R.R. Tolkien, ce livre précède Le Seigneur des Anneaux et narre une aventure fantastique.",
    "Beloved": "Livre de Toni Morrison, il aborde les conséquences de l'esclavage aux États-Unis.",
    "Le Journal d'Anne Frank": "Témoignage poignant sous forme de journal intime écrit pendant la Seconde Guerre mondiale.",
    "Les Trois Mousquetaires": "Livre d'Alexandre Dumas, une aventure pleine d'action et de loyauté.",
    "Orgueil et Préjugés": "Roman classique de Jane Austen sur l'amour et la société.",
    "L'Alchimiste": "Un conte philosophique de Paulo Coelho sur la quête de ses rêves.",
    "Frankenstein": "Ce livre de Mary Shelley invente le mythe du monstre créé par l'homme.",
    "Dracula": "Roman gothique de Bram Stoker qui popularise le vampire.",
    "La Métamorphose": "Nouvelle de Franz Kafka, ce livre explore la transformation absurde d'un homme en insecte.",
    "Une Vie": "Livre de Guy de Maupassant, portrait d'une femme dans la société du XIXe siècle.",
    "Cien años de soledad": "Roman magique de Gabriel García Márquez, ce livre raconte l'histoire d'une famille sur plusieurs générations.",
    "L'Iliade": "Épopée grecque attribuée à Homère, ce livre relate la guerre de Troie.",
    "L'Odyssée": "Autre grand poème d'Homère, ce livre narre les aventures d'Ulysse.",
    "Les Aventures de Sherlock Holmes": "Recueil de nouvelles de Sir Arthur Conan Doyle, avec le célèbre détective.",
    "Les Raisins de la colère": "Livre de John Steinbeck, une chronique sociale des années 30 aux États-Unis.",
    "Les Liaisons dangereuses": "Roman épistolaire de Pierre Choderlos de Laclos, intrigue et manipulation au XVIIIe siècle.",
    "Le Petit Nicolas": "Série de livres humoristiques de René Goscinny sur l'enfance.",
    "Le Parfum": "Roman de Patrick Süskind, ce livre raconte l'obsession d'un homme pour les odeurs.",
    "Harry Potter et la Chambre des Secrets": "Deuxième tome de la série de J.K. Rowling, ce livre poursuit l'aventure magique.",
    "Le Rouge et le Noir": "Roman de Stendhal, portrait d'un jeune ambitieux dans la société française.",
    "L'Écume des jours": "Livre de Boris Vian, un conte poétique et absurde.",
    "Le Procès": "Un livre de Franz Kafka sur la bureaucratie et l'absurdité.",
    "Le Vieil Homme et la Mer": "Court roman d'Ernest Hemingway sur la lutte entre un pêcheur et un poisson.",
    "L'Amant": "Livre de Marguerite Duras, récit autobiographique sur l'amour interdit.",
    "Le Grand Gatsby": "Roman de F. Scott Fitzgerald sur le rêve américain.",
    "Lolita": "Un livre controversé de Vladimir Nabokov sur une obsession.",
    "Le Nom du vent": "Premier tome d'une saga fantasy de Patrick Rothfuss, ce livre mêle magie et aventure.",
    "Shining": "Roman de Stephen King, un thriller horrifique dans un hôtel isolé et hanté.",
    "Ça": "Un livre de Stephen King où des enfants affrontent une entité maléfique prenant forme de clown.",
    "Dune": "Roman de Frank Herbert, grande fresque de science-fiction sur un désert et une ressource précieuse.",
    "Hunger Games": "Premier tome de Suzanne Collins, où des adolescents s'affrontent dans une arène mortelle.",
    "Divergente": "Roman de Veronica Roth, dystopie avec des castes sociales basées sur des traits de personnalité.",
    "Twilight": "Livre de Stephenie Meyer, romance entre une humaine et un vampire.",
    "Percy Jackson: Le Voleur de Foudre": "Premier tome de Rick Riordan, inspiré de la mythologie grecque.",
    "Percy Jackson: La Mer des Monstres": "Deuxième tome de la série Percy Jackson.",
    "Percy Jackson: Le Dernier Olympien": "Dernier tome de la première saga Percy Jackson.",
    "Eragon": "Premier tome de Christopher Paolini, saga de fantasy avec dragons.",
    "La Guerre des Clans": "Saga jeunesse d'Erin Hunter sur des chats sauvages organisés en clans.",
    "La Belle et la Bête": "Conte classique popularisé par Jeanne-Marie Leprince de Beaumont.",
    "Peau d'Âne": "Conte de Charles Perrault, mêlant magie et épreuves.",
    "Les Contes de Grimm": "Recueil de contes traditionnels européens par les frères Grimm.",
    "Les Contes d'Andersen": "Recueil de contes poétiques et mélancoliques.",
    "Les Mille et Une Nuits": "Recueil de contes orientaux célèbres avec Shéhérazade.",
    "Roméo et Juliette": "Tragédie de William Shakespeare sur l'amour impossible.",
    "Hamlet": "Pièce de Shakespeare sur la vengeance et la folie.",
    "Candide": "Un conte philosophique de Voltaire critiquant l'optimisme naïf.",
    "Zadig": "Conte philosophique de Voltaire.",
    "Nana": "Roman de Zola sur une courtisane et la décadence sociale.",
    "Au Bonheur des Dames": "Roman de Zola sur la naissance des grands magasins.",
    "L'Œuvre": "Roman de Zola sur un peintre et les affres de la création.",
    "Les Chants de Maldoror": "Poème en prose surréaliste de Lautréamont.",
    "Le Livre de la Jungle": "Recueil de Rudyard Kipling, aventures de Mowgli.",
    "Kim": "Roman d'aventures de Rudyard Kipling en Inde coloniale.",
    "Autant en emporte le vent": "Roman de Margaret Mitchell sur la guerre de Sécession.",
    "Docteur Jekyll et Mister Hyde": "Court roman de Robert Louis Stevenson sur la dualité humaine.",
    "L'Île au trésor": "Roman d'aventures de Stevenson sur des pirates et un trésor.",
    "Voyage au centre de la Terre": "Roman de Jules Verne explorant les profondeurs de la Terre.",
    "Vingt mille lieues sous les mers": "Aventure de Jules Verne avec le capitaine Nemo.",
    "Le Tour du monde en quatre-vingts jours": "Roman d'aventures de Jules Verne avec Phileas Fogg.",
    "De la Terre à la Lune": "Roman d'anticipation de Jules Verne.",
    "La Machine à explorer le temps": "Roman de H.G. Wells sur le voyage temporel.",
    "L'Homme invisible": "Roman de H.G. Wells sur un scientifique devenu invisible.",
    "Shogun": "Roman historique de James Clavell sur le Japon féodal.",
    "L'Art de la guerre": "Texte stratégique de Sun Tzu, classique chinois.",
    "Le Prince": "Traité politique de Machiavel.",
    "Par-delà bien et mal": "Autre ouvrage philosophique de Nietzsche.",
    "Critique de la raison pure": "Livre de Kant, un des grands textes philosophiques.",
    "Éthique": "Texte de Spinoza, réflexion sur Dieu, la nature et l'homme.",
    "Discours de la méthode": "Ouvrage philosophique de Descartes.",
    "L'Interprétation des rêves": "Texte fondateur de Freud sur la psychanalyse.",
    "Astérix": "Bande dessinée française humoristique suivant les aventures d'irréductibles Gaulois face aux Romains.",
    "Tintin": "Les aventures d'un jeune reporter belge et de son chien Milou, imaginées par Hergé.",
    "Lucky Luke": "BD de Morris et Goscinny où un cow-boy solitaire tire plus vite que son ombre.",
    "Les Schtroumpfs": "Créés par Peyo, ces petits lutins bleus vivent dans un village champignon.",
    "Gaston Lagaffe": "BD humoristique de Franquin, centrée sur un employé gaffeur d'un bureau.",
    "Spirou et Fantasio": "Les aventures de Spirou, journaliste, et son ami Fantasio dans des récits variés.",
    "Boule et Bill": "Histoires humoristiques d'un petit garçon et de son chien espiègle.",
    "Titeuf": "BD de Zep racontant avec humour la vie d'un garçon face à l'école et l'adolescence.",
    "Les Aventures de Blake et Mortimer": "BD de Jacobs mêlant science-fiction, aventure et mystère.",
    "Valérian et Laureline": "BD de science-fiction française qui a inspiré de nombreux films.",
    "Yakari": "BD franco-belge mettant en scène un petit Indien qui parle aux animaux.",
    "Marsupilami": "Créature imaginaire de Franquin, protagoniste de nombreuses aventures en forêt.",
    "Les Nombrils": "BD humoristique sur l'adolescence et les relations amicales et amoureuses.",
    "Garfield": "Comic strip américain humoristique centré sur un chat paresseux et sarcastique."
}

dict_celebrites = {
    "Marie Curie": "Pionnière de la radioactivité, première femme à recevoir un prix Nobel en physique et chimie.",
    "Nelson Mandela": "Leader sud-africain de la lutte contre l'apartheid, premier président noir d'Afrique du Sud.",
    "Frida Kahlo": "Peintre mexicaine reconnue pour ses autoportraits puissants et engagés.",
    "Léonard de Vinci": "Artiste et inventeur italien de la Renaissance, maître du \"Mona Lisa\" et du génie universel.",
    "Winston Churchill": "Premier ministre britannique pendant la Seconde Guerre mondiale, célèbre pour son leadership.",
    "Rosa Parks": "Icône du mouvement des droits civiques aux États-Unis pour son refus de céder sa place.",
    "Pablo Picasso": "Peintre et sculpteur espagnol, fondateur du cubisme et artiste influent du XXe siècle.",
    "Martin Luther King Jr.": "Pasteur et militant pour l'égalité raciale, célèbre pour son discours \"I Have a Dream\".",
    "Stephen Hawking": "Astrophysicien reconnu pour ses travaux sur les trous noirs et la cosmologie.",
    "Simone de Beauvoir": "Philosophe et écrivaine française, pionnière du féminisme moderne.",
    "Mahatma Gandhi": "Leader de l'indépendance indienne, adepte de la résistance non violente.",
    "Neil Armstrong": "Premier homme à poser le pied sur la Lune en 1969, astronaute américain emblématique.",
    "Jane Goodall": "Primatologue renommée pour ses études sur les chimpanzés en Afrique.",
    "Ada Lovelace": "Considérée comme la première programmeuse informatique, pionnière des mathématiques.",
    "Elon Musk": "Entrepreneur et innovateur, fondateur de Tesla, SpaceX et figure majeure de la technologie.",
    "Charles Darwin": "Naturaliste anglais, père de la théorie de l'évolution par sélection naturelle.",
    "Mother Teresa": "Religieuse catholique reconnue pour son engagement auprès des pauvres en Inde.",
    "Isaac Newton": "Mathématicien et physicien, inventeur du calcul infinitésimal et des lois du mouvement.",
    "Coco Chanel": "Créatrice de mode française, révolutionnaire dans l'industrie du vêtement féminin.",
    "Sigmund Freud": "Médecin autrichien, père de la psychanalyse et des théories de l'inconscient.",
    "Nikola Tesla": "Inventeur et ingénieur, pionnier de l'électricité et du courant alternatif.",
    "Florence Nightingale": "Fondatrice des soins infirmiers modernes, figure clé de la santé publique.",
    "Bill Gates": "Fondateur de Microsoft, philanthrope et acteur majeur du secteur informatique.",
    "Margaret Thatcher": "Première femme Premier ministre britannique, figure controversée du conservatisme.",
    "J.K. Rowling": "Auteure britannique célèbre pour la saga Harry Potter, best-sellers mondiaux.",
    "Mark Zuckerberg": "Co-fondateur de Facebook, influenceur majeur des réseaux sociaux.",
    "Angela Merkel": "Chancelière allemande, leader politique influente en Europe.",
    "Carl Sagan": "Astronome et vulgarisateur scientifique américain, célèbre pour la série \"Cosmos\".",
    "Malcom X": "Militant afro-américain pour les droits civiques et la justice sociale.",
    "Emmeline Pankhurst": "Pionnière britannique du droit de vote des femmes, leader du suffragisme.",
    "Carl Jung": "Psychiatre suisse, fondateur de la psychologie analytique.",
    "Greta Thunberg": "Jeune militante suédoise pour le climat, voix mondiale de la jeunesse engagée.",
    "Alexander Fleming": "Médecin écossais, découvreur de la pénicilline, révolution médicale majeure.",
    "James Watson": "Co-découvreur de la structure de l'ADN, prix Nobel de médecine.",
    "Rosalind Franklin": "Scientifique anglaise dont les travaux ont été essentiels à la découverte de l'ADN.",
    "Margaret Mead": "Anthropologue américaine, spécialiste des cultures et des sociétés.",
    "Neil deGrasse Tyson": "Astrophysicien et vulgarisateur scientifique américain reconnu.",
    "Charles Babbage": "Mathématicien britannique, inventeur du concept d'ordinateur mécanique.",
    "Jane Austen": "Romancière anglaise du XIXe siècle, célèbre pour ses portraits de la société.",
    "Virginia Woolf": "Écrivaine et figure du modernisme littéraire britannique.",
    "George Orwell": "Auteur britannique connu pour ses romans dystopiques comme \"1984\" et \"La Ferme des animaux\".",
    "Frédéric Chopin": "Compositeur et pianiste romantique polonais, maître du piano.",
    "Wolfgang Amadeus Mozart": "Compositeur autrichien du XVIIIe siècle, génie de la musique classique.",
    "Hypatie d'Alexandrie": "Philosophe et mathématicienne grecque de l'Antiquité.",
    "Galileo Galilei": "Astronome et physicien italien, père de la science moderne.",
    "Stephen King": "Écrivain américain célèbre pour ses romans d'horreur et de suspense.",
    "Agatha Christie": "Romancière britannique, reine du roman policier.",
    "Albert Einstein": "Physicien théoricien, auteur de la théorie de la relativité et icône scientifique du XXe siècle.",
    "Marie-Antoinette": "Reine de France, figure controversée de la Révolution française.",
    "Barack Obama": "44e président des États-Unis, premier président afro-américain.",
    "Oprah Winfrey": "Animatrice et productrice américaine, figure majeure des médias.",
    "Albert Camus": "Écrivain et philosophe français, prix Nobel de littérature.",
    "Salvador Dalí": "Peintre surréaliste espagnol, célèbre pour ses œuvres oniriques.",
    "Andy Warhol": "Artiste américain, pionnier du pop art.",
    "Che Guevara": "Révolutionnaire argentin, figure de la révolution cubaine.",
    "Fidel Castro": "Leader cubain, figure majeure du communisme au XXe siècle.",
    "Donald Trump": "45e président des États-Unis, homme d'affaires et personnalité médiatique.",
    "Joseph Staline": "Dirigeant de l'Union soviétique, acteur central de l'histoire du XXe siècle.",
    "Vladimir Poutine": "Président russe, acteur politique majeur de l'ère contemporaine.",
    "Cléopâtre": "Dernière reine d'Égypte, figure emblématique de l'Antiquité.",
    "Julius Caesar": "Chef militaire et homme politique romain, pivot de l'histoire romaine.",
    "Alexandre le Grand": "Conquérant macédonien, fondateur d'un immense empire antique.",
    "Aristote": "Philosophe grec de l'Antiquité, maître de nombreux domaines du savoir.",
    "Platon": "Philosophe grec, disciple de Socrate et maître d'Aristote.",
    "Socrate": "Philosophe grec, pionnier de la philosophie occidentale.",
    "Confucius": "Philosophe chinois, fondateur du confucianisme.",
    "Sun Tzu": "Stratège chinois, auteur de « L'Art de la guerre ».",
    "Akhenaton": "Pharaon égyptien, connu pour sa révolution religieuse.",
    "Ramsès II": "Pharaon égyptien, symbole de puissance et de longévité.",
    "Gengis Khan": "Fondateur de l'Empire mongol, grand conquérant de l'Histoire.",
    "Marco Polo": "Explorateur vénitien, célèbre pour ses récits de voyage en Asie.",
    "Christophe Colomb": "Explorateur génois, découvreur de l'Amérique pour l'Europe.",
    "Ferdinand Magellan": "Navigateur portugais, premier à initier un tour du monde.",
    "Amelia Earhart": "Aviatrice américaine, pionnière de l'aviation féminine.",
    "Bruce Lee": "Acteur et maître d'arts martiaux, icône mondiale.",
    "Jackie Chan": "Acteur et cascadeur chinois, star du cinéma d'action.",
    "Audrey Hepburn": "Actrice britannique, icône de mode et d'élégance.",
    "Marilyn Monroe": "Actrice américaine, légende et symbole glamour d'Hollywood.",
    "Charlie Chaplin": "Acteur et réalisateur britannique, figure du cinéma muet.",
    "Alfred Hitchcock": "Réalisateur britannique, maître du suspense.",
    "Steven Spielberg": "Réalisateur américain, pionnier du cinéma moderne.",
    "Quentin Tarantino": "Réalisateur américain, connu pour son style unique.",
    "Stan Lee": "Créateur de nombreux super-héros Marvel.",
    "George Lucas": "Créateur de la saga Star Wars.",
    "Thomas Hobbes": "Philosophe anglais, auteur du 'Léviathan', théoricien du contrat social.",
    "John Locke": "Philosophe anglais, père du libéralisme politique moderne.",
    "Jean-Jacques Rousseau": "Philosophe des Lumières, théoricien de l'égalité et du contrat social.",
    "Voltaire": "Philosophe français des Lumières, défenseur de la tolérance et de la liberté.",
    "Montesquieu": "Philosophe français, théoricien de la séparation des pouvoirs.",
    "Karl Marx": "Philosophe et économiste allemand, fondateur du marxisme.",
    "Friedrich Engels": "Philosophe et penseur politique, co-auteur du 'Manifeste du parti communiste'.",
    "Immanuel Kant": "Philosophe allemand, auteur de la 'Critique de la raison pure'.",
    "Friedrich Nietzsche": "Philosophe allemand, critique de la morale et du christianisme.",
    "Søren Kierkegaard": "Philosophe danois, considéré comme le père de l'existentialisme.",
    "René Descartes": "Philosophe et mathématicien français, auteur du célèbre 'Je pense donc je suis'.",
    "Blaise Pascal": "Mathématicien, physicien et philosophe français, inventeur de la machine à calculer.",
    "David Hume": "Philosophe écossais, figure de l'empirisme et du scepticisme.",
    "Michel Foucault": "Philosophe français du XXe siècle, critique des institutions et du pouvoir.",
    "Jean-Paul Sartre": "Philosophe existentialiste français, auteur de 'L'Être et le Néant'.",
    "Hannah Arendt": "Philosophe politique allemande, célèbre pour 'La banalité du mal'.",
    "Simone Weil": "Philosophe française engagée, auteur de réflexions sur la justice et la spiritualité.",
    "Baruch Spinoza": "Philosophe rationaliste néerlandais, auteur de l''Éthique'.",
    "Épicure": "Philosophe grec, fondateur de l'épicurisme, prônant le bonheur par la simplicité.",
    "Diogène de Sinope": "Philosophe cynique grec, connu pour son mode de vie austère.",
    "Auguste Comte": "Fondateur du positivisme, philosophe français du XIXe siècle.",
    "Claude Lévi-Strauss": "Anthropologue français, fondateur du structuralisme.",
    "Michel de Montaigne": "Philosophe français de la Renaissance, inventeur de l'essai moderne.",
    "Thucydide": "Historien grec antique, auteur de 'La Guerre du Péloponnèse'.",
    "Héraclite": "Philosophe grec présocratique, célèbre pour 'tout s'écoule'.",
    "Pythagore": "Mathématicien et philosophe grec, fondateur d'une école mystique et scientifique.",
    "Euclide": "Mathématicien grec, père de la géométrie classique.",
    "Archimède": "Scientifique grec antique, inventeur et grand mathématicien.",
    "Kepler": "Astronome allemand, connu pour ses lois du mouvement planétaire.",
    "Copernic": "Astronome polonais, fondateur de l'héliocentrisme.",
    "Max Planck": "Physicien allemand, fondateur de la théorie des quanta.",
    "Alan Turing": "Mathématicien britannique, pionnier de l'informatique et du décryptage de codes.",
    "John von Neumann": "Mathématicien hongrois-américain, fondateur de l'informatique moderne.",
    "Gregor Mendel": "Moine et scientifique autrichien, père de la génétique moderne.",
    "Louis Pasteur": "Scientifique français, inventeur de la vaccination et de la pasteurisation.",
    "Niels Bohr": "Physicien danois, pionnier de la mécanique quantique.",
    "Dmitri Mendeleïev": "Chimiste russe, créateur du tableau périodique des éléments.",
    "Max Weber": "Sociologue et économiste allemand, père de la sociologie moderne.",
    "Émile Durkheim": "Sociologue français, fondateur de la sociologie académique."
}

dict_jeux_videos = {
    "The Legend of Zelda": "Jeu d'aventure épique où le joueur incarne Link pour sauver le royaume d'Hyrule.",
    "Super Mario Bros": "Classique du jeu de plateforme où Mario doit sauver la princesse Peach du méchant Bowser.",
    "Minecraft": "Jeu de construction en monde ouvert permettant de créer et d'explorer des environnements infinis.",
    "Fortnite": "Jeu de battle royale célèbre pour ses constructions rapides et ses événements en direct.",
    "Call of Duty": "Jeu de tir à la première personne centré sur des missions militaires intenses.",
    "Grand Theft Auto V": "Jeu d'action en monde ouvert qui suit trois criminels dans la ville fictive de Los Santos.",
    "Among Us": "Jeu multijoueur de déduction sociale où les joueurs doivent trouver l'imposteur dans l'équipage.",
    "League of Legends": "Jeu de stratégie en équipe très populaire, où deux camps s'affrontent sur une carte.",
    "World of Warcraft": "Jeu de rôle en ligne massivement multijoueur dans un univers fantasy vaste.",
    "Overwatch": "Jeu de tir en équipe avec des héros aux capacités uniques.",
    "Red Dead Redemption 2": "Jeu d'aventure en western, centré sur la vie d'un hors-la-loi dans l'Amérique du XIXe siècle.",
    "The Witcher 3": "Jeu de rôle célèbre pour son scénario riche et son monde ouvert immersif.",
    "Cyberpunk 2077": "Jeu futuriste mêlant action et RPG dans une mégalopole dystopique.",
    "Halo": "Jeu de tir à la première personne se déroulant dans un univers de science-fiction.",
    "Doom": "Jeu de tir rapide et intense contre des hordes de démons.",
    "Assassin's Creed": "Série de jeux d'action et d'infiltration dans différentes périodes historiques.",
    "Animal Crossing": "Jeu de simulation sociale où le joueur vit dans un village avec des animaux anthropomorphes.",
    "Tetris": "Jeu de puzzle classique où il faut empiler des formes géométriques pour compléter des lignes.",
    "Final Fantasy VII": "Jeu de rôle emblématique avec une histoire captivante et un univers fantastique.",
    "God of War": "Jeu d'action-aventure centré sur le guerrier Kratos et la mythologie nordique.",
    "Apex Legends": "Jeu de battle royale en équipe avec des personnages dotés de pouvoirs spécifiques.",
    "Skyrim": "Jeu de rôle en monde ouvert dans un univers médiéval-fantastique riche.",
    "Counter-Strike": "Jeu de tir tactique en équipe très populaire dans l'e-sport.",
    "Pokémon (série)": "Jeux d'aventure et de capture de créatures fantastiques pour devenir maître Pokémon.",
    "Resident Evil": "Jeu d'horreur et de survie dans un monde envahi par des zombies.",
    "Metroid": "Jeu d'action et d'exploration mettant en scène la chasseuse de primes Samus Aran.",
    "Dark Souls": "Jeu d'action-RPG réputé pour sa difficulté et son univers sombre.",
    "The Sims": "Jeu de simulation de vie où le joueur contrôle la vie de personnages virtuels.",
    "Battlefield": "Jeu de tir à la première personne connu pour ses grandes batailles multijoueurs.",
    "Mario Kart": "Jeu de course fun avec les personnages de l'univers Mario.",
    "Rocket League": "Jeu mélangeant football et voitures dans des matchs rapides et dynamiques.",
    "Street Fighter": "Jeu de combat classique avec des personnages aux techniques variées.",
    "Mortal Kombat": "Jeu de combat célèbre pour sa violence et ses « fatalities ».",
    "Clash Royale": "Jeu de stratégie en temps réel avec des cartes et des combats rapides.",
    "Clash of Clans": "Jeu de stratégie où le joueur construit un village et défend son territoire.",
    "Brawl Stars": "Jeu de combat multijoueur avec différents modes et personnages.",
    "Splatoon": "Jeu de tir coloré où les joueurs s'affrontent en utilisant de l'encre.",
    "Diablo": "Jeu d'action-RPG dans un univers fantastique sombre.",
    "Candy Crush": "Jeu de puzzle très populaire où il faut aligner des bonbons colorés.",
    "FIFA": "Série de jeux de football réaliste très appréciée dans le monde entier.",
    "Just Cause": "Jeu d'action en monde ouvert connu pour ses explosions et son chaos.",
    "StarCraft": "Jeu de stratégie en temps réel se déroulant dans un univers de science-fiction.",
    "Fallout": "Jeu de rôle post-apocalyptique avec un vaste monde à explorer.",
    "Pac-Man": "Jeu d'arcade classique où le joueur doit manger toutes les pac-gommes sans se faire attraper.",
    "Metal Gear Solid": "Jeu d'infiltration avec une histoire complexe et des personnages profonds.",
    "Sonic the Hedgehog": "Jeu de plateforme rapide mettant en scène le hérisson bleu.",
    "Dead Space": "Jeu d'horreur de science-fiction avec une ambiance oppressante.",
    "Hollow Knight": "Jeu d'action-aventure en 2D dans un univers sombre et mystérieux.",
    "Animal Crossing: New Horizons": "Dernier opus de la série, offrant une expérience de vie sur une île déserte.",
    "Valorant": "Jeu de tir tactique en équipe avec des agents aux compétences uniques.",
    "Fire Emblem: Three Houses": "Jeu de stratégie au tour par tour avec une forte dimension narrative.",
    "Xenoblade Chronicles": "RPG japonais réputé pour son monde immense et son scénario profond.",
    "Genshin Impact": "RPG en monde ouvert gratuit, inspiré de Zelda, avec un système de gacha.",
    "Elden Ring": "Action-RPG de FromSoftware, en monde ouvert, célèbre pour sa difficulté.",
    "Sekiro: Shadows Die Twice": "Action-aventure exigeant, centré sur la précision et les combats de samouraï.",
    "Bloodborne": "Action-RPG sombre et gothique des créateurs de Dark Souls.",
    "Ghost of Tsushima": "Aventure en monde ouvert dans le Japon féodal, centrée sur un samouraï.",
    "Nioh": "Action-RPG inspiré du Japon médiéval, avec des combats intenses.",
    "For Honor": "Jeu de combat multijoueur mettant en scène chevaliers, samouraïs et vikings.",
    "Watch Dogs": "Jeu d'action où l'on pirate une ville intelligente pour accomplir des missions.",
    "The Division": "Jeu de tir tactique multijoueur dans un New York post-apocalyptique.",
    "Far Cry 3": "Jeu d'action-aventure en monde ouvert avec un antagoniste culte, Vaas.",
    "Far Cry 5": "Jeu en monde ouvert dans le Montana, avec une secte fanatique comme ennemie.",
    "Hitman 3": "Jeu d'infiltration où l'on incarne l'Agent 47, maître de la discrétion.",
    "Portal": "Jeu de puzzle unique basé sur la création de portails pour résoudre des énigmes.",
    "PUBG": "Jeu de battle royale réaliste et tactique très populaire.",
    "War Thunder": "Jeu multijoueur de simulation militaire avec avions, chars et navires.",
    "World of Tanks": "Jeu multijoueur en ligne où l'on pilote des chars d'assaut.",
    "World of Warships": "Simulation multijoueur de batailles navales.",
    "Civilization VI": "Jeu de stratégie où l'on construit un empire à travers les âges.",
    "Age of Empires II": "Stratégie en temps réel classique centrée sur les civilisations historiques.",
    "Football Manager": "Simulation réaliste de gestion d'équipe de football.",
    "NBA 2K": "Série de simulation de basketball réaliste.",
    "PES/efootball": "Ancien concurrent de FIFA dans les jeux de football.",
    "Tony Hawk's Pro Skater": "Jeu de skateboard culte des années 2000.",
    "Gran Turismo": "Simulation automobile culte sur PlayStation.",
    "Forza Horizon": "Jeu de course en monde ouvert avec des paysages variés.",
    "Need for Speed: Most Wanted": "Un des épisodes les plus populaires de la série de courses.",
    "Little Nightmares": "Jeu d'aventure horrifique avec une ambiance oppressante.",
    "Slither.io": "Jeu multijoueur en ligne où l'on contrôle un serpent qui grandit en mangeant des points lumineux.",
    "Agar.io": "Jeu multijoueur où l'on incarne une cellule qui absorbe les plus petites pour grossir.",
    "Crossy Road": "Jeu d'arcade où le joueur doit faire traverser routes et rivières à son personnage sans se faire écraser.",
    "Subway Surfers": "Jeu de course infinie où l'on fuit la police en surfant sur les rails de métro.",
    "Angry Birds": "Jeu de puzzle où l'on projette des oiseaux contre des structures pour détruire des cochons.",
    "Temple Run": "Course infinie où l'on échappe à des singes géants à travers des ruines.",
    "Candy Crush Saga": "Puzzle populaire où il faut aligner des bonbons colorés pour marquer des points.",
    "Fruit Ninja": "Jeu d'arcade où il faut trancher des fruits en un minimum de temps.",
    "Jetpack Joyride": "Course infinie où l'on contrôle un personnage équipé d'un jetpack.",
    "Flappy Bird": "Jeu culte où l'on doit faire voler un oiseau en évitant les tuyaux.",
    "2048": "Jeu de réflexion où il faut fusionner des tuiles pour atteindre le nombre 2048.",
    "Hill Climb Racing": "Jeu de conduite basé sur la physique avec des véhicules sur des terrains variés.",
    "Geometry Dash": "Jeu de plateforme musical basé sur des sauts précis et rapides.",
    "Plants vs Zombies": "Jeu de stratégie où l'on protège sa maison contre des vagues de zombies.",
    "Pokemon GO": "Jeu en réalité augmentée où l'on capture des Pokémon dans le monde réel.",
    "Hay Day": "Jeu de simulation agricole où l'on gère une ferme.",
    "My Talking Tom": "Jeu d'élevage interactif avec un chat qui répète ce qu'on dit.",
    "Asphalt 9: Legends": "Jeu de course spectaculaire avec des voitures de luxe.",
    "Score! Hero": "Jeu de football où l'on trace les passes et tirs pour marquer.",
    "Paper.io": "Jeu multijoueur où l'on conquiert un territoire avec une couleur.",
    "Color Switch": "Jeu d'adresse où il faut franchir des obstacles colorés avec une balle.",
    "Zombie Tsunami": "Course infinie où l'on incarne une horde de zombies dévorant les passants.",
    "Stack": "Jeu d'adresse où il faut empiler des blocs le plus haut possible.",
    "Boom Beach": "Jeu de stratégie militaire avec des batailles insulaires.",
    "Stumble Guys": "Clone mobile de Fall Guys où des joueurs s'affrontent dans des épreuves."
}

dict_jeux_sports = {
    "Échecs": "Jeu de stratégie à deux joueurs où chaque pièce a des déplacements spécifiques. L'objectif est de mettre le roi adverse en échec et mat.",
    "Monopoly": "Jeu de société où les joueurs achètent, vendent et échangent des propriétés pour ruiner leurs adversaires.",
    "Scrabble": "Jeu de lettres où les participants forment des mots sur une grille pour marquer un maximum de points.",
    "Uno": "Jeu de cartes coloré où le but est de se débarrasser de toutes ses cartes avant les autres joueurs.",
    "Cluedo": "Jeu d'enquête où les joueurs doivent résoudre un meurtre en découvrant le coupable, l'arme et le lieu.",
    "Dominos": "Jeu de tuiles où l'on doit associer les extrémités des pièces portant les mêmes chiffres.",
    "Shifumi (Pierre-Feuille-Ciseaux)": "Jeu de mains classique basé sur la confrontation rapide entre trois symboles.",
    "Jenga": "Jeu d'adresse où les joueurs retirent des blocs en bois d'une tour sans la faire tomber.",
    "Pictionary": "Jeu de dessin où l'on doit faire deviner un mot ou une expression à son équipe en le dessinant.",
    "Puissance 4": "Jeu de stratégie pour deux où l'objectif est d'aligner quatre jetons de sa couleur.",
    "Bataille Navale": "Jeu de stratégie à deux où l'on tente de couler la flotte ennemie en devinant la position de ses bateaux.",
    "Trivial Pursuit": "Jeu de questions-réponses où les joueurs testent leurs connaissances générales.",
    "Risk": "Jeu de stratégie militaire où les joueurs tentent de conquérir le monde.",
    "Dames": "Jeu de plateau où l'on saute par-dessus les pions adverses pour les éliminer.",
    "Jeu de l'Oie": "Jeu de parcours très simple basé sur les dés et l'avancée vers la case finale.",
    "Jeu des chaises musicales": "Jeu d'ambiance où les joueurs tournent autour de chaises et doivent s'asseoir dès que la musique s'arrête.",
    "Twister": "Jeu physique où l'on place les mains et pieds sur des cercles colorés en suivant les instructions données.",
    "Petits Chevaux": "Jeu de plateau familial où les pions doivent faire un tour complet pour arriver à leur maison.",
    "Jeu de mime": "Jeu d'expression corporelle où il faut faire deviner des mots sans parler.",
    "Ni oui ni non": "Jeu verbal où il faut éviter de prononcer les mots « oui » ou « non » le plus longtemps possible.",
    "Mikado": "Jeu d'adresse avec des baguettes en bois à retirer sans faire bouger les autres.",
    "Action ou Vérité": "Jeu de groupe où les participants choisissent entre répondre à une question ou relever un défi.",
    "Loup-Garou de Thiercelieux": "Jeu de rôle en groupe où les joueurs incarnent villageois ou loups-garous, et doivent se démasquer.",
    "Dobble": "Jeu d'observation et de rapidité où il faut identifier le symbole commun entre deux cartes.",
    "Jungle Speed": "Jeu de réflexes où il faut attraper un totem quand deux cartes identiques apparaissent.",
    "7 Wonders": "Jeu de stratégie et de civilisation où chaque joueur développe sa cité antique.",
    "Perudo": "Jeu de dés et de bluff originaire d'Amérique du Sud.",
    "Codenames": "Jeu d'associations d'idées où les joueurs doivent retrouver des mots à l'aide d'indices.",
    "Blanc Manger Coco": "Jeu d'humour noir et d'associations absurdes, réservé à un public averti.",
    "Poule Renard Vipère": "Jeu de course collectif inspiré du pierre-feuille-ciseaux.",
    "Memory": "Jeu de cartes basé sur la mémoire, où il faut retrouver des paires.",
    "Jeu du dictionnaire": "Jeu de groupe où chacun invente des définitions farfelues à un mot inconnu.",
    "Cartes Contre l'Humanité": "Jeu de société satirique et irrévérencieux basé sur des associations de phrases choquantes.",
    "Pétanque": "Jeu traditionnel français où les joueurs lancent des boules le plus près possible du cochonnet.",
    "Course en sac": "Jeu d'extérieur où les participants doivent sauter dans un sac jusqu'à la ligne d'arrivée.",
    "Tir à la corde": "Jeu d'équipe où deux groupes s'affrontent en tirant une corde de chaque côté.",
    "Cache-cache": "Jeu classique où un joueur compte pendant que les autres vont se cacher.",
    "1, 2, 3 soleil": "Jeu de mouvement où les enfants doivent avancer sans se faire repérer quand le meneur se retourne.",
    "Jeu des billes": "Un jeu classique d'enfants où les participants tentent de gagner les billes des autres en les touchant ou les éjectant d'un cercle tracé au sol.",
    "Rubik's Cube": "Un casse-tête tridimensionnel emblématique où il faut réaligner les couleurs sur chaque face en manipulant les différentes parties du cube.",
    "Backgammon": "Jeu de plateau très ancien où l'on déplace des pions selon le lancer de dés.",
    "Mahjong": "Jeu chinois de tuiles basé sur l'observation, la mémoire et la stratégie.",
    "Go": "Jeu de plateau asiatique où l'objectif est de contrôler le plus grand territoire.",
    "Shogi": "Variante japonaise des échecs où les pièces capturées peuvent être rejouées.",
    "Belote": "Jeu de cartes traditionnel français joué en équipes de deux.",
    "Tarot": "Jeu de cartes français avec un atout spécial appelé l'Excuse.",
    "Bridge": "Jeu de cartes complexe joué à quatre, basé sur des enchères et des plis.",
    "Poker": "Jeu de cartes de mise et de stratégie très populaire dans le monde entier.",
    "Blackjack": "Jeu de cartes où l'objectif est de s'approcher le plus possible de 21.",
    "Solitaire": "Casse-tête classique à un joueur avec des cartes à ordonner.",
    "Chat perché": "Jeu de poursuite où les enfants doivent grimper sur des zones de sécurité.",
    "Marelle": "Jeu traditionnel où l'on saute sur des cases tracées au sol.",
    "Colin-maillard": "Jeu d'aveugle où une personne aux yeux bandés doit attraper les autres.",
    "Chamboule-tout": "Jeu de kermesse où l'on lance des balles pour faire tomber des boîtes empilées.",
    "Morpion (Tic Tac Toe)": "Jeu papier simple où l'on aligne trois symboles identiques.",
    "Pendu": "Jeu de lettres où l'on devine un mot en proposant des lettres.",
    "Baccalauréat (Petit Bac)": "Jeu de mots où l'on remplit des catégories avec une lettre donnée.",
    "Jeu du téléphone arabe": "Jeu de communication où un message se déforme en passant de joueur en joueur.",
    "Les Aventuriers du Rail": "Jeu de stratégie où l'on construit des lignes de chemin de fer.",
    "Colons de Catane": "Jeu de plateau où l'on colonise une île en échangeant des ressources.",
    "Taboo": "Jeu de mots où il faut faire deviner sans prononcer des termes interdits.",
    "Qui est-ce ?": "Jeu de devinettes où l'on identifie un personnage en posant des questions.",
    "Mastermind": "Jeu de logique où l'on doit retrouver une combinaison secrète de couleurs.",
    "Mölkky": "Jeu d'extérieur finlandais avec des quilles numérotées.",
    "Triominos": "Variante des dominos avec des tuiles triangulaires.",
    "Kapla": "Jeu de construction avec des planchettes en bois.",
    "Jeu du Kem's": "Jeu de cartes en équipe basé sur la communication discrète.",
    "President (jeu)": "Jeu de cartes où l'on cherche à se débarrasser de toutes ses cartes.",
    "Jeu de la bataille": "Jeu de cartes simple où le plus fort l'emporte.",
    "Donjons et Dragons": "Jeu de rôle mythique basé sur la narration et l'imagination.",
    "Beer Pong": "Jeu d'adresse où il faut lancer une balle dans des gobelets remplis de boisson.",
    "Jeu du post-it": "Jeu d'ambiance où chacun colle un nom sur son front et doit le deviner.",
    "Ballon prisonnier": "Jeu collectif où l'on élimine les adversaires en les touchant avec un ballon.",
    "Tic Tac Boum": "Jeu de mots où il faut trouver des réponses avant que la bombe n'explose.",
    "Football": "Sport collectif où deux équipes de 11 joueurs s'affrontent pour marquer des buts avec un ballon rond.",
    "Rugby": "Sport collectif de contact où l'objectif est d'aplatir le ballon dans l'en-but adverse.",
    "Basket-ball": "Sport collectif où deux équipes de 5 joueurs marquent des points en lançant le ballon dans un panier.",
    "Handball": "Sport collectif où l'on marque en lançant le ballon à la main dans le but adverse.",
    "Volley-ball": "Sport collectif où l'on fait passer le ballon au-dessus d'un filet pour le faire tomber dans le camp adverse.",
    "Tennis": "Sport de raquette où deux joueurs (ou deux équipes de deux) s'affrontent en frappant une balle au-dessus d'un filet.",
    "Badminton": "Sport de raquette où l'on se renvoie un volant au-dessus d'un filet.",
    "Squash": "Sport de raquette qui se joue contre un mur dans une salle fermée.",
    "Ping-pong (Tennis de table)": "Sport de raquette joué sur une petite table avec un filet central.",
    "Golf": "Sport individuel où l'on doit envoyer une balle dans un trou avec le moins de coups possible.",
    "Athlétisme": "Ensemble de disciplines comprenant courses, sauts et lancers.",
    "Natation": "Sport aquatique consistant à parcourir une distance en nageant dans une piscine ou en eau libre.",
    "Plongeon": "Sport aquatique où l'on effectue des sauts acrobatiques depuis un tremplin ou une plateforme.",
    "Water-polo": "Sport collectif aquatique où deux équipes tentent de marquer des buts dans l'eau.",
    "Surf": "Sport nautique consistant à glisser sur les vagues debout sur une planche.",
    "Voile": "Sport nautique où l'on navigue en utilisant la force du vent.",
    "Aviron": "Sport nautique où des rameurs propulsent un bateau avec des rames.",
    "Canoë-kayak": "Sport nautique où l'on pagaye pour avancer dans une embarcation légère.",
    "Ski alpin": "Sport de glisse consistant à descendre des pistes enneigées en ski.",
    "Snowboard": "Sport de glisse sur neige avec une planche unique fixée aux pieds.",
    "Patinage artistique": "Sport de glace mêlant technique et esthétique sur patins à glace.",
    "Hockey sur glace": "Sport collectif rapide joué sur glace avec une crosse et un palet.",
    "Hockey sur gazon": "Sport collectif joué sur terrain avec une balle et des crosses.",
    "Boxe": "Sport de combat où deux adversaires s'affrontent avec les poings.",
    "Judo": "Art martial japonais basé sur des projections et immobilisations.",
    "Karaté": "Art martial japonais fondé sur les coups de poings et de pieds.",
    "Taekwondo": "Art martial coréen caractérisé par ses coups de pied spectaculaires.",
    "Lutte": "Sport de combat consistant à immobiliser ou faire tomber son adversaire.",
    "Escrime": "Sport de combat avec une arme blanche (fleuret, épée ou sabre).",
    "Cyclisme sur route": "Sport où les cyclistes parcourent de longues distances sur routes.",
    "VTT": "Variante du cyclisme pratiquée sur des chemins accidentés.",
    "BMX": "Discipline de vélo consistant en courses ou figures acrobatiques.",
    "Triathlon": "Épreuve combinant natation, cyclisme et course à pied.",
    "Marathon": "Course de fond de 42,195 km.",
    "Escalade": "Sport où l'on grimpe sur des parois naturelles ou artificielles.",
    "Alpinisme": "Pratique de l'ascension des montagnes.",
    "Gymnastique artistique": "Sport acrobatique exécuté sur agrès (barres, poutre, sol…).",
    "Gymnastique rythmique": "Sport alliant danse et manipulation d'engins (cerceau, ruban, ballon…).",
    "Parkour": "Discipline urbaine où l'on franchit des obstacles avec agilité.",
    "Équitation": "Sport consistant à monter et diriger un cheval.",
    "Esport": "Compétition de jeux vidéo considérée comme discipline sportive.",
    "Capoeira": "Art martial brésilien mêlant danse, musique et acrobaties.",
    "Cricket": "Sport collectif anglais joué avec une batte et une balle.",
    "Baseball": "Sport collectif américain joué avec une batte, une balle et des bases.",
    "Polo": "Sport équestre où les joueurs frappent une balle avec un maillet depuis leur cheval."
}

dict_marques = {
    "Apple": "Entreprise américaine célèbre pour ses produits technologiques comme l'iPhone, l'iPad et le MacBook.",
    "Google": "Leader mondial des moteurs de recherche et développeur du système Android et de nombreux services en ligne.",
    "Microsoft": "Multinationale spécialisée dans les logiciels, notamment le système d'exploitation Windows et la suite Office.",
    "Amazon": "Plateforme de commerce en ligne géante proposant aussi des services cloud avec AWS.",
    "Coca-Cola": "Marque emblématique de boisson gazeuse, l'un des symboles de la culture américaine.",
    "Nike": "Marque de vêtements et chaussures de sport célèbre pour son logo « Swoosh » et son slogan « Just Do It ».",
    "Adidas": "Entreprise allemande spécialisée dans les articles de sport, concurrent direct de Nike.",
    "Samsung": "Conglomérat sud-coréen produisant notamment des smartphones, téléviseurs et électroménagers.",
    "Toyota": "Constructeur automobile japonais connu pour ses voitures fiables et sa technologie hybride.",
    "McDonald's": "Chaîne de restauration rapide américaine célèbre pour ses hamburgers et son logo doré.",
    "BMW": "Marque allemande de voitures de luxe et de motos, connue pour son design et ses performances.",
    "Mercedes-Benz": "Constructeur automobile de prestige allemand, symbole d'élégance et d'innovation.",
    "L'Oréal": "Groupe français leader dans le secteur de la beauté et des cosmétiques.",
    "Pepsi": "Concurrent direct de Coca-Cola, célèbre pour ses sodas et ses campagnes marketing percutantes.",
    "Netflix": "Plateforme de streaming mondialement utilisée pour ses films, séries et productions originales.",
    "Facebook": "Réseau social majeur fondé par Mark Zuckerberg, aujourd'hui intégré dans Meta Platforms.",
    "Instagram": "Application de partage de photos et de vidéos devenue centrale dans les réseaux sociaux.",
    "Tesla": "Entreprise pionnière dans les voitures électriques, fondée par Elon Musk.",
    "Sony": "Géant japonais de l'électronique, du divertissement et des jeux vidéo (PlayStation).",
    "PlayStation": "Console de jeux vidéo développée par Sony, célèbre depuis les années 90.",
    "Nintendo": "Entreprise japonaise emblématique du jeu vidéo avec des licences comme Mario et Zelda.",
    "IKEA": "Entreprise suédoise spécialisée dans les meubles en kit et le design accessible.",
    "Zara": "Chaîne espagnole de prêt-à-porter connue pour son renouvellement rapide des collections.",
    "H&M": "Marque de vêtements suédoise à prix abordable présente dans le monde entier.",
    "Starbucks": "Chaîne américaine de cafés célèbre pour ses boissons personnalisables et son ambiance cosy.",
    "LEGO": "Marque danoise de jouets connue pour ses briques de construction modulaires.",
    "Airbnb": "Plateforme en ligne permettant la location de logements entre particuliers.",
    "Uber": "Service de transport via application, ayant bouleversé l'industrie du taxi.",
    "Visa": "Entreprise américaine de services financiers, surtout connue pour ses cartes de paiement.",
    "Mastercard": "Concurrent direct de Visa, acteur majeur dans les paiements électroniques mondiaux.",
    "Shell": "Multinationale énergétique active dans le pétrole, le gaz et les énergies renouvelables.",
    "Nikon": "Entreprise japonaise spécialisée dans les appareils photo et les optiques.",
    "Rolex": "Marque suisse de montres de luxe synonyme de prestige et de précision.",
    "Chanel": "Maison de mode française emblématique, fondée par Coco Chanel.",
    "Gucci": "Marque italienne de luxe connue pour ses vêtements, accessoires et sacs à main.",
    "Louis Vuitton": "Symbole du luxe français, célèbre pour ses sacs et bagages monogrammés.",
    "Cartier": "Maison de joaillerie et d'horlogerie française réputée dans le monde entier.",
    "Puma": "Marque allemande de sport et de mode, connue pour ses équipements et collaborations.",
    "Red Bull": "Marque autrichienne de boisson énergisante connue pour son marketing extrême.",
    "Nescafé": "Marque phare de café instantané appartenant au groupe Nestlé.",
    "Nestlé": "Multinationale suisse de l'agroalimentaire, active dans les produits laitiers, céréales et nutrition infantile.",
    "Lacoste": "Marque française de vêtements reconnaissable à son logo crocodile.",
    "Dior": "Maison de haute couture française, connue pour ses parfums, ses vêtements et accessoires de luxe.",
    "Balenciaga": "Marque de mode de luxe connue pour ses designs audacieux et ses défilés spectaculaires.",
    "Unilever": "Groupe anglo-néerlandais de produits de consommation, propriétaire de nombreuses marques d'hygiène et d'alimentation.",
    "Danone": "Groupe français spécialisé dans les produits laitiers, les eaux et la nutrition médicale.",
    "Heineken": "Brasserie néerlandaise célèbre pour sa bière distribuée dans le monde entier.",
    "Evian": "Marque d'eau minérale française issue des Alpes, synonyme de pureté.",
    "Volvo": "Constructeur automobile suédois connu pour la sécurité de ses véhicules.",
    "KFC": "Chaîne de restauration rapide spécialisée dans le poulet frit, fondée aux États-Unis.",
    "TikTok": "Application chinoise de partage de vidéos courtes, devenue virale chez les jeunes.",
    "Spotify": "Plateforme suédoise de streaming musical leader dans le monde.",
    "Deezer": "Service français de streaming musical avec un large catalogue.",
    "Twitter (X)": "Réseau social de microblogging renommé X en 2023.",
    "Snapchat": "Application de partage de photos et vidéos éphémères.",
    "WhatsApp": "Application de messagerie instantanée chiffrée appartenant à Meta.",
    "Huawei": "Géant technologique chinois dans les smartphones et équipements réseaux.",
    "Xiaomi": "Fabricant chinois de smartphones et objets connectés à prix abordable.",
    "Oppo": "Marque chinoise de smartphones en forte croissance mondiale.",
    "OnePlus": "Constructeur chinois de smartphones haut de gamme compétitifs.",
    "Lenovo": "Multinationale chinoise de l'informatique, propriétaire d'IBM PC.",
    "Dell": "Entreprise américaine spécialisée dans les ordinateurs et serveurs.",
    "HP": "Constructeur américain de PC, imprimantes et solutions IT.",
    "Asus": "Fabricant taïwanais d'ordinateurs, cartes mères et smartphones.",
    "Acer": "Marque taïwanaise spécialisée dans les ordinateurs et accessoires.",
    "Razer": "Marque américaine spécialisée dans les accessoires de gaming.",
    "Alienware": "Filiale gaming haut de gamme de Dell.",
    "Logitech": "Entreprise suisse spécialisée dans les périphériques informatiques.",
    "Corsair": "Marque américaine de matériel informatique et gaming.",
    "Intel": "Leader mondial des processeurs informatiques.",
    "AMD": "Concurrent direct d'Intel spécialisé dans processeurs et cartes graphiques.",
    "NVIDIA": "Entreprise américaine leader des cartes graphiques.",
    "Epic Games": "Studio américain de jeux vidéo, créateur de Fortnite et Unreal Engine.",
    "Activision Blizzard": "Éditeur de jeux vidéo comme Call of Duty et World of Warcraft.",
    "Electronic Arts (EA)": "Éditeur de jeux vidéo célèbre pour FIFA et The Sims.",
    "Ubisoft": "Éditeur français de jeux vidéo (Assassin's Creed, Just Dance).",
    "Capcom": "Éditeur japonais connu pour Street Fighter et Resident Evil.",
    "Konami": "Éditeur japonais créateur de Metal Gear et PES.",
    "SEGA": "Entreprise japonaise historique du jeu vidéo, Sonic en mascotte.",
    "Rockstar Games": "Studio américain créateur de GTA et Red Dead Redemption.",
    "Warner Bros.": "Multinationale américaine du divertissement et cinéma.",
    "Paramount": "Studio hollywoodien historique de cinéma.",
    "Universal Pictures": "Studio de cinéma et production musicale mondial.",
    "20th Century Studios": "Célèbre studio de cinéma racheté par Disney.",
    "Pixar": "Studio d'animation 3D appartenant à Disney.",
    "Marvel": "Maison d'édition de comics et studio de films à succès.",
    "DC Comics": "Concurrent de Marvel, créateur de Batman et Superman.",
    "HBO": "Chaîne américaine de séries et films, productrice de Game of Thrones.",
    "CNN": "Chaîne d'information en continu américaine.",
    "BBC": "Service public audiovisuel britannique reconnu mondialement.",
    "TF1": "Chaîne de télévision française historique.",
    "Canal+": "Chaîne française spécialisée dans le cinéma et le sport.",
    "M6": "Chaîne française privée généraliste.",
    "BNP Paribas": "Grande banque française présente mondialement.",
    "Société Générale": "Banque française internationale.",
    "Crédit Agricole": "Banque coopérative française leader en Europe.",
    "HSBC": "Banque britannique présente dans le monde entier.",
    "Barclays": "Grande banque anglaise.",
    "Goldman Sachs": "Banque d'investissement américaine.",
    "JP Morgan Chase": "Groupe bancaire et financier américain.",
    "American Express": "Marque américaine de cartes bancaires premium.",
    "PayPal": "Plateforme de paiements en ligne.",
    "Air France": "Compagnie aérienne nationale française.",
    "Lufthansa": "Compagnie aérienne allemande.",
    "British Airways": "Compagnie aérienne nationale du Royaume-Uni.",
    "Emirates": "Compagnie aérienne de Dubaï.",
    "Qatar Airways": "Compagnie aérienne du Qatar.",
    "Boeing": "Constructeur aéronautique américain.",
    "Airbus": "Constructeur aéronautique européen.",
    "Ferrari": "Marque italienne de voitures de luxe et de course.",
    "Lamborghini": "Constructeur italien de voitures sportives de prestige.",
    "Maserati": "Marque italienne de voitures haut de gamme.",
    "Bugatti": "Constructeur français de voitures de luxe et hypercars.",
    "Rolls-Royce": "Marque britannique de voitures de luxe.",
    "Aston Martin": "Constructeur britannique de voitures de prestige.",
    "Jaguar": "Marque britannique de voitures élégantes et sportives.",
    "Land Rover": "Marque britannique de 4x4 et SUV robustes.",
    "Jeep": "Marque américaine de véhicules tout-terrain.",
    "Ford": "Constructeur automobile américain historique.",
    "Chevrolet": "Marque américaine de voitures du groupe General Motors.",
    "Cadillac": "Constructeur américain de voitures de luxe.",
    "Hyundai": "Constructeur automobile sud-coréen.",
    "Kia": "Marque automobile sud-coréenne.",
    "Fiat": "Marque automobile italienne.",
    "Renault": "Constructeur automobile français.",
    "Citroën": "Marque française automobile au design innovant.",
    "DS Automobiles": "Marque française premium dérivée de Citroën.",
    "Opel": "Marque automobile allemande.",
    "Skoda": "Constructeur automobile tchèque.",
    "Seat": "Marque automobile espagnole.",
    "Peugeot": "Marque française historique d'automobiles."
}

dict_personnages_fiction = {
    "Harry Potter": "Jeune sorcier célèbre pour avoir survécu à une attaque de Voldemort et pour ses aventures à l'école de Poudlard.",
    "Sherlock Holmes": "Détective britannique brillant, connu pour son esprit d'analyse et ses enquêtes complexes.",
    "Frodon Sacquet": "Hobbit courageux chargé de détruire l'Anneau Unique dans la saga Le Seigneur des Anneaux.",
    "Luke Skywalker": "Héros de la saga Star Wars, Jedi qui lutte contre l'Empire galactique.",
    "Batman": "Super-héros de Gotham City, justicier masqué utilisant sa richesse et ses compétences pour combattre le crime.",
    "Hermione Granger": "Amie de Harry Potter, sorcière brillante et passionnée par les livres.",
    "Iron Man": "Tony Stark, inventeur milliardaire devenu super-héros grâce à une armure high-tech.",
    "Wonder Woman": "Princesse amazone dotée de pouvoirs surhumains, combattante pour la justice et la paix.",
    "Frozone": "Super-héros du film Les Indestructibles, capable de créer de la glace et de la neige.",
    "Gandalf": "Mage puissant et sage du Seigneur des Anneaux, guide des héros dans leur quête.",
    "Simba": "Lionceau qui devient roi dans Le Roi Lion, symbolisant la maturité et la responsabilité.",
    "Katniss Everdeen": "Héroïne de Hunger Games, symbole de rébellion et de survie.",
    "Peter Pan": "Garçon qui ne grandit jamais, vivant au Pays Imaginaire avec les Enfants Perdus.",
    "Elsa": "Reine des Neiges dans le film Disney, capable de contrôler la glace et la neige.",
    "Deadpool": "Anti-héros sarcastique de Marvel, doté d'un pouvoir de régénération rapide.",
    "Jack Sparrow": "Capitaine pirate excentrique de la saga Pirates des Caraïbes.",
    "Bilbo Sacquet": "Hobbit aventurier du Hobbit, protagoniste d'une quête pour récupérer un trésor.",
    "Darth Vader": "Antagoniste emblématique de Star Wars, ancien Jedi devenu seigneur Sith.",
    "Alice": "Jeune fille curieuse qui voyage dans un monde fantastique dans Alice au Pays des Merveilles.",
    "SpongeBob Carréponge": "Personnage principal de la série animée, habitant de Bikini Bottom toujours optimiste.",
    "Thor": "Dieu du tonnerre dans la mythologie nordique et héros de Marvel avec son marteau Mjolnir.",
    "Cendrillon": "Héroïne de conte de fées, célèbre pour sa transformation magique et son prince charmant.",
    "Shrek": "Ogre au grand cœur, héros de la série de films d'animation du même nom.",
    "Voldemort": "Méchant puissant dans Harry Potter, obsédé par la conquête de la magie noire.",
    "Spider-Man": "Adolescent doté de pouvoirs d'araignée, combattant le crime à New York.",
    "Rick Sanchez": "Scientifique excentrique et génial de la série Rick et Morty, voyageant entre les dimensions.",
    "Morty Smith": "Adolescent naïf et souvent nerveux, compagnon des aventures de Rick.",
    "Lara Croft": "Exploratrice et archéologue célèbre des jeux vidéo Tomb Raider, connue pour son courage et ses compétences au combat.",
    "Jon Snow": "Personnage clé de Game of Thrones, connu pour son sens de l'honneur et sa lutte contre les forces du mal.",
    "Arya Stark": "Jeune guerrière agile de Game of Thrones, en quête de justice et de vengeance.",
    "Walter White": "Professeur de chimie devenu baron de la drogue dans Breaking Bad.",
    "Daryl Dixon": "Chasseur et survivant dur à cuire dans The Walking Dead.",
    "Megaman": "Robot héros des jeux vidéo, combattant les menaces technologiques.",
    "Link": "Héros légendaire de la série The Legend of Zelda, toujours prêt à sauver le royaume d'Hyrule.",
    "Michelangelo": "Tortue ninja joyeuse et talentueuse en arts martiaux, spécialiste des nunchakus.",
    "Donatello": "Tortue ninja inventeur et expert en technologie.",
    "Raphaël": "Tortue ninja au tempérament rebelle, maître des sais.",
    "Leonardo": "Chef des Tortues Ninja, expert en katanas et en stratégie.",
    "Aladdin": "Jeune héros des contes arabes, qui découvre une lampe magique et un génie.",
    "Belle": "Personnage du conte La Belle et la Bête, connue pour son amour de la lecture et sa gentillesse.",
    "Hercule": "Demi-dieu de la mythologie grecque, célèbre pour sa force surhumaine.",
    "Mickey Mouse": "Icône Disney, souris anthropomorphe joyeuse et optimiste.",
    "Donald Duck": "Canard grincheux mais attachant, personnage classique de Disney.",
    "Goofy": "Chien maladroit et sympathique, ami de Mickey.",
    "Bart Simpson": "Garçon espiègle de la série Les Simpson.",
    "Lisa Simpson": "Sœur intelligente et engagée de Bart, adepte du saxophone.",
    "Homer Simpson": "Père de famille souvent comique et maladroit.",
    "Sailor Moon": "Guerrière magique et héroïne du manga du même nom.",
    "Naruto Uzumaki": "Jeune ninja au grand cœur, déterminé à devenir Hokage.",
    "Goku": "Héros de Dragon Ball, guerrier Saiyan connu pour sa force et ses combats épiques.",
    "Ash Ketchum": "Dresseur de Pokémon passionné et déterminé à devenir Maître Pokémon.",
    "Pikachu": "Pokémon emblématique, compagnon fidèle d'Ash.",
    "Dora l'Exploratrice": "Jeune fille curieuse qui part à l'aventure pour apprendre aux enfants.",
    "Scooby-Doo": "Chien détective peureux mais loyal, résolvant des mystères avec ses amis.",
    "Fred Flintstone": "Personnage principal de la série Les Pierrafeu, vivant à l'époque préhistorique.",
    "Barney Rubble": "Meilleur ami de Fred Flintstone.",
    "Winnie l'Ourson": "Petit ours gourmand et naïf, héros de nombreux contes pour enfants.",
    "Timon": "Suricate drôle et énergique du Roi Lion.",
    "Pumbaa": "Phacochère jovial et ami de Timon.",
    "Donkey": "Ane bavard et fidèle compagnon de Shrek.",
    "Megara": "Héroïne du film Hercule, connue pour son humour et son courage.",
    "C-3PO": "Robot protocolaire de Star Wars, toujours inquiet mais loyal.",
    "R2-D2": "Petit droïde astromech de Star Wars, débrouillard et courageux.",
    "Obi-Wan Kenobi": "Jedi sage et mentor dans Star Wars, formateur d'Anakin et Luke Skywalker.",
    "Yoda": "Maître Jedi emblématique, connu pour sa sagesse et son langage inversé.",
    "Han Solo": "Contrebandier devenu héros dans Star Wars, pilote du Faucon Millenium.",
    "Chewbacca": "Wookie fidèle compagnon de Han Solo, connu pour sa force et ses grognements.",
    "Harley Quinn": "Complice et amoureuse du Joker, devenue anti-héroïne charismatique.",
    "Poison Ivy": "Méchant de l'univers DC, femme-plante utilisant la nature comme arme.",
    "Green Lantern": "Super-héros de DC utilisant un anneau de pouvoir basé sur la volonté.",
    "Flash": "Super-héros ultra-rapide de DC Comics, connu pour voyager dans le temps.",
    "Aquaman": "Roi d'Atlantis, héros de DC capable de contrôler les océans.",
    "Doctor Strange": "Sorcier suprême de Marvel, gardien des dimensions mystiques.",
    "Captain America": "Héros de Marvel, soldat courageux doté d'un bouclier indestructible.",
    "Hulk": "Super-héros de Marvel, scientifique transformé en géant vert par la colère.",
    "Black Widow": "Espionne et super-héroïne de Marvel, experte en arts martiaux.",
    "Hawkeye": "Archer surdoué de Marvel, membre des Avengers.",
    "Wolverine": "Mutant de Marvel avec des griffes en adamantium et une régénération rapide.",
    "Professor X": "Fondateur des X-Men, télépathe puissant prônant la paix.",
    "Magneto": "Antagoniste des X-Men, mutant capable de contrôler le métal.",
    "Mystique": "Mutante métamorphe des X-Men, changeant d'apparence à volonté.",
    "Thanos": "Super-vilain de Marvel, obsédé par les Pierres d'Infinité.",
    "Legolas": "Archer elfe agile et fidèle compagnon de la Communauté de l'Anneau.",
    "Aragorn": "Ranger et héritier des rois de Gondor, héros du Seigneur des Anneaux.",
    "Sauron": "Seigneur maléfique du Seigneur des Anneaux, créateur de l'Anneau Unique.",
    "Sam Gamegie": "Fidèle compagnon de Frodon dans Le Seigneur des Anneaux.",
    "Gollum": "Créature obsédée par l'Anneau, déchirée entre le bien et le mal.",
    "Dracula": "Comte vampire emblématique créé par Bram Stoker.",
    "Frankenstein": "Créature née des expériences du docteur Victor Frankenstein.",
    "Le Petit Prince": "Jeune voyageur imaginaire de l'œuvre de Saint-Exupéry.",
    "Obélix": "Ami d'Astérix, tombé dans la potion magique et doté d'une grande force.",
    "Panoramix": "Druide gaulois préparant la potion magique.",
    "Tintin": "Jeune reporter curieux et intrépide, accompagné de son chien Milou.",
    "Capitaine Haddock": "Ami de Tintin, marin colérique mais courageux.",
    "Milou": "Chien fidèle et intelligent accompagnant Tintin.",
    "Les Dalton": "Fratrie de bandits maladroits opposée à Lucky Luke.",
    "Spirou": "Héros de bande dessinée belge, aventurier optimiste.",
    "Fantasio": "Compagnon fidèle de Spirou, souvent maladroit.",
    "Marsupilami": "Animal imaginaire à longue queue, originaire de Palombie.",
    "Corto Maltese": "Marin aventurier créé par Hugo Pratt.",
    "Goldorak": "Robot géant piloté par Actarus pour protéger la Terre.",
    "Vegeta": "Prince Saiyan, rival puis allié de Goku.",
    "Bulma": "Scientifique brillante et amie fidèle de Goku.",
    "Krillin": "Meilleur ami de Goku et combattant courageux.",
    "Cell": "Antagoniste de Dragon Ball, bio-androïde redoutable.",
    "Majin Boo": "Ennemi puissant de Dragon Ball, capable de se régénérer.",
    "Light Yagami": "Protagoniste de Death Note, étudiant manipulant un carnet mortel.",
    "L": "Détective génial traquant Light dans Death Note.",
    "Edward Elric": "Alchimiste talentueux de Fullmetal Alchemist.",
    "Sasuke Uchiwa": "Ninja rival de Naruto, animé par la vengeance.",
    "Kakashi Hatake": "Maître ninja de Naruto, célèbre pour son Sharingan.",
    "Itachi Uchiwa": "Frère de Sasuke, ninja complexe au destin tragique.",
    "Gaara": "Ninja manipulant le sable, marqué par une enfance difficile.",
    "Eren Jäger": "Héros de L'Attaque des Titans, capable de se transformer en Titan.",
    "Mikasa Ackerman": "Combattante redoutable, protectrice d'Eren.",
    "Levi Ackerman": "Caporal légendaire dans L'Attaque des Titans, expert en combat.",
    "Armin Arlert": "Stratège brillant et ami d'Eren et Mikasa.",
    "Grover Underwood": "Satyre protecteur et ami de Percy Jackson.",
    "Hercule Poirot": "Détective belge créé par Agatha Christie.",
    "Miss Marple": "Vieille dame détective rusée dans les romans de Christie.",
    "James Bond": "Agent secret britannique 007, expert en gadgets et espionnage.",
    "Jason Bourne": "Agent amnésique poursuivi par la CIA.",
    "Ralph": "Personnage de jeu vidéo dans Les Mondes de Ralph.",
    "Vanellope": "Amie espiègle de Ralph, conductrice de kart.",
    "Sonic": "Hérisson bleu supersonique des jeux vidéo.",
    "Tails": "Renard à deux queues, ami et compagnon de Sonic.",
    "Knuckles": "Échidné puissant, gardien de l'émeraude mère.",
    "Shadow": "Hérisson noir mystérieux de l'univers Sonic.",
    "Kratos": "Demi-dieu guerrier de God of War."
}

dict_objets_du_quotidien = {
    "Brosse à dents": "Outil utilisé pour nettoyer les dents et maintenir une bonne hygiène bucco-dentaire.",
    "Téléphone portable": "Appareil de communication mobile permettant d'appeler, envoyer des messages et accéder à Internet.",
    "Clé": "Objet métallique servant à ouvrir ou fermer une serrure.",
    "Montre": "Accessoire porté au poignet pour indiquer l'heure.",
    "Sac à dos": "Sac porté sur le dos pour transporter des affaires personnelles ou scolaires.",
    "Stylo": "Instrument utilisé pour écrire ou dessiner à l'encre.",
    "Couteau": "Outil tranchant utilisé en cuisine ou pour couper divers matériaux.",
    "Chaise": "Meuble conçu pour s'asseoir, généralement avec un dossier.",
    "Lampe": "Appareil produisant de la lumière artificielle.",
    "Ordinateur portable": "Appareil informatique compact et transportable utilisé pour travailler ou se divertir.",
    "Bouteille d'eau": "Récipient utilisé pour stocker et transporter de l'eau potable.",
    "Lunettes": "Accessoire porté sur le visage pour corriger la vue ou protéger les yeux du soleil.",
    "Casque audio": "Écouteurs couvrant les oreilles pour écouter de la musique ou des sons de manière privée.",
    "Table": "Meuble avec un plateau horizontal servant à poser des objets ou manger.",
    "Chaussures": "Accessoires portés aux pieds pour protéger et faciliter la marche.",
    "Cadenas": "Dispositif de verrouillage portable pour sécuriser des objets ou des portes.",
    "Cintre": "Objet utilisé pour suspendre des vêtements dans une armoire.",
    "Télécommande": "Appareil permettant de contrôler à distance une télévision ou un autre équipement électronique.",
    "Chargeur": "Accessoire servant à recharger les batteries des appareils électroniques.",
    "Portefeuille": "Petit objet utilisé pour ranger de l'argent, des cartes et des papiers d'identité.",
    "Clé USB": "Petit périphérique de stockage portable utilisé pour transférer des fichiers informatiques.",
    "Parapluie": "Accessoire pliable utilisé pour se protéger de la pluie.",
    "Casserole": "Ustensile de cuisine utilisé pour faire cuire des aliments sur le feu.",
    "Serviette": "Pièce de tissu utilisée pour s'essuyer après la douche ou le lavage.",
    "Sac à main": "Petit sac porté à la main ou à l'épaule pour transporter des objets personnels.",
    "Brosse à cheveux": "Outil utilisé pour démêler et coiffer les cheveux.",
    "Agenda": "Carnet ou application servant à noter des rendez-vous et des tâches.",
    "Mug": "Tasse utilisée pour boire des boissons chaudes comme le café ou le thé.",
    "Oreiller": "Coussin utilisé pour soutenir la tête pendant le sommeil.",
    "Porte-monnaie": "Petit contenant pour ranger de la monnaie et parfois des cartes.",
    "Crayon": "Instrument d'écriture ou de dessin à base de graphite.",
    "Ciseaux": "Outil tranchant utilisé pour couper du papier, du tissu ou d'autres matériaux.",
    "Bougie": "Objet servant à produire de la lumière par combustion d'une mèche dans de la cire.",
    "Clavier": "Périphérique informatique permettant de taper du texte et de donner des commandes.",
    "Télévision": "Appareil électronique qui diffuse des programmes audiovisuels.",
    "Gourde": "Récipient réutilisable pour transporter de l'eau ou d'autres boissons.",
    "Trousse": "Petit sac utilisé pour ranger des fournitures comme des stylos, crayons et gommes.",
    "Chaise roulante": "Fauteuil équipé de roues destiné à faciliter la mobilité des personnes à mobilité réduite.",
    "Balance": "Appareil permettant de mesurer le poids d'un objet ou d'une personne.",
    "Fer à repasser": "Appareil électrique utilisé pour lisser les vêtements en les chauffant.",
    "Fourchette": "Ustensile de table à dents utilisé pour piquer et porter la nourriture à la bouche.",
    "Couvercle": "Objet servant à couvrir une casserole ou un récipient pour conserver la chaleur.",
    "Clé de voiture": "Télécommande ou clé mécanique utilisée pour démarrer et ouvrir un véhicule.",
    "Tapis": "Revêtement posé au sol pour décorer ou protéger le sol.",
    "Poubelle": "Récipient où l'on jette les déchets ménagers.",
    "Rideau": "Tissu suspendu à une fenêtre pour la décoration ou pour bloquer la lumière.",
    "Thermomètre": "Instrument qui mesure la température corporelle ou ambiante.",
    "Ventilateur": "Appareil électrique qui génère un flux d'air pour rafraîchir une pièce.",
    "Marteau": "Outil manuel utilisé pour enfoncer des clous ou casser des objets.",
    "Lampe de poche": "Petit appareil portatif produisant une lumière directionnelle alimentée par des piles.",
    "Bouilloire électrique": "Appareil pour chauffer rapidement de l'eau.",
    "Horloge": "Dispositif qui indique l'heure dans une pièce.",
    "Cafetière": "Appareil utilisé pour préparer du café.",
    "Presse-agrumes": "Ustensile servant à extraire le jus des agrumes.",
    "Porte-clés": "Accessoire servant à regrouper plusieurs clés.",
    "Brosse WC": "Outil utilisé pour nettoyer les toilettes.",
    "Panier à linge": "Grand contenant utilisé pour ranger le linge sale.",
    "Boîte à outils": "Coffret contenant des outils divers pour bricoler.",
    "Rideau de douche": "Tissu ou plastique qui empêche l'eau de s'échapper de la douche.",
    "Mouchoir": "Petit morceau de tissu utilisé pour se moucher ou s'essuyer.",
    "Éponge": "Accessoire absorbant utilisé pour nettoyer les surfaces.",
    "Coussin": "Petit oreiller décoratif souvent placé sur un canapé ou un lit.",
    "Aspirateur": "Appareil électroménager servant à nettoyer le sol et enlever la poussière.",
    "Torchon": "Morceau de tissu utilisé pour essuyer la vaisselle ou les surfaces.",
    "Planche à découper": "Support utilisé en cuisine pour couper les aliments.",
    "Balai": "Outil ménager servant à balayer le sol.",
    "Tapis de bain": "Petit tapis absorbant placé devant la douche ou la baignoire.",
    "Savon": "Produit utilisé pour se laver les mains ou le corps.",
    "Gel douche": "Produit liquide pour la toilette quotidienne.",
    "Peigne": "Accessoire utilisé pour coiffer et démêler les cheveux.",
    "Couverture": "Pièce de tissu épaisse pour se réchauffer dans un lit ou sur un canapé.",
    "Plaid": "Couverture légère souvent utilisée pour se couvrir en regardant la télévision.",
    "Table de chevet": "Petit meuble placé près du lit pour poser une lampe ou des objets.",
    "Placard": "Meuble ou espace de rangement fermé par des portes.",
    "Étagère": "Plan horizontal fixé au mur ou dans un meuble pour poser des objets.",
    "Chaise pliante": "Chaise pratique qui peut se replier pour être rangée facilement.",
    "Tabouret": "Petit siège sans dossier, souvent utilisé en cuisine ou au bar.",
    "Porte-manteau": "Accessoire permettant de suspendre des vêtements ou des manteaux.",
    "Serpillière": "Tissu absorbant utilisé pour nettoyer le sol avec de l'eau.",
    "Seau": "Récipient utilisé pour transporter de l'eau ou d'autres liquides.",
    "Évier": "Bassin avec robinet installé en cuisine ou dans la salle de bain.",
    "Poêle": "Ustensile de cuisine plat servant à faire frire ou cuire des aliments.",
    "Fouet": "Ustensile de cuisine utilisé pour battre ou mélanger les préparations.",
    "Spatule": "Outil plat servant à retourner ou mélanger des aliments en cuisine.",
    "Loupe": "Petit instrument optique qui agrandit la vision des objets.",
    "Carnet": "Petit cahier utilisé pour prendre des notes.",
    "Bloc-notes": "Ensemble de feuilles attachées pour écrire ou dessiner.",
    "Post-it": "Petits papiers autocollants pour noter des rappels.",
    "Gomme": "Objet servant à effacer les traces de crayon.",
    "Agrafeuse": "Petit appareil utilisé pour assembler des feuilles de papier.",
    "Trombones": "Accessoires métalliques pour maintenir plusieurs feuilles ensemble.",
    "Ruban adhésif": "Bande collante utilisée pour fixer ou réparer.",
    "Règle": "Instrument permettant de mesurer ou tracer des lignes droites.",
    "Cartable": "Sac rigide ou souple utilisé pour transporter des affaires scolaires.",
    "Valise": "Grand bagage utilisé pour transporter ses affaires lors d'un voyage.",
    "Glacière": "Récipient isolant qui conserve les aliments et boissons au frais.",
    "Louche": "Ustensile de cuisine à long manche, utilisé pour servir les soupes.",
    "Passoire": "Ustensile percé servant à égoutter les aliments.",
    "Mixeur": "Appareil électrique qui mélange ou réduit les aliments en purée.",
    "Grille-pain": "Appareil servant à griller des tranches de pain.",
    "Micro-ondes": "Appareil de cuisson rapide utilisant des ondes électromagnétiques.",
    "Four": "Appareil électroménager utilisé pour cuire des plats.",
    "Congélateur": "Appareil servant à congeler et conserver les aliments longtemps.",
    "Réfrigérateur": "Appareil électroménager permettant de garder les aliments au frais.",
    "Tablier": "Vêtement porté en cuisine pour protéger ses habits.",
    "Miroir": "Surface réfléchissante permettant de se voir.",
    "Coton-tige": "Petit bâtonnet utilisé pour l'hygiène des oreilles et le maquillage.",
    "Rasoir": "Outil utilisé pour se raser la barbe ou les poils.",
    "Mousse à raser": "Produit utilisé pour faciliter le rasage.",
    "Nappe": "Tissu utilisé pour recouvrir et protéger une table.",
    "Calculatrice": "Appareil électronique permettant d'effectuer des calculs.",
    "Imprimante": "Appareil qui imprime du texte ou des images sur papier.",
    "Scanner": "Appareil servant à numériser des documents.",
    "Cartouche d'encre": "Élément d'une imprimante contenant de l'encre.",
    "Surligneurs": "Stylos colorés utilisés pour mettre du texte en évidence.",
    "Tablette": "Petit appareil tactile utilisé pour lire, naviguer ou travailler.",
    "Casque de vélo": "Accessoire de sécurité pour protéger la tête à vélo.",
    "Gants": "Accessoires pour protéger ou réchauffer les mains.",
    "Écharpe": "Accessoire porté autour du cou pour se protéger du froid.",
    "Chapeau": "Accessoire porté sur la tête pour se protéger ou s'habiller.",
    "Bonnet": "Couvre-chef en laine pour protéger du froid.",
    "Ceinture": "Accessoire servant à maintenir un pantalon.",
    "Collier": "Bijou porté autour du cou.",
    "Bracelet": "Bijou porté au poignet.",
    "Bague": "Bijou circulaire porté au doigt.",
    "Boucles d'oreilles": "Bijoux portés aux oreilles.",
    "Pantoufles": "Chaussures confortables portées à la maison.",
    "Sandales": "Chaussures ouvertes utilisées en été.",
    "Bottes": "Chaussures montantes pour protéger les pieds.",
    "Escabeau": "Petit escalier portatif servant à atteindre des hauteurs.",
    "Tondeuse à cheveux": "Appareil électrique servant à couper les cheveux.",
    "Sèche-cheveux": "Appareil servant à sécher les cheveux avec de l'air chaud.",
    "Lisseur": "Appareil utilisé pour lisser les cheveux.",
    "Ventouse": "Accessoire utilisé pour déboucher un évier ou des toilettes.",
    "Balai-brosse": "Balai muni de poils durs pour frotter le sol.",
    "Chiffon": "Morceau de tissu utilisé pour nettoyer la poussière.",
    "Lingettes": "Petits tissus humides utilisés pour nettoyer rapidement.",
    "Thermos": "Récipient isolant qui conserve une boisson chaude ou froide.",
    "Ouvre-boîte": "Ustensile servant à ouvrir les boîtes de conserve.",
    "Décapsuleur": "Ustensile servant à ouvrir les bouteilles à capsule.",
    "Tire-bouchon": "Ustensile utilisé pour déboucher les bouteilles de vin.",
    "Récipient hermétique": "Boîte alimentaire qui se ferme hermétiquement.",
    "Coffre-fort": "Boîte solide utilisée pour protéger des objets de valeur.",
    "Boîte aux lettres": "Contenant servant à recevoir le courrier."
}

dict_dessins_animes = {
    "Les Simpsons": "Série humoristique animée centrée sur une famille américaine aux aventures satiriques dans la ville fictive de Springfield.",
    "Bob l'éponge": "Cartoon délirant suivant une éponge de mer qui vit dans un ananas au fond de l'océan avec ses amis marins.",
    "Tom et Jerry": "Classique du cartoon américain mettant en scène une éternelle course-poursuite entre un chat et une souris.",
    "Les Tortues Ninja": "Dessins animés mettant en scène quatre tortues mutantes adeptes d'arts martiaux qui combattent le crime à New York.",
    "Pokémon": "Série animée japonaise suivant un jeune dresseur nommé Sacha et ses aventures pour capturer des créatures appelées Pokémon.",
    "Avatar : Le dernier maître de l'air": "Dessins animés américano-asiatiques sur une épopée de fantasy où un jeune garçon doit maîtriser les quatre éléments pour restaurer l'équilibre du monde.",
    "Scooby-Doo": "Cartoon emblématique où un groupe d'adolescents et leur chien peureux résolvent des mystères apparemment surnaturels.",
    "Les Razmoket": "Dessins animés racontant le monde à travers le regard de bébés curieux et aventuriers.",
    "South Park": "Série animée satirique aux graphismes simples abordant avec humour noir des sujets controversés à travers des enfants d'une petite ville.",
    "Les Schtroumpfs": "Dessins animés franco-belges mettant en scène des petits lutins bleus vivant en harmonie dans une forêt magique.",
    "Miraculous": "Dessins animés français modernes où deux adolescents se transforment en super-héros pour protéger Paris.",
    "Code Lyoko": "Série animée franco-japonaise où des adolescents combattent un virus informatique dans un monde virtuel.",
    "La Panthère Rose": "Cartoon muet iconique connu pour l'élégance silencieuse et les gags de sa célèbre panthère rose.",
    "Teen Titans": "Dessins animés de super-héros suivant une équipe d'adolescents dotés de pouvoirs qui luttent contre le mal.",
    "Les Supers Nanas": "Cartoon explosif mettant en scène trois fillettes créées en laboratoire qui sauvent leur ville avec leurs super-pouvoirs.",
    "Dora l'exploratrice": "Série éducative d'animation destinée aux jeunes enfants, où une fillette bilingue part à l'aventure avec l'aide des spectateurs.",
    "Les Aventures de Tintin": "Dessins animés adaptés de la célèbre BD, où un jeune reporter globe-trotter résout des énigmes internationales.",
    "Les Minions": "Film d'animation humoristique mettant en scène des petites créatures jaunes servant les plus grands méchants de l'histoire.",
    "Mickey Mouse": "Dessins animés classiques mettant en scène la célèbre souris emblématique de l'univers Disney.",
    "La Reine des Neiges": "Film d'animation Disney adapté d'un conte, centré sur deux sœurs et les pouvoirs de glace de l'aînée.",
    "Alvin et les Chipmunks": "Série d'animation mettant en scène trois petits écureuils chanteurs au tempérament bien différent.",
    "Inspecteur Gadget": "Dessins animés humoristiques autour d'un détective maladroit équipé de gadgets farfelus.",
    "Adventure Time": "Série animée loufoque où un garçon et son chien magique explorent un monde post-apocalyptique fantastique.",
    "Garfield": "Cartoon centré sur un chat paresseux, sarcastique et gourmand qui mène une vie tranquille.",
    "Beyblade": "Série animée japonaise où des adolescents s'affrontent dans des combats de toupies magiques.",
    "Les Lapins Crétins": "Série dérivée de jeux vidéo avec des créatures animées au comportement absurde et chaotique.",
    "Yakari": "Dessins animés suivant un petit garçon sioux capable de parler aux animaux dans un environnement naturel.",
    "Les Bisounours": "Dessins animés aux couleurs pastel où des créatures pleines d'amour propagent des messages de gentillesse et de bonheur.",
    "Samurai Jack": "Série animée de style japonais où un samouraï est propulsé dans le futur pour combattre un démon maléfique.",
    "Les Animaniacs": "Cartoon délirant de la Warner mettant en scène des personnages incontrôlables et parodiques.",
    "L'Âge de glace": "Série de films d'animation humoristique avec un groupe d'animaux préhistoriques confrontés aux bouleversements du climat.",
    "Bleach": "Animé de combat surnaturel dans lequel un adolescent devient un shinigami pour affronter des esprits maléfiques.",
    "Dragon Ball Z": "Animé culte d'action où Goku et ses compagnons protègent l'univers contre des menaces puissantes.",
    "Naruto": "Animé narratif suivant un jeune ninja en quête de reconnaissance et de paix.",
    "One Piece": "Animé d'aventure où des pirates extravagants sillonnent les mers à la recherche d'un trésor légendaire.",
    "L'Attaque des Titans": "Animé sombre de science-fiction où l'humanité lutte contre des créatures géantes dévoreuses d'hommes.",
    "My Hero Academia": "Animé se déroulant dans un monde où la majorité des humains possède un pouvoir, et où un jeune garçon sans don rêve de devenir un héros.",
    "Death Note": "Thriller psychologique animé dans lequel un lycéen découvre un carnet mortel permettant de tuer n'importe qui.",
    "Fullmetal Alchemist": "Animé dramatique où deux frères alchimistes bravent les lois de la nature pour retrouver leur corps.",
    "Tokyo Ghoul": "Animé d'horreur sur un étudiant devenu mi-goule, coincé entre le monde des humains et celui des monstres.",
    "One Punch Man": "Parodie animée de super-héros où un homme peut vaincre tout ennemi en un seul coup, mais s'ennuie profondément.",
    "Fairy Tail": "Animé fantastique centré sur une guilde de mages accomplissant des quêtes dans un monde magique.",
    "Demon Slayer": "Animé prenant place dans un Japon féodal alternatif, où un jeune garçon combat des démons pour sauver sa sœur.",
    "Hunter x Hunter": "Meilleur animé de tous les temps, à voir de toute urgence.",
    "Evangelion": "Animé de science-fiction où des adolescents pilotent des robots géants pour défendre la Terre contre des créatures mystérieuses.",
    "Yu-Gi-Oh!": "Animé basé sur un jeu de cartes magique où les duels décident du sort du monde.",
    "Saint Seiya (Les Chevaliers du Zodiaque)": "Animé mythologique où de jeunes guerriers défendent Athéna avec des armures sacrées.",
    "Black Clover": "Animé magique mettant en scène un jeune garçon sans pouvoirs rêvant de devenir le roi mage.",
    "Gintama": "Comédie animée dans un Japon anachronique où samouraïs et extraterrestres coexistent dans un chaos hilarant.",
    "Toradora!": "Animé romantique explorant la relation entre deux lycéens aux tempéraments opposés.",
    "Code Geass": "Animé stratégique où un jeune homme doté d'un pouvoir absolu cherche à renverser un empire tyrannique.",
    "Your Lie in April": "Animé musical et dramatique où un jeune pianiste retrouve la passion grâce à une violoniste excentrique.",
    "Haikyuu!!": "Animé sportif vibrant suivant une équipe de volley-ball lycéenne déterminée à gravir les sommets.",
    "Mon voisin Totoro": "Film d'animation poétique du studio Ghibli mettant en scène des esprits forestiers bienveillants.",
    "Le Voyage de Chihiro": "Chef-d'œuvre du film d'animation japonais où une jeune fille traverse un monde",
    "Princess Mononoke": "Film d'animation épique mêlant nature, guerre et spiritualité, centré sur le conflit entre humains et esprits.",
    "Le Château ambulant": "Conte animé où une jeune fille maudite rencontre un sorcier dans un château magique qui se déplace.",
    "Babar": "Série animée racontant les aventures d'un éléphant roi et de sa famille.",
    "Ben 10": "Un garçon découvre un appareil lui permettant de se transformer en différents extraterrestres.",
    "Digimon": "Des enfants sont transportés dans un monde numérique où ils se lient avec des créatures digitales.",
    "Foster's Home for Imaginary Friends": "Un orphelinat pour amis imaginaires abandonnés, rempli de situations comiques.",
    "Garfield et ses amis": "Cartoon du chat paresseux et de son quotidien avec Jon et Odie.",
    "Jackie Chan Adventures": "Jackie Chan combat des créatures magiques tout en résolvant des mystères.",
    "Looney Tunes": "Classiques du cartoon américain avec Bugs Bunny, Daffy Duck et d'autres personnages cultes.",
    "Maya l'abeille": "Les aventures d'une petite abeille curieuse et espiègle.",
    "Peppa Pig": "Une série animée pour jeunes enfants centrée sur les aventures d'une petite cochonne et sa famille.",
    "Phineas et Ferb": "Deux frères inventifs vivent des aventures farfelues pendant leurs vacances d'été.",
    "Sonic le Hérisson": "Cartoon basé sur le célèbre jeu vidéo avec Sonic affrontant le maléfique Dr. Robotnik.",
    "Star Wars: The Clone Wars": "Animé explorant la guerre des clones entre Jedi et Sith dans l'univers Star Wars.",
    "Teenage Mutant Ninja Turtles": "Nouvelle version des aventures des tortues ninja combattant le crime.",
    "The Powerpuff Girls (2016)": "Reboot moderne des aventures des Supers Nanas sauvant la ville de Townsville.",
    "Totally Spies!": "Trois adolescentes travaillent comme espionnes secrètes tout en gérant leur vie d'adolescente.",
    "Zig & Sharko": "Une hyène et un requin se livrent à des batailles comiques autour d'une sirène.",
    "Inazuma Eleven": "Animé sportif où une équipe de football de collège affronte des adversaires incroyables grâce à des techniques spéciales.",
    "Captain Tsubasa": "Classique du football animé suivant Tsubasa et ses matchs épiques pour devenir le meilleur joueur du monde.",
    "Les Mystérieuses Cités d'Or": "Aventures de trois enfants à la recherche de cités légendaires en Amérique du Sud au XVIe siècle.",
    "Il était une fois… l'Homme": "Série éducative racontant l'histoire de l'humanité de la préhistoire à nos jours.",
    "Il était une fois… la Vie": "Série pédagogique expliquant le fonctionnement du corps humain à travers des personnages personnifiant des cellules et organes.",
    "Oggy et les Cafards": "Cartoon comique où un chat bleu doit gérer trois cafards farceurs qui détruisent sa vie quotidienne.",
    "Titeuf": "Les aventures humoristiques d'un jeune garçon confronté aux petits et grands problèmes de l'enfance.",
    "Les Zinzins de l'Espace": "Quatre extraterrestres comiques échouent sur Terre et tentent de s'adapter à la vie humaine.",
    "Petit Ours Brun": "Série éducative et tendre sur les aventures quotidiennes d'un petit ourson et de sa famille.",
    "Corneil et Bernie": "Un chien intelligent et son maître maladroit vivent des situations absurdes et hilarantes.",
    "Calimero": "Petit poussin noir malchanceux confronté à des situations comiques dans son quotidien.",
    "Barbapapa": "Une famille de créatures capables de se transformer et de résoudre des problèmes avec créativité.",
    "Le Roi Lion": "Chef-d'œuvre de Disney racontant l'histoire de Simba, un lion destiné à devenir roi.",
    "Toy Story": "Premier film Pixar, suivant les aventures de jouets qui prennent vie quand les humains ne regardent pas.",
    "Le Monde de Nemo": "Un poisson clown traverse l'océan pour retrouver son fils capturé par un plongeur.",
    "Les Indestructibles": "Famille de super-héros tentant de mener une vie normale tout en sauvant le monde.",
    "Monstres et Cie": "Deux monstres travaillant dans une usine de cris découvrent l'importance du rire.",
    "Ratatouille": "Un rat passionné de cuisine rêve de devenir chef dans un grand restaurant parisien.",
    "Wall-E": "Petit robot chargé de nettoyer la Terre déserte découvre l'amour et l'avenir de l'humanité.",
    "Vice-Versa": "Voyage dans l'esprit d'une jeune fille à travers ses émotions personnifiées.",
    "Là-Haut": "Vieil homme part à l'aventure en accrochant des ballons à sa maison, accompagné d'un jeune scout.",
    "Zootopie": "Une lapine policière et un renard escroc enquêtent dans une ville peuplée d'animaux anthropomorphes.",
    "Dragons": "Un jeune viking se lie d'amitié avec un dragon qu'il devait chasser.",
    "Kung Fu Panda": "Un panda maladroit devient maître du kung-fu et sauve la vallée avec ses amis.",
    "Madagascar": "Des animaux du zoo de New York se retrouvent perdus dans la jungle de Madagascar.",
    "Les 101 Dalmatiens": "Un couple de chiens lutte contre la méchante Cruella qui veut leur fourrure.",
    "La Petite Sirène": "Une princesse sirène rêve de vivre sur la terre et tombe amoureuse d'un humain.",
    "Aladdin": "Un jeune voleur découvre une lampe magique et affronte le terrible vizir Jafar.",
    "Cendrillon": "Une jeune fille maltraitée par sa belle-famille voit sa vie transformée par une fée.",
    "Blanche-Neige et les Sept Nains": "Premier long-métrage Disney, racontant l'histoire d'une princesse aidée par sept nains.",
    "Bambi": "Film poétique suivant la vie d'un jeune faon confronté aux beautés et cruautés de la nature.",
    "Mulan": "Une jeune femme chinoise prend la place de son père à l'armée pour défendre son pays.",
    "Tarzan": "Un homme élevé par des singes découvre ses origines et rencontre l'amour avec Jane.",
    "Hercule": "Le fils de Zeus doit prouver qu'il est un véritable héros pour retrouver sa place parmi les dieux.",
    "Frère des Ours": "Un jeune homme transformé en ours apprend la valeur de la fraternité et de la nature.",
    "Pocahontas": "Film Disney (1995) inspiré de l'histoire de la rencontre entre Amérindiens et colons.",
    "Lilo et Stitch": "Film Disney (2002) racontant l'amitié entre une petite fille et une créature extraterrestre.",
    "Toy Story 3": "Troisième volet de la saga (2010), salué comme un chef-d'œuvre.",
    "Shrek 2": "Suite (2004), encore plus déjantée, centrée sur Fiona et sa famille.",
    "Les Croods": "Film DreamWorks (2013) sur une famille préhistorique en quête d'un nouveau foyer.",
    "Moi, moche et méchant": "Film Illumination (2010) avec Gru et les Minions.",
    "Comme des bêtes": "Film Illumination (2016) sur la vie secrète des animaux domestiques.",
    "L'Âge de glace 2": "Suite (2006) centrée sur la fonte des glaces.",
    "Rio": "Film Blue Sky (2011) sur un perroquet apprivoisé parti au Brésil.",
    "Epic": "Film Blue Sky (2013) sur une bataille secrète dans la forêt.",
    "Ernest et Célestine": "Film franco-belge (2012) sur l'amitié entre une souris et un ours.",
    "Kirikou et la sorcière": "Film français (1998) inspiré des contes africains.",
    "Le Petit Prince": "Adaptation animée (2015) du célèbre roman de Saint-Exupéry.",
    "Le Tombeau des lucioles": "Film Ghibli (1988) sur deux enfants pendant la guerre."
}

dict_chansons = {
    "Bohemian Rhapsody - Queen": "Rock opéra emblématique des années 70, cette chanson mélange plusieurs styles et explore les tourments d'un homme hanté par ses actes.",
    "Imagine - John Lennon": "Ballade pop pacifiste devenue hymne universel pour la paix, où Lennon imagine un monde sans frontières ni possessions.",
    "Ne me quitte pas - Jacques Brel": "Chanson française poignante et théâtrale sur la supplication amoureuse, devenue un classique de la chanson francophone.",
    "Like a Rolling Stone - Bob Dylan": "Titre rock-folk majeur des années 60, racontant la chute d'une femme autrefois privilégiée, perdue dans un monde nouveau.",
    "Someone Like You - Adele": "Ballade pop mélancolique portée par la voix puissante d'Adele, sur l'acceptation douloureuse d'un amour perdu.",
    "La vie en rose - Édith Piaf": "Chanson française romantique devenue mythique, où Piaf décrit le bonheur d'aimer avec un regard plein d'espoir.",
    "Billie Jean - Michael Jackson": "Hit pop-funk des années 80, racontant l'histoire d'une fan obsessionnelle qui prétend que son enfant est celui de la star.",
    "Smells Like Teen Spirit - Nirvana": "Hymne grunge des années 90, reflet du mal-être adolescent et symbole de la contre-culture alternative.",
    "Hallelujah - Leonard Cohen": "Chanson spirituelle et poétique mêlant amour, foi et douleur, reprise de nombreuses fois à travers les décennies.",
    "Je te promets - Johnny Hallyday": "Ballade rock française sur l'engagement amoureux, portée par la voix profonde de Johnny.",
    "Hello - Lionel Richie": "Ballade soul-romantique des années 80, dans laquelle un homme cherche désespérément à retrouver la femme qu'il aime.",
    "L'hymne à l'amour - Édith Piaf": "Déclaration passionnée sur l'amour absolu, chantée avec intensité par Piaf après la mort de son amant Marcel Cerdan.",
    "Creep - Radiohead": "Titre alternatif rock sur l'auto-dépréciation et le sentiment d'exclusion, devenu culte auprès des esprits marginaux.",
    "Formidable - Stromae": "Chanson pop francophone qui dépeint avec ironie et émotion la détresse d'un homme ivre abandonné par sa compagne.",
    "Thriller - Michael Jackson": "Tube pop-funk aux accents disco et horrifiques, célèbre pour son clip vidéo inspiré des films de zombies.",
    "Let It Be - The Beatles": "Chanson pop-rock apaisante évoquant le lâcher-prise et l'acceptation, inspirée d'un rêve de Paul McCartney.",
    "Je vole - Louane": "Reprise d'une chanson de Michel Sardou, racontant avec émotion le départ d'une adolescente quittant le foyer familial.",
    "Shake It Off - Taylor Swift": "Titre pop entraînant et libérateur sur le fait d'ignorer les critiques et d'assumer qui l'on est.",
    "L'amour existe encore - Céline Dion": "Chanson pop francophone aux accents lyriques sur l'espérance de l'amour malgré les épreuves du monde.",
    "Shape of You - Ed Sheeran": "Chanson pop aux sonorités tropicales, racontant une rencontre amoureuse dans un bar et une passion naissante.",
    "Tous les mêmes - Stromae": "Titre électro-pop ironique où un homme adopte le point de vue d'une femme dénonçant les stéréotypes masculins.",
    "Lose Yourself - Eminem": "Rap motivant et introspectif sur le dépassement de soi, devenu un hymne de persévérance.",
    "Perfect - Ed Sheeran": "Ballade romantique douce où l'artiste évoque un amour sincère et idéal, accompagné d'arrangements acoustiques.",
    "Despacito - Luis Fonsi ft. Daddy Yankee": "Succès mondial reggaeton-pop, aux paroles sensuelles et au rythme latino irrésistible.",
    "J'ai demandé à la lune - Indochine": "Chanson pop-rock mélancolique aux paroles symboliques, exprimant l'incompréhension face à l'indifférence.",
    "Take on Me - a-ha": "Tube pop norvégien emblématique des années 80, célèbre pour sa mélodie accrocheuse et son clip en rotoscopie.",
    "Believer - Imagine Dragons": "Chanson rock énergique sur la transformation de la souffrance en force, portée par un rythme percutant.",
    "La Camisa Negra - Juanes": "Chanson latino-pop colombienne au ton joyeux mais au texte parlant d'un chagrin d'amour profond.",
    "Zombie - The Cranberries": "Titre rock engagé sur les conséquences des conflits armés, particulièrement en Irlande du Nord.",
    "Dernière danse - Indila": "Chanson pop française à la fois mélancolique et entraînante, exprimant la douleur d'un rejet.",
    "On verra - Nekfeu": "Rap français léger et positif, évoquant la liberté, la jeunesse et le refus de se prendre trop au sérieux.",
    "Hotel California - Eagles": "Ballade rock mythique dénonçant les pièges de la société matérialiste, au son planant des années 70.",
    "Je t'aimais, je t'aime et je t'aimerai - Francis Cabrel": "Chanson d'amour intemporelle à la guitare, pleine de tendresse et de promesses d'éternité.",
    "Poker Face - Lady Gaga": "Hit électro-pop provocant sur les jeux de séduction et le masque qu'on porte en amour.",
    "Chandelier - Sia": "Chanson puissante sur la fuite dans l'alcool et la solitude, portée par une performance vocale impressionnante.",
    "Loco Contigo - DJ Snake, J. Balvin & Tyga": "Titre électro-latino entraînant sur une passion amoureuse qui rend fou.",
    "Mon précieux - Soprano": "Chanson urbaine dénonçant l'addiction au téléphone et à la vie virtuelle.",
    "Titanium - David Guetta ft. Sia": "Titre électro-pop sur la résilience et la force intérieure, mêlant beats puissants et voix émotive.",
    "Sous le vent - Garou & Céline Dion": "Duo pop lyrique chantant la force de l'amour face aux tempêtes de la vie.",
    "Je suis malade - Serge Lama": "Interprétation dramatique d'un amour destructeur, devenu un classique de la chanson à texte française.",
    "Halo - Beyoncé": "Chanson R&B aux accents spirituels sur la lumière d'un amour rédempteur.",
    "Viva la Vida - Coldplay": "Chanson pop-orchestrale poétique sur un roi déchu et la perte de pouvoir, au rythme entraînant.",
    "Freed From Desire - Gala": "Hit dance des années 90 sur le rejet du matérialisme, devenu hymne dans les stades.",
    "Jerusalema - Master KG ft. Nomcebo": "Chanson sud-africaine devenue virale, mélangeant house et gospel, symbole d'espoir en pleine pandémie.",
    "Bad Guy - Billie Eilish": "Chanson pop alternative où l'artiste joue avec les codes du bien et du mal dans une ambiance décalée.",
    "Havana - Camila Cabello ft. Young Thug": "Chanson pop-latine entraînante évoquant la ville de La Havane et une romance torride.",
    "Smooth - Santana ft. Rob Thomas": "Mélange de rock latino et pop, cette chanson est une ode au charme et à la séduction.",
    "Wonderwall - Oasis": "Ballade rock britannique emblématique, parlant d'un amour fragile et d'espoir.",
    "Yesterday - The Beatles": "Ballade douce et mélancolique sur la nostalgie et la perte.",
    "Call Me Maybe - Carly Rae Jepsen": "Hit pop accrocheur sur l'espoir d'une rencontre amoureuse.",
    "Rolling in the Deep - Adele": "Titre puissant de pop-soul exprimant la colère et la tristesse après une rupture.",
    "I Will Always Love You - Whitney Houston": "Ballade emblématique pleine d'émotion, promesse d'un amour éternel malgré la séparation.",
    "Desire - U2": "Titre rock sur la puissance du désir et de la passion humaine.",
    "Gangnam Style - PSY": "Hit sud-coréen devenu viral mondialement grâce à sa danse décalée.",
    "Waka Waka - Shakira": "Chanson pop entraînante choisie comme hymne de la Coupe du Monde 2010, aux rythmes africains.",
    "Radioactive - Imagine Dragons": "Chanson rock électro sur le changement, la révolution intérieure et la renaissance.",
    "Don't Stop Me Now - Queen": "Hymne rock joyeux et entraînant sur le plaisir de vivre pleinement.",
    "Happy - Pharrell Williams": "Chanson pop optimiste qui invite à ressentir la joie et la bonne humeur.",
    "Vivir Mi Vida - Marc Anthony": "Titre salsa célébrant la vie malgré les difficultés, devenu un hymne latino.",
    "La Isla Bonita - Madonna": "Chanson pop latine célébrant un paradis exotique et un amour idyllique.",
    "Perfecto Amor - Tito El Bambino": "Chanson reggaeton romantique pleine de charme et de sensualité.",
    "Black or White - Michael Jackson": "Titre pop engagé sur l'égalité raciale et l'unité.",
    "Eye of the Tiger - Survivor": "Chanson rock emblématique du dépassement de soi, popularisée par le film Rocky.",
    "Counting Stars - OneRepublic": "Chanson pop-rock sur les rêves, les doutes et les ambitions.",
    "Danza Kuduro - Don Omar ft. Lucenzo": "Hit latino dance irrésistible aux rythmes entraînants et festifs.",
    "Karma Police - Radiohead": "Chanson alternative rock avec un message critique sur le pouvoir et la justice.",
    "Feel Good Inc. - Gorillaz": "Titre électro-rock mélancolique et critique de la société de consommation.",
    "I Gotta Feeling - Black Eyed Peas": "Chanson pop-dance joyeuse annonçant une soirée de fête inoubliable.",
    "Paint It Black - Rolling Stones": "Chanson rock psychédélique aux paroles sombres et au rythme hypnotique.",
    "Senorita - Shawn Mendes & Camila Cabello": "Chanson pop sensuelle racontant une romance passionnée et enflammée.",
    "Tchoin - Kaaris": "Titre trap avec un flow dur et des paroles crues, typique du style agressif de Kaaris.",
    "Bande organisée - Jul, SCH, Kofs, et al.": "Hymne collectif de la scène marseillaise, qui célèbre l'unité et la puissance du rap local.",
    "Maman ne le sait pas - Ninho ft. Niska": "Rap introspectif évoquant les sacrifices et les difficultés de la vie dans la rue.",
    "Basique - Orelsan": "Chanson aux paroles simples et directes, qui critique les travers de la société actuelle.",
    "Sapés comme jamais - Maître Gims ft. Niska": "Mélodie entraînante sur le thème du style et du succès dans le monde du show-business.",
    "Jeune millionaire - SCH": "Rap sombre qui parle de richesse, de solitude et de la pression du succès.",
    "Réseaux - Niska": "Chanson dynamique qui évoque l'influence et les pièges des réseaux sociaux.",
    "Chocolat - Lartiste ft. Awa Imani": "Mélange de rap et de rythmes afro, avec des paroles légères et festives.",
    "Binks to Binks - Booba": "Titre affirmant la domination et la puissance du rappeur dans le milieu.",
    "Au DD - PNL": "Morceau mélodique qui parle de réussite, d'ambition et des racines des deux frères.",
    "Hey Jude - The Beatles": "Ballade intemporelle portée par un refrain mémorable et une intensité progressive.",
    "Uptown Funk - Mark Ronson ft. Bruno Mars": "Morceau funk-pop dynamique et festif, parfait pour faire danser.",
    "Sorry - Justin Bieber": "Chanson pop dancehall avec des sonorités accrocheuses et un message de pardon.",
    "Wake Me Up - Avicii": "Mélange de folk et d'électro qui a marqué le début des années 2010.",
    "Blinding Lights - The Weeknd": "Morceau pop aux influences 80's, connu pour son beat entraînant et sa mélodie accrocheuse.",
    "Heroes - David Bowie": "Hymne romantique et puissant sur l'amour et la résistance face aux obstacles.",
    "Another Brick in the Wall - Pink Floyd": "Chanson rock contestataire contre l'autorité et l'éducation rigide.",
    "Comfortably Numb - Pink Floyd": "Ballade psychédélique exprimant la déconnexion et l'isolement émotionnel.",
    "Stairway to Heaven - Led Zeppelin": "Chef-d'œuvre du rock progressif, mêlant poésie et envolée instrumentale.",
    "Whole Lotta Love - Led Zeppelin": "Titre rock emblématique au riff puissant et sensuel.",
    "Born to Run - Bruce Springsteen": "Hymne rock sur la liberté, l'amour et la fuite de la routine.",
    "Dancing in the Dark - Bruce Springsteen": "Chanson entraînante sur la frustration et la quête de renouveau.",
    "Purple Rain - Prince": "Ballade rock-funk intense et émotionnelle devenue culte.",
    "Kiss - Prince": "Chanson funk minimaliste et sensuelle, aux paroles suggestives.",
    "Nothing Else Matters - Metallica": "Ballade métal devenue universelle, sur l'amour et la vulnérabilité.",
    "Enter Sandman - Metallica": "Hymne heavy metal puissant inspiré des cauchemars d'enfance.",
    "Highway to Hell - AC/DC": "Hymne hard rock énergique sur la vie débridée et la liberté.",
    "Back in Black - AC/DC": "Chanson rock culte en hommage au chanteur Bon Scott, énergique et festive.",
    "Californication - Red Hot Chili Peppers": "Chanson dénonçant la superficialité d'Hollywood et du rêve californien.",
    "Under the Bridge - Red Hot Chili Peppers": "Titre mélancolique évoquant la solitude et la dépendance.",
    "American Idiot - Green Day": "Chanson punk-rock engagée contre la société américaine post-2000.",
    "Seven Nation Army - The White Stripes": "Titre rock culte porté par un riff devenu hymne dans les stades.",
    "Fell in Love with a Girl - The White Stripes": "Chanson garage rock rapide et brute, symbole de leur style minimaliste.",
    "Take Me Out - Franz Ferdinand": "Titre rock dansant des années 2000, marqué par son rythme cassé.",
    "Mr. Brightside - The Killers": "Chanson rock emblématique des années 2000 sur la jalousie amoureuse.",
    "Somebody Told Me - The Killers": "Hit électro-rock au rythme entraînant sur les relations amoureuses compliquées.",
    "Clocks - Coldplay": "Titre planant au piano hypnotique sur la fuite du temps.",
    "In the End - Linkin Park": "Titre emblématique sur l'échec et la résilience.",
    "Crawling - Linkin Park": "Chanson puissante sur la lutte contre les démons intérieurs.",
    "One - U2": "Ballade rock symbolique de l'unité et de l'amour universel.",
    "With or Without You - U2": "Titre mythique sur l'amour impossible et la dépendance affective.",
    "Sunday Bloody Sunday - U2": "Chanson engagée dénonçant la violence en Irlande du Nord.",
    "No Woman, No Cry - Bob Marley": "Hymne reggae réconfortant et porteur d'espoir.",
    "Three Little Birds - Bob Marley": "Chanson optimiste avec le refrain rassurant 'every little thing gonna be alright'.",
    "I Shot the Sheriff - Bob Marley": "Titre reggae engagé devenu mondialement connu avec la reprise d'Eric Clapton.",
    "Respect - Aretha Franklin": "Hymne soul et féministe sur la dignité et l'émancipation.",
    "Think - Aretha Franklin": "Chanson soul entraînante qui appelle à la réflexion et au respect.",
    "What's Going On - Marvin Gaye": "Chanson soul engagée sur la paix et la fraternité.",
    "Sexual Healing - Marvin Gaye": "Chanson soul sensuelle devenue un classique romantique.",
    "Superstition - Stevie Wonder": "Titre funk culte sur la superstition et la croyance.",
    "Isn't She Lovely - Stevie Wonder": "Chanson joyeuse célébrant la naissance de sa fille.",
    "Riders on the Storm - The Doors": "Titre sombre et planant mêlant rock et atmosphère orageuse.",
    "Break on Through - The Doors": "Premier single des Doors, hymne psychédélique et rebelle.",
    "Sweet Dreams (Are Made of This) - Eurythmics": "Titre new wave hypnotique devenu un classique de la pop.",
    "Here Comes the Sun - The Beatles": "Chanson optimiste écrite par George Harrison, annonçant des jours meilleurs.",
    "Come Together - The Beatles": "Titre culte à l'atmosphère psychédélique et groovy.",
    "Across the Universe - The Beatles": "Ballade planante sur l'amour universel et la spiritualité.",
    "La Bohème - Charles Aznavour": "Chanson française emblématique sur la nostalgie de la jeunesse et de l'art.",
    "Emmenez-moi - Charles Aznavour": "Hymne à l'évasion et au rêve de nouveaux horizons.",
    "We Are the Champions - Queen": "Hymne rock universel sur la victoire et la persévérance.",
    "I Want to Break Free - Queen": "Titre pop-rock sur la liberté et l'émancipation.",
    "Say My Name - Destiny's Child": "Titre R&B emblématique sur l'infidélité et la confiance.",
    "Crazy in Love - Beyoncé ft. Jay-Z": "Titre R&B énergique sur l'ivresse amoureuse.",
    "Allumer le feu - Johnny Hallyday": "Chanson rock française énergique sur la passion de la scène.",
    "Pour que tu m'aimes encore - Céline Dion": "Ballade française sur l'amour et le désir de réconciliation.",
    "L'aventurier - Indochine": "Chanson culte inspirée de Bob Morane, symbole d'une génération.",
    "Le Sud - Nino Ferrer": "Chanson française poétique sur la nostalgie du bonheur.",
    "Comme d'habitude - Claude François": "Chanson française iconique, devenue 'My Way' en anglais.",
    "Alexandrie Alexandra - Claude François": "Titre disco festif et énergique culte des années 70.",
    "Je l'aime à mourir - Francis Cabrel": "Ballade romantique devenue un classique de la chanson française.",
    "Petite Marie - Francis Cabrel": "Chanson tendre écrite pour l'amour de sa vie."
}

dict_plats_aliments = {
    "Pomme": "Fruit croquant et sucré, riche en fibres et en vitamines.",
    "Banane": "Fruit doux et énergétique, source importante de potassium.",
    "Carotte": "Légume orange, riche en bêta-carotène, bon pour la vue.",
    "Tomate": "Fruit souvent utilisé en légume, juteux et riche en vitamine C.",
    "Riz": "Céréale de base dans de nombreuses cultures, source d'énergie.",
    "Poulet": "Viande blanche riche en protéines, faible en gras.",
    "Saumon": "Poisson gras riche en oméga-3, bon pour le cœur.",
    "Pain": "Produit de boulangerie à base de farine, essentiel dans de nombreux repas.",
    "Lait": "Boisson riche en calcium, importante pour la santé des os.",
    "Oeuf": "Aliment riche en protéines et en nutriments essentiels.",
    "Fromage": "Produit laitier fermenté, disponible en nombreuses variétés.",
    "Pomme de terre": "Tubercule énergétique, source importante de glucides.",
    "Brocoli": "Légume vert riche en vitamines et antioxydants.",
    "Orange": "Fruit agrume juteux, riche en vitamine C.",
    "Avoine": "Céréale riche en fibres, souvent consommée au petit déjeuner.",
    "Yaourt": "Produit laitier fermenté, bon pour la digestion.",
    "Amande": "Noix riche en graisses saines et en protéines.",
    "Tomate cerise": "Petite tomate sucrée, idéale pour les salades.",
    "Steak": "Viande rouge, riche en protéines et en fer.",
    "Poivron": "Légume coloré, riche en vitamine C.",
    "Concombre": "Légume croquant, très rafraîchissant et peu calorique.",
    "Miel": "Produit sucré naturel fabriqué par les abeilles.",
    "Citron": "Fruit acide utilisé pour aromatiser et en cuisine.",
    "Épinards": "Légume vert foncé, riche en fer et en vitamines.",
    "Thon": "Poisson maigre, riche en protéines.",
    "Chocolat": "Produit sucré à base de cacao, apprécié dans le monde entier.",
    "Avocat": "Fruit riche en bonnes graisses, idéal pour la santé du cœur.",
    "Pois chiches": "Légumineuse riche en protéines et fibres.",
    "Céréales": "Mélange de grains souvent consommé au petit déjeuner.",
    "Crevette": "Fruit de mer riche en protéines et faible en gras.",
    "Noix": "Fruit sec riche en acides gras essentiels.",
    "Betterave": "Légume racine rouge, bon pour le sang.",
    "Pastèque": "Fruit très rafraîchissant, riche en eau.",
    "Ananas": "Fruit tropical sucré et juteux.",
    "Fromage blanc": "Produit laitier frais, souvent consommé au petit déjeuner.",
    "Pêche": "Fruit sucré et juteux, riche en vitamines.",
    "Lentilles": "Légumineuse riche en protéines végétales et fibres.",
    "Champignon": "Fungus comestible, faible en calories et riche en goût.",
    "Saussice": "Produit à base de viande hachée et épices, souvent grillé.",
    "Chou-fleur": "Légume blanc riche en fibres et vitamines.",
    "Melon": "Fruit sucré et juteux, parfait pour l'été.",
    "Yaourt grec": "Produit laitier épais, riche en protéines.",
    "Myrtille": "Petit fruit bleu, riche en antioxydants.",
    "Kiwi": "Fruit vert acide, riche en vitamine C.",
    "Huile d'olive": "Huile végétale saine, utilisée en cuisine méditerranéenne.",
    "Café": "Boisson stimulante à base de grains torréfiés.",
    "Sucre": "Produit sucré utilisé pour aromatiser les aliments.",
    "Beurre": "Produit laitier gras, utilisé en cuisine et pâtisserie.",
    "Saumon fumé": "Poisson fumé, souvent consommé en entrée.",
    "Châtaigne": "Fruit sec riche en glucides et fibres.",
    "Lasagnes": "Plat italien à base de pâtes, viande hachée, sauce tomate et béchamel.",
    "Cassoulet": "Ragoût français de haricots blancs, viande de porc et saucisses.",
    "Paella": "Plat espagnol de riz, fruits de mer, poulet et légumes colorés.",
    "Boeuf Bourguignon": "Ragoût français de boeuf mijoté au vin rouge et légumes.",
    "Pizza Margherita": "Pizza italienne classique avec tomate, mozzarella et basilic.",
    "Ratatouille": "Mélange provençal de légumes mijotés, tomates, courgettes et aubergines.",
    "Sushi": "Plat japonais à base de riz vinaigré et poisson cru ou légumes.",
    "Tacos": "Spécialité mexicaine avec tortilla garnie de viande, légumes et sauces.",
    "Couscous": "Plat nord-africain de semoule accompagné de légumes et viandes épicées.",
    "Chili con carne": "Plat tex-mex épicé à base de viande hachée, haricots et tomates.",
    "Quiche Lorraine": "Tarte salée française aux oeufs, crème et lardons.",
    "Hamburger": "Sandwich américain composé de pain, steak haché, fromage et condiments.",
    "Bouillabaisse": "Soupe de poissons provençale parfumée aux herbes et épices.",
    "Pad Thaï": "Plat thaïlandais de nouilles sautées avec crevettes, tofu et cacahuètes.",
    "Moussaka": "Gratin grec à base d'aubergines, viande hachée et sauce béchamel.",
    "Gratin dauphinois": "Plat français de pommes de terre cuites au four avec crème et ail.",
    "Poulet Tikka Masala": "Plat indien de poulet mariné dans une sauce tomate épicée.",
    "Falafel": "Boulette de pois chiches frite, spécialité du Moyen-Orient.",
    "Fish and Chips": "Plat britannique de poisson frit servi avec des frites croustillantes.",
    "Tarte Tatin": "Tarte aux pommes caramélisées, renversée avant cuisson.",
    "Ceviche": "Plat sud-américain de poisson cru mariné au citron vert.",
    "Fondue Savoyarde": "Fromage fondu à partager, spécialité des Alpes françaises.",
    "Crêpe": "Fine galette de farine, souvent garnie de sucre, chocolat ou fruits.",
    "Boeuf Stroganoff": "Plat russe de boeuf en sauce à la crème et champignons.",
    "Ramen": "Soupe japonaise de nouilles avec bouillon, viande et légumes.",
    "Tajine": "Plat marocain mijoté dans un récipient en terre cuite avec épices.",
    "Salade Niçoise": "Salade française composée de thon, olives, œufs et légumes frais.",
    "Spaghetti Carbonara": "Pâtes italiennes avec sauce à base d'œufs, pancetta et fromage.",
    "Pavé de saumon": "Filet de saumon cuit souvent accompagné de légumes ou sauce légère.",
    "Hachis Parmentier": "Gratin français de viande hachée recouverte de purée de pommes de terre.",
    "Poulet Basquaise": "Poulet mijoté avec poivrons, tomates et épices du Pays Basque.",
    "Boulette de viande": "Petite boule de viande hachée, souvent servie en sauce.",
    "Tartiflette": "Gratin savoyard à base de pommes de terre, lardons et reblochon.",
    "Maki": "Sushi roulé avec riz et garnitures variées enveloppées dans une feuille de nori.",
    "Cannelés": "Petits gâteaux bordelais croustillants à l'extérieur et moelleux à l'intérieur.",
    "Tarte aux fraises": "Pâtisserie composée d'une pâte, crème pâtissière et fraises fraîches.",
    "Poulet rôti": "Plat classique de poulet entier rôti au four avec herbes.",
    "Couscous royal": "Version festive du couscous avec plusieurs viandes (agneau, poulet, merguez).",
    "Risotto": "Plat italien de riz crémeux cuit lentement avec bouillon et parmesan.",
    "Gnocchis": "Petites pâtes italiennes à base de pomme de terre, souvent servies en sauce.",
    "Boeuf Wellington": "Filet de boeuf enveloppé de pâte feuilletée et cuit au four.",
    "Clafoutis": "Dessert français avec fruits cuits dans une pâte à crêpe épaisse.",
    "Pizza Quatre Fromages": "Pizza garnie de plusieurs fromages fondus et savoureux.",
    "Soupe à l'oignon": "Soupe traditionnelle française aux oignons caramélisés et gratinée au fromage.",
    "Mangue": "Fruit tropical sucré et juteux, riche en vitamines A et C.",
    "Grenade": "Fruit à graines rouges, riche en antioxydants.",
    "Papaye": "Fruit exotique doux, bon pour la digestion.",
    "Litchi": "Petit fruit asiatique au goût floral et sucré.",
    "Goyave": "Fruit tropical riche en fibres et vitamine C.",
    "Noix de coco": "Fruit tropical dont on consomme la chair et l'eau rafraîchissante.",
    "Figue": "Fruit sucré riche en fibres, souvent séché ou frais.",
    "Kaki": "Fruit orange d'automne au goût doux et sucré.",
    "Framboise": "Petit fruit rouge acidulé, riche en vitamines.",
    "Pamplemousse": "Agrume amer et rafraîchissant, riche en vitamine C.",
    "Mirabelle": "Petite prune jaune sucrée, spécialité de Lorraine.",
    "Coing": "Fruit parfumé utilisé en confiture et gelée.",
    "Patate douce": "Tubercule sucré, riche en fibres et bêta-carotène.",
    "Courgette": "Légume vert polyvalent, utilisé cru ou cuit.",
    "Aubergine": "Légume violet, base de nombreux plats méditerranéens.",
    "Artichaut": "Légume aux feuilles comestibles et au cœur tendre.",
    "Fenouil": "Légume au goût anisé, utilisé cru ou en salade.",
    "Navet": "Légume racine blanc et violet, doux une fois cuit.",
    "Potiron": "Légume d'automne idéal pour les soupes et gratins.",
    "Haricot vert": "Légume croquant, riche en fibres et vitamines.",
    "Petits pois": "Légume vert sucré, souvent utilisé dans les plats mijotés.",
    "Radis": "Petit légume racine croquant et piquant.",
    "Topinambour": "Tubercule ancien au goût de noisette.",
    "Manioc": "Tubercule tropical riche en amidon.",
    "Chou rouge": "Légume coloré riche en vitamines et minéraux.",
    "Chou de Bruxelles": "Petit chou amer, riche en vitamine C.",
    "Endive": "Légume croquant légèrement amer, consommé cru ou cuit.",
    "Mangoustan": "Fruit tropical violet au goût sucré et acidulé.",
    "Pistache": "Fruit sec vert, souvent utilisé en dessert.",
    "Noisette": "Fruit sec au goût doux, utilisé en confiserie.",
    "Macadamia": "Noix au goût beurré, riche en graisses saines.",
    "Pignon de pin": "Graines comestibles utilisées dans le pesto.",
    "Noix de pécan": "Noix sucrée très utilisée en pâtisserie américaine.",
    "Canneberge": "Petit fruit rouge acidulé, souvent séché ou en jus.",
    "Açaï": "Baie d'Amazonie riche en antioxydants.",
    "Fève": "Légumineuse ancienne, riche en protéines.",
    "Edamame": "Jeunes fèves de soja, consommées en apéritif.",
    "Haricot rouge": "Légumineuse courante dans les plats tex-mex.",
    "Haricot blanc": "Base de nombreux plats mijotés comme le cassoulet.",
    "Tofu": "Produit à base de soja, riche en protéines végétales.",
    "Quinoa": "Pseudo-céréale riche en protéines végétales.",
    "Orge": "Céréale utilisée en soupes et en bière.",
    "Épeautre": "Céréale ancienne, alternative au blé.",
    "Sarrasin": "Grain utilisé dans les galettes bretonnes.",
    "Seigle": "Céréale utilisée pour fabriquer du pain noir.",
    "Boulgour": "Blé concassé, base de nombreux plats orientaux.",
    "Taboulé": "Salade orientale à base de boulgour, légumes et herbes.",
    "Houmous": "Purée de pois chiches et tahini, spécialité du Moyen-Orient.",
    "Baba ganoush": "Purée d'aubergine grillée, spécialité orientale.",
    "Guacamole": "Préparation mexicaine à base d'avocat écrasé.",
    "Tapenade": "Purée d'olives noires et câpres, spécialité provençale.",
    "Pesto": "Sauce italienne à base de basilic, ail, parmesan et pignons.",
    "Ketchup": "Sauce tomate sucrée, très populaire en accompagnement.",
    "Mayonnaise": "Sauce froide à base d'œufs et d'huile.",
    "Moutarde": "Condiment piquant à base de graines de moutarde.",
    "Wasabi": "Condiment japonais vert, très piquant.",
    "Harissa": "Pâte de piment rouge, spécialité d'Afrique du Nord.",
    "Sriracha": "Sauce piquante thaïlandaise à base de piment.",
    "Tzatziki": "Sauce grecque à base de yaourt, concombre et ail.",
    "Caviar": "Œufs d'esturgeon, mets de luxe raffiné.",
    "Foie gras": "Spécialité française à base de foie de canard ou d'oie.",
    "Truffe": "Champignon rare et cher, au goût intense."

}

dict_phenomenes_emotions_sentiments = {

    # Catégorie : Phénomènes naturels
    "Tremblement de terre": "Secousse du sol causée par le mouvement des plaques tectoniques.",
    "Erosion": "Usure des sols et roches par l'eau, le vent ou la glace.",
    "Glissement de terrain": "Mouvement rapide de terres ou roches sur une pente.",
    "Pluie acide": "Précipitation contenant des substances chimiques nocives pour l'environnement.",
    "Aurore boréale": "Lumières colorées dans le ciel causées par les particules solaires.",
    "Tsunami": "Vague gigantesque provoquée par un séisme sous-marin ou une éruption volcanique.",
    "Tornade": "Colonne d'air en rotation rapide, capable de détruire tout sur son passage.",
    "Éruption volcanique": "Libération brutale de lave, cendres et gaz par un volcan actif.",
    "Séisme": "Secousse de la croûte terrestre due à la libération d'énergie souterraine.",
    "Inondation": "Débordement des eaux qui submerge une zone terrestre habituellement sèche.",
    "Avalanche": "Chute massive et rapide de neige accumulée sur une pente montagneuse.",
    "Feu de forêt": "Incendie qui se propage rapidement dans les zones boisées ou sèches.",
    "Ouragan": "Cyclone tropical très puissant avec des vents destructeurs et des pluies intenses.",
    "Cyclone": "Tempête tropicale avec vents forts et pluies torrentielles.",
    "Tempête de sable": "Vents forts qui soulèvent et transportent des particules de sable sur de grandes distances.",
    "Éruption solaire": "Éjection massive de particules et de radiations depuis le Soleil vers la Terre.",

    # Anthropiques
    "Pollution": "Contamination de l'air, de l'eau ou du sol par l'activité humaine.",
    "Industrialisation": "Développement des industries et des infrastructures.",
    "Innovation technologique": "Introduction de nouvelles techniques ou machines.",
    "Construction de barrages": "Modification des cours d'eau pour produire de l'énergie ou irriguer.",
    "Déchets plastiques": "Accumulation de plastiques dans l'environnement terrestre et marin.",
    "Exploration spatiale": "Envoi d'objets ou humains dans l'espace pour la recherche.",
    "Agriculture intensive": "Exploitation intensive des sols pour produire plus de nourriture.",

    # Catégorie : Environnement et climat
    "Déforestation": "Destruction massive des forêts par l'homme, souvent pour l'agriculture ou l'urbanisation.",
    "Réchauffement climatique": "Augmentation progressive des températures moyennes à cause des gaz à effet de serre.",
    "Sécheresse": "Période prolongée de manque de précipitations affectant les ressources en eau.",
    "Marée noire": "Déversement accidentel de pétrole en mer, causant une pollution grave.",
    "Désertification": "Processus de dégradation des terres arides par les activités humaines ou naturelles.",

     # Sociologiques
    "Mode vestimentaire": "Tendance culturelle concernant les vêtements.",
    "Rituel": "Pratique répétée à signification symbolique dans une société.",
    "Migration": "Déplacement de populations pour des raisons économiques ou politiques.",
    "Coutume": "Habitude ou norme propre à un groupe social.",
    "Criminalité": "Ensemble des comportements considérés illégaux par la société.",

    # Catégorie : Sociétal et économique
    "Inflation": "Augmentation générale des prix dans une économie.",
    "Récession": "Période de baisse de l'activité économique.",
    "Spéculation": "Achat ou vente pour profiter des variations de prix.",
    "Investissement": "Placement de capitaux pour générer des profits futurs.",
    "Crise financière": "Effondrement soudain des marchés et des institutions économiques.",
    "Taxation": "Prélèvement obligatoire d'argent par l'État.",
    "Commerce international": "Échanges de biens et services entre pays.",
    "Mondialisation": "Processus d'intégration économique, culturelle et politique à l'échelle mondiale.",
    "Urbanisation": "Croissance rapide des villes et concentration de la population urbaine.",
    "Chômage": "Situation où une partie de la population active est sans emploi et en recherche d'un travail.",
    "Crise économique": "Période de récession marquée par une baisse de la production et de l'emploi.",
    "Inégalités sociales": "Disparités dans l'accès aux ressources, au pouvoir et aux opportunités entre groupes sociaux.",
    "Pauvreté": "Manque des ressources matérielles et immatérielles nécessaires pour vivre dignement.",
    "Individualisme": "Valorisation de l'autonomie et de l'indépendance de l'individu dans la société.",
    "Télétravail": "Travail réalisé à distance grâce aux technologies numériques.",
    "Inégalités de genre": "Disparités entre hommes et femmes en matière de droits, salaires et opportunités.",
    "Crise sanitaire": "Situation exceptionnelle qui perturbe gravement la santé publique, comme une pandémie.",
    "Capitalisme": "Système économique basé sur la propriété privée des moyens de production et la recherche du profit.",
    "Cybercriminalité": "Activités illégales utilisant les technologies de l'information et d'Internet.",
    "Discrimination raciale": "Traitement inégal et défavorable envers une personne à cause de sa race ou origine.",
    "Terrorisme": "Usage de la violence pour créer la peur et atteindre des objectifs politiques.",
    "Féminisme": "Mouvement social et politique pour l'égalité des sexes.",
    "Boom démographique": "Croissance rapide et soutenue de la population d'un pays ou d'une région.",
    "Radicalisation": "Processus par lequel une personne adopte des idées extrêmes souvent violentes.",

    # Politiques
    "Révolution": "Changement brusque et radical d'un système politique.",
    "Election": "Processus de choix de dirigeants par vote.",
    "Conflict armé": "Conflit entre États ou groupes armés.",
    "Diplomatie": "Relations et négociations entre pays.",
    "Législation": "Élaboration et application des lois.",
    "Coup d'État": "Prise de pouvoir violente et soudaine par un groupe.",
    "Nationalisme": "Sentiment de fierté et loyauté envers sa nation.",
    "Réforme politique": "Modification planifiée du système politique.",
    "Manifestation": "Rassemblement pour exprimer un avis politique.",
    "Guerre civile": "Conflit armé interne à un pays.",

    # Psychologiques
    "Stress": "Réaction émotionnelle et physique face à une pression.",
    "Mémoire": "Capacité à enregistrer, conserver et restituer des informations.",
    "Apprentissage": "Acquisition de connaissances ou compétences nouvelles.",
    "Phobie": "Peur intense et irrationnelle d'un objet ou d'une situation.",
    "Dépression": "Trouble émotionnel caractérisé par une tristesse persistante.",
    "Motivation": "Facteur interne poussant à agir.",
    "Perception": "Processus par lequel le cerveau interprète les stimuli.",
    "Créativité": "Capacité à produire des idées originales.",

    # Physiques / chimiques / biologiques
    "Gravité": "Force d'attraction entre les objets possédant une masse.",
    "Electricité": "Phénomène lié au mouvement des charges électriques.",
    "Magnétisme": "Force d'attraction ou de répulsion entre objets aimantés.",
    "Photosynthèse": "Processus par lequel les plantes produisent de l'énergie.",
    "Radioactivité": "Émission de particules par certains noyaux atomiques instables.",
    "Fusion nucléaire": "Combinaison de noyaux atomiques pour libérer de l'énergie.",
    "Pression atmosphérique": "Force exercée par l'air sur une surface.",
    "Dissolution": "Processus de mélange d'un soluté dans un solvant.",


    # Technologiques / scientifiques
    "Robotique": "Conception et utilisation de robots.",
    "Informatique quantique": "Informatique utilisant les principes de la physique quantique.",
    "Energie solaire": "Production d'énergie à partir de la lumière du soleil.",
    "Energie éolienne": "Production d'électricité grâce au vent.",
    "Impression 3D": "Fabrication d'objets en ajoutant couche par couche de matériau.",
    "Réalité virtuelle": "Simulation informatique immersive d'un environnement.",
    "Cryptomonnaie": "Monnaie numérique basée sur la cryptographie.",

    # Catégorie : Émotions et sentiments
    "Joie": "Sentiment de bonheur intense et de satisfaction.",
    "Tristesse": "Émotion liée à une perte ou une déception.",
    "Colère": "Sentiment de mécontentement face à une injustice ou frustration.",
    "Peur": "Réaction émotionnelle à une menace ou un danger.",
    "Surprise": "Émotion provoquée par un événement inattendu.",
    "Dégoût": "Réaction de rejet face à quelque chose de désagréable.",
    "Amour": "Sentiment d'affection profonde envers quelqu'un ou quelque chose.",
    "Haine": "Sentiment intense d'aversion ou d'hostilité.",
    "Fierté": "Satisfaction liée à une réussite ou une qualité personnelle.",
    "Honte": "Sentiment de gêne ou de culpabilité suite à une action ou situation.",
    "Jalousie": "Sentiment d'envie mêlé de méfiance envers une tierce personne.",
    "Envie": "Désir d'avoir ce que possède autrui.",
    "Solitude": "Sentiment d'être seul et isolé.",
    "Espoir": "Attente positive d'un événement futur souhaité.",
    "Anxiété": "Inquiétude diffuse et souvent persistante.",
    "Déception": "Tristesse liée à un espoir non réalisé.",
    "Gratitude": "Reconnaissance envers quelqu'un pour un bienfait.",
    "Confusion": "Sentiment d'incertitude ou de désordre mental.",
    "Nostalgie": "Regret du passé avec une touche de mélancolie.",
    "Sérénité": "Calme intérieur et absence de trouble.",
    "Frustration": "Mécontentement causé par un obstacle à un désir.",
    "Culpabilité": "Sentiment de responsabilité pour un tort commis.",
    "Compassion": "Sympathie et désir d'aider ceux qui souffrent.",
    "Admiration": "Estime profonde pour une qualité ou un accomplissement.",
    "Mépris": "Dévalorisation d'une personne ou d'une idée.",
    "Émerveillement": "Fascination intense devant quelque chose de beau ou inattendu.",
    "Inquiétude": "Préoccupation liée à une incertitude.",
    "Détermination": "Volonté ferme d'atteindre un objectif.",
    "Pitié": "Sentiment de tristesse mêlé de tendresse envers la souffrance d'autrui.",
    "Désespoir": "Perte totale d'espoir et de confiance en l'avenir.",
    "Fascination": "Attraction intense et durable pour quelque chose ou quelqu'un.",
    "Amertume": "Sentiment douloureux de rancune ou de déception.",
    "Excitation": "État d'enthousiasme ou d'agitation positive.",
    "Soulagement": "Disparition d'une inquiétude ou d'une souffrance.",
    "Sympathie": "Affection modérée pour quelqu'un, compréhension de ses sentiments.",
    "Hostilité": "Attitude agressive ou opposée envers une personne ou un groupe.",
    "Énervement": "Agitation ou irritation passagère.",
    "Timidité": "Gêne ou réserve dans les relations sociales.",
    "Plaisir": "Sensation agréable liée à la satisfaction d'un désir.",
    "Doute": "Manque de certitude ou d'assurance.",
    "Ressentiment": "Sentiment prolongé d'amertume envers une injustice.",
    "Empathie": "Capacité à comprendre et partager les émotions d'autrui.",
    "Chagrin": "Douleur morale profonde et durable.",
    "Bienveillance": "Disposition favorable à autrui avec volonté de faire du bien.",
    "Mélancolie": "Tristesse douce et réfléchie, souvent nostalgique.",
    "Exaltation": "Joie intense accompagnée d'un sentiment de puissance.",
    "Calme": "Absence de tension ou d'agitation émotionnelle.",

    # Catégorie : Autres phénomènes
    "Explosion nucléaire": "Détonation d'une bombe atomique libérant une énergie destructrice énorme.",
    "Migration animale": "Déplacement saisonnier d'espèces animales à la recherche de nourriture ou de reproduction.",
    "Déclin de la biodiversité": "Perte progressive des espèces animales et végétales à cause des activités humaines."
}


dict_mouvements_instruments = {
    # Musique
    "Rock": "Genre musical apparu dans les années 1950, caractérisé par des guitares électriques et un rythme énergique.",
    "Rap": "Genre musical urbain basé sur le rythme et le texte parlé, né dans les années 1970 aux États-Unis.",
    "Classique": "Musique savante européenne, de la période baroque au romantisme et au-delà.",
    "Jazz": "Style musical né aux États-Unis mêlant improvisation et influences africaines et européennes.",
    "Blues": "Musique afro-américaine exprimant tristesse et émotion, à l'origine du jazz et du rock.",
    "Reggae": "Musique jamaïcaine née dans les années 1960, souvent associée à la culture rastafari.",
    "Pop": "Musique populaire accessible et commerciale, centrée sur le rythme et la mélodie.",
    "Electro": "Musique électronique centrée sur les synthétiseurs et les rythmes programmés.",
    "Metal": "Genre musical puissant et agressif dérivé du rock, souvent avec des thèmes sombres.",
    "Country": "Musique américaine traditionnelle racontant la vie rurale et les histoires personnelles.",

    # Arts visuels
    "Impressionnisme": "Mouvement artistique français du XIXe siècle, privilégiant la lumière et la couleur.",
    "Cubisme": "Mouvement pictural du début du XXe siècle basé sur la décomposition géométrique des formes.",
    "Réaliste": "Mouvement artistique du XIXe siècle représentant la vie quotidienne de manière fidèle.",
    "Abstrait": "Art non figuratif privilégiant formes, couleurs et émotions sur la représentation du réel.",
    "Surréalisme": "Mouvement artistique et littéraire explorant l'inconscient et les rêves.",
    "Expressionnisme": "Style artistique mettant en avant les émotions et l'intériorité.",
    "Fauvisme": "Mouvement pictural du XXe siècle privilégiant les couleurs vives et la spontanéité.",
    "Art déco": "Style artistique des années 1920-1930 caractérisé par l'élégance, le luxe et la géométrie.",
    "Street art": "Art urbain souvent engagé, utilisant les murs et espaces publics comme support.",
    "Bauhaus": "Mouvement allemand du XXe siècle combinant design, architecture et arts appliqués.",

    # Littérature
    "Romantisme": "Mouvement du XIXe siècle exaltant les émotions et la nature.",
    "Réalisme": "Mouvement littéraire représentant fidèlement la société et les personnages.",
    "Naturalisme": "Extension du réalisme centrée sur les déterminismes sociaux et biologiques.",
    "Surréalisme littéraire": "Exploration de l'inconscient et des rêves à travers l'écriture.",
    "Existentialisme": "Philosophie et littérature centrées sur la liberté et l'existence humaine.",
    "Symbolisme": "Mouvement poétique valorisant la suggestion et les symboles.",
    "Modernisme": "Renouvellement des formes et thèmes littéraires au début du XXe siècle.",
    "Postmodernisme": "Mouvement qui remet en question les grands récits et les conventions.",
    "Minimalisme": "Style littéraire ou artistique utilisant la simplicité et l'économie de moyens.",
    "Beat Generation": "Mouvement littéraire américain des années 1950, rebelle et anticonformiste.",

    # Cinéma
    "Thriller": "Genre cinématographique basé sur le suspense et le mystère.",
    "Romance": "Genre centré sur les relations amoureuses et émotionnelles.",
    "Comédie": "Films visant à provoquer le rire et le divertissement.",
    "Science-fiction": "Films explorant technologies, futur et mondes imaginaires.",
    "Horreur": "Films destinés à effrayer ou choquer le spectateur.",
    "Documentaire": "Genre cinématographique représentant la réalité et les faits.",
    "Film noir": "Genre sombre des années 1940-1950, centrée sur le crime et la fatalité.",
    "Western": "Films se déroulant dans le Far West, avec cow-boys et hors-la-loi.",
    "Animation": "Films utilisant des images créées par dessin, ordinateur ou stop-motion.",
    "Fantastique": "Films mêlant éléments surnaturels et réalité.",

    # Philosophie
    "Stoïcisme": "École antique centrée sur la maîtrise de soi et la vertu.",
    "Épicurisme": "Philosophie antique valorisant le plaisir modéré et l'absence de douleur.",
    "Nihilisme": "Doctrine niant l'existence de valeurs et de sens objectif.",
    "Structuralisme": "Approche analysant les structures sous-jacentes des phénomènes.",
    "Postmodernisme philosophique": "Mouvement critiquant les certitudes et les grands récits.",
    "Utilitarisme": "Philosophie évaluant les actions selon le bien-être produit.",
    "Déconstruction": "Mouvement critique de la pensée occidentale et des textes.",
    "Humanisme": "Philosophie centrée sur l'homme et sa dignité.",

    # Politique et société
    "Féminisme": "Mouvement pour l'égalité des sexes et les droits des femmes.",
    "Anarchisme": "Idéologie prônant l'absence d'autorité étatique.",
    "Socialisme": "Courant prônant la justice sociale et la propriété collective.",
    "Communisme": "Idéologie visant l'abolition des classes et la propriété collective.",
    "Libéralisme": "Doctrine valorisant la liberté individuelle et économique.",
    "Écologisme": "Mouvement pour la protection de l'environnement et le développement durable.",
    "Droits civiques": "Lutte pour l'égalité des droits et la fin de la discrimination raciale.",
    "Nationalisme": "Mouvement centrée sur l'intérêt et l'identité d'une nation.",
    "Pacifisme": "Doctrine prônant la non-violence et la résolution pacifique des conflits.",
    "Suffragisme": "Mouvement pour le droit de vote des femmes.",

    # Sciences et technologies
    "Informatique": "Mouvement technologique centré sur le développement des ordinateurs et logiciels.",
    "Intelligence artificielle": "Développement de systèmes capables de simuler l'intelligence humaine.",
    "Exploration spatiale": "Recherche et découverte de l'espace et des planètes.",
    "Nanotechnologie": "Travail sur la matière à l'échelle atomique et moléculaire.",
    "Révolution industrielle": "Période de transformation économique et sociale par les machines.",
    "Open source": "Idée de partager librement logiciels et connaissances scientifiques.",


    # Culture et mode
    "Pop culture": "Ensemble des phénomènes culturels populaires contemporains.",
    "Hippie": "Mouvement des années 1960 prônant paix, amour et liberté.",
    "Gothique": "Style vestimentaire et culturel associé au sombre et au romantique.",
    "Streetwear": "Mode urbaine influencée par le hip-hop et le skate.",
    "Baroque": "Style artistique riche et extravagant, du XVIIe siècle.",
    "Renaissance": "Mouvement culturel européen centrée sur l'art, la science et l'humanisme.",
    "Avant-garde": "Courants artistiques novateurs et expérimentaux.",
    "Cyberpunk": "Mouvement de science-fiction mêlant technologie avancée et dystopie urbaine.",

    # Instruments de musique
    "Guitare": "Instrument à cordes pincées très répandu, la guitare permet d'accompagner ou de jouer des mélodies variées, du classique au rock.",
    "Guitare électrique": "Amplifiée et associée au rock et au métal, elle offre une grande palette de sons grâce aux effets électroniques.",
    "Violon": "Petit instrument à cordes frottées, il joue souvent le rôle de soliste dans l'orchestre et exige une grande précision technique.",
    "Violoncelle": "Plus grave que le violon, il produit un son profond et chaleureux, utilisé en musique classique et contemporaine.",
    "Contrebasse": "Plus grand instrument de la famille des cordes frottées, il apporte la base rythmique et harmonique de nombreux ensembles.",
    "Harpe": "À la fois majestueuse et délicate, la harpe se joue en pinçant ses nombreuses cordes tendues verticalement.",
    "Mandoline": "Petit instrument à cordes pincées, elle est reconnaissable à son timbre brillant et son usage fréquent dans les musiques traditionnelles.",
    "Banjo": "Doté d'une caisse circulaire et d'un son sec et claquant, il est emblématique du bluegrass et du folk américain.",
    "Ukulélé": "Originaire d'Hawaï, ce petit instrument à quatre cordes produit un son léger et joyeux.",
    "Luth": "Ancêtre de la guitare, cet instrument à cordes pincées était très prisé à la Renaissance.",
    "Clavecin": "Instrument à clavier à cordes pincées, il était central dans la musique baroque avant l'avènement du piano.",
    "Flûte traversière": "Instrument à vent en métal ou en bois, on la joue en soufflant sur un trou latéral.",
    "Flûte à bec": "Instrument d'apprentissage courant, mais aussi utilisé dans la musique médiévale et baroque.",
    "Clarinette": "Instrument à anche simple, elle possède une large tessiture et s'adapte à de nombreux styles, du classique au jazz.",
    "Hautbois": "Son timbre nasal et expressif le rend très reconnaissable dans les orchestres symphoniques.",
    "Saxophone": "Inventé au XIXe siècle, ce bois en laiton est omniprésent dans le jazz, la variété et les fanfares.",
    "Trompette": "Instrument à vent en cuivre, son timbre éclatant est parfait pour les solos percutants et les fanfares.",
    "Trombone": "Grâce à sa coulisse, il peut glisser d'une note à l'autre, offrant un son puissant et flexible.",
    "Tuba": "Plus grave des cuivres, il soutient l'harmonie avec des sons profonds et ronds dans les orchestres ou fanfares.",
    "Batterie": "Ensemble de percussions jouées avec des baguettes, cœur rythmique du rock, jazz et pop.",
    "Xylophone": "Percussion à lames en bois frappées avec des maillets, souvent utilisée en musique classique ou pour enfants.",
    "Timbales": "Grands tambours accordables, elles donnent de l'impact rythmique aux orchestres symphoniques.",
    "Piano": "Instrument à clavier et à cordes frappées, il est aussi bien soliste qu'accompagnateur, polyvalent et universel.",
    "Orgue": "Utilisé dans les églises et les salles de concert, il produit un son majestueux grâce à ses tuyaux.",
    "Accordéon": "Instrument à vent et à clavier, il est emblématique des musiques traditionnelles d'Europe et d'Amérique du Sud.",
    "Harmonica": "Petit instrument à vent, il se joue en soufflant et aspirant dans des lamelles métalliques.",
    "Didgeridoo": "Long tube en bois d'origine aborigène, il émet un son grave et vibrant par vibration continue des lèvres.",
    "Cornemuse": "Instrument à vent à anche et sac, emblématique de l'Écosse et de diverses traditions.",
    "Maracas": "Instruments de percussion secoués, typiques de la musique latine.",
    "Castagnettes": "Petits instruments claqués avec les doigts, typiques du flamenco.",
    "Triangle": "Percussion métallique simple mais très percutante.",
    "Shofar": "Corne de bélier utilisée dans la tradition juive.",
    "Ocarina": "Flûte globulaire en céramique ou en plastique.",
    "Lyre": "Ancien instrument à cordes pincées de la Grèce antique."
}

dict_influenceurs_medias = {
    # ------------------- YOUTUBEURS / CREATEURS -------------------
    # International
    "MrBeast": "Créateur américain célèbre pour ses défis extravagants et philanthropiques.",
    "PewDiePie": "YouTubeur suédois connu pour ses vidéos gaming et son humour décalé.",
    "Dude Perfect": "Groupe américain réalisant des vidéos de tricks et défis sportifs incroyables.",
    "Jacksepticeye": "YouTubeur irlandais spécialisé dans les vidéos gaming et les vlogs dynamiques.",
    "Logan Paul": "YouTubeur américain connu pour ses vlogs et contenus de divertissement.",
    "Mark Rober": "Ancien ingénieur de la NASA devenu YouTubeur scientifique et vulgarisateur.",

    # Français
    "Squeezie": "YouTubeur français très populaire pour ses vidéos gaming et ses sketches humoristiques.",
    "Cyprien": "Créateur français de vidéos humoristiques et culturelles sur YouTube.",
    "Norman": "Humoriste français connu pour ses sketchs vidéos sur la vie quotidienne.",
    "Amixem": "YouTubeur français réalisant des vidéos de défis, vlogs et expériences amusantes.",
    "JoueurDuGrenier": "Créateur français qui teste et critique des jeux vidéo rétro avec humour.",
    "Michou": "Streamer et YouTubeur français spécialisé dans le gaming et le divertissement.",
    "Pierre Croce": "Humoriste français spécialisé dans les présentations comiques et vidéos créatives.",
    "Le Rire Jaune": "YouTubeur français connu pour ses vidéos humoristiques et anecdotes de vie.",
    "Poisson Fécond": "Créateur français spécialisé dans les sketchs humoristiques et critiques culturelles.",
    "Nota Bene": "YouTubeur français réalisant des vidéos historiques et documentaires accessibles.",
    "Mister V": "YouTubeur français créant sketches, vidéos humoristiques et contenus musicaux.",
    "Léna Situations": "YouTubeuse française connue pour ses vlogs lifestyle et collaborations mode.",
    "McFly et Carlito": "Duo de YouTubeurs français réalisant des défis et vidéos humoristiques.",
    "Tibo InShape": "YouTubeur français spécialisé dans le fitness, motivation et challenges sportifs.",
    "Lolywood": "Duo de YouTubeurs français réalisant des sketchs et vidéos humoristiques populaires.",
    "Natoo": "YouTubeuse française réalisant des vidéos humoristiques et créatives sur la vie quotidienne.",
    "Le Grand JD": "YouTubeur français explorant des lieux insolites et documentaires d'investigation.",
    "Jérôme Jarre": "Créateur français connu pour ses vidéos humoristiques et ses campagnes humanitaires.",
    "Wankil Studio": "Duo de YouTubeurs français spécialisés dans le gaming et vidéos humoristiques.",
    "Doc Seven": "YouTubeur français spécialisé dans les vidéos culturelles et éducatives.",
    "Antoine Daniel": "YouTubeur français créateur de 'What The Cut' et projets humoristiques.",

    # ------------------- STREAMERS -------------------
    # International
    "Ninja": "Streamer américain célèbre pour ses parties de Fortnite et ses performances e-sport.",
    "Pokimane": "Streamuse canadienne connue pour ses sessions gaming et son interaction avec la communauté.",
    "Tfue": "Streamer américain spécialisé dans les jeux compétitifs, notamment Fortnite.",
    "KSI": "YouTubeur britannique célèbre pour ses vidéos gaming et son humour décalé.",
    "Ibai Llanos": "Streamer espagnol extrêmement populaire, organisateur d'événements e-sport.",

    # Français
    "Gotaga": "Streamer français et joueur professionnel de FPS, surnommé le 'French Monster'.",
    "Locklear": "Streamer français connu pour ses lives sur Fortnite et Minecraft.",
    "Kameto": "Streamer français et co-fondateur de la structure Karmine Corp, orienté e-sport.",
    "Sardoche": "Streamer français reconnu pour ses sessions League of Legends et son franc-parler.",
    "Ponce": "Streamer français spécialisé dans le divertissement et le talk-show sur Twitch.",
    "MisterMV": "Streamer français vétéran de Twitch, spécialisé dans les jeux rétro et variés.",
    "Baghera Jones": "Streamuse française connue pour ses streams Minecraft et variés.",
    "ZeratoR": "Streamer français organisateur du Z Event et joueur multi-gaming.",
    "Domingo": "Streamer français animateur de talk-shows et gaming.",
    "Maghla": "Streamuse française orientée gaming, connue pour sa bonne humeur.",

    # ------------------- INFLUENCEURS -------------------
    # International
    "Charli D'Amelio": "TikTokeuse américaine célèbre pour ses danses et challenges viraux.",
    "Addison Rae": "Influenceuse américaine connue pour ses vidéos TikTok et ses collaborations musicales.",
    "Zach King": "Créateur américain célèbre pour ses vidéos illusions et effets spéciaux sur TikTok.",
    "Bella Poarch": "Influenceuse et chanteuse américaine, devenue célèbre grâce à TikTok et ses clips courts.",
    "James Charles": "Influenceur américain spécialisé dans la beauté et le maquillage.",
    "Khaby Lame": "TikTokeur italien devenu célèbre pour ses vidéos comiques muettes et virales.",
    "Kylie Jenner": "Influenceuse américaine spécialisée dans la mode, beauté et lifestyle, très suivie sur Instagram.",
    "Dixie D'Amelio": "Influenceuse et chanteuse américaine, connue pour ses contenus sur TikTok et réseaux sociaux.",
    "Kim Kardashian": "Icône américaine de la mode et de la télévision, star mondiale d'Instagram.",
    "Kendall Jenner": "Top-modèle américaine et influenceuse Instagram.",
    "Gigi Hadid": "Mannequin américaine suivie massivement sur Instagram.",
    "Hailey Bieber": "Influenceuse américaine et mannequin.",
    "Georgina Rodríguez": "Influenceuse espagnole, compagne de Cristiano Ronaldo.",

    # Français
    "Paola Locatelli": "Influenceuse française spécialisée dans la mode, le lifestyle et les collaborations marques.",
    "EnjoyPhoenix": "YouTubeuse et influenceuse française spécialisée dans la beauté et le lifestyle.",
    "Hugo Décrypte": "YouTubeur français qui vulgarise l'actualité et l'information de manière pédagogique.",
    "Just Riadh": "Influenceur français créant des vidéos humoristiques et challenges sur TikTok.",
    "Maeva Ghennam": "Influenceuse française issue de la télé-réalité.",
    "Jessica Thivenin": "Influenceuse française télé-réalité.",
    "Valouzz": "Influenceur humoristique français TikTok.",
    "Maskey": "Créateur français TikTok et influenceur musique.",

    # ------------------- COMEDIENS -------------------
    # Français (quasi exclusif)
    "Florent Peyre": "Humoriste français réalisant des sketchs et participations télévisées.",
    "Gad Elmaleh": "Comédien et humoriste français célèbre pour ses spectacles sur scène et vidéos en ligne.",
    "Kev Adams": "Comédien et humoriste français, créateur de vidéos et spectacles humoristiques.",
    "Franck Dubosc": "Comédien et humoriste français reconnu pour ses sketchs et interventions télévisées.",
    "Baptiste Lecaplain": "Humoriste français créant des vidéos et spectacles humoristiques en ligne.",
    "Anne Roumanoff": "Humoriste française connue pour ses chroniques et vidéos humoristiques sur internet.",
    "Jamel Debbouze": "Comédien et humoriste français, célèbre pour ses spectacles et vidéos comiques.",
    "Paul Mirabel": "Humoriste français au style absurde et minimaliste.",
    "Kyan Khojandi": "Comédien français, créateur de la série Bref et humoriste stand-up.",
    "Thomas Ngijol": "Comédien français au style énergique et engagé.",
    "Ahmed Sylla": "Humoriste français apprécié pour son humour physique et chaleureux.",
    "Jonathan Cohen": "Comédien français connu pour ses rôles humoristiques et parodiques.",

    # MEDIAS:
    # ------------------- INTERNATIONAUX -------------------
    "BBC": "Média public britannique couvrant l'information internationale, reconnu pour son sérieux et son influence.",
    "CNN": "Chaîne d'information américaine en continu, connue pour sa couverture des événements mondiaux.",
    "Al Jazeera": "Média qatari international en anglais et arabe, influent au Moyen-Orient et à l'international.",
    "The New York Times": "Journal américain de référence, très influent dans le monde.",
    "The Guardian": "Journal britannique reconnu pour ses enquêtes et son orientation progressiste.",
    "Reuters": "Agence de presse internationale basée à Londres, référence pour les dépêches d'actualité.",
    "Bloomberg": "Média américain spécialisé dans l'économie, la finance et les marchés mondiaux.",
    "Fox News": "Chaîne américaine d'information continue, connue pour sa ligne éditoriale conservatrice.",
    "Sky News": "Chaîne britannique d'information en continu.",
    "El País": "Journal espagnol de référence, diffusant à l'échelle internationale.",
    "Der Spiegel": "Magazine allemand influent, spécialisé dans les enquêtes et la politique.",
    "The Washington Post": "Grand quotidien américain, connu pour ses enquêtes et son sérieux journalistique.",

    # ------------------- FRANÇAIS -------------------
    "Le Monde": "Quotidien français de référence, couvrant l'actualité nationale et internationale.",
    "Le Figaro": "Grand quotidien français, orienté centre-droit, couvrant politique, économie et culture.",
    "Libération": "Journal français orienté à gauche, couvrant actualité, société et culture.",
    "Les Échos": "Quotidien français spécialisé dans l'économie et la finance.",
    "La Croix": "Journal français d'orientation catholique, couvrant société, politique et culture.",
    "France 24": "Chaîne d'information française en continu, diffusée à l'international.",
    "BFMTV": "Chaîne d'information en continu la plus suivie en France.",
    "CNews": "Chaîne française d'information continue, connue pour ses débats et son orientation marquée.",
    "LCI": "Chaîne d'information en continu du groupe TF1.",
    "TF1": "Première chaîne de télévision française généraliste.",
    "France 2": "Chaîne publique française généraliste, diffusant info, divertissement et culture.",
    "M6": "Chaîne privée française généraliste, connue pour ses émissions populaires.",
    "Arte": "Chaîne culturelle franco-allemande, diffusant documentaires, films et débats.",
    "Mediapart": "Média d'investigation en ligne, financé par ses abonnés, connu pour ses enquêtes.",
    "Radio France": "Groupe public français regroupant France Inter, France Info, France Culture, etc."
}

liste_des_dicos = ['dict_sportifs', 'dict_chanteurs', 'dict_evenements_historiques', 'dict_metiers',
                   'dict_animaux', 'dict_acteurs', 'dict_films_series','dict_livres_bd', 'dict_celebrites',
                   'dict_jeux_videos', 'dict_jeux_sports', 'dict_marques','dict_personnages_fiction',
                   'dict_objets_du_quotidien', 'dict_dessins_animes','dict_chansons', 'dict_plats_aliments',
                   'dict_phenomenes_emotions_sentiments', 'dict_mouvements_instruments', 'dict_influenceurs_medias']
mots_totaux = 0
for dico in liste_des_dicos:
    print(dico,f":{len(globals()[dico])}")
    mots_totaux+=len(globals()[dico])
print(mots_totaux)
nb_de_mots = 200
for l in liste_des_dicos:
    if nb_de_mots > len(globals()[l]):
        nb_de_mots = len(globals()[l])
print(nb_de_mots*len(liste_des_dicos))
print(nb_de_mots)
print(len(liste_des_dicos))

liste_ste_u = ["Cyane GOURDAULT-MONTAGNE", "Chloé CARDON", "Marilou GALLES", "Jasmine DUMANOIS", "Alexis PICHON",
               "Vincent BERTHOMIER", "Albertine VIALA", "Simon FOURCADE", "Arnaud OTT", "Zoé JUBERT",
               "Gabriel EL KHAZEN", "Achilkle GAMBIER", "Margaux AUBOUIN", "Emma PERRON", "Alexandre VITALl",
               "Cyprien MOREAU", "Côme MAINKA", "Myrtille VIENOT DE VAUBLANC", "Roman MEAULLE", "Sarah HOUNDJI",
               "Marie-Marthe MADJOULBA", "Ariane BOUTTIER", "Neïla ETHEVE", "Robin VERNIER", "Valentine ROUSSEAU",
               "Aristote BOURLET", "Annabelle FOURCADE", "Ferdinand ANGIBEAU", "Fanny MEARY", "Paul GUY",
               "Eloy HOUSSET", "Louis FOUGEROLE", "Maya BETHENOD", "Soline OUDOUMANESSAH", "Josefa CUGINI", "Samuel HYEST",
               "Paul MASSELIN","Valentine AIME-ROQUEBERT", "Romy ZAGOURY", "Romy PEREZ", "Lucie DU CHATELIER",
               "Alix FRANC DU BREIL","Grégoire SEGUELA", "Thaïs MEARY", "Jules MONTET", "Héloïse SACHOT",
               "Paul VAUTHIER", "Lorenzo PHILIPPE", "Nicola CORBELLINI", "Clarisse DA SILVA", "Constantin ASSAF",
               "Elena RAVILY-GELY", "Jeanne REYNAUD","Juliette FRETE", "Catherine LEE", "Milane ROULOT--GAMBOA",
               "Maud BREVET", "François DAVY", "Victoria CHAMBELLAN", "Pauline KOSTELITZ", "Mathieu D'ELBEE-LOPEZ",
               "Paul DE VORGES", "Pierre-Aimé LEFAFTA", "Jude METAIS", "Héloïse COLLET", "Alexia BOMBRUN",
               "Xavier DE LONGEVIALLE", "Charles BATAIILLE", "Jeanne BIGEARD", "Baptiste BIACHE", "Matthieu HOUDART",
               "Léopold BAUD", "Mila TROUILLER", "Andréas SCALISI", "Pauline SALAH", "Lazare BURG", "Nina GARCELON",
               "Victoria LEVIS", "Amandine CIVET", "Anaëlle BIACABE", "Antoine MOSCONI", "Salomé BURBAN",
               "Sixtine GLEIZES", "Hortense DU PLESSIX", " Margot TAMNGA", "Pauline HALBEHER", "Clémence BOYER",
               "Maëlys FOURNIER", "Rose DELAFAYE", "Oscar REMY", "Les Frères YUN", "Masae MAINCENT",
               "Emma-Louise GEORGE", "Anne DE KERMOAL", "Chloé FOURNIER", "Lucie PUJOL", "Diane CORNELOUP",
               "Alix JOLY", "Romain GUILLAUME", "Ombeline FERRERO", "Matthias CHEVALIER-JACOME", "Maguelone DELMAS",
               "Clara DAVIAUD", "Agathe THIBORD", "Eugénie VILAIHONGS", "Cybèle THOMASSONT-OJEIMI", "Emilie CAZENAVE",
               "Céleste DU PONTAVICE", "Camille FORT", "Camille NIQUET", "Chloé VANDROUX", "Marine GINEBRE",
               "Maxime FINAS", "Madeleine KERNEÏS", "Adrien DURAND", "Bruno TEIXEIRA", "Iris DE CHAUNAC-LANZAC",
               "Carlota CLEMENCE VAZQUEZ", "William LE VASLOT", "Théo DIEP-PEREIRA", "Gabrielle MALHERBE",
               "Blanche TAILLANDIER", "Ruben BERRHOUN", "Claire SEYDOUX", "Eva SAURET", "Delphine CHIROL", 
               "Mme THERMES", "M ALVES", "Mme HAMON", "Mme VENCENT", "Mme BARTHELEMY", "M DE BELZUNCE", "M RENE", 
               "M MBADINGA", "Mme ROUSSEAU", "M RINGEARD", "M SCIMECA", "M NOIRET", "M SIVANESAN", "Mme BIROUSTE", 
               "Mme D'HEROUEL", "Mme BINACHON", "MME SELLAM", "M BOUESTE", "Mme HERSENT", "M DE l'ESPINAY", "Mme JOUET", "Mme DUHESME",
               "Mme PAVLOVA", "Mme WARAS", "Mme DE TRUCHIS", "Mme HOARAU", "Mme PLANCHET"]

class CenteredTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.halign = 'center'
        self.multiline = False
        self.font_size = self.height * 0.6 if self.height else 20
        self.bind(height=self.adjust_font_size)

    def adjust_font_size(self, instance, value):
        # Adapter font_size seulement, pas padding_y
        self.font_size = max(value * 0.67, 10)



class MonJeu(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accueil(None)

    annonce_manche = ['1ere manche, aucune contrainte pour faire deviner!', '2eme manche, faites deviner en 1 mot!',
                      '3eme manche, faites deviner en mimant!']



    def calcul_score(self):
        self.tuples_classement = []
        for x,y in self.equipes_et_points.items():
            idx_classement = 0
            for couple in self.tuples_classement:
                if y < self.equipes_et_points[couple[0]]:
                    idx_classement += 1
            self.tuples_classement.insert(idx_classement, (x, y))
        self.dict_classement = dict(self.tuples_classement)
        print(self.dict_classement)
        return self.dict_classement

    def affichage_score(self, contenu):
        
        self.calcul_score()

        self.liste_classement = []
        for x,y in self.dict_classement.items():
            self.liste_classement.append("{}: {} points".format(x, y))
        self.string_classement = "\n".join(self.liste_classement)

        
        self.clear_widgets()
        scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False)

        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        self.label = Label(text="\n{}:\n\n{}".format(contenu, self.string_classement),
                           size_hint=(0.9, None),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='35sp'
                           )
        
        
        self.label.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.label.bind(size=self._update_text_size)
        layout.add_widget(self.label)
        scroll.add_widget(layout)
        self.add_widget(scroll)

    def arreter_jeu(self, dt):
        self.fin_chrono = True
        self.faux_label = Label(text="non")
        self.verif(self.faux_label)

    def accueil(self, instance):
        self.accès_spécial = False
        self.clear_widgets()

        self.label = Label(text="Tmz'up\ndu\nPeuple",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.65},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='60sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.bouton = Button(text="Jouer", size_hint=(0.6, 0.2), pos_hint={"center_x": 0.5, "center_y": 0.25},
                             background_color=(0/255, 128/255, 255/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
        self.bouton.bind(on_press=self.choix_equipes)
        self.add_widget(self.bouton)
        self.bouton = Button(text="*", size_hint=(0.2, 0.1), pos_hint={"x": 0.8, "y": 0.9}, 
                             background_color=(0, 0, 0, 0), color=(255/255, 215/255, 0/255, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='50sp')
        self.bouton.bind(on_press=self.code_secret)
        self.add_widget(self.bouton)
    
    def code_secret(self, instance):
        self.clear_widgets()

        self.label = Label(text="Entrer le code secret :",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.7},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.input = CenteredTextInput(
            multiline=False,
            size_hint=(0.8, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=35,
            halign="center",
            font_name="Fredoka-Regular.ttf"
            )
        self.add_widget(self.input)
        Clock.schedule_once(lambda dt: setattr(self.input, 'focus', True), 0.1)

        self.bouton = Button(text="Valider", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                            background_color=(0/255, 142/255, 35/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=self.verif_code)
        self.add_widget(self.bouton)

        self.bouton = Button(text="X", size_hint=(0.2, 0.1), pos_hint={"x": 0.8, "y": 0.9}, 
                             background_color=(139/255, 0/255, 0/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='40sp')
        self.bouton.bind(on_press=self.accueil)
        self.add_widget(self.bouton)

    def verif_code(self, instance):
        self.tentative_code_secret = self.input.text
        if self.tentative_code_secret == "FKOZPMEZSZ":
            self.accès_spécial = True
            self.choix_equipes(None)
        else:
            self.label.text = "Code invalide"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', "Entrer le code secret :"), 1)


    def choix_equipes(self, instance):
        self.mode_mort_subite = False
        self.manche = 1
        self.tour = 0
        self.clear_widgets()

        self.label = Label(text="Combien d'équipes : ",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.input = CenteredTextInput(
            multiline=False,
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=35,
            halign="center",
            font_name="Fredoka-Regular.ttf"
            )
        self.add_widget(self.input)
        Clock.schedule_once(lambda dt: setattr(self.input, 'focus', True), 0.1)

        self.bouton = Button(text="Valider", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                            background_color=(0/255, 142/255, 35/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=self.equipes_choisies)
        self.add_widget(self.bouton)

    def _update_text_size(self, instance, value):
        instance.text_size = (instance.width, None)


    def equipes_choisies(self, instance):
        try:
            if int(float(self.input.text)) < 1 or int(float(self.input.text)) > 20:
                self.nb_equipes_bug = self.input.text + "M"
                self.nb_equipes = int(float(self.nb_equipes_bug))
            else:
                self.nb_equipes = int(float(self.input.text))
            self.equipes_et_points = {}
            for x in range(self.nb_equipes):
                self.equipes_et_points["Equipe {}".format(x + 1)] = 0
            print(self.equipes_et_points)

            self.equipes = []
            for x in range(10000):
                for team in self.equipes_et_points:
                    self.equipes.append(team)

            self.choix_mots()
        except ValueError:
            self.label.text = "Max 20 équipes!"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', "Combien d'équipes : "), 1)

    def choix_mots(self):
        self.clear_widgets()
        self.label = Label(text='Combien de mots pour cette partie: ',
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.input = CenteredTextInput(
            multiline=False,
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=35,
            halign="center",
            font_name="Fredoka-Regular.ttf"
            )
        self.add_widget(self.input)
        Clock.schedule_once(lambda dt: setattr(self.input, 'focus', True), 0.1)

        self.bouton = Button(text="Valider", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                            background_color=(0/255, 142/255, 35/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=self.mots_choisis)
        self.add_widget(self.bouton)

    def mots_choisis(self, instance):
        try:
            if int(float(self.input.text)) <= 0 or int(float(self.input.text)) > 1000:
                self.nb_mots_bug = self.input.text + "M"
                self.nb_mots = int(float(self.nb_mots_bug))
            else:
                self.nb_mots = int(float(self.input.text))

            if self.accès_spécial:
                if int(float(self.input.text)) > len(liste_ste_u)-self.nb_equipes:#le nombre max d'équipes (au cas où pour la mort subite)
                    self.nb_mots_bug = self.input.text + "M"
                    self.nb_mots = int(float(self.nb_mots_bug))
                else:  
                    self.mots = random.sample(liste_ste_u, self.nb_mots+self.nb_equipes)
                    self.mots_phase_principale = self.mots[:self.nb_mots]
                    self.mots_mort_subite = self.mots[self.nb_mots:]
                    self.mots_round = {1: self.mots_phase_principale, 2: self.mots_phase_principale, 3: self.mots_phase_principale}
            
            else:
                if self.nb_mots < len(liste_des_dicos)-self.nb_equipes:
                    self.categories = random.sample(liste_des_dicos, self.nb_mots+self.nb_equipes)
                    self.dict_nb_mots_par_categorie = {}
                    for cat in self.categories:
                        self.dict_nb_mots_par_categorie[cat] = 1
                    self.liste_mots = []
                    self.dict_mot_dict = {}
                    for x, y in self.dict_nb_mots_par_categorie.items():
                        self.liste_boucle = random.sample(list(globals()[x]), y)
                        self.liste_mots.extend(self.liste_boucle)
                        for mot in self.liste_boucle:
                            self.dict_mot_dict[mot] = x
                    print(self.dict_mot_dict)
                
                else:
                    self.categories = random.sample(liste_des_dicos, len(liste_des_dicos))
                    self.dict_nb_mots_par_categorie = {}
                    for cat in self.categories:
                        self.dict_nb_mots_par_categorie[cat] = 0
                    nums = 0
                    while nums < self.nb_mots+self.nb_equipes:
                        for cat in self.categories:
                            if nums == self.nb_mots+self.nb_equipes:
                                break
                            self.dict_nb_mots_par_categorie[cat] += 1
                            nums += 1
                    self.liste_mots = []
                    self.dict_mot_dict = {}
                    for x, y in self.dict_nb_mots_par_categorie.items():
                        self.liste_boucle = random.sample(list(globals()[x]), y)
                        self.liste_mots.extend(self.liste_boucle)
                        for mot in self.liste_boucle:                           
                            self.dict_mot_dict[mot] = x
                    print(self.dict_mot_dict)
                self.mots = random.sample(self.liste_mots, self.nb_mots+self.nb_equipes)
                self.mots_phase_principale = self.mots[:self.nb_mots]
                self.mots_mort_subite = self.mots[self.nb_mots:]
                self.mots_round = {1: self.mots_phase_principale, 2: self.mots_phase_principale, 3: self.mots_phase_principale}
            self.choix_temps()

        except ValueError:
            if self.accès_spécial:
                self.label.text = "Max {} mots!".format(len(liste_ste_u)-self.nb_equipes)
            else:
                self.label.text = "Max 1000 mots!"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', 'Combien de mots pour cette partie: '), 1)

    def choix_temps(self):
        self.clear_widgets()
        self.label = Label(text="Temps entre chaque tour?",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.input = CenteredTextInput(
            multiline=False,
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=35,
            halign="center",
            font_name="Fredoka-Regular.ttf"
            )
        self.add_widget(self.input)
        Clock.schedule_once(lambda dt: setattr(self.input, 'focus', True), 0.1)

        self.bouton = Button(text="Valider", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                            background_color=(0/255, 142/255, 35/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=self.temps_choisi)
        self.add_widget(self.bouton)

    def temps_choisi(self, instance):
        try:
            if int(float(self.input.text)) <= 0:
                self.temps_max_bug = self.input.text + "M"
                self.temps_max = int(float(self.temps_max_bug))
            else:
                self.temps_max = int(float(self.input.text))
            if self.accès_spécial:
                self.affiche_manche()
                return
            self.choix_nb_indices()

        except ValueError:
            self.label.text = "Entre un nombre positif!"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', "Temps entre chaque tour?"), 1)

    def choix_nb_indices(self):
        self.clear_widgets()
        self.label = Label(text="Nombre d'indices par équipe?",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)
        self.input = CenteredTextInput(
            multiline=False,
            size_hint=(0.2, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_size=35,
            halign="center",
            font_name="Fredoka-Regular.ttf"
            )
        self.add_widget(self.input)
        Clock.schedule_once(lambda dt: setattr(self.input, 'focus', True), 0.1)

        self.bouton = Button(text="Valider", size_hint=(0.3, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.2},
                            background_color=(0/255, 142/255, 35/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=self.nb_indices_choisi)
        self.add_widget(self.bouton)

    def nb_indices_choisi(self, instance):
        try:
            if int(float(self.input.text)) < 0:
                self.nb_indices_bug = self.input.text + "M"
                self.nb_indices = int(float(self.nb_indices_bug))
            else:
                self.nb_indices = int(float(self.input.text))
            self.dict_indices = {}
            for team in self.equipes_et_points:
                self.dict_indices[team] = self.nb_indices
            print(self.dict_indices)
            self.affiche_manche()

        except ValueError:
            self.label.text = "Entre un nombre positif!"
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', "Nombre d'indices par équipe?"), 1)


    def affiche_manche(self):
        self.clear_widgets()
        self.label = Label(text=self.annonce_manche[self.manche - 1],
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.mots_melanges = random.sample(self.mots_round[self.manche], len(self.mots_round[self.manche]))
        self.min_une_bonne_reponse = False
        self.bouton = Button(size_hint=(1, 1),
                            background_color=(0,0,0,0))
        self.bouton.bind(on_press=lambda x: self.pret())
        self.add_widget(self.bouton)

    def pret(self):
        print("{}, prête:".format(self.equipes[self.tour]))
        print("tour",self.tour)
        if self.mode_mort_subite:
            if self.mot_index_mort_subite == len(self.mots_mort_subite):
                self.affichage_mot_fin_partie()
                return
            else:
                self.indice_appuye = False
                self.mot_index = 1 #au cas où au dernier tour de la 3e manche il n'y ait plus qu'un mot à faire deviner (et qu'on utilise pas d'indice), alors cette variable reste à 0 et donc en mort subit le minuteur se lance, ce qu'on ne veut pas dans le mode mort subite
            
        elif sum(list(self.equipes_et_points.values())) % self.nb_mots == 0 and self.min_une_bonne_reponse:
            print(self.mot_index)
            print(self.indice_appuye)
            self.manche += 1
            self.scores()
            return
        else:
            self.indice_appuye = False
            self.fin_chrono = False
            self.dernier_mot_trouve = False
            self.idx = len(self.mots_melanges)
            self.mot_index = 0
            self.copie_mots = self.mots_melanges[:]
        
        self.texte_du_label_pret = [self.equipes_mort_subite[self.mot_index_mort_subite] if self.mode_mort_subite else self.equipes[self.tour] for x in range(1)]
        self.clear_widgets()
        self.label = Label(text="{}, prête:".format(self.texte_du_label_pret[0]),
                        size_hint=(0.8, 0.2),
                        pos_hint={'center_x': 0.5, 'center_y': 0.6},
                        halign="center",
                        valign="middle",
                        font_name="Fredoka-Regular.ttf",
                        font_size='40sp'
                        )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.bouton = Button(text="Commencer", size_hint=(0.5, 0.1), pos_hint={'center_x': 0.5, 'center_y': 0.3}, halign="center", valign="middle",
                            background_color=(252/255, 81/255, 110/255, 1), color=(1, 1, 1, 1), font_name="Fredoka-Regular.ttf",
                            font_size='24sp')
        self.bouton.bind(on_press=lambda x: self.Tour())
        self.add_widget(self.bouton)
    
    def scores(self):
        self.clear_widgets()
        if sum(list(self.equipes_et_points.values())) == self.nb_mots*3:
            self.calcul_score()
            self.equipes_egalite = 1
            for equipe in list(self.dict_classement)[1:]:
                if self.dict_classement[list(self.dict_classement)[0]]>self.dict_classement[equipe]:
                    break
                self.equipes_egalite+=1
            print(self.equipes_egalite)
            if self.equipes_egalite > 1:
                self.clear_widgets
                self.label = Label(text="{} équipes sont à égalité, que choisissez vous:".format(self.equipes_egalite),
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.8},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
                self.label.bind(size=self._update_text_size)

                self.add_widget(self.label)

                self.bouton = Button(text="Mort subite", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.25, "center_y": 0.25},
                             background_color=(76/255, 0/255, 153/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
                self.bouton.bind(on_press=self.decision_egalite)
                self.add_widget(self.bouton)
                self.bouton = Button(text="Match nul", size_hint=(0.5, 0.5), pos_hint={"center_x": 0.75, "center_y": 0.25},
                             background_color=(192/255, 192/255, 192/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
                self.bouton.bind(on_press=self.decision_egalite)
                self.add_widget(self.bouton)
                return

            else:
                self.affichage_mot_fin_partie()
                return
                
        self.affichage_score("Score à la fin de la manche {}".format(self.manche-1))
        self.bouton = Button(size_hint=(1, 1),
                            background_color=(0,0,0,0))
        self.bouton.bind(on_press=lambda x: self.affiche_manche())
        self.add_widget(self.bouton)
    
    def affichage_mot_fin_partie(self):
        self.clear_widgets()
        self.label = Label(text="Fin de la partie!",
                        size_hint=(0.8, 0.2),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        halign="center",
                        valign="middle",
                        font_name="Fredoka-Regular.ttf",
                        font_size='40sp'
                        )
        self.label.bind(size=self._update_text_size)
        self.add_widget(self.label)
        if self.mode_mort_subite:
            Clock.schedule_once(self.verdict_mort_subite, 3)
        else:
            Clock.schedule_once(self.resultat_final, 3)


    def decision_egalite(self, instance):
        if instance.text == "Mort subite":
            self.mot_index_mort_subite = 0
            self.mode_mort_subite = True
            self.mots_mort_subite = self.mots_mort_subite[:self.equipes_egalite]
            self.equipes_mort_subite = list(self.dict_classement)[:self.equipes_egalite]
            #self.dict_chrono_mort_subite = {x:y for x,y in zip(self.equipes_mort_subite, [0 for x in range(len(self.equipes_mort_subite))])}
            self.dict_chrono_mort_subite = {}
            print(self.equipes_mort_subite)
            print(self.mots_mort_subite)
            print(self.dict_chrono_mort_subite)
            self.clear_widgets()
            self.label = Label(text="Chaque équipe à égalité va avoir un mot à faire deviner le plus rapidement possible.",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.5},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
            self.label.bind(size=self._update_text_size)
            self.add_widget(self.label)
            self.bouton = Button(size_hint=(1, 1),
                            background_color=(0,0,0,0))
            Clock.schedule_once(lambda dt: setattr(self.label, 'text', "L'équipe la plus rapide remporte la partie!"), 3)
            Clock.schedule_once(lambda dt: self.bouton.bind(on_press=lambda x: self.pret()), 3)


            self.add_widget(self.bouton)

        else:
            self.affichage_mot_fin_partie()


    def Tour(self):
        print(self.mots_melanges)
        print(sum(list(self.equipes_et_points.values())))
        self.texte_du_label_Tour = [self.mots_mort_subite[self.mot_index_mort_subite] if self.mode_mort_subite else self.copie_mots[self.mot_index] for x in range(1)]
        self.clear_widgets()
        if self.mode_mort_subite and not self.indice_appuye:
            self.start = time.perf_counter()
        if self.mot_index == 0 and not self.indice_appuye:
            self.timer = Clock.schedule_once(self.arreter_jeu, self.temps_max)

        self.label = Label(text=self.texte_du_label_Tour[0],
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.7},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='40sp'
                           )
        self.label.bind(size=self._update_text_size)

        self.add_widget(self.label)

        self.bouton = Button(text="oui", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.25, "center_y": 0.4}, 
                             background_color=(255/255, 255/255, 0/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
        self.bouton.bind(on_press=self.verif)
        self.add_widget(self.bouton)

        self.bouton = Button(text="non", size_hint=(0.5, 0.1), pos_hint={"center_x": 0.75, "center_y": 0.4},
                             background_color=(205/255, 133/255, 63/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
        self.bouton.bind(on_press=self.verif)
        self.add_widget(self.bouton)

        if not self.accès_spécial:
            self.bouton = Button(text="?", size_hint=(0.2, 0.1), pos_hint={"x": 0.8, "y": 0.9}, 
                             background_color=(0, 0, 0, 0), color=(255/255, 215/255, 0/255, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
            self.bouton.bind(on_press=self.verif_indice)
            self.add_widget(self.bouton)

    def verif_indice(self, instance):
        self.indice_appuye = True
        if self.dict_indices[self.texte_du_label_pret[0]]>0:
            self.dict_indices[self.texte_du_label_pret[0]] -= 1
            self.clear_widgets()
            self.label = Label(text=globals()[self.dict_mot_dict[self.texte_du_label_Tour[0]]][self.texte_du_label_Tour[0]],
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.7},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='30sp'
                           )
            self.label.bind(size=self._update_text_size)
            self.add_widget(self.label)

            if self.dict_indices[self.texte_du_label_pret[0]] == 1:
                self.label = Label(text="(Il ne vous reste plus qu'1 indice)",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.25},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='20sp'
                           )
                self.label.bind(size=self._update_text_size)
                self.add_widget(self.label)

            elif self.dict_indices[self.texte_du_label_pret[0]] == 0:
                self.label = Label(text="(Il ne vous reste plus aucun indice)",
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.25},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='20sp'
                           )
                self.label.bind(size=self._update_text_size)
                self.add_widget(self.label)
            else:
                self.label = Label(text="(Il ne vous reste plus que {} indices)".format(self.dict_indices[self.texte_du_label_pret[0]]),
                           size_hint=(0.8, 0.2),
                           pos_hint={'center_x': 0.5, 'center_y': 0.25},
                           halign="center",
                           valign="middle",
                           font_name="Fredoka-Regular.ttf",
                           font_size='20sp'
                           )
                self.label.bind(size=self._update_text_size)
                self.add_widget(self.label)
            self.bouton = Button(text="retour", size_hint=(0.6, 0.1), pos_hint={"x": 0.2, "y": 0.1},
                                  background_color=(139/255, 0/255, 0/255, 1), color=(1, 1, 1, 1),
                                    font_name="Fredoka-Regular.ttf", font_size='24sp')
            self.bouton.bind(on_press=lambda x: self.Tour())
            self.add_widget(self.bouton)
        else:
            self.label = Label(
                text="Vous n'avez plus d'indice en réserve!",
                size_hint=(0.6, 0.1),
                pos_hint={"x": 0.2, "y": 0.5}, 
                color=(255/255, 0, 0, 1)
                )
            self.add_widget(self.label)


    def verif(self, instance):
        if instance.text == "oui":
            print("oui")
            if self.mode_mort_subite:
                self.end = time.perf_counter()
                self.chrono_mort_subite = self.end - self.start
                self.dict_chrono_mort_subite[self.chrono_mort_subite] = self.texte_du_label_pret[0]
                self.mot_index_mort_subite += 1
                print(self.dict_chrono_mort_subite)
                self.pret()
                return

            else:
                self.mots_melanges.pop(0)
                self.equipes_et_points[self.equipes[self.tour]] += 1
                self.dernier_mot_trouve = True
                self.min_une_bonne_reponse = True
        else:
            print("non")
            if self.mode_mort_subite:
                self.dict_chrono_mort_subite[f"/{self.mot_index_mort_subite}"] = self.texte_du_label_pret[0]
                self.mot_index_mort_subite += 1
                self.pret()
                return

            else:
                print(self.mots_melanges)
                self.mots_melanges.append(self.mots_melanges[0])
                self.mots_melanges.pop(0)
                self.dernier_mot_trouve = False

        self.idx -= 1

        if self.fin_chrono or self.mot_index == len(self.copie_mots) - 1:
            self.timer.cancel()
            print("fin du tour")
            if self.dernier_mot_trouve:
                self.replace_sequence = random.sample(self.mots_melanges[self.idx:], len(self.mots_melanges[self.idx:]))
                self.mots_melanges[self.idx:] = self.replace_sequence
                self.tour += 1
                self.pret()
                return

            else:
                self.mots_melanges.insert(0, self.mots_melanges[-1])
                self.mots_melanges.pop(-1)
                self.replace_sequence = random.sample(self.mots_melanges[self.idx + 1:],
                                                      len(self.mots_melanges[self.idx + 1:]))
                self.mots_melanges[self.idx + 1:] = self.replace_sequence
                self.tour += 1
                self.pret()
                return
        self.mot_index += 1
        self.Tour()

    def verdict_mort_subite(self, dt):
        self.dict_rep_non_mort_subite = {}
        for chrno in list(self.dict_chrono_mort_subite)[:]:
            if type(chrno)==float:
                pass
            elif "/" in chrno:
                self.dict_rep_non_mort_subite[chrno] = self.dict_chrono_mort_subite[chrno]
                self.dict_chrono_mort_subite.pop(chrno)

        self.classement_mort_subite = sorted(self.dict_chrono_mort_subite)
        self.texte_du_label_mort_subite = ["C'est l'{} qui l'emporte avec un temps de {}s.".format(self.dict_chrono_mort_subite[self.classement_mort_subite[0]], round(self.classement_mort_subite[0], 3))
                                            if len(self.classement_mort_subite)>0 else "Personne n'a trouvé son mot, il y a donc match nul." for x in range(1)]

        self.clear_widgets()
        self.label = Label(text=self.texte_du_label_mort_subite[0],
                        size_hint=(0.8, 0.2),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
                        halign="center",
                        valign="middle",
                        font_name="Fredoka-Regular.ttf",
                        font_size='40sp'
                        )
        self.label.bind(size=self._update_text_size)
        self.add_widget(self.label)
        Clock.schedule_once(self.resultat_final, 3)
    def resultat_final(self, dt):
        if self.mode_mort_subite:
            self.liste_classement = []
            for x,y in self.dict_classement.items():
                self.liste_classement.append("{}: {} points".format(x, y))
            self.liste_classement_mort_subite = self.liste_classement[self.equipes_egalite:]
            self.classement_mort_subite.sort(reverse=True)
            for x,y in self.dict_rep_non_mort_subite.items():
                self.dict_chrono_mort_subite[x]=y
                self.classement_mort_subite.insert(0,x)
            print(self.dict_rep_non_mort_subite)
            print(self.dict_chrono_mort_subite)
            print(self.classement_mort_subite)

            for chrono in self.classement_mort_subite:
                if type(chrono)==float:
                    self.liste_classement_mort_subite.insert(0, "{}: {} points ({}s)".format(self.dict_chrono_mort_subite[chrono], self.dict_classement[self.dict_chrono_mort_subite[chrono]],round(chrono, 3)))
                elif "/" in chrono:
                    self.liste_classement_mort_subite.insert(0, "{}: {} points (/)".format(self.dict_chrono_mort_subite[chrono], self.dict_classement[self.dict_chrono_mort_subite[chrono]]))
            self.string_classement = "\n".join(self.liste_classement_mort_subite)

            
            self.clear_widgets()
            scroll = ScrollView(size_hint=(1, 1), do_scroll_x=False)

            layout = BoxLayout(orientation='vertical', size_hint_y=None)
            layout.bind(minimum_height=layout.setter('height'))
            self.label = Label(text="\n{}:\n\n{}".format("Score final", self.string_classement),
                            size_hint=(0.9, None),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            halign="center",
                            valign="middle",
                            font_name="Fredoka-Regular.ttf",
                            font_size='35sp'
                            )
            
            self.label.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
            self.label.bind(size=self._update_text_size)
            layout.add_widget(self.label)
            scroll.add_widget(layout)
            self.add_widget(scroll)

            self.bouton = Button(size_hint=(1, 1),
                            background_color=(0,0,0,0))
            self.bouton.bind(on_press=self.fin_partie)
            self.add_widget(self.bouton)
            
            #Clock.schedule_once(self.fin_partie, 10)
        else:
            self.affichage_score("Score final")
            self.bouton = Button(size_hint=(1, 1),
                            background_color=(0,0,0,0))
            self.bouton.bind(on_press=self.fin_partie)
            self.add_widget(self.bouton)
            #Clock.schedule_once(self.fin_partie, 2)
    
    def fin_partie(self, instance):
        self.accès_spécial = False
        self.clear_widgets()
        self.bouton = Button(text="Nouvelle Partie", size_hint=(1, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.75},
                             background_color=(0/255, 128/255, 255/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
        self.bouton.bind(on_press=self.choix_equipes)
        self.add_widget(self.bouton)

        self.bouton = Button(text="Quitter", size_hint=(1, 0.5), pos_hint={"center_x": 0.5, "center_y": 0.25},
                             background_color=(246/255, 119/255, 34/255, 1), color=(1, 1, 1, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='24sp')
        self.bouton.bind(on_press=lambda x: App.get_running_app().stop())
        self.add_widget(self.bouton)
        self.bouton = Button(text="*", size_hint=(0.2, 0.1), pos_hint={"x": 0.8, "y": 0.9}, 
                             background_color=(0, 0, 0, 0), color=(255/255, 215/255, 0/255, 1), 
                             font_name="Fredoka-Regular.ttf", font_size='50sp')
        self.bouton.bind(on_press=self.code_secret)
        self.add_widget(self.bouton)




                        

partie = MonJeu()


class JeuApp(App):
    def build(self):
        return partie


JeuApp().run()
