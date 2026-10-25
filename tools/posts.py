"""Fleurinelle: 30 days of posts, Oct 27 to Nov 25 2026.
Each post: slides (rendered to 1080x1350), caption, up to 5 hashtags.
FR posts use the keyword VILLE, EN posts use CITY."""

CITIES = ["Casablanca", "Fes", "Rabat", "Meknes", "Marrakech", "Tetouan",
          "Tangier", "Kenitra", "Agadir", "Mohammedia"]
VILLES = ["Casablanca", "Fès", "Rabat", "Meknès", "Marrakech", "Tétouan",
          "Tanger", "Kénitra", "Agadir", "Mohammedia"]

POSTS = [
# 1
dict(kind="Promo", lang="EN", title="Flowers for Morocco",
 slides=[dict(layout="frame", head="Mama is in Morocco. You're not.", sub="We bring the flowers to her door", photo="rosalie")],
 caption="""Flower delivery in Morocco, ordered from wherever you live.

Someone you love is in Casablanca, Fes or Tangier. You're in Paris, Brussels or Madrid. Fleurinelle brings the flowers to their door, with your card in Arabic, French, English or Spanish.

10 cities. Prices in €, delivery included. A tracking page for every order.

Comment CITY and we'll tell you if we deliver to theirs.""",
 tags="#flowersmorocco #flowerdeliverymorocco #moroccandiaspora #sendflowers #fleurinelle"),

# 2
dict(kind="Offer", lang="EN", title="10% off with FIRST10", commercial=True,
 slides=[dict(layout="promo", eyebrow="Mabrouk!", big="10%", head="off your first bouquet",
              photo="heaven", code_label="USE CODE",
              terms="Orders above 50€  ·  First 100 orders only  ·  Conditions apply")],
 caption="""10% off your first order with code FIRST10.

Sending flowers to Morocco for the first time? Use FIRST10 at checkout on fleurinelle.com and save 10% on your first bouquet.

The fine print: orders above 50€, valid for the first 100 orders only, conditions apply.

Pick their city, choose the bouquet, write your card. We take it from there.""",
 tags="#flowersmorocco #sendflowers #moroccandiaspora #promocode #fleurinelle"),

# 3
dict(kind="Educational", lang="FR", title="Comment envoyer des fleurs au Maroc",
 slides=[
  dict(photo="beauty", head="Envoyer des fleurs au Maroc ?", line="C'est possible. Voici comment, depuis chez vous.", arch_h=520),
  dict(eyebrow="Étape 1", head="Choisissez sa ville.", cities=VILLES),
  dict(photo="sofia", eyebrow="Étape 2", head="Choisissez un bouquet.", line="Ils sont tous sur fleurinelle.com."),
  dict(eyebrow="Étape 3", head="Écrivez votre carte.", line="En arabe, français, anglais ou espagnol. Vos mots, pas les nôtres."),
  dict(eyebrow="Étape 4", head="Le jour et le créneau.", line="Le prix total en €, livraison incluse, avant de payer. Sans créer de compte."),
  dict(eyebrow="Étape 5", head="L'adresse complète.", line="Quartier, immeuble, étage et un numéro de téléphone. C'est ce qui fait arriver la surprise."),
  dict(photo="valentina", eyebrow="Étape 6", head="Suivez-le jusqu'à sa porte.", line="Votre page de suivi l'affiche jusqu'à « Livré ».", arch_h=380),
  dict(head="Elle habite où ?", key_pre="Commentez", key="VILLE", key_post="et on vous dit ce qu'on peut livrer chez elle."),
 ],
 caption="""Envoyer des fleurs au Maroc depuis la France, la Belgique ou l'Espagne, en 6 étapes.

Choisissez sa ville. Choisissez le bouquet. Écrivez la carte en arabe, en français, en anglais ou en espagnol. Choisissez le jour et le créneau, avec le prix total en € affiché avant de payer.

L'étape qu'on oublie, c'est l'adresse : quartier, immeuble, étage et un numéro de téléphone. C'est ce qui fait arriver la surprise à la bonne porte.

Enregistrez ce post pour son prochain anniversaire.""",
 tags="#livraisonfleurs #fleursmaroc #diasporamarocaine #cadeaumaman #fleurinelle"),

# 4
dict(kind="Funny", lang="EN", title="I'll call Mama tomorrow",
 slides=[dict(layout="text", eyebrow="Honest moment", head="“I'll call Mama tomorrow.”", ar="غادي نعيط لماما غدا",
              line="Me, three weeks later:", photo="passionate-love", ph=430, after="Sorry, Mama.")],
 caption="""We all have a sibling who says "I'll call Mama tomorrow" every single week. Sometimes it's us.

When the call keeps slipping, flowers to Morocco say it for you. They're on her table in Rabat by the time you finally ring. She'll tell you off for spending money, and keep the card anyway.

Comment CITY and tell us where your mum lives.""",
 tags="#moroccandiaspora #moroccanmom #flowersmorocco #sendflowers #fleurinelle"),

# 5
dict(kind="Promo", lang="EN", title="Five bouquets Mama would love",
 slides=[
  dict(photo="pop-of-color", head="Five bouquets Mama would love", line="Swipe and pick hers.", arch_h=540),
  dict(photo="rosalia", eyebrow="1 · Rosalia", head="Peach roses, white dahlias and a teddy bear.", hcls="h-m"),
  dict(photo="lisa", eyebrow="2 · Lisa", head="A heart of red roses in black and gold.", hcls="h-m"),
  dict(photo="sofia", eyebrow="3 · Sofia", head="Cream and coral roses in a gift bag.", hcls="h-m"),
  dict(photo="rosalie", eyebrow="4 · Rosalie", head="A cloud of coral pink roses with gold trim.", hcls="h-m"),
  dict(photo="valentina", eyebrow="5 · Valentina", head="Red and ivory roses in a red carrier.", hcls="h-m"),
  dict(head="Which one would she pick?", key_pre="Comment", key="1 to 5", key_post="All five deliver to 10 cities in Morocco."),
 ],
 caption="""Five bouquets we deliver across Morocco. Which one would she pick?

Rosalia, Lisa, Sofia, Rosalie or Valentina. Each one goes to her door in Casablanca, Rabat, Marrakech, Tangier, Agadir, Fes, Meknes, Tetouan, Kenitra or Mohammedia, with your card inside.

Comment the number of her favourite.""",
 tags="#flowersmorocco #bouquet #roses #moroccandiaspora #fleurinelle"),

# 6
dict(kind="Tip", lang="FR", title="Quartier, immeuble, étage, téléphone",
 slides=[dict(layout="text", eyebrow="Le conseil qui sauve la surprise",
              head="Quartier.\nImmeuble.\nÉtage.\nTéléphone.", hcls="h-xl",
              line="Avec ces 4 infos, votre bouquet trouve la bonne porte du premier coup.")],
 caption="""Livraison de fleurs au Maroc : le détail qui change tout, c'est l'adresse.

Au Maroc, une rue ne suffit pas toujours. Donnez-nous le quartier, l'immeuble, l'étage et un numéro de téléphone joignable. Le livreur trouve la porte, et la surprise arrive à l'heure.

Un repère connu aide aussi : une mosquée, une pharmacie, un café.

Commentez VILLE et on vous dit si on livre chez elle.""",
 tags="#livraisonfleurs #fleursmaroc #diasporamarocaine #astuce #fleurinelle"),

# 7
dict(kind="Educational", lang="EN", title="What rose colours mean",
 slides=[
  dict(photo="endless-love", head="What her roses are really saying", line="A two minute guide to rose colours.", arch_h=460),
  dict(photo="passionate-love", eyebrow="Red", head="Love. The deep kind.", line="For a partner, or anyone you'd cross the sea for."),
  dict(photo="heaven", eyebrow="Pink and blush", head="Thank you.", line="Gratitude and admiration. Perfect for Mama."),
  dict(photo="rosalie", eyebrow="Coral and peach", head="You make me happy.", line="Warmth and joy, without the drama of red."),
  dict(photo="beauty", eyebrow="Red with white", head="Together.", line="Unity. For anniversaries and family."),
  dict(photo="pop-of-color", eyebrow="A mix of colours", head="Pure joy.", line="When you can't choose, choose all of them."),
  dict(head="Save this for next time.", list=["Red: love", "Pink: thank you", "Coral: you make me happy", "Red and white: together", "Mixed: pure joy"]),
 ],
 caption="""What do rose colours mean? Before you send flowers to Morocco, here's the short version.

Red is love, the deep kind. Pink says thank you. Coral and peach say you make me happy. Red with white means togetherness. A mix of colours is pure joy.

Save this for the next time you're stuck choosing.""",
 tags="#rosemeaning #flowermeaning #roses #flowersmorocco #fleurinelle"),

# 8
dict(kind="Testimonial", lang="EN", title="Fast service and honesty",
 slides=[dict(layout="review", head="“Thank you for your fast service and for your honesty.”", img="review-002", ih=820)],
 caption=""""Thank you for your fast service and for your honesty."

A message from a customer who sent red roses to someone in Morocco. Messages like this one make our week.

Have someone to surprise? Comment CITY and we'll help you choose.""",
 tags="#customerreview #flowersmorocco #flowerdeliverymorocco #moroccandiaspora #fleurinelle"),

# 9
dict(kind="Promo", lang="EN", title="Five reasons to send with Fleurinelle",
 slides=[
  dict(photo="beauty", head="Sending flowers home, without the stress", line="Five things we do differently.", arch_h=500),
  dict(eyebrow="1", head="The full price, upfront.", line="In €, delivery included, before you pay."),
  dict(eyebrow="2", head="No account needed.", line="Order in a few minutes, no password to forget."),
  dict(eyebrow="3", head="Your card, her language.", line="Arabic, French, English or Spanish."),
  dict(eyebrow="4", head="Your day, your time window.", line="You choose when it arrives."),
  dict(photo="all-my-love", eyebrow="5", head="Follow it to her door.", line="Your tracking page shows it until it says Delivered.", arch_h=400),
  dict(head="Where does she live?", key="CITY", key_post="and we'll tell you what we can deliver there."),
 ],
 caption="""Five reasons people abroad send flowers to Morocco with Fleurinelle.

You see the full price in €, delivery included, before you pay. No account to create. Your card in Arabic, French, English or Spanish. You choose the day and the time window. And a tracking page follows it to her door.

Comment CITY and we'll tell you what we can deliver there.""",
 tags="#flowerdeliverymorocco #sendflowers #moroccandiaspora #onlineflowers #fleurinelle"),

# 10
dict(kind="Funny", lang="EN", title="What Mama does when your flowers arrive",
 slides=[
  dict(photo="valentina", head="What Mama does when your flowers arrive", line="A documentary in five steps.", arch_h=500),
  dict(eyebrow="Step 1", head="“Why did you spend money?”", hcls="h-xl"),
  dict(eyebrow="Step 2", head="Puts them in the best spot in the salon.", hcls="h-xl"),
  dict(eyebrow="Step 3", head="Sends a photo to the family group.\nThen another one.", hcls="h-l"),
  dict(eyebrow="Step 4", head="Tells the neighbours.\nAll of them.", hcls="h-xl"),
  dict(eyebrow="Step 5", head="Keeps the card.\nForever.", hcls="h-xl"),
  dict(head="Is your mum a step 1 or a step 4?", line="Tell us in the comments.", rule=True),
 ],
 caption="""What Mama does when your flowers arrive, in five steps.

First she asks why you spent money. Then the flowers get the best spot in the salon. Then the family group gets a photo. Then the neighbours hear about it. And the card goes somewhere safe, forever.

Is your mum a step 1 or a step 4? Tell us in the comments.""",
 tags="#moroccanmom #moroccandiaspora #flowersmorocco #momlife #fleurinelle"),

# 11
dict(kind="Engagement", lang="EN", title="Rosalia or Lisa",
 slides=[dict(layout="versus", eyebrow="This or that", head="Which one would your mum pick?",
              pair=[("rosalia", "Rosalia"), ("lisa", "Lisa")], line="Vote in the comments.")],
 caption="""Rosalia or Lisa: which one would your mum pick?

Rosalia is peach roses, white dahlias and a teddy bear holding a heart. Lisa is a heart of red roses wrapped in black and gold.

Vote in the comments. Both deliver to 10 cities across Morocco.""",
 tags="#flowersmorocco #roses #bouquet #moroccandiaspora #fleurinelle"),

# 12
dict(kind="Tips", lang="EN", title="Make her bouquet last longer",
 slides=[
  dict(photo="eterna", head="Make her bouquet last longer", line="Five tips. Send them to whoever just got flowers.", arch_h=500),
  dict(eyebrow="Tip 1", head="Trim the stems.", line="Cut 2 cm off at an angle with sharp scissors."),
  dict(eyebrow="Tip 2", head="Fresh water every 2 days.", line="A clean vase and cool water."),
  dict(eyebrow="Tip 3", head="Leaves out of the water.", line="Leaves below the waterline rot fast."),
  dict(eyebrow="Tip 4", head="Away from sun and fruit.", line="Heat and ripening fruit age flowers quicker."),
  dict(eyebrow="Tip 5", head="Somewhere cool at night.", line="A cooler room overnight keeps them fresh for longer."),
  dict(head="Save it. Send it to Mama.", list=["Trim the stems", "Fresh water every 2 days", "Leaves out of the water", "Away from sun and fruit", "Cool room at night"]),
 ],
 caption="""How to make a bouquet last longer: five tips to send to whoever just got flowers.

Trim the stems at an angle. Change the water every two days. Keep leaves out of the water. Keep the vase away from direct sun and the fruit bowl. Move it somewhere cool at night.

Save it, or send it to Mama with her next bouquet.""",
 tags="#flowercare #flowertips #roses #flowersmorocco #fleurinelle"),

# 13
dict(kind="Story", lang="EN", title="Paris, 7pm",
 slides=[dict(layout="riad", eyebrow="Paris, 7pm", head="You can't be in Fes.", line="The doorbell still rings.", photo="rosalia")],
 caption="""Paris, 7pm. It's her birthday, and you can't be in Fes.

Your flight home isn't until March. So this morning you picked a bouquet and wrote five words on the card, in Arabic. Now someone is climbing the stairs to the third floor.

That's what we do: flower delivery in Morocco for the people who can't be there.

Comment CITY and tell us where she lives.""",
 tags="#moroccandiaspora #flowersmorocco #fes #sendflowers #fleurinelle"),

# 14
dict(kind="B2B", lang="EN", title="Flowers for your clients in Morocco",
 slides=[dict(layout="frame", head="Flowers for your clients in Morocco", sub="Thank a client  ·  Welcome a partner", photo="all-my-love")],
 caption="""Corporate flowers in Morocco, ordered from your office abroad.

A client signs in Casablanca. A partner opens in Tangier. A colleague in Rabat has a baby. Send a bouquet with a card in Arabic, French, English or Spanish, on the day and in the time window you choose.

Prices in €, delivery included, and a tracking page for every order. For several deliveries at once, send us a message.""",
 tags="#corporategifts #businessgifts #morocco #flowerdeliverymorocco #fleurinelle"),

# 15
dict(kind="Tips", lang="EN", title="What to write on the card",
 slides=[
  dict(photo="heaven", head="Stuck on the card?", line="Steal one of these. Five lines, five languages.", arch_h=500),
  dict(eyebrow="Arabic · for her birthday", ar="كل عام وأنتِ بخير يا أمي", line="Happy birthday, Mama."),
  dict(eyebrow="Darija · when you miss her", ar="توحشتك بزاف أ ماما", line="Twahechtek bzaf a mama.\nI miss you so much, Mama."),
  dict(eyebrow="French · from far away", head="« Je suis loin, mais je pense à toi. »", line="I'm far away, but I'm thinking of you."),
  dict(eyebrow="Spanish · just because", head="«Aunque esté lejos, estoy contigo.»", line="Even far away, I'm with you."),
  dict(eyebrow="English · for the tea lover", head="“Save me a glass of tea. I'll be home soon.”"),
  dict(head="Your card, her language.", line="Write it in Arabic, French, English or Spanish when you order.", rule=True),
 ],
 caption="""What to write on a flower card, in five languages.

Arabic for her birthday, Darija for when you miss her, and French, Spanish or English for everything else. When you order, your card can be written in Arabic, French, English or Spanish.

Save this, and steal whichever line sounds like you.""",
 tags="#cardmessage #giftideas #moroccandiaspora #flowersmorocco #fleurinelle"),

# 16
dict(kind="Offer", lang="FR", title="-10% avec FIRST10", commercial=True,
 slides=[dict(layout="promo", eyebrow="Mabrouk !", big="-10%", bigsize=180, head="sur votre premier bouquet",
              photo="lisa", code_label="CODE PROMO",
              terms="Commandes de plus de 50€  ·  100 premières commandes  ·  Conditions applicables")],
 caption="""-10% sur votre première commande de fleurs au Maroc, avec le code FIRST10.

Première fois que vous envoyez des fleurs à Casablanca, Rabat, Marrakech ou Tanger ? Entrez FIRST10 au paiement sur fleurinelle.com.

Conditions : commande supérieure à 50€, valable pour les 100 premières commandes, conditions applicables.""",
 tags="#livraisonfleurs #fleursmaroc #codepromo #diasporamarocaine #fleurinelle"),

# 17
dict(kind="Educational", lang="EN", title="What happens after you press Order",
 slides=[
  dict(photo="sofia", head="What happens after you press Order", line="From your screen to her door.", arch_h=480),
  dict(eyebrow="1", head="We get your order.", line="The bouquet, your card, the day and the time window."),
  dict(eyebrow="2", head="The bouquet is made.", line="By hand, with your card tucked inside."),
  dict(eyebrow="3", head="On its way.", line="In the time window you picked."),
  dict(eyebrow="4", head="At her door.", line="District, building, floor. That's why we ask."),
  dict(photo="rosalia", eyebrow="5", head="Delivered.", line="Your tracking page says so.", arch_h=420),
  dict(head="Questions about an order?", line="hello@fleurinelle.com\nHave your order number ready.", rule=True),
 ],
 caption="""What happens after you order flowers to Morocco with Fleurinelle.

Your order comes in with the bouquet, your card, the day and the time window. The bouquet is made by hand with your card inside. It goes out in the window you chose, finds her door thanks to the full address, and your tracking page shows Delivered.

Questions about an order? Write to hello@fleurinelle.com with your order number.""",
 tags="#flowerdeliverymorocco #howitworks #sendflowers #moroccandiaspora #fleurinelle"),

# 18
dict(kind="Occasion", lang="EN", title="World Kindness Day",
 slides=[dict(layout="riad", eyebrow="World Kindness Day", head="Be the reason someone in Morocco smiles today.", line="13 November", photo="heaven", arch_h=600)],
 caption="""It's World Kindness Day. Who in Morocco deserves a surprise today?

A grandmother in Meknes. A friend in Agadir who's had a hard month. The aunt in Kenitra who always fills your suitcase with food.

Send flowers to Morocco with a card in her language. Comment CITY and we'll tell you if we deliver there.""",
 tags="#worldkindnessday #kindness #flowersmorocco #moroccandiaspora #fleurinelle"),

# 19
dict(kind="Funny", lang="EN", title="Gifts you send home, ranked",
 slides=[dict(layout="ranked", eyebrow="Honestly ranked", head="Gifts we send home to Morocco",
              rows=[("Perfume", "Saved for a wedding in 2031."),
                    ("Money", "Gone by Friday."),
                    ("Clothes", "Wrong size. Now your cousin's."),
                    ("Chocolate", "Shared with the whole building."),
                    ("Flowers", "On the table. Photographed. Discussed for a week.")])],
 caption="""Gifts we send home to Morocco, honestly ranked.

Perfume gets saved for a wedding in 2031. Money is gone by Friday. Clothes are the wrong size and end up with a cousin. Chocolate feeds the whole building. Flowers go on the table, get photographed for the family group and get talked about for a week.

Which one have you sent this year? Tell us in the comments.""",
 tags="#moroccandiaspora #moroccanmom #giftideas #flowersmorocco #fleurinelle"),

# 20
dict(kind="Tip", lang="FR", title="Le bon créneau",
 slides=[dict(layout="text", eyebrow="Astuce", head="Le bon créneau, c'est quand elle est là.", hcls="h-xl",
              line="Pas le matin du souk. Pas pendant la sieste.\nVous choisissez le jour et le créneau.", photo="dulcina", ph=380)],
 caption="""Astuce pour une livraison de fleurs au Maroc réussie : choisissez un créneau où elle est à la maison.

Pas le matin du souk, pas pendant la sieste, pas à l'heure où elle part chez sa sœur. Vous choisissez le jour et le créneau au moment de commander, alors profitez-en.

Et ajoutez un numéro joignable : si elle est descendue chercher le pain, le livreur peut l'appeler.

Commentez VILLE et dites-nous où elle habite.""",
 tags="#livraisonfleurs #fleursmaroc #astuce #diasporamarocaine #fleurinelle"),

# 21
dict(kind="Promo", lang="EN", title="A new baby back home",
 slides=[dict(layout="frame", head="Mabrouk! A new baby back home?", sub="Send Blessing from wherever you are", photo="blessing")],
 caption="""A new baby in the family in Morocco, and you can't make the first visit?

Blessing is soft pink blooms, white lilies and a teddy bear, made for welcoming a baby girl. Send it to the new parents with a card in Arabic, French, English or Spanish.

Comment CITY and we'll tell you if we deliver to theirs.""",
 tags="#newbaby #babygirl #flowersmorocco #moroccandiaspora #fleurinelle"),

# 22
dict(kind="Cities", lang="FR", title="Livraison dans 10 villes",
 slides=[
  dict(photo="pop-of-color", head="Livraison de fleurs dans 10 villes du Maroc", line="Laquelle est la sienne ?", arch_h=480, hcls="h-m"),
  dict(photo="all-my-love", eyebrow="Ville 1 et 2", head="Casablanca\net Mohammedia", hcls="h-m"),
  dict(photo="heaven", eyebrow="Ville 3 et 4", head="Rabat\net Kénitra", hcls="h-m"),
  dict(photo="rosalie", eyebrow="Ville 5 et 6", head="Marrakech\net Agadir", hcls="h-m"),
  dict(photo="valentina", eyebrow="Ville 7 et 8", head="Tanger\net Tétouan", hcls="h-m"),
  dict(photo="rosalia", eyebrow="Ville 9 et 10", head="Fès\net Meknès", hcls="h-m"),
  dict(head="Votre ville n'y est pas ?", line="Dites-le-nous en commentaire. Chaque ville citée nous aide à choisir la prochaine.", rule=True),
 ],
 caption="""Livraison de fleurs au Maroc dans 10 villes : Casablanca, Rabat, Marrakech, Tanger, Agadir, Fès, Meknès, Tétouan, Kénitra et Mohammedia.

Où que vous viviez, en France, en Belgique, en Espagne ou ailleurs, vous choisissez la ville, le bouquet, le jour et le créneau. On l'apporte jusqu'à sa porte.

Votre ville n'est pas dans la liste ? Dites-le-nous en commentaire : chaque ville citée nous aide à choisir la prochaine.""",
 tags="#livraisonfleurs #fleursmaroc #casablanca #marrakech #fleurinelle"),

# 23
dict(kind="Occasion", lang="EN", title="Independence Day",
 slides=[dict(layout="riad", eyebrow="18 November", head="Happy Independence Day, Morocco.", ar="عيد الاستقلال المجيد",
              line="To everyone at home, and everyone celebrating from far away.", photo="valentina", arch_h=520)],
 caption="""Happy Independence Day to everyone in Morocco, and to every Moroccan celebrating from far away.

Today is a good day to call home. Or to send something red and green to the people who taught you what home means.

عيد الاستقلال المجيد""",
 tags="#morocco #independenceday #moroccandiaspora #flowersmorocco #fleurinelle"),

# 24
dict(kind="Funny", lang="EN", title="Yes, you can send flowers to your dad",
 slides=[dict(layout="text", eyebrow="International Men's Day", head="Yes, you can send flowers to your dad.",
              line="He'll say it wasn't necessary.\nHe'll keep the card in his wallet.", photo="passionate-love", ph=420)],
 caption="""It's International Men's Day, and yes, you can send flowers to your dad in Morocco.

He'll say it wasn't necessary. He'll put them on the table anyway. And the card will end up in his wallet, next to a photo of you from 1998.

Brothers, grandfathers and uncles count too. Comment CITY and we'll tell you if we deliver to his.""",
 tags="#internationalmensday #dad #moroccandiaspora #flowersmorocco #fleurinelle"),

# 25
dict(kind="Testimonial", lang="EN", title="Review from Germany",
 slides=[dict(layout="review", head="“Thank you for the update and for the delivery photos.”", img="review-001", ih=820)],
 caption=""""Thank you for the update and for the delivery photos. I really appreciate your service!"

Sent from Germany, delivered in Morocco. Messages like this one make our week.

Comment CITY if there's someone you'd like to surprise.""",
 tags="#customerreview #flowersmorocco #flowerdeliverymorocco #moroccandiaspora #fleurinelle"),

# 26
dict(kind="Guide", lang="FR", title="Quel bouquet pour quelle occasion",
 slides=[
  dict(photo="beauty", head="Quel bouquet pour quelle occasion ?", line="Le petit guide à enregistrer.", arch_h=460),
  dict(photo="rosalie", eyebrow="Un anniversaire", head="Rosalie", line="Un nuage de roses corail."),
  dict(photo="blessing", eyebrow="Une naissance", head="Blessing", line="Fleurs roses, lys blancs et un ourson."),
  dict(photo="heaven", eyebrow="Se faire pardonner", head="Heaven", line="Roses blush et blanches, tout en douceur."),
  dict(photo="lisa", eyebrow="Dire je t'aime", head="Lisa", line="Un cœur de roses rouges en noir et or."),
  dict(photo="sofia", eyebrow="Dire merci", head="Sofia", line="Roses crème et corail dans un sac cadeau."),
  dict(photo="pop-of-color", eyebrow="Juste comme ça", head="A Pop of Color", line="Rouge, orange, rose et blanc."),
  dict(head="Enregistrez ce guide.", list=["Anniversaire : Rosalie", "Naissance : Blessing", "Pardon : Heaven", "Je t'aime : Lisa", "Merci : Sofia", "Juste comme ça : A Pop of Color"]),
 ],
 caption="""Quel bouquet envoyer au Maroc pour quelle occasion ? Notre petit guide.

Un anniversaire : Rosalie. Une naissance : Blessing. Se faire pardonner : Heaven. Dire je t'aime : Lisa. Dire merci : Sofia. Et juste comme ça : A Pop of Color.

Enregistrez ce guide pour la prochaine occasion.""",
 tags="#bouquet #ideecadeau #fleursmaroc #livraisonfleurs #fleurinelle"),

# 27
dict(kind="Engagement", lang="EN", title="Who would you send flowers to?",
 slides=[dict(layout="text", eyebrow="Your turn", head="If you could send flowers to one person in Morocco today, who would it be?",
              hcls="h-l", line="Tell us who, and which city.", photo="endless-love", ph=400)],
 caption="""If you could send flowers to one person in Morocco today, who would it be?

Mama in Fes. Your grandmother in Tetouan. The friend in Marrakech who never forgets your birthday.

Tell us who, and which city, in the comments.""",
 tags="#moroccandiaspora #flowersmorocco #morocco #sendflowers #fleurinelle"),

# 28
dict(kind="Funny", lang="EN", title="You know you're a Moroccan abroad when",
 slides=[
  dict(photo="for-your-heart", head="You know you're a Moroccan living abroad when...", arch_h=440, hcls="h-m"),
  dict(eyebrow="1", head="Your suitcase home is 80% gifts.", hcls="h-xl"),
  dict(eyebrow="2", head="You video call Mama from the supermarket to ask which tea to buy.", hcls="h-l"),
  dict(eyebrow="3", head="You know the euro to dirham rate by heart.", hcls="h-xl"),
  dict(eyebrow="4", head="“Are you eating properly?”\nEvery. Single. Call.", hcls="h-l"),
  dict(eyebrow="5", head="You've learned to send love by delivery.", hcls="h-xl"),
  dict(head="Which one is you?", line="Comment the number.", rule=True),
 ],
 caption="""You know you're a Moroccan living abroad when your suitcase home is 80% gifts.

Plus the supermarket video calls to ask Mama which tea to buy. The exchange rate you know by heart. The "are you eating properly?" on every single call.

Which one is you? Comment the number.""",
 tags="#moroccandiaspora #moroccansabroad #moroccanmom #morocco #fleurinelle"),

# 29
dict(kind="Offer", lang="EN", title="Your first bouquet, 10% off", commercial=True,
 slides=[dict(layout="promo", eyebrow="Mazal kayn!", big="10%", head="off your first bouquet",
              photo="rosalia", code_label="USE CODE",
              terms="Orders above 50€  ·  First 100 orders only  ·  Conditions apply")],
 caption="""Still haven't sent your first bouquet to Morocco? Code FIRST10 takes 10% off.

Use it at checkout on fleurinelle.com for flower delivery in Casablanca, Rabat, Marrakech, Tangier, Agadir, Fes, Meknes, Tetouan, Kenitra or Mohammedia.

Orders above 50€, valid for the first 100 orders only, conditions apply.""",
 tags="#flowersmorocco #promocode #sendflowers #moroccandiaspora #fleurinelle"),

# 30
dict(kind="Brand", lang="EN", title="Someone you love is in Morocco",
 slides=[dict(layout="riad", eyebrow="Fleurinelle", head="From far away, with love.", ar="من الغربة بالحب", line="Someone you love is in Morocco. We bring the flowers.", photo="eterna", arch_h=560)],
 caption="""Someone you love is in Morocco. You're not. We bring the flowers.

That's what Fleurinelle is: flower delivery in Morocco for people who live far from home. 10 cities, your card in her language, and a tracking page until it says Delivered.

Follow us so you never miss a birthday back home.""",
 tags="#flowersmorocco #flowerdeliverymorocco #moroccandiaspora #sendflowers #fleurinelle"),
]

