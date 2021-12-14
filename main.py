from tkinter import *
from tkinter import messagebox
from tkinter import font as tkFont
import string
import random
import json


NORMAL_FONT = ("Arial", 12, "normal")
SMALL_FONT = ("Arial", 10, "normal")
BIG_FONT = ("Arial", 18, "normal")
LETTERS = string.ascii_letters + string.ascii_letters
NUMBERS = string.digits + string.digits
SPECIAL = string.punctuation

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password(length_pass):
    random_pass = []
    for digit in range(int(length_pass)):
        random_letter = random.choice(LETTERS)
        random_number = random.choice(NUMBERS)
        random_special = random.choice(SPECIAL)
        random_pass.append(
            random.choice([random_letter, random_number, random_special])
        )
    new_password = "".join(random_pass)
    password_input.delete(0, "end")
    password_input.insert(0, new_password)
    return new_password


def valid_pass():
    length_pass = variable.get()
    if length_pass.isnumeric():
        new_pass = generate_password(length_pass)
        # print(f"condition is {test_password(new_pass, 'user@mail.com')}")
        while test_password(new_pass, "user@mail.com") != True:
            new_pass = generate_password(length_pass)
            # print(new_pass)
        # send new_pass to clipboard
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(new_pass)
        r.update()
        r.destroy()
        # another method #
        # import pyperclip
        # pyperclip.copy(new_pass)
        return new_pass
    else:
        messagebox.showerror("Error", "Please select a valid length")


