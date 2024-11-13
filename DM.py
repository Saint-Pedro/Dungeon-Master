import random
import time

class Ennemi:
    def __init__(self, nom, description, victoire, defaite):
        self.nom = nom
        self.description = description
        self.victoire = victoire
        self.defaite = defaite

ENNEMIS = [
    Ennemi(
        "Gobelins affamés",
        "Des gobelins affamés surgissent des ombres",
        "Essoufflé, vous essuyez votre lame sur votre cape alors que le dernier gobelin s'effondre dans un gargouillis pathétique. Leur faim ne les tourmentera plus.",
        "Les petites lames rouillées des gobelins trouvent les failles de votre armure. Leur rire aigu est la dernière chose que vous entendez avant de sombrer."
    ),
    Ennemi(
        "Bande de pillards gobelins",
        "Une bande de gobelins pillards vous tend une embuscade",
        "D'un mouvement circulaire, vous dispersez les derniers assaillants. Les gobelins survivants fuient en couinant, abandonnant leur butin.",
        "Leur embuscade était trop bien préparée. Les gobelins vous submergent sous leur nombre, leurs dagues trouvant mille fois leur cible."
    ),
    Ennemi(
        "Ogre dévorant",
        "Vous surprenez un ogre en train de dévorer sa dernière proie",
        "L'ogre s'écroule dans un fracas assourdissant. Sa masse imposante s'effondre près des restes de son dernier repas, qu'il ne finira jamais.",
        "La massue de l'ogre vous heurte de plein fouet. Votre vision se trouble alors qu'il vous saisit, vous ajoutant à son festin macabre."
    ),
    Ennemi(
        "Squelettes",
        "Les os craquent sous vos pieds alors que des squelettes émergent de la terre",
        "Votre arme fracasse le dernier crâne en morceaux. Les ossements retombent, inertes, rejoignant la poussière d'où ils venaient.",
        "Les squelettes sont trop nombreux. Leurs doigts osseux vous déchirent alors que vous rejoignez leur armée maudite."
    ),
    Ennemi(
        "Spectre",
        "L'air se glace tandis qu'un spectre traverse le mur devant vous",
        "Votre arme bénie traverse une dernière fois l'entité spectrale qui se dissipe dans un hurlement glacial, retournant dans le néant.",
        "Le toucher du spectre gèle votre âme. Votre corps s'effondre, vidé de toute essence vitale, alors que votre esprit rejoint les ombres."
    ),
    Ennemi(
        "Zombies",
        "Des zombies en décomposition se traînent dans votre direction, attirés par votre chaleur vitale",
        "Le dernier mort-vivant tombe, définitivement inerte. L'odeur de putréfaction persiste, mais la menace est écartée.",
        "Les morts-vivants vous submergent sous leur nombre. Leurs dents pourries déchirent votre chair alors que vous rejoignez leurs rangs."
    ),
    Ennemi(
        "Meute de wargs",
        "Une meute de wargs affamés sort des fourrés en grognant",
        "Le dernier warg s'effondre dans un gémissement. Le sol est jonché de leurs corps massifs, leur férocité enfin domptée.",
        "Les crocs acérés des wargs déchirent votre chair. Leur hurlement de victoire accompagne vos derniers instants."
    ),
    Ennemi(
        "Ours-garou",
        "Un ours-garou massif se dresse sur ses pattes arrière en rugissant",
        "La bête s'effondre, reprenant forme humaine dans la mort. Votre lame d'argent a mis fin à sa malédiction.",
        "Les griffes de l'ours-garou vous déchirent. Votre sang se mêle à la terre alors que son rugissement victorieux résonne."
    ),
    Ennemi(
        "Golem de pierre",
        "Un golem de pierre s'anime en votre présence, ses yeux brillant d'une lueur arcanique",
        "Dans un dernier coup, vous brisez le cœur magique du golem. La construction s'effrite, redevenant simple pierre inerte.",
        "Les poings de pierre vous écrasent contre le mur. Votre corps se brise alors que la lueur arcanique du golem continue de briller."
    ),
    Ennemi(
        "Harpies",
        "Des harpies plongent du plafond en poussant des cris stridents",
        "La dernière harpie tombe du ciel, ses ailes tranchées. Leurs cris stridents s'éteignent enfin dans le silence.",
        "Les serres des harpies vous arrachent du sol. Votre chute mortelle est accompagnée de leurs rires perçants."
    ),
    Ennemi(
        "Bandits",
        "Des bandits embusqués vous barrent la route",
        "Vous essuyez votre lame ensanglantée. Les bandits gisent à vos pieds, leur embuscade ayant tourné à leur désavantage.",
        "Une lame dans le dos vous fait trébucher. Les bandits vous dépouillent alors que votre vie s'écoule sur le sol."
    ),
    Ennemi(
        "Cultistes",
        "Un groupe de cultistes interrompt leur rituel pour vous faire face",
        "Le dernier cultiste tombe, son sang se mêlant aux cercles rituels. Leur cérémonie maudite restera inachevée.",
        "Leur magie noire vous consume lentement. Vos cris d'agonie se mêlent à leurs cantiques profanes."
    )
]

