import random


def random_color(theme=""):
    # lists of all preset colors
    red_colors = ["lightsalmon", "salmon", "darksalmon", "lightcoral", "indianred",
                  "crimson", "firebrick", "red", "darkred"]
    orange_colors = ["coral", "tomato", "orangered", "gold", "orange",
                     "darkorange"]
    yellow_colors = ["lightyellow", "lemonchiffon", "lightgoldenrodyellow", "papayawhip", "moccasin",
                     "peachpuff", "palegoldenrod", "khaki", "darkkhaki", "yellow"]
    green_colors = ["lawngreen", "chartreuse", "limegreen", "lime", "forestgreen",
                    "green", "darkgreen", "greenyellow", "yellowgreen", "springgreen",
                    "mediumspringgreen", "lightgreen", "palegreen", "darkseagreen", "mediumseagreen",
                    "seagreen", "olive", "darkolivegreen", "olivedrab"]
    cyan_colors = ["lightcyan", "cyan", "aqua", "aquamarine", "mediumaquamarine",
                   "paleturquoise", "turquoise", "mediumturquoise", "darkturquoise", "lightseagreen",
                   "cadetblue", "darkcyan", "teal"]
    blue_colors = ["powderblue", "lightblue", "lightskyblue", "skyblue", "deepskyblue",
                   "lightsteelblue", "dodgerblue", "cornflowerblue", "steelblue", "royalblue",
                   "blue", "mediumblue", "darkblue", "navy", "midnightblue",
                   "mediumslateblue", "slateblue", "darkslateblue"]
    purple_colors = ["lavender", "thistle", "plum", "violet", "orchid",
                     "fuchsia", "magenta", "mediumorchid", "mediumpurple", "blueviolet",
                     "darkviolet", "darkorchid", "darkmagenta", "purple", "indigo"]
    pink_colors = ["pink", "lightpink", "hotpink", "deeppink", "palevioletred",
                   "mediumvioletred"]
    brown_colors = ["cornsilk", "blanchedalmond", "bisque", "navajowhite", "wheat",
                    "burlywood", "tan", "rosybrown", "sandybrown", "goldenrod",
                    "peru", "chocolate", "saddlebrown", "sienna", "brown",
                    "maroon"]
    white_colors = ["white", "snow", "honeydew", "mintcream", "azure",
                    "aliceblue", "ghostwhite", "whitesmoke", "seashell", "beige",
                    "oldlace", "floralwhite", "ivory", "antiquewhite", "linen",
                    "lavenderblush", "mistyrose"]
    gray_colors = ["gainsboro", "lightgray", "silver", "darkgray", "gray",
                   "dimgray", "lightslategray", "slategrey", "darkslategray", "black"]

    # 2D list of all color lists
    color_list = [red_colors, orange_colors, yellow_colors, green_colors, cyan_colors,
                  blue_colors, purple_colors, pink_colors, brown_colors, white_colors, gray_colors]

    # all color themes
    color_themes = ["red", "orange", "yellow", "green", "cyan",
                    "blue", "purple", "pink", "brown", "white", "gray"]

    # if no theme requested, outputs rand int that excludes white and gray colors
    group = random.randint(0, len(color_list) - 3)

    # if user requests color theme, checks within, excludes white and gray
    for color in range(0, len(color_themes) - 1):
        if theme == color_themes[color]:
            # uses index of color_themes to choose requested color among color_list
            group = color

    # chosen color group
    chosen_group = color_list[group]

    # chooses random int to choose color within color group
    color = random.randint(0, len(chosen_group) - 1)
    chosen_color = color_list[group][color]

    return chosen_color