def test_password(password_input, username_input):
    car_one_letter = False
    car_one_number = False
    car_one_special = False
    FORTUNE = [
        "walmart",
        "amazon",
        "apple",
        "cvs health",
        "unitedhealth group",
        "berkshire hathaway",
        "mckesson",
        "amerisourcebergen",
        "alphabet",
        "exxon mobil",
        "at&t",
        "costco wholesale",
        "cigna",
        "cardinal health",
        "microsoft",
        "walgreens boots alliance",
        "kroger",
        "home depot",
        "jpmorgan chase",
        "verizon communications",
        "ford motor",
        "general motors",
        "anthem",
        "centene",
        "fannie mae",
        "comcast",
        "chevron",
        "dell technologies",
        "bank of america",
        "target",
        "lowe's",
        "marathon petroleum",
        "citigroup",
        "facebook",
        "ups",
        "johnson & johnson",
        "wells fargo",
        "general electric",
        "state farm insurance",
        "intel",
        "humana",
        "ibm",
        "procter & gamble",
        "pepsico",
        "fedex",
        "metlife",
        "freddie mac",
        "phillips 66",
        "lockheed martin",
        "walt disney",
        "archer daniels midland",
        "albertsons",
        "valero energy",
        "boeing",
        "prudential financial",
        "hp",
        "raytheon technologies",
        "stonex group",
        "goldman sachs group",
        "sysco",
        "morgan stanley",
        "hca healthcare",
        "cisco systems",
        "charter communications",
        "merck",
        "best buy",
        "new york life insurance",
        "abbvie",
        "publix super markets",
        "allstate",
        "liberty mutual insurance group",
        "aig",
        "tyson foods",
        "progressive",
        "bristol-myers squibb",
        "nationwide",
        "pfizer",
        "caterpillar",
        "tiaa",
        "oracle",
        "energy transfer",
        "dow",
        "american express",
        "general dynamics",
        "nike",
        "northrop grumman",
        "usaa",
        "deere",
        "abbott laboratories",
        "northwestern mutual",
        "dollar general",
        "exelon",
        "coca-cola",
        "honeywell international",
        "thermo fisher scientific",
        "3m",
        "tjx",
        "travelers",
        "capital one financial",
        "tesla",
        "philip morris international",
        "arrow electronics",
        "chs",
        "jabil",
        "enterprise products partners",
        "hewlett packard enterprise",
        "united natural foods",
        "mondelez international",
        "viacomcbs",
        "kraft heinz",
        "dollar tree",
        "amgen",
        "u.s. bancorp",
        "performance food group",
        "netflix",
        "gilead sciences",
        "synnex",
        "eli lilly",
        "truist financial",
        "pnc financial services group",
        "broadcom",
        "cbre group",
        "massachusetts mutual life insurance",
        "qualcomm",
        "starbucks",
        "duke energy",
        "plains gp holdings",
        "us foods holding",
        "lennar",
        "danaher",
        "aflac",
        "rite aid",
        "visa",
        "paypal holdings",
        "micron technology",
        "carmax",
        "salesforce",
        "altria group",
        "lumen technologies",
        "baker hughes",
        "international paper",
        "hartford financial services group",
        "penske automotive group",
        "dupont",
        "autonation",
        "southern",
        "world fuel services",
        "d.r. horton",
        "nucor",
        "cummins",
        "ngl energy partners",
        "dxc technology",
        "union pacific",
        "whirlpool",
        "molina healthcare",
        "conocophillips",
        "mcdonald's",
        "kimberly-clark",
        "paccar",
        "pg&e",
        "cdw",
        "sherwin-williams",
        "l3harris technologies",
        "macy's",
        "manpowergroup",
        "nextera energy",
        "tenet healthcare",
        "avnet",
        "general mills",
        "westrock",
        "carrier global",
        "lincoln national",
        "genuine parts",
        "american airlines group",
        "marsh & mclennan",
        "applied materials",
        "becton dickinson",
        "delta air lines",
        "lear",
        "bank of new york mellon",
        "emerson electric",
        "western digital",
        "occidental petroleum",
        "nvidia",
        "cognizant technology solutions",
        "jones lang lasalle",
        "synchrony financial",
        "colgate-palmolive",
        "aecom",
        "xpo logistics",
        "c.h. robinson worldwide",
        "blackrock",
        "dominion energy",
        "rocket companies",
        "kohl's",
        "fluor",
        "dish network",
        "bj's wholesale club",
        "tenneco",
        "united airlines holdings",
        "mastercard",
        "waste management",
        "pbf energy",
        "american electric power",
        "fiserv",
        "principal financial",
        "reinsurance group of america",
        "automatic data processing",
        "stanley black & decker",
        "texas instruments",
        "halliburton",
        "stryker",
        "estã©e lauder",
        "corteva",
        "freeport-mcmoran",
        "qurate retail",
        "wayfair",
        "laboratory corp. of america",
        "land o'lakes",
        "ppg industries",
        "gap",
        "kellogg",
        "parker-hannifin",
        "core-mark holding",
        "jacobs engineering group",
        "edison international",
        "guardian life ins. co. of america",
        "biogen",
        "omnicom group",
        "unum group",
        "lithia motors",
        "american family insurance group",
        "discover financial services",
        "adobe",
        "aramark",
        "otis worldwide",
        "ecolab",
        "autozone",
        "loews",
        "illinois tool works",
        "fidelity national information services",
        "ross stores",
        "peter kiewit sons'",
        "equitable holdings",
        "wesco international",
        "goodyear tire & rubber",
        "fox",
        "leidos holdings",
        "consolidated edison",
        "dte energy",
        "charles schwab",
        "state street",
        "ameriprise financial",
        "viatris",
        "sempra energy",
        "farmers insurance exchange",
        "l brands",
        "w.w. grainger",
        "community health systems",
        "ball",
        "berry global group",
        "kinder morgan",
        "vf",
        "baxter international",
        "textron",
        "lkq",
        "keurig dr pepper",
        "o'reilly automotive",
        "crown holdings",
        "universal health services",
        "davita",
        "xcel energy",
        "newmont",
        "vistra",
        "iqvia holdings",
        "ebay",
        "corning",
        "quanta services",
        "hollyfrontier",
        "bed bath & beyond",
        "uber technologies",
        "mutual of omaha insurance",
        "conagra brands",
        "pultegroup",
        "eog resources",
        "group 1 automotive",
        "ally financial",
        "fidelity national financial",
        "nordstrom",
        "discovery",
        "tractor supply",
        "csx",
        "marriott international",
        "firstenergy",
        "jones financial (edward jones)",
        "borgwarner",
        "republic services",
        "henry schein",
        "expeditors intl. of washington",
        "entergy",
        "advance auto parts",
        "assurant",
        "pacific life",
        "lam research",
        "boston scientific",
        "altice usa",
        "norfolk southern",
        "sonic automotive",
        "advanced micro devices",
        "united states steel",
        "markel",
        "odp",
        "aes",
        "molson coors beverage",
        "j.b. hunt transport services",
        "kkr",
        "hormel foods",
        "public service enterprise group",
        "steel dynamics",
        "dick's sporting goods",
        "mohawk industries",
        "murphy usa",
        "square",
        "quest diagnostics",
        "newell brands",
        "liberty media",
        "huntington ingalls industries",
        "cheniere energy",
        "spartannash",
        "alcoa",
        "agco",
        "voya financial",
        "nrg energy",
        "interpublic group",
        "campbell soup",
        "southwest airlines",
        "news corp.",
        "eversource energy",
        "alleghany",
        "air products & chemicals",
        "auto-owners insurance",
        "centerpoint energy",
        "reliance steel & aluminum",
        "emcor group",
        "owens & minor",
        "mosaic",
        "erie insurance group",
        "genworth financial",
        "amphenol",
        "builders firstsource",
        "oneok",
        "united rentals",
        "brighthouse financial",
        "regeneron pharmaceuticals",
        "eastman chemical",
        "commscope holding",
        "ryder system",
        "fifth third bancorp",
        "constellation brands",
        "insight enterprises",
        "global partners",
        "univar solutions",
        "yum china holdings",
        "targa resources",
        "intercontinental exchange",
        "andersons",
        "raymond james financial",
        "thor industries",
        "thrivent financial for lutherans",
        "hershey",
        "casey's general stores",
        "w.r. berkley",
        "activision blizzard",
        "western & southern financial group",
        "american tower",
        "american financial group",
        "darden restaurants",
        "j.m. smucker",
        "williams",
        "intuit",
        "citizens financial group",
        "ppl",
        "nvr",
        "westinghouse air brake technologies",
        "foot locker",
        "cincinnati financial",
        "weyerhaeuser",
        "westlake chemical",
        "navistar international",
        "magellan health",
        "booz allen hamilton holding",
        "autoliv",
        "s&p global",
        "global payments",
        "motorola solutions",
        "keycorp",
        "delek us holdings",
        "masco",
        "graybar electric",
        "wec energy group",
        "old republic international",
        "frontier communications",
        "chewy",
        "pvh",
        "asbury automotive group",
        "seaboard",
        "polaris",
        "dana",
        "first american financial",
        "cintas",
        "toll brothers",
        "science applications international",
        "owens corning",
        "zimmer biomet holdings",
        "xerox holdings",
        "arthur j. gallagher",
        "avery dennison",
        "sanmina",
        "jefferies financial group",
        "beacon roofing supply",
        "securian financial group",
        "oshkosh",
        "fm global",
        "booking holdings",
        "williams-sonoma",
        "coty",
        "clorox",
        "pioneer natural resources",
        "dover",
        "cms energy",
        "zoetis",
        "hanesbrands",
        "packaging corp. of america",
        "regions financial",
        "graphic packaging holding",
        "ugi",
        "sprouts farmers market",
        "avantor",
        "veritiv",
        "rockwell automation",
        "mastec",
        "dcp midstream",
        "northern trust",
        "m&t bank",
        "realogy holdings",
        "ncr",
        "t. rowe price",
        "vertex pharmaceuticals",
        "big lots",
        "ralph lauren",
        "ulta beauty",
        "taylor morrison home",
        "icahn enterprises",
        "blackstone group",
        "o-i glass",
        "fortune brands home & security",
        "nov",
        "ovintiv",
        "alexion pharmaceuticals",
        "huntsman",
        "equinix",
        "abm industries",
        "ingredion",
        "chipotle mexican grill",
        "sinclair broadcast group",
        "lpl financial holdings",
        "crown castle international",
        "kla",
        "ameren",
        "kbr",
        "burlington stores",
        "olin",
        "caci international",
        "post holdings",
        "academy sports and outdoors",
        "arconic",
        "celanese",
        "yum brands",
        "fastenal",
        "nasdaq",
        "analog devices",
        "mccormick",
        "carvana",
        "franklin resources",
        "electronic arts",
        "mdu resources group",
        "select medical holdings",
        "roper technologies",
        "rpm international",
        "cerner",
        "patterson",
        "commercial metals",
        "boise cascade",
        "hasbro",
        "a-mark precious metals",
        "camping world holdings",
        "netapp",
        "avis budget group",
        "r.r. donnelley & sons",
        "moody's",
    ]
    COMMON = [
        "111111",
        "passw0rd",
        "123456",
        "dragon",
        "iloveyou",
        "letmein",
        "1234567",
        "master",
        "shadow",
        "Football",
        "superman",
        "ashley",
        "abc123",
        "sunshine",
        "bailey",
        "monkey",
        "baseball",
        "123123",
        "michael",
        "12345678",
        "654321",
        "qazwsx",
        "qwerty",
        "trustno1",
        "password",
    ]

    if password_input == 0:
        return "Please select a valid length"

    if password_input == username_input:
        return "Generated password is the same as user login"

    if 7 < len(password_input) < 33:
        pass
    else:
        return f"Password not between 8 to 32 characters"

    # testing if there is a letter, a number and a special character
    for car in password_input:
        if car in LETTERS:
            car_one_letter = True
        if car in NUMBERS:
            car_one_number = True
        if car in SPECIAL:
            car_one_special = True

    if not car_one_letter:
        return "Missing one letter"
    if not car_one_number:
        return "Missing one number"
    if not car_one_special:
        return "Missing one special character"

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        password_list = []
    else:
        password_list = [value["password"] for (key, value) in data.items()]
    number_of_pass = len(password_list)
    if number_of_pass >= 5:
        reps = 5
    else:
        reps = number_of_pass
    passes = password_list[-1 : -reps - 1 : -1]
    if password_input in passes:
        return "Same password as the past 5"

    # sequential testing
    for num in range(2, len(password_input)):
        first_char = password_input[num - 2]
        second_char = password_input[num - 1]
        third_char = password_input[num]

        if first_char == third_char and second_char == third_char:
            return f"There are three identical characters in sequence '{first_char}{second_char}{third_char}'"

        if first_char.isalpha():
            index_first_letter = LETTERS.index(first_char)
            if (
                second_char == LETTERS[index_first_letter + 1]
                and third_char == LETTERS[index_first_letter + 2]
            ):
                return f"There are three sequential characters '{first_char}{second_char}{third_char}'"

        if first_char.isnumeric():
            index_first_num = NUMBERS.index(first_char)
            if (
                second_char == NUMBERS[index_first_num + 1]
                and third_char == NUMBERS[index_first_num + 2]
            ):
                return f"There are three sequential characters '{first_char}{second_char}{third_char}'"

    for word in FORTUNE:
        if len(word) >= 4 and word in password_input.lower():
            return f"Password contains Fortune 500 company name: {word.title()}"

    for common_passwords in COMMON:
        if common_passwords.lower() in password_input.lower():
            return f"Common password used: {common_passwords}"

    return True


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_password = password_input.get()
    user_email = email_input.get()
    user_website = website_input.get()
    new_data = {user_website: {"username": user_email, "password": user_password}}
    abc = {}
    if user_password == "" or user_email == "" or user_website == "":
        messagebox.showerror("Error", "Missing one of the mandatory fields")
        return
    else:
        result_test = test_password(user_password, user_email)
        if result_test == True:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_input.delete(0, END)
                password_input.delete(0, END)
            return user_password, user_email, user_website
        else:
            messagebox.showerror("Error", f"Invalid password\n{result_test}")


