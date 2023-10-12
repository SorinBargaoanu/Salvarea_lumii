def get(strings_id):
    if strings_id == "Welcome":
        return ("Într-o lume unde timpul a uitat de om, dinozaurii trăiesc în pace și armonie.\n"
                "Ei se adună pentru a juca un joc tradițional numit 'Pui vs Părinți', un joc care, deși amical, "
                "este plin de competiție și curaj.\n"
                "Dar astăzi nu este o zi obișnuită. Astăzi, destinul lumii lor este pus la încercare.\n")        
    elif strings_id == "Welcome2":
        return ("Vulcanul sacru a erupt, amenințând să distrugă tot ce aceste creaturi iubesc și cunosc.\n"
                "Dar speranța nu este pierdută.\n"
                "Șase dinozauri curajoși s-au ridicat pentru a face față amenințării și a salva lumea lor:\n"
                "Ruaiti, Tirics, Scundi, Rozi, Veli si Speri\n")
    elif strings_id == "Welcome3":
        return ("Ruaiti: 'Salut, străine! Suntem în mare nevoie de ajutor. Te-ai alăturat nouă la timp.'\n"
                "Tirics: 'Vulcanul trebuie oprit, altfel totul va fi distrus.'\n"
                "Scundi: 'Avem un plan, dar avem nevoie de cineva ca tine pentru a-l pune în practică.'\n"
                "Rozi: 'Ești pregătit să te alături nouă în această misiune periculoasă?'\n")
    elif strings_id == "Welcome4":
        return "Rozi: 'Excelent! Vino cu noi și hai să salvăm lumea!'\n"
    elif strings_id == "Start":
        return ("După ce ai acceptat invitația de a ajuta, Ruaiti vine în față și zâmbește, "
                "bucurându-se de alegerea făcută.\n"
                "Ruaiti: 'Bine ai venit în echipa noastră! Fiecare dintre noi are un rol special în acest plan, "
                "dar avem nevoie de tine pentru a ne coordona și a ne ajuta să facem față provocărilor.'\n")
    elif strings_id == "Start2":
        return ("Ruaiti: 'Avem trei misiuni cruciale. Poți alege cu care să începi:'\n"
                "1. Misiunea Scurgerii. Trebuie să găsim scurgerea secretă a vulcanului și să tragem dopul. "
                "Scundi și Rozi se ocupă de asta, dar avem nevoie de cineva care să ne ajute să o localizăm "
                "și să evităm pericolele.\n"
                "2. Misiunea Baricadei - condusă de Veli și Speri. Trebuie să blochăm craterele vulcanului cu roci "
                "masive pentru a opri erupția permanent. Dar avem nevoie de ajutor pentru a transporta rocile "
                "și a lupta împotriva creaturilor care păzesc craterele.\n"
                "3. Misiunea Pazei - condusă de mine și Tirics. Aceasta implică apărarea echipei de creaturile "
                "periculoase și de dinozaurii rău intenționați.\n"
                "\nTe rog să alegi cu care misiune vrei să începi introducând numărul corespunzător "
                "și apoi să apeși 'Enter': ")
    elif strings_id == "Mission1Title":
        return "\nMisiunea 1: Căutarea Dopului Vulcanului"
    elif strings_id == "Mission1Text1":
        return ("\nAjungând la poalele muntelui vulcanic, Veli și Speri se confruntă cu o perspectivă măreață. "
                "În fața lor, vulcanul își varsă furia sub formă de lavă și fum. Pe măsură ce erupția se intensifică, "
                "cei doi dinozauri realizează că singura șansă de a opri erupția este să găsească și să plaseze "
                "un dop gigant pentru a bloca deschiderea vulcanului.")
    elif strings_id == "Mission1Text2":
        return ("Veli: 'Am auzit de trei locuri unde s-ar putea afla acest dop. Fiecare dintre acestea este păzit "
                "de provocări diferite și creaturi misterioase. E esențial să găsim dopul "
                "și să salvăm lumea dinozaurilor.'\n"
                "Speri: 'E o misiune periculoasă, dar știu că putem reuși împreună. "
                "Unde crezi că ar trebui să începem?'")
    elif strings_id == "Mission1Text3":
        return ("Veli: 'Avem următoarele opțiuni:'\n"
                "1. Valea Aburilor: O vale adâncă unde aburii fierbinți se ridică din sol. Se spune că în centrul "
                "acestei văi se află o piatră mistică care poate funcționa ca dop.\n"
                "2. Labirintul Lavic: Un labirint sinuos creat din cursuri solide de lavă. Legenda spune că la "
                "centrul labirintului există o rocă care poate opri vulcanul.\n"
                "3. Gardienii Scurgerii: Un sanctuar păzit de creaturi misterioase făcute din stâncă și metal. "
                "Se crede că aceste creaturi păzesc dopul final necesar pentru a opri erupția.\n"
                "\nTe rog să alegi cu care submisiune vrei să începi introducând numărul corespunzător "
                "și apoi să apeși 'Enter': ")
    elif strings_id == "Mission1Job1Choices":
        return (
            "Rozi: 'Valea Aburilor este cunoscută pentru capcanele și pericolele sale. "
            "Avem mai multe rute de explorat. "
            "Care crezi că ar fi cea mai bună abordare?'\n"
            "1. Ruta Cascadelor Fierbinți: 'Se spune că pe această rută, un vechi erou a găsit "
            "o cheie misterioasă care deschide camere secrete.'\n"
            "2. Trecerea Prin Gheizere: 'Este cea mai rapidă cale, dar și cea mai periculoasă. "
            "Vapori fierbinți explodează din pământ la intervale regulate.'\n"
            "3. Calea Labirintului de Vapori: 'Un labirint natural creat de fântânile termale. "
            "Dacă reușim să trecem, artefactul ar putea fi în centru.'")
    elif strings_id == "Mission1Job1Choice1":
        return (
            "Scundi: 'Cascadele Fierbinți! Este o alegere curajoasă. Am auzit povești despre frumusețea lor hipnotică, "
            "dar și despre capcanele ascunse.'")
    elif strings_id == "Mission1Job1Choice2":
        return (
            "Rozi: 'Trecerea Prin Gheizere este o provocare chiar și pentru cei mai îndrăzneți dintre noi. "
            "Vom avea nevoie de toate abilitățile noastre pentru a evita vaporii fierbinți.'")
    elif strings_id == "Mission1Job1Choice3":
        return (
            "Scundi: 'Labirintul de Vapori... Am visat să-l explorez! Se spune că nimeni "
            "nu a reușit vreodată să ajungă la centrul său. Să sperăm că vom fi primii!'")
    elif strings_id == "Mission1Job1Conclusion":
        return (
            "Rozi: 'Indiferent de calea aleasă, am făcut un progres semnificativ. Dar nu putem uita de misiunea "
            "noastră principală. Artefactul este esențial pentru supraviețuirea noastră și a dinozaurilor.'")
    elif strings_id == "Mission1Job2Choices":
        return (
            "Rozi: 'Labirintul Lavic este cunoscut pentru pereții săi fierbinți și canalele cu lavă. Avem mai multe "
            "indicii care ne pot ajuta să găsim piatra. Care crezi că ar fi cea mai bună abordare?'\n"
            "1. Urmează inscripțiile antice: 'Am descoperit texte vechi gravate pe pereți care indică posibila "
            "locație a pietrei magice.'\n"
            "2. Explorează canalele cu lavă: 'Chiar dacă este periculos, lava curgătoare ar putea să ne conducă "
            "spre camera unde se află piatra.'\n"
            "3. Urmărește ecourile: 'Unele coridoare ale labirintului emit ecouri misterioase. "
            "Acestea ar putea indica drumul corect spre destinație.'")
    elif strings_id == "Mission1Job2Choice1":
        return (
            "Scundi: 'Inscripțiile sunt adesea înșelătoare, dar cred că acestea ne pot conduce spre piatra magică. "
            "Trebuie doar să descifram mesajele corect.'")
    elif strings_id == "Mission1Job2Choice2":
        return (
            "Rozi: 'Canalele cu lavă sunt periculoase, dar riscul poate fi recompensat. "
            "Piatra ar putea fi ascunsă într-o cameră încălzită de aceste canale.'")
    elif strings_id == "Mission1Job2Choice3":
        return (
            "Scundi: 'Ecourile! Am auzit povești despre ele. Se spune că spiritul vulcanului vorbește "
            "prin ecouri pentru a-i ghida pe cei vrednici.'")
    elif strings_id == "Mission1Job2Conclusion":
        return (
            "Rozi: 'Fiecare indiciu și decizie ne apropie mai mult de piatra magică. Trebuie să fim vigilenți "
            "și să ne păstrăm forțele pentru momentul final. Vulcanul devine tot mai activ.'")
    elif strings_id == "Mission1Job3Start1":
        return ("Narator: În timp ce pasajul se lărgește, lumina slabă a lavii aruncă umbre pe pereții tunelului. "
                "Scundi și Rozi ajung la intrarea scurgerii, doar pentru a fi opriți de niște siluete "
                "înalte și amenințătoare.\n")
    elif strings_id == "Mission1Job3Start2":
        return ("Rozi: 'Aceștia trebuie să fie Gardienii Scurgerii despre care am auzit! Cum vom trece de ei?'"
                "\nScundi: 'Artefactul și piatra magică pe care le-am obținut ar trebui să ne ajute. "
                "Trebuie să găsim o cale de a le folosi corect.'")
    elif strings_id == "Mission1Job3Start3":
        return ("Scundi, cu piatra strălucitoare în mână, începe să recite un vechi cântec pe care l-a învățat. "
                "Gardienii, atrași de lumina pietrei, încep să se miște lent către ei, hipnotizați. "
                "Rozi folosește acest moment "
                "și plasează artefactul în mijlocul lor, activându-l. Un val de energie emană, calmand Gardienii "
                "și deschizând drumul spre dop.")
    elif strings_id == "Mission1Job3Start4":
        return ("Rozi: 'A fost mai ușor decât mă așteptam! Cu acești Gardieni în afara jocului, putem continua.'"
                "\nNarator: Cu Gardienii neutralizați și drumul deschis, Scundi și Rozi se îndreaptă rapid "
                "spre dopul vulcanului, "
                "sperând să elibereze presiunea înainte ca totul să explodeze.")
    elif strings_id == "Mission1Job3Return":
        return "Scundi: 'Ar fi bine să revedem opțiunile. Putem folosi artefactul sau piatra într-un alt mod?'\n"
    elif strings_id == "Mission1Job3ErrorOnJob1_1":
        return ("Narator: Încercând să folosească doar artefactul, Gardienii par să devină și mai agresivi. "
                "Pietra magică pare să fie cheia, dar este prea târziu acum.")
    elif strings_id == "Mission1Job3ErrorOnJob1_2":
        return ("Rozi: 'Poate că am subestimat puterea acestor Gardieni. Fără piatra, nu avem cum să-i oprim!'"
                "\nScundi: 'Trebuie să găsim un alt mod de a trece sau să revenim cu piatra.'")
    elif strings_id == "Mission1Job3ErrorOnJob1_3":
        return ("Narator: Deși au făcut tot posibilul să treacă fără a utiliza piatra, Gardienii erau prea puternici. "
                "Fără a putea deschide scurgerea, presiunea din vulcan continuă să crească, "
                "prevestind un dezastru iminent.")
    elif strings_id == "Mission1Job3ErrorOnJob2_1":
        return ("Rozi: 'Am folosit doar piatra, uitând de artefact. Acesta era esențial pentru a controla Gardienii.'"
                "\nScundi: 'Ai dreptate, Rozi. Am subestimat importanța artefactului. "
                "Trebuie să rectificăm această greșeală rapid. Timpul este împotriva noastră!'")
    elif strings_id == "Mission1Job3ErrorOnJob2_2":
        return ("Narator: Folosirea exclusivă a pietrei a avut un efect neașteptat. Gardienii s-au înfuriat mai mult, "
                "blocând și mai solid accesul la scurgere. "
                "Presiunea din vulcan continuă să crească, semnalând o iminentă erupție.")
    elif strings_id == "Mission1Job3ErrorOnJob2_3":
        return ("Scundi: 'Dacă nu combinăm corect puterile pietrei și ale artefactului, "
                "nu vom putea trece de Gardieni. "
                "Este vital să folosim ambele obiecte pentru a reuși.'\n"
                "Rozi: 'Ne-am aventurat prea departe pentru a eșua acum. Haide să găsim soluția corectă "
                "și să salvăm vulcanul.'")
    elif strings_id == "Mission1Job3ErrorOnAnyJob_1":
        return (
            "Scundi: 'Dacă nu găsim rapid o soluție, totul va fi pierdut. Acești Gardieni sunt ultimul obstacol "
            "dintre noi și salvarea vulcanului.'\n"
            "Rozi: 'Nu putem renunța acum! Să gândim strategic și să folosim tot ce avem.'")
    elif strings_id == "Mission1Job3ErrorOnAnyJob_2":
        return (
            "\nFără o strategie clară, Scundi și Rozi sunt învinși de Gardieni. "
            "Deși au încercat să deschidă scurgerea, "
            "presiunea acumulată în vulcan duce la o erupție catastrofală.")
    elif strings_id == "Mission1Job3ErrorOnAnyJob_3":
        return (
            "\033[1mSe pare că ai fost depășit de evenimente. Revenirea cu echipamentul corect "
            "și o strategie bine gândită ar fi putut schimba soarta misiunii.\033[0m\n")
    elif strings_id == "Mission2Title":
        return "\nMisiunea 2: Baricada Vulcanului"
    elif strings_id == "Mission2Text1":
        return ("\nVeli și Speri, doi dintre cei mai curajoși membri ai tribului, stau în fața 'Baricadei Vulcanului'. "
                "Au o misiune vitală: să colecteze și să arunce obiecte masive în craterele vulcanului "
                "pentru a opri flăcările furioase. "
                "În acest teren periculos, acești eroi trebuie să colecteze roci mari "
                "și să le arunce în gura vulcanului, încercând să încetinească erupția devastatoare.")
    elif strings_id == "Mission2Text2":
        return (
            "Veli: 'Am auzit povești despre acest loc, dar realitatea e și mai intimidantă. Flăcările, fumul, "
            "creaturile... totul pare a fi împotriva noastră.'\n"
            "Speri: 'Trebuie să avem grijă. Misiunea noastră este crucială. Nu putem lăsa erupția să distrugă totul.'")
    elif strings_id == "Mission2Text3":
        return ("Veli: 'Avem trei zone majore în care să acționăm aici în Baricada Vulcanului. Unde să începem?'\n"
                "1. Câmpul Pietrelor: Un teren accidentat, plin de roci masive ce așteaptă să fie colectate "
                "și folosite în misiunea noastră.\n"
                "2. Pădurea Fumurilor: O zonă acoperită de un fum dens, unde se zvonește că sunt ascunse creaturi "
                "care păzesc craterele vulcanului.\n"
                "3. Apărătorii Craterei: Se spune că aceasta este zona cea mai apropiață de gura vulcanului, "
                "dar și cea mai periculoasă datorită creaturilor ce o apără.\n"
                "\nTe rog să alegi cu care submisiune vrei să începi introducând numărul corespunzător "
                "și apoi să apeși 'Enter': ")
    elif strings_id == "Mission2Job1Choices":
        return (
            "Veli: 'Acest câmp este plin de pietre masive care ar putea fi utile. Dar, avem o problemă. "
            "Multe dintre ele sunt prea mari sau prea grele. Cum să procedăm?'\n"
            "1. Folosirea unor unelte speciale: 'Speri a venit cu niște unelte care pot sparge pietrele "
            "în bucăți mai mici, ușor de manevrat.'\n"
            "2. Crearea unui dispozitiv de ridicat: 'Ar putea să construim o macara rudimentară "
            "pentru a ridica pietrele.'\n"
            "3. Căutarea unui aliat puternic: 'Am auzit de o creatură locală, o ființă cu o forță nebănuită, "
            "care ar putea să ne ajute să transportăm pietrele.'")
    elif strings_id == "Mission2Job1Choice1":
        return (
            "Speri: 'Da, cu aceste unelte, putem descompune pietrele în bucăți mai mici și a le face "
            "mai ușor de manevrat. Vom avea nevoie de ceva timp, dar sunt optimist.'")
    elif strings_id == "Mission2Job1Choice2":
        return (
            "Veli: 'Un dispozitiv de ridicat poate fi exact ceea ce avem nevoie. Dacă folosim lemnul "
            "și sforile potrivite, putem construi o macara care să ne ajute la ridicarea pietrelor.'")
    elif strings_id == "Mission2Job1Choice3":
        return (
            "Veli: 'Am auzit și eu despre acea creatură. E o ființă care habitează pe versanții vulcanului. "
            "Dacă o găsim și ne ajută, ar putea fi soluția perfectă!'")
    elif strings_id == "Mission2Job1Conclusion":
        return (
            "Speri: 'E un progres excelent. Cu aceste pietre, avem o șansă bună să încetinim erupția vulcanului. "
            "Dar trebuie să acționăm rapid.'")
    elif strings_id == "Mission2Job2Choices":
        return ("Veli: 'Pădurea Fumurilor este un loc misterios și periculos. Dar suntem aici pentru acel mineral. "
                "Cum să procedăm pentru a-l găsi cât mai repede?'\n"
                "1. Urmărirea surselor de fum: 'Zvonurile spun că acolo unde fumul este mai dens, "
                "acolo este mai probabil să găsim mineralul.'\n"
                "2. Căutarea în apropierea izvoarelor fierbinți: 'Mineralul s-ar putea forma în zonele "
                "cu activitate geotermală ridicată.'\n"
                "3. Folosirea unui detector de minerale: 'Speri a adus un dispozitiv care detectează "
                "compoziția chimică a rocilor din jur. Ar putea fi util.'")
    elif strings_id == "Mission2Job2Choice1":
        return (
            "Începeți să urmați zonele unde fumul este mai dens. Aerul devine tot mai irespirabil, "
            "dar măștile de oxigen vă protejează. Pe măsură ce avansați, observați străluciri ciudate pe pământ.")
    elif strings_id == "Mission2Job2Choice2":
        return (
            "Căutând în jurul izvoarelor fierbinți, găsiți roci strălucitoare. Deși temperatura este extrem de înaltă, "
            "reușiți să colectați câteva mostre care par să fie mineralul căutat.")
    elif strings_id == "Mission2Job2Choice3":
        return (
            "Speri scoate detectorul și începe să scaneze zona. După câteva minute de căutări, "
            "dispozitivul indică o zonă unde concentrația mineralului pare să fie ridicată.")
    elif strings_id == "Mission2Job2Conclusion":
        return (
            "Veli: 'Am avut succes în misiunea noastră, dar trebuie să ne grăbim și să folosim acest mineral "
            "înainte ca vulcanul să erupă. Timpul este esențial.'")
    elif strings_id == "Mission2Job3Start1":
        return ("Narator: Ajunși la marginea vârfului, Veli și Speri observă siluetele mișcându-se: sunt "
                "Apărătorii Craterei, ființe din lavă și stâncă care păzesc vulcanul.\n")
    elif strings_id == "Mission2Job3Start2":
        return ("Veli: 'Trebuie să folosim mineralul colectat și să le înfruntăm. Cu ajutorul acestuia, putem "
                "încetini erupția și să-i ținem la distanță pe Apărători.'")
    elif strings_id == "Mission2Job3Start3":
        return ("Speri: 'Vom folosi roci masive pentru a construi baricade și a împiedica avansul Apărătorilor. "
                "Cu fiecare moment care trece, mineralul pe care îl avem începe să-și arate puterea, "
                "diminuând forța vulcanului.'\nNarator: După un conflict intens, Apărătorii sunt învinși, "
                "iar erupția vulcanului încetinește, salvând habitatul dinozaurilor.")
    elif strings_id == "Mission2Job3Start4":
        return ("Veli: 'A fost o victorie măreață, dar mai avem multe de făcut.'\n"
                "Narator: Cu încredere și determinare, te pregătești pentru următoarea etapă a aventurii.")
    elif strings_id == "Mission2Job3Return":
        return "Speri: 'Nu suntem încă gata. Trebuie să revedem planul și să ne asigurăm că avem tot ce ne trebuie.'\n"
    elif strings_id == "Mission2Job3ErrorOnJob1_1":
        return ("Narator: Fără mineralul din Pădurea Fumurilor, Apărătorii Craterei sunt prea puternici, iar "
                "Veli și Speri sunt copleșiți de forța lor.\n")
    elif strings_id == "Mission2Job3ErrorOnJob1_2":
        return ("Veli: 'Am subestimat puterea lor fără mineralul pe care trebuia să-l aducem. Trebuie să găsim "
                "o altă cale de a încetini erupția.'")
    elif strings_id == "Mission2Job3ErrorOnJob1_3":
        return ("Speri: 'Mă tem că am pierdut această bătălie. Dar trebuie să continuăm lupta pentru a salva "
                "lumea dinozaurilor.'\n"
                "Apărătorii Craterei triumfă și vulcanul continuă să erupă cu o furie neoprită.")
    elif strings_id == "Mission2Job3ErrorOnJob2_1":
        return ("Veli: 'Chiar dacă avem mineralul, ne lipsește puterea rocilor masive pentru a construi baricade. "
                "Ești sigur că vrem să ne confruntăm cu Apărătorii acum?'")
    elif strings_id == "Mission2Job3ErrorOnJob2_2":
        return ("Narator: Veli și Speri încearcă să țină piept valurilor de Apărători. Dar fără resursele suficiente, "
                "se dovedește a fi o misiune imposibilă. Vulcanul începe să erupă, amenințând totul în jurul său.")
    elif strings_id == "Mission2Job3ErrorOnJob2_3":
        return ("\033[1mA fost o încercare nobilă, dar forțele Apărătorilor Craterei au fost prea puternice. "
                "Planificarea și pregătirea sunt esențiale în aventurile viitoare.\033[0m\n")
    elif strings_id == "Mission2Job3ErrorOnAnyJob_1":
        return ("Speri: 'Am auzit legende despre acești Apărători. Trebuie să ne pregătim corect înainte de "
                "a ne confrunta cu ei.'\n"
                "'Crezi că putem să-i învingem fără ajutorul mineralului și a rocilor?'")
    elif strings_id == "Mission2Job3ErrorOnAnyJob_2":
        return ("Narator: Cu curaj, Veli și Speri încearcă să țină piept Apărătorilor Craterei. Dar fără resursele "
                "corecte și pregătirea adecvată, erupția vulcanului nu poate fi oprită "
                "și distrugerea este inevitabilă.")
    elif strings_id == "Mission2Job3ErrorOnAnyJob_3":
        return ("\033[1mLipsa unei planificări adecvate a dus la un dezastru. Este esențial să te pregătești corect "
                "înainte de a te confrunta cu provocări atât de mari.\033[0m\n")
    elif strings_id == "Mission3Title":
        return "\nMisiunea 3: Paza cetății"
    elif strings_id == "Mission3Text1":
        return ("\nRuaiti, Tirics și jucătorul se găsesc la intrarea în 'Cetatea Ascunsă' - un fort bine păzit, "
                "situat la marginea pădurii. Acesta este locul unde dinozaurii și-au stabilit cartierul general "
                "în lupta împotriva erupției vulcanice.")
    elif strings_id == "Mission3Text2":
        return ("Ruaiti: 'Creaturile vulcanului, atrase de activitatea noastră, au venit să atace cetatea. "
                "Aceste creaturi sunt conduse de un dinozaur rău numit Zarnak, care dorește să profite de erupția "
                "vulcanului pentru a prelua controlul asupra teritoriului.\n"
                "Ruaiti: 'Rolul tău este să ne ajuți să apărăm cetatea. Trebuie să facem față valurilor de inamici, "
                "să consolidăm apărarea și, în cele din urmă, să înfruntăm însuși pe Zarnak.'")
    elif strings_id == "Mission3Text3":
        return ("Tirics: 'Ce crezi că ar trebui să facem?'\n"
                "1. Să consolidăm intrarea: ar trebuie să strângem resurse din apropiere (precum lemn sau pietre) "
                "pentru a consolida poarta cetății și a împiedica intrarea inamicilor.\n"
                "2. Să așezăm capcane: ar trebui să plăsăm capcane în jurul cetății, care vor răni sau întârzia "
                "inamicii. Capcanele pot fi făcute din spini, groapă cu smoală sau bolovani care se prăbușesc.\n"
                "3. Să mergem la cetate, să îl așteptăm pe Zarnak, și să îl înfruntăm?\n"
                "\nTe rog să alegi cu care misiune vrei să începi introducând numărul corespunzător "
                "și apoi să apeși 'Enter': ")
    elif strings_id == "Mission3Job1Choices":
        return ("Tirics: 'Consolidarea intrării cetății este o decizie înțeleaptă. Dar avem mai multe opțiuni "
                "despre cum să o facem. Care crezi că ar fi cea mai bună abordare?'\n"
                "1. Întărirea porților: 'Putem adăuga straturi suplimentare de lemn și fier la porți, "
                "făcându-le mult mai rezistente la atacuri.'\n"
                "2. Turnarea de smoală: 'Rozi a venit cu ideea de a pregăti niște smoală fierbinte. "
                "Dacă inamicii se apropie prea mult de poartă, o putem turna peste ei de pe ziduri.'\n"
                "3. Fosă cu apă sau smoală: 'Scundi sugerează să săpăm o fosă adâncă în fața porții și să o umplem "
                "cu apă sau smoală. Aceasta va fi o barieră naturală împotriva atacatorilor.'")
    elif strings_id == "Mission3Job1Choice1":
        return ("Tirics: 'Excelentă alegere! Cu porțile noastre întărite, va fi mult mai dificil pentru Zarnak "
                "și armata sa să pătrundă în cetate.'")
    elif strings_id == "Mission3Job1Choice2":
        return ("Ruaiti: 'Smoala fierbinte este o armă redutabilă. Am văzut-o folosită în alte cetăți "
                "și efectul asupra asaltatorilor este devastator.'")
    elif strings_id == "Mission3Job1Choice3":
        return ("Tirics: 'O fosă în fața porții? Genial! Nu doar că va fi o barieră fizică, dar va și demoraliza "
                "trupele inamice care încearcă să treacă peste.'")
    elif strings_id == "Mission3Job1Conclusion":
        return ("Tirics: 'Bine făcut! Cetatea arată mult mai pregătită acum. Dar să nu ne culcăm pe o ureche. "
                "Zarnak este un adversar formidabil și cu siguranță va avea trucuri în mânecă.'")
    elif strings_id == "Mission3Job2Choices":
        return ("Tirics: 'Alegerea de a plasa capcane este înțeleaptă. Înainte de a începe, să decidem "
                "ce fel de capcane să folosim.'\n"
                "1. Capcane cu spini: Aceste capcane vor răni inamicii și îi vor încetini.\n"
                "2. Groapă cu smoală: Inamicii care cad în aceste gropi vor fi prinși și nu vor mai putea avansa.\n"
                "3. Bolovani care se prăbușesc: Aceste capcane pot elimina mai mulți inamici deodată, "
                "dar sunt mai greu de pregătit.")
    elif strings_id == "Mission3Job2Choice1":
        return "Vă grăbiți să plasați capcane cu spini în jurul cetății. Mulți dintre inamici se vor răni în ei.\n"
    elif strings_id == "Mission3Job2Choice2":
        return ("Săpați cu grijă gropile și le umpleți cu smoală fierbinte. Când inamicii vor ataca, "
                "mulți dintre ei vor cădea în capcane și se vor zbate să iasă.")
    elif strings_id == "Mission3Job2Choice3":
        return ("Pregătiți bolovanii pe dealurile din jurul cetății. Când inamicii se vor apropia, îi veți eliberați, "
                "zdrobindu-i pe mulți dintre atacatori.")
    elif strings_id == "Mission3Job2Conclusion":
        return ("Tirics: 'Acum că avem capcanele în loc, avem un avantaj. Dar să nu ne subestimăm inamicul. "
                "Zarnak este puternic și înțelept.'")
    elif strings_id == "Mission3Job3Start1":
        return ("Narator: Pe măsură ce soarele apune, pașii grei ai lui Zarnak și ai armatei sale răsună în depărtare. "
                "Dar, cu capcanele setate și cetatea consolidată, inamicii au un timp greu avansând.\n")
    elif strings_id == "Mission3Job3Start2":
        return ("Tirics: 'Toate pregătirile noastre ne-au dat un avantaj semnificativ. Inamicii sunt dezorientați "
                "și răniți de capcane, iar porțile noastre întărite le împiedică să intre cu ușurință.'")
    elif strings_id == "Mission3Job3Start3":
        return ("Ruaiti: 'Lupta este intensă, dar avem avantajul terenului și pregătirilor. Cu fiecare oră care trece, "
                "Zarnak și armata sa sunt respinși.'\nNarator: După o luptă lungă și intensă, Zarnak este forțat "
                "să se retragă, lăsând în urmă numeroși soldați răniți și demoralizați. Cetatea a rezistat, "
                "și victoria este a ta.")
    elif strings_id == "Mission3Job3Start4":
        return ("Ruaiti: 'Am reușit să apărăm cetatea de această dată. Dar mai sunt alte provocări care ne așteaptă.'\n"
                "Narator: Ai demonstrat curaj și înțelepciune în alegerile tale. Acum, este timpul să te îndrepți "
                "spre următoarea misiune și să continui lupta pentru salvarea lumii dinozaurilor.")
    elif strings_id == "Mission3Job3Return":
        return "Tirics: 'Ești înțelept. Hai să revedem ce opțiuni avem.'\n"
    elif strings_id == "Mission3Job3ErrorOnJob1_1":
        return ("Narator: Pe măsură ce soarele apune, pașii grei ai lui Zarnak și ai armatei sale răsună în depărtare. "
                "Fără capcanele pentru a încetini avansul lor, inamicii se apropie rapid de porțile cetății.\n")
    elif strings_id == "Mission3Job3ErrorOnJob1_2":
        return ("Tirics: 'Fără capcane, trebuie să ne pregătim pentru o luptă intensă la porțile cetății. "
                "Dar măcar porțile sunt acum mult mai solide datorită consolidărilor pe care le-am făcut.'")
    elif strings_id == "Mission3Job3ErrorOnJob1_3":
        return ("Ruaiti: 'Voi sta la intrare și voi lupta până la ultima suflare. Cu porțile întărite, "
                "avem o șansă să rezistăm mai mult.'\n"
                "Primele rânduri ale armatei lui Zarnak ajung la porți. Datorită consolidărilor, "
                "porțile rezistă primului val de atac. Cu toate acestea, numărul mare de inamici începe "
                "să pună presiune pe apărătorii cetății, iar armata lui Zarnak obține avantajul și, "
                "în cele din urmă, victoria.")
    elif strings_id == "Mission3Job3ErrorOnJob2_1":
        return ("Tirics: 'Deși capcanele ne vor oferi un avantaj, cetatea nu este încă complet consolidată. "
                "Ești sigur că vrei să înfrunți armata lui Zarnak acum?'")
    elif strings_id == "Mission3Job3ErrorOnJob2_2":
        return ("Te avânți alături de Tirics și ceilalți dinozauri în lupta cu armata lui Zarnak. "
                "Deși capcanele au făcut ravagii în rândurile inamice, Zarnak este încă o forță formidabilă. "
                "Lupta este intensă și echilibrată. Cu toate acestea, fără consolidarea completă a cetății, "
                "armata lui Zarnak obține avantajul și, în cele din urmă, victoria.")
    elif strings_id == "Mission3Job3ErrorOnJob2_3":
        return ("\033[1mA fost o luptă eroică și strânsă. Cu toate acestea, forțele lui Zarnak au fost prea puternice "
                "și cetatea a căzut. Poate că o pregătire mai bună ar fi putut schimba soarta bătăliei.\033[0m\n")
    elif strings_id == "Mission3Job3ErrorOnAnyJob_1":
        return ("Tirics: 'Ar fi bine să consolidăm cetatea înainte de a încerca să o apărăm. "
                "Zarnak are o armată puternică.'\n"
                "'Crezi că îl putem învinge fără să consolidăm cetatea?'\n")
    elif strings_id == "Mission3Job3ErrorOnAnyJob_2":
        return ("\nCu o încăpățânare admirabilă, te arunci în mijlocul luptei, alături de Tirics "
                "și ceilalți dinozauri. Dar cetatea nu este pregătită pentru asaltul care urmează. "
                "Zarnak și armata sa au avut un avantaj imens datorită zidurilor slabe și neprotejate ale cetății.\n"
                "După ore intense de luptă, ești copleșit. Inamicii au invadat cetatea, iar apărătorii sunt forțați "
                "să se retragă sau sunt capturați. Într-o liniște sumbră, Zarnak își proclamă victoria, "
                "iar cetatea odată puternică este acum în ruine sub stăpânirea sa.\n")
    elif strings_id == "Mission3Job3ErrorOnAnyJob_3":
        return ("\033[1mSe pare că ai pierdut această bătălie. Consolidarea cetății ar fi putut oferi "
                "o șansă mai bună de victorie.\033[0m\n")
    elif strings_id == "FinalMessage":
        return ("După multe ore de luptă cu natura furioasă, eroii noștri au reușit să oprească erupția "
                "și să salveze lumea lor. În semn de recunoștință, comunitatea dinozaurilor i-a sărbătorit "
                "ca pe niște eroi adevărați, iar legenda lor va fi cântată prin văile luxuriante "
                "ale lumii dinozaurilor pentru generații întregi.\n"
                "\nSfârşit")

    elif strings_id == "text":
        return "text"