assert len(POSTS) == 30


# ---- Lifestyle photos with people (AI generated in Ocoya from the brand templates).
# Used for mood, story and occasion posts; any post that names a bouquet also shows
# the real product photo from fleurinelle.com.
L = lambda **k: dict(layout="lifestyle", **k)
LIFESTYLE = {
 1:  {"replace": [L(bg="test-riad", logo=True, eyebrow="", head="Mama is in Morocco.\nYou're not.", hcls="h-l", line="We bring the flowers to her door")]},
 3:  {"cover": L(bg="cafe-phone", eyebrow="Depuis Lyon ou Bruxelles", head="Envoyer des fleurs\nau Maroc ?", hcls="h-l", line="Voici comment, en 6 étapes  →")},
 10: {"cover": L(bg="salon-tea", eyebrow="A documentary in 5 steps", head="What Mama does when your flowers arrive", line="Swipe  →")},
 13: {"replace": [L(bg="paris-window", eyebrow="Paris, 7pm", head="You can't be in Fes.", line="But the doorbell still rings.")]},
 14: {"replace": [L(bg="office", logo=True, eyebrow="", head="Flowers for your\nclients in Morocco", hcls="h-l", line="Thank a client  ·  Welcome a partner")]},
 17: {"cover": L(bg="door-delivery", eyebrow="From your screen to her door", head="What happens after you press Order", line="Swipe  →")},
 18: {"replace": [L(bg="grandmother", eyebrow="World Kindness Day", head="Be the reason someone in Morocco smiles today.", line="13 November")]},
 21: {"replace": [L(bg="new-baby", eyebrow="Mabrouk!", head="A new baby back home?", line="Send flowers from wherever you are"),
                  dict(photo="blessing", eyebrow="Meet Blessing", head="Soft pink blooms, white lilies and a teddy bear.", hcls="h-m", arch_h=600)]},
 23: {"replace": [L(bg="rabat-terrace", eyebrow="18 November", head="Happy Independence Day,\nMorocco.", hcls="h-m", ar="عيد الاستقلال المجيد", fade=680)]},
 24: {"replace": [L(bg="father", eyebrow="International Men's Day", head="Yes, you can send flowers to your dad.", line="He'll keep the card in his wallet.")]},
 27: {"replace": [L(bg="friends-hug", eyebrow="Your turn", head="Who would you send flowers to in Morocco?", line="Tell us who, and which city")]},
 28: {"cover": L(bg="airport-suitcase", eyebrow="Be honest", head="You know you're a Moroccan living abroad when...", hcls="h-m", line="Swipe  →")},
 30: {"replace": [L(bg="fes-door", eyebrow="Fleurinelle", head="From far away,\nwith love.", hcls="h-l", ar="من الغربة بالحب", fade=700, line="10 cities across Morocco")]},
}
for _n, _o in LIFESTYLE.items():
    _p = POSTS[_n - 1]
    if "replace" in _o:
        _p["slides"] = _o["replace"]
    else:
        _p["slides"] = [_o["cover"]] + _p["slides"][1:]
    _p["aigc"] = True