# ---------------------------- SEARCH ------------------------------- #
def search():
    user_website = website_input.get()
    if user_website == "":
        messagebox.showerror("Error", "Nothing to search for")
        return
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror("Error", "No entries yet")
            return
        else:
            try:
                messagebox.showinfo(
                    f"{user_website}",
                    f"Username: {data[user_website]['username']}\nPassword: {data[user_website]['password']}",
                )
            except KeyError:
                messagebox.showerror("Error", f"No inputs for {user_website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.resizable(width=False, height=False)
window.config(padx=20, pady=20)

canvas = Canvas(width=100, height=100, highlightthickness=0)
tomato = PhotoImage(file="logo.png")
tomato = tomato.subsample(2, 2)
canvas.create_image(50, 52, image=tomato)
canvas.grid(row=0, column=1, pady=20)


website = Label(text="Website", font=NORMAL_FONT)
website.grid(row=1, column=0)
website.config(padx=5, pady=5)
website_input = Entry(width=35)
website_input.focus()
website_input.insert(0, "Google")
website_input.grid(row=1, column=1, sticky=W, columnspan=2)

website_search = Button(
    text="Search",
    font=NORMAL_FONT,
    command=search,
    highlightthickness=0,
    width=8,
)
website_search.grid(row=1, column=1, sticky=E)

email = Label(text="Email or Username", font=NORMAL_FONT)
email.grid(row=2, column=0)
email.config(padx=5, pady=5)
email_input = Entry(width=48)
email_input.insert(0, "user@mail.com")
email_input.grid(row=2, column=1, sticky=W, columnspan=2)

password = Label(text="Password", font=NORMAL_FONT)
password.grid(row=3, column=0)
password.config(padx=5, pady=5)
password_input = Entry(width=48)
password_input.grid(row=3, column=1, sticky=W)
generate_button = Button(
    text="Generate",
    font=NORMAL_FONT,
    command=valid_pass,
    highlightthickness=0,
    width=30,
)
generate_button.grid(row=4, column=1, sticky=W)

variable = StringVar(window)
variable.set("Length")
options = list(range(8, 33))
selected_length = OptionMenu(window, variable, *options)
selected_length.config(font=tkFont.Font(family="Arial", size=12))  # set the button font

selected_font = tkFont.Font(family="Arial", size=12)
menu = window.nametowidget(selected_length.menuname)
menu.config(font=selected_font)  # Set the dropdown menu's font
selected_length.grid(row=4, column=1, sticky=E)


save_button = Button(
    text="Save",
    font=NORMAL_FONT,
    command=save,
    highlightthickness=0,
    width=32,
    height=0,
)
# save_button.config(padx=5, pady=50)
save_button.grid(row=5, column=1, sticky=W, columnspan=2)

orientation = [
    "• Must be 8-32 characters long",
    "  - At least one letter (upper or lowercase)",
    "  - At least one number",
    "  - At least one special character from the following (below)",
    '              !"#$%&' + "'()*+,-./:;<=>?@[\]^_`{|}~           ",
    "• Most be different than your previous five passwords",
    "• Must not match your Email or User ID",
    "• Must not include more than 2 identical characters (for example 111 or aaa)",
    "• Must not include more than 2 consecutive characters (for example 123 or abc)",
    "• Must not use the name of the Fortune 500 institution (for Apple, Microsoft)",
    "• Must not be a commonly used password (example password1)",
]

guidelines_title = Label(text="\nGuidelines", font=BIG_FONT)
guidelines_title.grid(row=6, column=0, columnspan=3)

set_of_guidelines = []
for i in range(len(orientation)):
    current_line = orientation[i]
    set_of_guidelines.append(Label(text=current_line, font=SMALL_FONT))
    set_of_guidelines[i].grid(row=(7 + i), column=0, sticky=W, columnspan=3)

window.mainloop()
