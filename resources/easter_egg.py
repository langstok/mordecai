from flask_restful import Resource

output = """
        _   _         _            _          _            _             _             _                    _
       /\_\/\_\ _    /\ \         /\ \       /\ \         /\ \         /\ \           / /\                 /\ \
      / / / / //\_\ /  \ \       /  \ \     /  \ \____   /  \ \       /  \ \         / /  \                \ \ \
     /\ \/ \ \/ / // /\ \ \     / /\ \ \   / /\ \_____\ / /\ \ \     / /\ \ \       / / /\ \               /\ \_\
    /  \____\__/ // / /\ \ \   / / /\ \_\ / / /\/___  // / /\ \_\   / / /\ \ \     / / /\ \ \             / /\/_/
   / /\/________// / /  \ \_\ / / /_/ / // / /   / / // /_/_ \/_/  / / /  \ \_\   / / /  \ \ \           / / /
  / / /\/_// / // / /   / / // / /__\/ // / /   / / // /____/\    / / /    \/_/  / / /___/ /\ \         / / /
 / / /    / / // / /   / / // / /_____// / /   / / // /\____\/   / / /          / / /_____/ /\ \       / / /
/ / /    / / // / /___/ / // / /\ \ \  \ \ \__/ / // / /______  / / /________  / /_________/\ \ \  ___/ / /__
\/_/    / / // / /____\/ // / /  \ \ \  \ \___\/ // / /_______\/ / /_________\/ / /_       __\ \_\/\__\/_/___\
        \/_/ \/_________/ \/_/    \_\/   \/_____/ \/__________/\/____________/\_\___\     /____/_/\/_________/

"She may not look like much, but she's got it where it counts, kid. I've made a lot of special modifications myself."

"""


class EasterEgg(Resource):
    def get(self):
        return output
