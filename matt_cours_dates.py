# %%
##### créer une date
from datetime import datetime, timedelta

dt = datetime(2025, 9, 10, 14, 3)
dt.year, dt.month, dt.date(), dt.weekday()
# nb de second depuis le 1er janvier 1970 à minuit (temps unix)
dt.timestamp()

# %%
###### maintenant
now = datetime.now()
now

# %%
###### créer une date à partir d'une str
date_str = "2025-09-10 14:08"
dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
dt

# %%
###### formater un objet datetime en str
dt.strftime("%d/%m/%Y, %H:%M:%S")

# %%
###### gérer les dates et les durées
fin_journee = dt.strptime("2025-09-10 17:00", "%Y-%m-%d %H:%M")
now = datetime.now()
reste = fin_journee - now
reste.seconds // 3600, reste.seconds % 3600 // 60 , reste.seconds % 60

# %%
###### date + duree
now = datetime.now()
cuisson_oeuf_coque = timedelta(minutes=3)
now + cuisson_oeuf_coque


# %%
