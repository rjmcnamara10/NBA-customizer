from team_file import Team
from team_file import get_team
from player import Player
from player import Position

def team_player_init():
    try:
        sixers = get_team("Philadelphia 76ers")
    except ValueError:
        sixers = Team("Philadelphia", "76ers")
    Player("Joel", "Embiid", sixers, "21", 7, 0, [Position.CENTER], 28)
    Player("James", "Harden", sixers, "1", 6, 5, [Position.SHOOTING_GUARD], 33)
    Player("Tobias", "Harris", sixers, "12", 6, 7, [Position.POWER_FORWARD], 30)
    Player("Tyrese", "Maxey", sixers, "0", 6, 2, [Position.POINT_GUARD], 22)
    Player("P.J.", "Tucker", sixers, "17", 6, 5, [Position.SHOOTING_GUARD, Position.SMALL_FORWARD], 37)
    Player("Shake", "Milton", sixers, "18", 6, 5, [Position.SHOOTING_GUARD], 26)
    Player("Montrezl", "Harrell", sixers, "5", 6, 7, [Position.CENTER], 29)
    Player("Mac", "McClung", sixers, "9", 6, 2, [Position.SHOOTING_GUARD], 24)
    
    try:
        bucks = get_team("Milwaukee Bucks")
    except ValueError:
        bucks = Team("Milwaukee", "Bucks")
    Player("Giannis", "Antetokounmpo", bucks, "34", 6, 11, [Position.POWER_FORWARD], 28)
    Player("Jrue", "Holiday", bucks, "21", 6, 4, [Position.POINT_GUARD], 32)
    Player("Khris", "Middleton", bucks, "22", 6, 7, [Position.SMALL_FORWARD], 31)
    Player("Brook", "Lopez", bucks, "11", 7, 0, [Position.CENTER], 34)
    Player("Joe", "Ingles", bucks, "7", 6, 8, [Position.SHOOTING_GUARD, Position.SMALL_FORWARD], 35)
    Player("Bobby", "Portis", bucks, "9", 6, 10, [Position.POWER_FORWARD], 28)
    Player("Grayson", "Allen", bucks, "12", 6, 4, [Position.SHOOTING_GUARD], 27)
    Player("Wesley", "Matthews", bucks, "23", 6, 4, [Position.SHOOTING_GUARD], 36)
    Player("Jae", "Crowder", bucks, "99", 6, 6, [Position.POWER_FORWARD], 32)
    
    try:
        bulls = get_team("Chicago Bulls")
    except ValueError:
        bulls = Team("Chicago", "Bulls")
    Player("DeMar", "DeRozan", bulls, "11", 6, 6, [Position.SMALL_FORWARD, Position.SHOOTING_GUARD], 33)
    Player("Zach", "LaVine", bulls, "8", 6, 5, [Position.SHOOTING_GUARD], 27)
    Player("Lonzo", "Ball", bulls, "2", 6, 6, [Position.POINT_GUARD], 25)
    Player("Nikola", "Vucevic", bulls, "9", 6, 10, [Position.CENTER], 32)
    Player("Alex", "Caruso", bulls, "6", 6, 5, [Position.SHOOTING_GUARD], 28)
    Player("Ayo", "Dosunmu", bulls, "12", 6, 4, [Position.SHOOTING_GUARD], 23)
    Player("Patrick", "Beverley", bulls, "21", 6, 1, [Position.POINT_GUARD], 34)
    Player("Patrick", "Williams", bulls, "44", 6, 7, [Position.POWER_FORWARD], 21)
    Player("Coby", "White", bulls, "0", 6, 4, [Position.POINT_GUARD], 22)
    Player("Javonte", "Green", bulls, "24", 6, 5, [Position.SHOOTING_GUARD, Position.SMALL_FORWARD], 29)

    try:
        cavs = get_team("Cleveland Cavaliers")
    except ValueError:
        cavs = Team("Cleveland", "Cavaliers")
    Player("Donovan", "Mitchell", cavs, "45", 6, 1, [Position.SHOOTING_GUARD], 26)
    Player("Jarrett", "Allen", cavs, "31", 6, 9, [Position.CENTER], 24)
    Player("Evan", "Mobley", cavs, "4", 6, 11, [Position.POWER_FORWARD], 21)
    Player("Darius", "Garland", cavs, "10", 6, 1, [Position.POINT_GUARD], 23)
    Player("Isaac", "Okoro", cavs, "35", 6, 5, [Position.SMALL_FORWARD], 22)
    Player("Caris", "LeVert", cavs, "3", 6, 6, [Position.SHOOTING_GUARD], 28)
    Player("Cedi", "Osman", cavs, "16", 6, 7, [Position.SMALL_FORWARD], 27)

    try:
        celtics = get_team("Boston Celtics")
    except ValueError:
        celtics = Team("Boston", "Celtics")
    Player("Jayson", "Tatum", celtics, "0", 6, 8, [Position.SMALL_FORWARD, Position.POWER_FORWARD], 24)
    Player("Jaylen", "Brown", celtics, "7", 6, 6, [Position.SHOOTING_GUARD], 26)
    Player("Marcus", "Smart", celtics, "36", 6, 4, [Position.POINT_GUARD, Position.SHOOTING_GUARD], 28)
    Player("Robert", "Williams III", celtics, "44", 6, 9, [Position.CENTER], 25)
    Player("Al", "Horford", celtics, "42", 6, 9, [Position.POWER_FORWARD, Position.CENTER], 36)
    Player("Grant", "Williams", celtics, "12", 6, 6, [Position.POWER_FORWARD, Position.SMALL_FORWARD], 24)
    Player("Malcolm", "Brogdon", celtics, "13", 6, 4, [Position.POINT_GUARD], 30)
    Player("Derrick", "White", celtics, "9", 6, 4, [Position.SHOOTING_GUARD, Position.POINT_GUARD], 28)
    Player("Sam", "Hauser", celtics, "30", 6, 7, [Position.SMALL_FORWARD], 25)
    Player("Payton", "Pritchard", celtics, "11", 6, 1, [Position.POINT_GUARD], 25)
    Player("Luke", "Kornet", celtics, "40", 7, 2, [Position.CENTER], 27)
    Player("Blake", "Griffin", celtics, "91", 6, 9, [Position.POWER_FORWARD], 33)

    try:
        clippers = get_team("LA Clippers")
    except ValueError:
        clippers = Team("LA", "Clippers")
    Player("Kawhi", "Leonard", clippers, "2", 6, 7, [Position.SMALL_FORWARD], 31)
    Player("Paul", "George", clippers, "13", 6, 8, [Position.SMALL_FORWARD], 32)
    Player("Russell", "Westbrook", clippers, "0", 6, 3, [Position.POINT_GUARD], 34)
    Player("Ivica", "Zubac", clippers, "40", 7, 0, [Position.CENTER], 25)
    Player("Robert", "Covington", clippers, "23", 6, 7, [Position.POWER_FORWARD, Position.SMALL_FORWARD], 32)
    Player("Terance", "Mann", clippers, "14", 6, 5, [Position.SHOOTING_GUARD], 26)
    Player("Marcus", "Morris Sr.", clippers, "8", 6, 8, [Position.SMALL_FORWARD], 33)
    Player("Nicolas", "Batum", clippers, "33", 6, 8, [Position.POWER_FORWARD], 34)
    Player("Norman", "Powell", clippers, "24", 6, 3, [Position.SMALL_FORWARD], 29)
    Player("Brandon", "Boston Jr.", clippers, "4", 6, 6, [Position.SHOOTING_GUARD], 21)

    try:
        grizzlies = get_team("Memphis Grizzlies")
    except ValueError:
        grizzlies = Team("Memphis", "Grizzlies")
    Player("Ja", "Morant", grizzlies, "12", 6, 3, [Position.POINT_GUARD], 23)
    Player("Jaren", "Jackson Jr.", grizzlies, "13", 6, 11, [Position.POWER_FORWARD], 23)
    Player("Desmond", "Bane", grizzlies, "22", 6, 5, [Position.SHOOTING_GUARD], 24)
    Player("Dillon", "Brooks", grizzlies, "24", 6, 7, [Position.SMALL_FORWARD], 27)
    Player("Steven", "Adams", grizzlies, "4", 6, 11, [Position.CENTER], 29)
    Player("Brandon", "Clarke", grizzlies, "15", 6, 8, [Position.POWER_FORWARD], 26)
    Player("Tyus", "Jones", grizzlies, "21", 6, 0, [Position.POINT_GUARD], 26)
    
    try:
        hawks = get_team("Atlanta Hawks")
    except ValueError:
        hawks = Team("Atlanta", "Hawks")
    Player("Trae", "Young", hawks, "11", 6, 1, [Position.POINT_GUARD], 24)
    Player("John", "Collins", hawks, "20", 6, 9, [Position.POWER_FORWARD], 25)
    Player("Dejounte", "Murray", hawks, "5", 6, 5, [Position.SHOOTING_GUARD], 26)
    Player("Clint", "Capela", hawks, "15", 6, 10, [Position.CENTER], 28)
    Player("Bogdan", "Bogdanovic", hawks, "13", 6, 5, [Position.SHOOTING_GUARD], 30)
    Player("De'Andre", "Hunter", hawks, "12", 6, 8, [Position.SMALL_FORWARD], 25)
    
    try:
        heat = get_team("Miami Heat")
    except ValueError:
        heat = Team("Miami", "Heat")
    Player("Jimmy", "Butler", heat, "22", 6, 7, [Position.SMALL_FORWARD], 33)
    Player("Bam", "Adebayo", heat, "13", 6, 9, [Position.CENTER], 25)
    Player("Kyle", "Lowry", heat, "7", 6, 0, [Position.POINT_GUARD], 36)
    Player("Tyler", "Herro", heat, "14", 6, 5, [Position.SHOOTING_GUARD], 23)
    Player("Victor", "Oladipo", heat, "4", 6, 4, [Position.SHOOTING_GUARD], 30)
    Player("Kevin", "Love", heat, "42", 6, 8, [Position.POWER_FORWARD], 34)
    Player("Duncan", "Robinson", heat, "55", 6, 7, [Position.SHOOTING_GUARD, Position.SMALL_FORWARD], 28)
    Player("Max", "Strus", heat, "31", 6, 5, [Position.SHOOTING_GUARD], 26)
    Player("Gabe", "Vincent", heat, "2", 6, 3, [Position.POINT_GUARD], 26)
    Player("Caleb", "Martin", heat, "16", 6, 5, [Position.SMALL_FORWARD], 27)
    Player("Nikola", "Jovic", heat, "5", 6, 10, [Position.SMALL_FORWARD, Position.POWER_FORWARD], 19)
    Player("Udonis", "Haslem", heat, "40", 6, 8, [Position.POWER_FORWARD], 42)

    try:
        hornets = get_team("Charlotte Hornets")
    except ValueError:
        hornets = Team("Charlotte", "Hornets")
    Player("LaMelo", "Ball", hornets, "1", 6, 7, [Position.POINT_GUARD], 21)
    Player("Gordon", "Hayward", hornets, "20", 6, 7, [Position.SMALL_FORWARD], 32)
    Player("Terry", "Rozier", hornets, "3", 6, 1, [Position.SHOOTING_GUARD], 28)
    Player("Mark", "Williams", hornets, "5", 7, 0, [Position.CENTER], 21)
    Player("P.J.", "Washington", hornets, "25", 6, 7, [Position.POWER_FORWARD], 24)
    Player("Dennis", "Smith Jr.", hornets, "8", 6, 2, [Position.POINT_GUARD], 25)
    Player("Kelly", "Oubre Jr.", hornets, "12", 6, 6, [Position.SHOOTING_GUARD], 27)
    Player("James", "Bouknight", hornets, "2", 6, 4, [Position.SHOOTING_GUARD], 22)

    try:
        jazz = get_team("Utah Jazz")
    except ValueError:
        jazz = Team("Utah", "Jazz")
    Player("Lauri", "Markkanen", jazz, "23", 7, 0, [Position.POWER_FORWARD], 25)
    Player("Collin", "Sexton", jazz, "2", 6, 2, [Position.POINT_GUARD], 24)
    Player("Kelly", "Olynyk", jazz, "41", 6, 11, [Position.POWER_FORWARD], 31)
    Player("Jordan", "Clarkson", jazz, "00", 6, 5, [Position.SHOOTING_GUARD], 30)
    Player("Walker", "Kessler", jazz, "24", 7, 0, [Position.CENTER], 21)
    Player("Rudy", "Gay", jazz, "22", 6, 8, [Position.SMALL_FORWARD], 36)
    Player("Kris", "Dunn", jazz, "11", 6, 3, [Position.POINT_GUARD], 28)

    try:
        kings = get_team("Sacramento Kings")
    except ValueError:
        kings = Team("Sacramento", "Kings")
    Player("De'Aaron", "Fox", kings, "5", 6, 3, [Position.POINT_GUARD], 25)
    Player("Domantas", "Sabonis", kings, "10", 7, 0, [Position.POWER_FORWARD], 26)
    Player("Keegan", "Murray", kings, "13", 6, 8, [Position.SMALL_FORWARD], 22)
    Player("Kevin", "Huerter", kings, "9", 6, 7, [Position.SHOOTING_GUARD], 24)
    Player("Harrison", "Barnes", kings, "40", 6, 8, [Position.SMALL_FORWARD], 30)
    Player("Malik", "Monk", kings, "0", 6, 3, [Position.SHOOTING_GUARD], 25)
    Player("Richaun", "Holmes", kings, "22", 6, 9, [Position.POWER_FORWARD], 29)
    Player("Alex", "Len", kings, "25", 7, 1, [Position.CENTER], 29)

    try:
        knicks = get_team("New York Knicks")
    except ValueError:
        knicks = Team("New York", "Knicks")
    Player("Jalen", "Brunson", knicks, "11", 6, 1, [Position.POINT_GUARD], 26)
    Player("Julius", "Randle", knicks, "30", 6, 8, [Position.POWER_FORWARD], 28)
    Player("RJ", "Barrett", knicks, "9", 6, 6, [Position.SHOOTING_GUARD], 22)
    Player("Immanuel", "Quickley", knicks, "5", 6, 3, [Position.SHOOTING_GUARD], 23)
    Player("Josh", "Hart", knicks, "3", 6, 4, [Position.SHOOTING_GUARD], 27)
    Player("Mitchell", "Robinson", knicks, "23", 7, 0, [Position.CENTER], 24)
    Player("Obi", "Toppin", knicks, "1", 6, 9, [Position.POWER_FORWARD], 24)
    Player("Quentin", "Grimes", knicks, "6", 6, 4, [Position.SHOOTING_GUARD], 22)
    Player("Jericho", "Sims", knicks, "45", 6, 9, [Position.CENTER], 24)
    Player("Derrick", "Rose", knicks, "4", 6, 3, [Position.POINT_GUARD], 34)

    try:
        lakers = get_team("Los Angeles Lakers")
    except ValueError:
        lakers = Team("Los Angeles", "Lakers")
    Player("LeBron", "James", lakers, "6", 6, 9, [Position.SMALL_FORWARD], 38)
    Player("Anthony", "Davis", lakers, "3", 6, 10, [Position.POWER_FORWARD], 29)
    Player("D'Angelo", "Russell", lakers, "1", 6, 4, [Position.POINT_GUARD], 26)
    Player("Rui", "Hachimura", lakers, "28", 6, 8, [Position.SMALL_FORWARD], 25)
    Player("Mo", "Bamba", lakers, "12", 7, 0, [Position.CENTER], 24)
    Player("Dennis", "Schroder", lakers, "17", 6, 1, [Position.POINT_GUARD], 29)
    Player("Malik", "Beasley", lakers, "5", 6, 4, [Position.SHOOTING_GUARD], 26)
    Player("Lonnie", "Walker IV", lakers, "4", 6, 4, [Position.SHOOTING_GUARD], 24)
    Player("Austin", "Reaves", lakers, "15", 6, 5, [Position.SHOOTING_GUARD], 24)

    try:
        magic = get_team("Orlando Magic")
    except ValueError:
        magic = Team("Orlando", "Magic")
    Player("Paolo", "Banchero", magic, "5", 6, 10, [Position.POWER_FORWARD], 20)
    Player("Markelle", "Fultz", magic, "20", 6, 4, [Position.POINT_GUARD], 24)
    Player("Jonathan", "Isaac", magic, "1", 6, 10, [Position.POWER_FORWARD], 25)
    Player("Jalen", "Suggs", magic, "4", 6, 5, [Position.SHOOTING_GUARD], 21)
    Player("Cole", "Anthony", magic, "50", 6, 3, [Position.POINT_GUARD], 22)
    Player("Bol", "Bol", magic, "10", 7, 2, [Position.CENTER], 23)
    Player("Wendell", "Carter Jr.", magic, "34", 6, 10, [Position.CENTER], 23)
    Player("Franz", "Wagner", magic, "22", 6, 10, [Position.SMALL_FORWARD], 21)

    try:
        mavs = get_team("Dallas Mavericks")
    except ValueError:
        mavs = Team("Dallas", "Mavericks")
    Player("Luka", "Doncic", mavs, "77", 6, 7, [Position.POINT_GUARD, Position.SHOOTING_GUARD], 23)
    Player("Kyrie", "Irving", mavs, "2", 6, 2, [Position.POINT_GUARD], 30)
    Player("Christian", "Wood", mavs, "35", 6, 9, [Position.POWER_FORWARD, Position.SMALL_FORWARD], 27)
    Player("Reggie", "Bullock", mavs, "25", 6, 6, [Position.SMALL_FORWARD], 31)
    Player("Maxi", "Kleber", mavs, "42", 6, 10, [Position.POWER_FORWARD], 31)
    Player("Dwight", "Powell", mavs, "7", 6, 10, [Position.CENTER], 31)
    Player("JaVale", "McGee", mavs, "00", 7, 0, [Position.CENTER], 35)
    Player("Davis", "Bertans", mavs, "44", 6, 10, [Position.POWER_FORWARD, Position.CENTER], 30)

    try:
        nets = get_team("Brooklyn Nets")
    except ValueError:
        nets = Team("Brooklyn", "Nets")
    Player("Cam", "Thomas", nets, "24", 6, 3, [Position.SHOOTING_GUARD], 21)
    Player("Mikal", "Bridges", nets, "1", 6, 6, [Position.SMALL_FORWARD], 26)
    Player("Nic", "Claxton", nets, "33", 6, 11, [Position.CENTER], 23)
    Player("Spencer", "Dinwiddie", nets, "26", 6, 6, [Position.POINT_GUARD], 29)
    Player("Cameron", "Johnson", nets, "2", 6, 8, [Position.SMALL_FORWARD], 26)
    Player("Ben", "Simmons", nets, "10", 6, 10, [Position.POWER_FORWARD], 26)
    Player("Yuta", "Watanabe", nets, "18", 6, 8, [Position.SMALL_FORWARD], 28)
    Player("Joe", "Harris", nets, "12", 6, 6, [Position.SMALL_FORWARD, Position.SHOOTING_GUARD], 31)
    Player("Seth", "Curry", nets, "30", 6, 1, [Position.SHOOTING_GUARD], 32)
    Player("Dorian", "Finney-Smith", nets, "28", 6, 7, [Position.POWER_FORWARD], 29)
    Player("Patty", "Mills", nets, "8", 6, 0, [Position.POINT_GUARD], 34)
    Player("Royce", "O'Neale", nets, "00", 6, 6, [Position.POWER_FORWARD], 29)

    try:
        nuggets = get_team("Denver Nuggets")
    except ValueError:
        nuggets = Team("Denver", "Nuggets")
    Player("Nikola", "Jokic", nuggets, "15", 6, 11, [Position.CENTER], 27)
    Player("Jamal", "Murray", nuggets, "27", 6, 4, [Position.POINT_GUARD], 25)
    Player("Aaron", "Gordon", nuggets, "50", 6, 8, [Position.POWER_FORWARD], 27)
    Player("Jeff", "Green", nuggets, "32", 6, 8, [Position.POWER_FORWARD], 36)
    Player("Kentavious", "Caldwell-Pope", nuggets, "5", 6, 5, [Position.SHOOTING_GUARD], 29)
    Player("Reggie", "Jackson", nuggets, "7", 6, 2, [Position.POINT_GUARD], 32)
    Player("DeAndre", "Jordan", nuggets, "6", 6, 11, [Position.CENTER], 34)
    Player("Michael", "Porter Jr.", nuggets, "1", 6, 10, [Position.SMALL_FORWARD], 24)
    Player("Bruce", "Brown", nuggets, "11", 6, 4, [Position.SMALL_FORWARD], 26)
    Player("Thomas", "Bryant", nuggets, "13", 6, 10, [Position.CENTER], 25)

    try:
        pacers = get_team("Indiana Pacers")
    except ValueError:
        pacers = Team("Indiana", "Pacers")
    Player("Tyrese", "Haliburton", pacers, "0", 6, 5, [Position.POINT_GUARD], 22)
    Player("Myles", "Turner", pacers, "33", 6, 11, [Position.CENTER], 26)
    Player("Buddy", "Hield", pacers, "24", 6, 4, [Position.SHOOTING_GUARD], 30)
    Player("Bennedict", "Mathurin", pacers, "00", 6, 5, [Position.SHOOTING_GUARD], 20)
    Player("Aaron", "Nesmith", pacers, "23", 6, 5, [Position.SMALL_FORWARD], 23)
    Player("Daniel", "Theis", pacers, "27", 6, 8, [Position.CENTER], 30)
    Player("Jalen", "Smith", pacers, "25", 6, 9, [Position.POWER_FORWARD], 22)
    Player("T.J.", "McConnell", pacers, "9", 6, 1, [Position.POINT_GUARD], 30)
    Player("Andrew", "Nembhard", pacers, "2", 6, 3, [Position.POINT_GUARD], 23)
    Player("Chris", "Duarte", pacers, "3", 6, 5, [Position.SHOOTING_GUARD], 25)

    try:
        pelicans = get_team("New Orleans Pelicans")
    except ValueError:
        pelicans = Team("New Orleans", "Pelicans")
    Player("Zion", "Williamson", pelicans, "1", 6, 6, [Position.POWER_FORWARD], 22)
    Player("Brandon", "Ingram", pelicans, "14", 6, 8, [Position.SMALL_FORWARD], 25)
    Player("CJ", "McCollum", pelicans, "3", 6, 3, [Position.SHOOTING_GUARD], 31)
    Player("Jonas", "Valanciunas", pelicans, "17", 6, 11, [Position.CENTER], 30)
    Player("Jose", "Alvarado", pelicans, "15", 6, 0, [Position.POINT_GUARD], 24)
    Player("Herbert", "Jones", pelicans, "5", 6, 7, [Position.SMALL_FORWARD], 24)
    Player("Larry", "Nance Jr.", pelicans, "22", 6, 8, [Position.POWER_FORWARD, Position.CENTER], 30)
    Player("Jaxson", "Hayes", pelicans, "10", 7, 0, [Position.CENTER], 22)
    Player("Kira", "Lewis Jr.", pelicans, "13", 6, 1, [Position.POINT_GUARD], 21)

    try:
        pistons = get_team("Detroit Pistons")
    except ValueError:
        pistons = Team("Detroit", "Pistons")
    Player("Bojan", "Bogdanovic", pistons, "44", 6, 7, [Position.SMALL_FORWARD], 33)
    Player("Marvin", "Bagley III", pistons, "35", 6, 10, [Position.POWER_FORWARD], 23)
    Player("Cade", "Cunningham", pistons, "2", 6, 7, [Position.POINT_GUARD], 21)
    Player("Jalen", "Duren", pistons, "0", 6, 11, [Position.CENTER], 19)
    Player("James", "Wiseman", pistons, "33", 7, 0, [Position.CENTER], 21)
    Player("Isaiah", "Stewart", pistons, "28", 6, 8, [Position.CENTER], 21)
    Player("Jaden", "Ivey", pistons, "23", 6, 4, [Position.POINT_GUARD], 20)
    Player("Killian", "Hayes", pistons, "7", 6, 5, [Position.POINT_GUARD], 21)

    try:
        raptors = get_team("Toronto Raptors")
    except ValueError:
        raptors = Team("Toronto", "Raptors")
    Player("Pascal", "Siakam", raptors, "43", 6, 8, [Position.POWER_FORWARD], 28)
    Player("Scottie", "Barnes", raptors, "4", 6, 8, [Position.SMALL_FORWARD], 21)
    Player("Fred", "VanVleet", raptors, "23", 6, 0, [Position.SHOOTING_GUARD], 28)
    Player("Chris", "Boucher", raptors, "25", 6, 9, [Position.POWER_FORWARD], 30)
    Player("O.G.", "Anunoby", raptors, "3", 6, 7, [Position.SMALL_FORWARD], 25)
    Player("Precious", "Achiuwa", raptors, "5", 6, 8, [Position.POWER_FORWARD], 23)
    Player("Gary", "Trent Jr.", raptors, "33", 6, 5, [Position.SHOOTING_GUARD], 24)
    Player("Jakob", "Poeltl", raptors, "19", 7, 1, [Position.CENTER], 27)
    Player("Malachi", "Flynn", raptors, "22", 6, 1, [Position.POINT_GUARD], 24)
    
    try:
        rockets = get_team("Houston Rockets")
    except ValueError:
        rockets = Team("Houston", "Rockets")
    Player("Jalen", "Green", rockets, "4", 6, 4, [Position.SHOOTING_GUARD], 21)
    Player("Alperen", "Sengun", rockets, "28", 6, 11, [Position.CENTER], 20)
    Player("Jabari", "Smith Jr.", rockets, "1", 6, 11, [Position.POWER_FORWARD], 19)
    Player("Kevin", "Porter Jr.", rockets, "3", 6, 4, [Position.SHOOTING_GUARD], 22)
    Player("Boban", "Marjanovic", rockets, "51", 7, 4, [Position.CENTER], 34)

    try:
        spurs = get_team("San Antonio Spurs")
    except ValueError:
        spurs = Team("San Antonio", "Spurs")
    Player("Jeremy", "Sochan", spurs, "10", 6, 8, [Position.POWER_FORWARD, Position.SMALL_FORWARD], 19)
    Player("Romeo", "Langford", spurs, "35", 6, 5, [Position.SHOOTING_GUARD], 23)
    Player("Keldon", "Johnson", spurs, "3", 6, 5, [Position.SMALL_FORWARD], 23)

    try:
        suns = get_team("Phoenix Suns")
    except ValueError:
        suns = Team("Phoenix", "Suns")
    Player("Kevin", "Durant", suns, "35", 6, 10, [Position.SMALL_FORWARD, Position.POWER_FORWARD], 34)
    Player("Devin", "Booker", suns, "1", 6, 5, [Position.SHOOTING_GUARD], 26)
    Player("Chris", "Paul", suns, "3", 6, 0, [Position.POINT_GUARD], 37)
    Player("Deandre", "Ayton", suns, "22", 7, 0, [Position.CENTER], 24)
    Player("Cameron", "Payne", suns, "15", 6, 1, [Position.POINT_GUARD], 28)
    Player("T.J.", "Warren", suns, "21", 6, 8, [Position.SMALL_FORWARD], 29)
    Player("Terrence", "Ross", suns, "8", 6, 7, [Position.SHOOTING_GUARD], 32)

    try:
        thunder = get_team("Oklahoma City Thunder")
    except ValueError:
        thunder = Team("Oklahoma City", "Thunder")
    Player("Shai", "Gilgeous-Alexander", thunder, "2", 6, 6, [Position.POINT_GUARD], 24)
    Player("Josh", "Giddey", thunder, "3", 6, 8, [Position.SHOOTING_GUARD], 20)
    Player("Chet", "Holmgren", thunder, "7", 7, 1, [Position.POWER_FORWARD, Position.CENTER], 20)
    Player("Luguentz", "Dort", thunder, "5", 6, 4, [Position.SHOOTING_GUARD], 23)
    Player("Aleksej", "Pokusevski", thunder, "17", 7, 0, [Position.POWER_FORWARD], 21)
    Player("Jalen", "Williams", thunder, "8", 6, 6, [Position.SMALL_FORWARD], 21)
    Player("Jaylin", "Williams", thunder, "6", 6, 9, [Position.SMALL_FORWARD], 20)

    try:
        timberwolves = get_team("Minnesota Timberwolves")
    except ValueError:
        timberwolves = Team("Minnesota", "Timberwolves")
    Player("Karl-Anthony", "Towns", timberwolves, "32", 7, 0, [Position.CENTER, Position.POWER_FORWARD], 27)
    Player("Anthony", "Edwards", timberwolves, "1", 6, 4, [Position.SHOOTING_GUARD], 21)
    Player("Rudy", "Gobert", timberwolves, "27", 7, 1, [Position.CENTER], 30)
    Player("Jaden", "McDaniels", timberwolves, "3", 6, 9, [Position.POWER_FORWARD], 22)
    Player("Mike", "Conley", timberwolves, "10", 6, 1, [Position.POINT_GUARD], 35)
    Player("Naz", "Reid", timberwolves, "11", 6, 9, [Position.CENTER], 23)
    Player("Nickeil", "Alexander-Walker", timberwolves, "9", 6, 5, [Position.SHOOTING_GUARD], 24)

    try:
        trail_blazers = get_team("Portland Trail Blazers")
    except ValueError:
        trail_blazers = Team("Portland", "Trail Blazers")
    Player("Damian", "Lillard", trail_blazers, "0", 6, 2, [Position.POINT_GUARD], 32)
    Player("Anfernee", "Simons", trail_blazers, "1", 6, 3, [Position.SHOOTING_GUARD], 23)
    Player("Jerami", "Grant", trail_blazers, "9", 6, 8, [Position.SMALL_FORWARD], 28)
    Player("Kevin", "Knox II", trail_blazers, "20", 6, 7, [Position.SMALL_FORWARD], 23)
    Player("Jusuf", "Nurkic", trail_blazers, "27", 7, 0, [Position.CENTER], 28)
    Player("Matisse", "Thybulle", trail_blazers, "22", 6, 5, [Position.SHOOTING_GUARD], 25)

    try:
        warriors = get_team("Golden State Warriors")
    except ValueError:
        warriors = Team("Golden State", "Warriors")
    Player("Stephen", "Curry", warriors, "30", 6, 2, [Position.POINT_GUARD], 34)
    Player("Klay", "Thompson", warriors, "11", 6, 6, [Position.SHOOTING_GUARD], 33)
    Player("Draymond", "Green", warriors, "23", 6, 6, [Position.POWER_FORWARD], 32)
    Player("Jordan", "Poole", warriors, "3", 6, 4, [Position.SHOOTING_GUARD], 23)
    Player("Kevon", "Looney", warriors, "5", 6, 9, [Position.CENTER], 27)
    Player("Andrew", "Wiggins", warriors, "22", 6, 7, [Position.SMALL_FORWARD], 27)
    Player("Jonathan", "Kuminga", warriors, "00", 6, 7, [Position.POWER_FORWARD], 20)
    Player("Moses", "Moody", warriors, "4", 6, 5, [Position.SHOOTING_GUARD], 20)
    Player("Gary", "Payton II", warriors, "8", 6, 2, [Position.SHOOTING_GUARD], 30)
    Player("Donte", "DiVincenzo", warriors, "0", 6, 4, [Position.SHOOTING_GUARD], 26)
    Player("Andre", "Iguodala", warriors, "9", 6, 6, [Position.SMALL_FORWARD], 39)

    try:
        wizards = get_team("Washington Wizards")
    except ValueError:
        wizards = Team("Washington", "Wizards")
    Player("Bradley", "Beal", wizards, "3", 6, 4, [Position.SHOOTING_GUARD], 29)
    Player("Kyle", "Kuzma", wizards, "33", 6, 9, [Position.SMALL_FORWARD], 27)
    Player("Kristaps", "Porzingis", wizards, "6", 7, 3, [Position.CENTER], 27)
    Player("Corey", "Kispert", wizards, "24", 6, 6, [Position.SMALL_FORWARD], 23)