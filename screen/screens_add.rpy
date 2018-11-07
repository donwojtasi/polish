# Input your language label by replacing the your_label_here.
# You can check what your language label is in your map.txt file (first line).

# Example:
    # translate thai strings:

translate polish strings:

    # Add your translation by replacing ONLY the strings (texts between pairs of "") after each of the words new.

    # Example:
        # old "限定版"
        # new "รูปแบบจำกัดอายุ"

    # This is the tool tip which tells that the age-limited version of the game is currently loaded.
    old "限定版"
    new "Edycja limitowana"

    # This is the tool tip which tells that the standard version of the game is currently loaded.
    old "標準版"
    new "Edycja zwykła"

    ######## Do NOT edit anything below this line. ########

    # These allow your game to display official languages correctly in preference (setting) screen if your custom fonts do not support Chinese or Japanese characters.

    # persistent/languages.rpy:10
    old "繁體中文"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}繁體中文{/font}"

    # persistent/languages.rpy:10
    old "简体中文"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}简体中文{/font}"

    # persistent/languages.rpy:10
    old "日本語"
    new "{font=tl/None/NotoSansCJKjp-Regular.otf}日本語{/font}"

    # This allows your game to display Team Nekojishi (in Chinese) name correctly during start of game if your custom fonts do not support Chinese characters.

    # screen/splashscreen.rpy:16
    old "家  有  大  貓  製  作  委  員  會"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}家  有  大  貓  製  作  委  員  會{/font}"

    # These allow your game to display copyright symbols correctly in various places of program if your custom fonts do not support special symbols.

    # screen/screens.rpy:279
    old "©"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}©{/font}"

    # screen/about.rpy:65
    old "© Taira Komori (http://taira-komori.jpn.org)"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}©{/font} Taira Komori (http://taira-komori.jpn.org)"

    # screen/about.rpy:69
    old "© Team Nekojishi"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}©{/font} Team Nekojishi"

    # screen/about.rpy:70
    old "© Orange Juice Dog"
    new "{font=tl/None/NotoSansCJKtc-Regular.otf}©{/font} Orange Juice Dog"

    # This turns a Chinese whitespace into a universal whitespace. It fixes the glitch where a square appears in the dialogue box during a character's monologue if your custom fonts do not support Chinese characters.

    # script/define.rpy:26
    old "　"
    new " "