# ---- Final captions: hook first, search phrase inside, one ask, Moroccan touch.
CAPTIONS = {
1: """Mama is in Morocco. You're not. That's exactly why we started.

Fleurinelle is flower delivery in Morocco for everyone who lives far from home. You pick the bouquet from Paris, Brussels or Madrid. We take it to her door in Casablanca, Fes or Tangier, with your card inside.

10 cities. Prices in €, delivery included. A tracking page for every order.

Comment CITY and we'll tell you if we deliver to hers.""",
2: """Mabrouk, your first bouquet is 10% off. Code: FIRST10.

Sending flowers to Morocco for the first time? Enter FIRST10 at checkout on fleurinelle.com. That's it.

The fine print: orders above 50€, valid for the first 100 orders only, conditions apply.

Pick her city. Choose the bouquet. Write your card. We'll do the rest.""",
3: """Envoyer des fleurs au Maroc depuis la France ou la Belgique ? Six étapes. Trois minutes.

Choisissez sa ville. Choisissez le bouquet. Écrivez la carte en arabe, en français, en anglais ou en espagnol. Choisissez le jour et le créneau, avec le prix total en € affiché avant de payer.

L'étape qu'on oublie toujours ? L'adresse. Quartier, immeuble, étage et un numéro de téléphone : c'est ce qui fait arriver la surprise à la bonne porte.

Enregistrez ce post pour son prochain anniversaire.""",
4: """"I'll call Mama tomorrow." Every week. We all know someone. Sometimes it's us.

When the call keeps slipping, flowers to Morocco do the talking. They're on her table in Rabat before you finally ring. She'll scold you for spending money. Then she'll keep the card.

Comment CITY and tell us where your mum lives.""",
5: """Five bouquets. One mama. Which one would she pick?

Rosalia, Lisa, Sofia, Rosalie or Valentina. Every one of them is part of our flower delivery in Morocco, to Casablanca, Rabat, Marrakech, Tangier, Agadir, Fes, Meknes, Tetouan, Kenitra or Mohammedia, with your card inside.

Comment the number of her favourite.""",
6: """Livraison de fleurs au Maroc : le secret, c'est l'adresse.

Au Maroc, une rue ne suffit pas toujours. Donnez-nous le quartier, l'immeuble, l'étage et un numéro joignable. Le livreur trouve la porte. La surprise arrive.

Un repère aide aussi : la mosquée du quartier, une pharmacie, le café du coin.

Commentez VILLE et on vous dit si on livre chez elle.""",
7: """Red means love. But do you know what coral means? Here's what her roses are really saying.

Red? Love, the deep kind you'd cross the sea for. Pink says thank you, which is why it's Mama's colour. Coral and peach say "you make me happy" without the drama of red. Red with white means we're in this together. And when you can't choose, a mix of all of them is pure joy.

We send flowers to Morocco every day, and now you know the code too. Save this for next time.""",
8: """"Thank you for your fast service and for your honesty."

A customer sent red roses to someone in Morocco and wrote us this. We read it three times.

That's the job: flower delivery in Morocco you can trust from far away. Have someone to surprise? Comment CITY and we'll help you choose.""",
9: """Sending flowers home shouldn't feel like a gamble. So we made it boring, in the best way.

You see the full price in €, delivery included, before you pay. No account. Your card in Arabic, French, English or Spanish. You pick the day and the time window, and a tracking page follows it all the way to her door in one of our 10 cities.

That's why people abroad send flowers to Morocco with us. Comment CITY and we'll tell you what we deliver there.""",
10: """What Mama does when your flowers arrive. We've seen it a hundred times.

Step 1: "Why did you spend money?" Step 2: they get the best spot in the salon. Step 3: a photo goes to the family group. Then another one, from a better angle. Step 4: the neighbours. All of them. Step 5: she keeps the card. Forever.

Send flowers to Morocco and you'll see it too. So, is your mum a step 1 or a step 4?""",
11: """Rosalia or Lisa. Be honest: which one would your mum pick?

Rosalia's the soft one, with peach roses, white dahlias and a teddy bear holding a heart. Lisa doesn't whisper. It's a heart of red roses wrapped in black and gold.

Both are part of our flower delivery in Morocco, in 10 cities. Vote in the comments and we'll tell you which one wins.""",
12: """You sent flowers to Morocco. Now help them last. Five tips most people never hear.

Trim 2 cm off the stems, at an angle. Change the water every 2 days. Pull off any leaf that sits in the water, it rots fast. Keep the vase away from the sun and the fruit bowl. And if she can, she should move them somewhere cool at night.

That's it. Forward this to Mama with a voice note, she'll love that you checked.""",
13: """Paris, 7pm. It's her birthday. You can't be in Fes.

Your flight home isn't until March. So this morning you picked a bouquet and wrote five words on the card, in Arabic. Right now someone is climbing the stairs to the third floor.

That's what flower delivery in Morocco means to us. Comment CITY and tell us where she lives.""",
14: """A client signs in Casablanca. Your team is in Paris. What do you send?

Corporate flower delivery in Morocco, ordered from your office abroad: thank a client, welcome a partner, congratulate a colleague in Rabat on a new baby. Your card in Arabic, French, English or Spanish, on the day and in the time window you choose.

Prices in €, delivery included, a tracking page for every order. Planning several flower deliveries to Morocco at once? Send us a message.""",
15: """Stuck on the card? Steal one of these. Five lines, five languages.

Arabic for her birthday. Darija for when you miss her: twahechtek bzaf. French, Spanish or English for everything else. When you send flowers to Morocco with us, your card can be written in Arabic, French, English or Spanish.

Save this and use whichever line sounds like you.""",
16: """Mabrouk ! -10% sur votre premier bouquet avec le code FIRST10.

Première livraison de fleurs au Maroc ? Casablanca, Rabat, Marrakech, Tanger : entrez FIRST10 au paiement sur fleurinelle.com.

Conditions : commande supérieure à 50€, valable pour les 100 premières commandes, conditions applicables.""",
17: """You press Order in Lyon. What happens next in Morocco?

Your order comes in with the bouquet, your card, the day and the time window. The bouquet is made by hand, card tucked inside. It leaves in the window you picked, finds her door thanks to the full address, and your tracking page flips to Delivered.

That's flower delivery in Morocco, step by step. Questions about an order? hello@fleurinelle.com, with your order number.""",
18: """It's World Kindness Day. Who in Morocco deserves a surprise today?

The grandmother in Meknes. The friend in Agadir who's had a hard month. The aunt in Kenitra who always fills your suitcase with msemen.

Send flowers to Morocco with a card in her language. Comment CITY and we'll tell you if we deliver there.""",
19: """Gifts we send home to Morocco, honestly ranked.

Perfume: saved for a wedding in 2031. Money: gone by Friday. Clothes: wrong size, now your cousin's. Chocolate: shared with the whole building. Flowers to Morocco: on the table, photographed for the family group, discussed for a week.

Which one did you send this year? Confess in the comments.""",
20: """Livraison de fleurs au Maroc : choisissez un créneau où elle est à la maison.

Pas le matin du souk. Pas pendant la sieste. Pas à l'heure où elle part chez sa sœur. Vous choisissez le jour et le créneau en commandant : profitez-en.

Et laissez un numéro joignable. Si elle est descendue chercher le pain, le livreur l'appelle.

Commentez VILLE et dites-nous où elle habite.""",
21: """Mabrouk! A new baby in the family, and you can't make the first visit?

Send flowers to Morocco instead. Blessing is soft pink blooms, white lilies and a teddy bear, made for welcoming a baby girl. It arrives at the new parents' door with your card in Arabic, French, English or Spanish.

Comment CITY and we'll tell you if we deliver to theirs.""",
22: """Livraison de fleurs au Maroc dans 10 villes. La sienne en fait partie ?

Casablanca, Rabat, Marrakech, Tanger, Agadir, Fès, Meknès, Tétouan, Kénitra et Mohammedia. Vous choisissez la ville, le bouquet, le jour et le créneau, où que vous viviez.

Votre ville n'est pas dans la liste ? Dites-le-nous en commentaire. Chaque ville citée nous aide à choisir la prochaine.""",
23: """Happy Independence Day to everyone in Morocco, and to every Moroccan celebrating from far away.

Call home today. Or send flowers to Morocco, red and white, to the people who taught you what home means.

عيد الاستقلال المجيد""",
24: """Yes, you can send flowers to your dad. He'll pretend he doesn't care.

He'll say it wasn't necessary. He'll put them on the table anyway. And the card will end up in his wallet, next to a photo of you from 1998.

It's International Men's Day. Brothers, grandfathers and uncles count too. Flowers to Morocco, for him: comment CITY and we'll tell you if we deliver to his.""",
25: """"Thank you for the update and for the delivery photos. I really appreciate your service!"

Sent from Germany. Delivered in Morocco. Read by us about ten times.

Flower delivery in Morocco, ordered from anywhere. Comment CITY if there's someone you'd like to surprise.""",
26: """Anniversaire, naissance, pardon : quel bouquet envoyer au Maroc ? Le guide.

Un anniversaire : Rosalie. Une naissance : Blessing. Se faire pardonner : Heaven. Dire je t'aime : Lisa. Dire merci : Sofia. Juste comme ça : A Pop of Color.

Livraison de fleurs au Maroc dans 10 villes. Enregistrez ce guide pour la prochaine occasion.""",
27: """One person in Morocco. One bouquet. Who would you send it to?

Mama in Fes. Your grandmother in Tetouan. The friend in Marrakech who never forgets your birthday, even from 2,000 km away.

Tell us who, and which city, in the comments. If we can send flowers to Morocco for them, we'll let you know.""",
28: """You know you're a Moroccan living abroad when your suitcase home is 80% gifts.

Plus the supermarket video calls to ask Mama which tea to buy. The euro to dirham rate you know by heart. The "are you eating properly?" on every single call. And now, flowers to Morocco by delivery.

Which one is you? Comment the number.""",
29: """Mazal kayn! Your first bouquet is still 10% off with FIRST10.

You've been meaning to do it since Ramadan, haven't you? Use FIRST10 at checkout on fleurinelle.com for flower delivery in Morocco: Casablanca, Rabat, Marrakech, Tangier, Agadir, Fes, Meknes, Tetouan, Kenitra or Mohammedia.

Orders above 50€, valid for the first 100 orders only, conditions apply.""",
30: """From far away, with love. Mn l'ghorba, b l'hobb.

Someone you love is in Morocco. You're not. We bring the flowers. That's all Fleurinelle is: flower delivery in Morocco for people who live far from home, in 10 cities, with your card in her language.

Follow us so you never miss a birthday back home.""",
}
for _n, _c in CAPTIONS.items():
    POSTS[_n - 1]["caption"] = _c