MESSAGES_SURVIE = [
    "Dans un dernier sursaut d'énergie, vous parvenez à vous extraire du combat et à fuir",
    "Puisant dans vos dernières forces, vous réussissez à vous dégager et à battre en retraite",
    "Le destin semble vous sourire alors que vous trouvez miraculeusement une échappatoire",
    "Votre divinité se manifeste au moment crucial, vous sauvant la vie"
]

DESCRIPTIONS_SALLES_VIDES = [
    "Le silence règne dans cette pièce déserte, uniquement troublé par l'écho de vos pas",
    "La salle est vide, mais étrangement accueillante dans sa simplicité",
    "Rien à signaler dans cette pièce, si ce n'est quelques toiles d'araignées dans les coins",
    "Vous vous sentez observé, mais après inspection minutieuse, la salle est définitivement vide",
    "Un frisson vous parcourt l'échine, pourtant rien ne semble anormal dans cette pièce déserte",
    "Vos instincts vous mettent en alerte, mais la salle ne révèle aucune menace",
    "Des meubles renversés témoignent d'une activité passée, mais plus rien ne bouge désormais",
    "L'air garde une odeur étrange, pourtant la pièce est indubitablement vide",
    "Des marques sur les murs racontent une histoire, mais leurs auteurs ont depuis longtemps disparu",
    "Quelque chose cloche dans cette salle, mais impossible de mettre le doigt dessus",
    "Un bruit vous fait sursauter, mais ce n'était que le vent dans les couloirs",
    "Un mouvement attire votre attention, mais ce n'était que votre propre reflet"
]

def generer_niveau():
    niveau = []
    for _ in range(20):
        niveau.append(random.randint(0, 1))
    return niveau

def get_combat_description():
    return random.choice(ENNEMIS)

def get_empty_room_description():
    return f"{random.choice(DESCRIPTIONS_SALLES_VIDES)}. La salle est vide, passage tranquille..."

def afficher_niveau(niveau):
    symboles = {0: "□", 1: "■"}
    return " ".join(symboles[salle] for salle in niveau)

def traverse_niveau(niveau):
    vie = 1
    for i, salle in enumerate(niveau):
        print(f"\n{'-'*50}")
        print(f"Salle {i+1}/20:")
        print(f"Points de vie actuels : {'❤️ ' * vie}")
        time.sleep(1)
        
        if salle == 1:  # ennemi
            ennemi = get_combat_description()
            print(f"\n⚔️  {ennemi.description}. Préparez-vous au combat!")
            time.sleep(2)
            
            resultat_de = random.randint(1, 6)
            print(f"\nLancer de dé : {resultat_de}")
            time.sleep(1)
            
            if resultat_de == 1:  
                print("\n💀 ÉCHEC CRITIQUE ! 💀")
                print(f"\n{ennemi.defaite}")
                return False
            elif resultat_de == 6:  
                print("\n✨ SUCCÈS CRITIQUE ! ✨")
                print(f"\n{ennemi.victoire}")
                vie += 1
                print(f"Vous gagnez un point de vie ! (Total: {vie})")
            elif resultat_de <= 3:
                print("\n❌ Le combat tourne mal !")
                print(f"\n{ennemi.defaite}")
                vie -= 1
                if vie <= 0:
                    return False
                else:
                    print(f"\n{random.choice(MESSAGES_SURVIE)}")
                    print(f"Vous perdez 1 point de vie. Points de vie restants: {vie}")
            else:
                print("\n✅ Vous triomphez !")
                print(f"\n{ennemi.victoire}")
        else:
            print(f"\n🏃 {get_empty_room_description()}")
        
        input("\nAppuyez sur Entrée pour continuer...")
        
    return True

def main():
    tentatives = 0
    victoire = False
    
    print("\n=== DUNGEON MASTER ===\n")
    print("Règles:")
    print("- Vous commencez avec 1 point de vie")
    print("- □ = salle vide (sûre)")
    print("- ■ = salle avec ennemi (combat)")
    print("\nSystème de combat:")
    print("Lancer de dé (1-6):")
    print("  * 1: ÉCHEC CRITIQUE - Mort instantanée")
    print("  * 2-3: Vous perdez 1 point de vie (si vous en avez encore, vous parvenez à fuir)")
    print("  * 4-5: Vous survivez au combat")
    print("  * 6: SUCCÈS CRITIQUE - Vous gagnez 1 point de vie")
    print("\nObjectif: traverser un niveau complet sans mourir\n")
    
    input("Appuyez sur Entrée pour commencer l'aventure...")
    
    while not victoire:
        tentatives += 1
        niveau = generer_niveau()
        print(f"\n{'='*50}")
        print(f"=== Niveau {tentatives} ===")
        print(f"{'='*50}")
        print("\nPlan du niveau:")
        print(afficher_niveau(niveau))
        print("\nDébut de l'exploration...")
        input("Appuyez sur Entrée pour commencer ce niveau...")
        
        victoire = traverse_niveau(niveau)
        if not victoire:
            print("\n💀 Votre aventure s'achève ici...")
            while True:
                reponse = input("\nAppuyez sur 'R' pour tenter une nouvelle aventure : ").upper()
                if reponse == 'R':
                    break
        else:
            print("\n🏆 Victoire! Vous avez survécu aux dangers du donjon!")
    
    print(f"\nVotre légende s'achève ici ! {tentatives} tentatives auront été nécessaires pour triompher!")
    input("\nAppuyez sur Entrée pour quitter...")

if __name__ == "__main__":
    main()