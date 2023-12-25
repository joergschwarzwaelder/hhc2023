# Objective 24: BONUS! Fishing Mastery
**Location: Sea**

Based on the [Objective 23](../Objective-23), the objective to catch one of each individual species living in the sea.
In the "sea" HTML code we can see a link to the [Fish Density Reference](https://2023.holidayhackchallenge.com/sea/fishdensityref.html)
```
<!-- <a href='fishdensityref.html'>[DEV ONLY] Fish Density Reference</a> -->
```
Using this information, we know that there are 171 different species out there in different habitats.

Ideally fishing is performed in the hotspot location of Piscis Cyberneticus Skodo, as all 171 species are available here. There is no need to move to another location to catch all fishes.  
![Hotspot of Piscis Cyberneticus Skodo overlayed with map of Geese Islands](Piscis%20Cyberneticus%20Skodo-on-Minimap.png)

Fishing automated using a Python3 script [Fishing-as-a-Service.py](faas.py):
```
HHC2023 🪿  username:joergen
HHC2023 🪿  password:
Dockslip 97addec9-e134-49c9-8998-9d782cacc4ee
Gotta Catch 'Em All 🎣
171 🐠 missing...
🐠 missing: Flutterfin Rainbow-Roll
🐠 missing: Gelatina Ringletfin
🐠 missing: Funfetti Flick-Flick
🐠 missing: Fluffle-Muffin Sparklefin
🐠 missing: Jovian Jamboree Jellydonut Jellyfish
🐠 missing: Gumball Glooperfish
🐠 missing: Jester Jellyfin
🐠 missing: The Chocolate Star Gingo Guppy
🐠 missing: Whirly Snuffleback Trout
🐠 missing: Jolly Jellyjam Fish
🐠 missing: Lounging Liquorice Crustacean-Nosed Berryfin
🐠 missing: Jinglefin Jellyfrizzle
🐠 missing: The Polka-Dot-Propeller Puffling Fish
🐠 missing: JubiliFLOPinear Snorkeldonut
🐠 missing: Glittering Gummy Guppy
🐠 missing: Whiskered Whizzler
🐠 missing: Flamango-Buzzling Sushi Swimmer
🐠 missing: Flutterfin Bubblegum Gumball
🐠 missing: ChocoSeahorsefly
🐠 missing: Speckled Toastfin Snorkelback
🐠 missing: Jamboree Jellywing
🐠 missing: Fantabulous Fry-Sherbert Aquapine
🐠 missing: Jamboree Jellofish
🐠 missing: Bubblegum Blowfish-Bee
🐠 missing: Frizzle Fringe Flutterfin
🐠 missing: Whiskered Jumblefish
🐠 missing: Bumblefin Toffee Torpedo
🐠 missing: Jolly Jellypeanut Fish
🐠 missing: Gumbubble Guppy
🐠 missing: Glittering Gummy Whipray
🐠 missing: Flippity Flan Flopper
🐠 missing: Biscuit Bugle-Tail Fish
🐠 missing: Strudel Scuttle Scalefish
🐠 missing: Bubblegum Bumblefin
🐠 missing: Flutterfin Falafeluncher
🐠 missing: The Splendiferous Spaghetti Starfin
🐠 missing: The Rainbow Jelibelly Floatfish
🐠 missing: Rhinoceros Beetle Bumble Tuna
🐠 missing: Hatwearing Hippofish
🐠 missing: Frizzle Fish
🐠 missing: Polka-Pop CandyFloss Fish
🐠 missing: Bumbleberry Floatfish
🐠 missing: Caramelotus Humming Float
🐠 missing: Dandy Candy Goby
🐠 missing: The Polka-Dot Pudding Puff
🐠 missing: Frosted Donut Jellyfluff Puffer
🐠 missing: Flamingo Flapjack Finaticus
🐠 missing: The Splendiferous Spaghetti Seahorsicle
🐠 missing: Flutterfin Scoopscale
🐠 missing: Frizzle Frazzle Fly-n-Fish
🐠 missing: Frizzle-Frizzled Jambalaya Jellyfish
🐠 missing: Sprinkfish
🐠 missing: Fantail Flutterfin
🐠 missing: JellyChip CuddleSwimmer
🐠 missing: Whiskered Lollipop Loonfish
🐠 missing: Jester Gumball Pufferfish
🐠 missing: The Hummingbrewster BumbleFlish
🐠 missing: Jangleroo Snackfin
🐠 missing: Blibbering Blubberwing
🐠 missing: The Bubblegum Confeetish
🐠 missing: Fantastical Fusilloni Flounderfish
🐠 missing: Pizzafin Flutterbub
🐠 missing: The Whiskered Watermelon Pufferfish
🐠 missing: The Bumblebee Doughnut Delphin
🐠 missing: Pistachio Pizzafin Puffinfly
🐠 missing: Aquatic JellyPuff Doughnut Shark
🐠 missing: Gumball Guppygator
🐠 missing: The Burgerwing Seahorse
🐠 missing: Bellychuckle Balloonfish
🐠 missing: FizzleWing PuffleGill
🐠 missing: Bumbleberry Rainbow Flicorn Fish
🐠 missing: Whistlefin Wafflegill
🐠 missing: Pizzadillo Glitter-Guppy
🐠 missing: Jamboree Jellydonut Jellyfish Trout
🐠 missing: The Bubblegum Bumblefin
🐠 missing: Gelatino Floatyfin
🐠 missing: The Frambuzzle Flickerfin
🐠 missing: The Speckled Pizzafin Fizzflyer
🐠 missing: Sparkling Pizzafin Pixie-fish
🐠 missing: Bumblecado Finstache Hybridsail
🐠 missing: Pizzamarine Popcorn Puffer
🐠 missing: Laughter Ligrolomia
🐠 missing: Frosted Jelly Doughnut Pegasus Finfish
🐠 missing: The Whirling Donut Jellygator
🐠 missing: Flutterfin Cupcake Goby
🐠 missing: The Gumball Guppy
🐠 missing: Bubblegum Blowfish Beetle Bug
🐠 missing: Sparkling Gumbubble Piscadot
🐠 missing: The Flamboyant Flutter-fish
🐠 missing: Twinkling Tortellini Trouterfly
🐠 missing: Beatleberry Fluff Guppy.
🐠 missing: Glaze Meringuelle
🐠 missing: The Whiskered Blubberberry Flapper
🐠 missing: Sherbet Swooshfin
🐠 missing: Marzipoisson Popsicala
🐠 missing: Bubblegum Ballistic Barracuda
🐠 missing: Puzzletail Splashcake
🐠 missing: Fantasia Fluffernutter Finfish
🐠 missing: Rainbow Jelly-Dough Fish
🐠 missing: Flutterfin Pizzapuffer
🐠 missing: BugBrella Aquacake
🐠 missing: Twirly Finny Cakeling
🐠 missing: Frizzleberry Flapjack Fish
🐠 missing: Whiskered Sprinkle Glider
🐠 missing: The Pristimaela Parfait Pengu-Angel
🐠 missing: Bubblerooni WhiskerWaffle
🐠 missing: The Speckled Whisker-Spoon Puffer
🐠 missing: BumbleSquid Donutella
🐠 missing: Sparkleberry Gobblefin
🐠 missing: Fizzgiggle Frizzlefin
🐠 missing: JibberJelly Sundae Swimmer
🐠 missing: The Flutterfin Pastry Puffer
🐠 missing: Rainbow Gummy Scalefish
🐠 missing: Jingle JellyFroth Fish
🐠 missing: The Spotted Flutterfin Pastrytetra
🐠 missing: Flutterfin Hotcheeto Penguinfish
🐠 missing: Piscis Cyberneticus Skodo
🐠 missing: Oreo OctoPufferRock
🐠 missing: Fluffernutter Pufferpine
🐠 missing: Whirlygig Polka-Dotted Jelly-Donut Pufferfish
🐠 missing: Bumbleberry Gilled Glider
🐠 missing: Polkadot Pancake Puffer
🐠 missing: Mermacorn Fish
🐠 missing: Sprinkle Starfish Sardine
🐠 missing: Choco-Bumblefin Parrot Trout
🐠 missing: The Fantabulous Gala Glazed-Guppy
🐠 missing: Pudding Puff ParrotMoth Fish
🐠 missing: Fantastical Flapjack Flipperfin
🐠 missing: TruffleBugle ZephyrFish
🐠 missing: Bumbleberry Glitterfin
🐠 missing: The Jester Jellycarafe
🐠 missing: The Flamingotuna McSprinklefin
🐠 missing: Whiskerfroth Flutterfin
🐠 missing: Spotted Sprinkledonut Puffer
🐠 missing: Stripe-tailed Pepperoni Puffer
🐠 missing: Jelly-Feather Macaroon Guppy
🐠 missing: Flutterfin Pancake Puffer.
🐠 missing: Whiskered Rainbow Glidleberry
🐠 missing: Chucklefin Clownfish
🐠 missing: Bumbleberry Snorkelsnout
🐠 missing: Jolly Jellydozer
🐠 missing: The Polka Dotted Jello-fish
🐠 missing: The Bumbleberry Guppiesaurus
🐠 missing: Flutterfin Pizzacrust Glimmertail
🐠 missing: Bumblebee, Pizza-fin Jamboree
🐠 missing: Whizzbizzle Poptuckle
🐠 missing: Candyfloss Clownphino
🐠 missing: Flutterglaze Bumblefin
🐠 missing: Bumbleberry Poptarticus
🐠 missing: Plaid Zephyr Cuddlefin
🐠 missing: Jolly Jambalaya Jubilee Fish
🐠 missing: Confetti Clownfrippery Fish
🐠 missing: Rainbow Jelly-Bumble Shark
🐠 missing: Marshmallow Pogo-Starfish
🐠 missing: The Spangled Jelly-Tortle Ripplefin
🐠 missing: Fantabulous Rainbow Polka Poptartfish
🐠 missing: The ChocoChandelier Goldnipper
🐠 missing: Gummybrella Anemofin
🐠 missing: Gummy Fizzler
🐠 missing: The Bumblebelly Polkadot Glaze-fish
🐠 missing: Fantaray Flakefin
🐠 missing: Splendiferous Ribbontail
🐠 missing: The Butterfleagleberry Seahorse
🐠 missing: Sushinano Sweetsquid
🐠 missing: The Whiskered Melonfin
🐠 missing: The Fantastical Fizzbopper
🐠 missing: Splashtastic Bagelback Rainbownose
🐠 missing: Pizzafly Rainbowgill
🐠 missing: Frizzling Bubblehopper
🐠 missing: Cuckoo Bubblegum Unicornfish
🐠 missing: The Lucid Lollyscale
171 🐠 missing...
Thu Dec 21 08:27:08 2023: *** caught 🐠 Fantasia Fluffernutter Finfish, 170 more to go
Thu Dec 21 08:27:16 2023: *** caught 🐠 Gelatino Floatyfin, 169 more to go
Thu Dec 21 08:27:40 2023: *** caught 🐠 The Flutterfin Pastry Puffer, 168 more to go
Thu Dec 21 08:27:42 2023: *** caught 🐠 Rainbow Gummy Scalefish, 167 more to go
Thu Dec 21 08:27:48 2023: *** caught 🐠 Fantaray Flakefin, 166 more to go
Thu Dec 21 08:27:51 2023: *** caught 🐠 Jolly Jellypeanut Fish, 165 more to go
Thu Dec 21 08:27:55 2023: *** caught 🐠 Flutterglaze Bumblefin, 164 more to go
Thu Dec 21 08:28:08 2023: *** caught 🐠 Hatwearing Hippofish, 163 more to go
Thu Dec 21 08:28:16 2023: *** caught 🐠 Gummybrella Anemofin, 162 more to go
Thu Dec 21 08:28:32 2023: *** caught 🐠 The Flamboyant Flutter-fish, 161 more to go
Thu Dec 21 08:28:46 2023: *** caught 🐠 JibberJelly Sundae Swimmer, 160 more to go
Thu Dec 21 08:28:58 2023: *** caught 🐠 Jingle JellyFroth Fish, 159 more to go
Thu Dec 21 08:29:24 2023: *** caught 🐠 Gumball Guppygator, 158 more to go
Thu Dec 21 08:29:50 2023: *** caught 🐠 Pizzadillo Glitter-Guppy, 157 more to go
Thu Dec 21 08:30:54 2023: *** caught 🐠 Pizzafly Rainbowgill, 156 more to go
Thu Dec 21 08:30:56 2023: *** caught 🐠 Fluffernutter Pufferpine, 155 more to go
Thu Dec 21 08:31:08 2023: *** caught 🐠 Bumbleberry Gilled Glider, 154 more to go
Thu Dec 21 08:31:32 2023: *** caught 🐠 Piscis Cyberneticus Skodo, 153 more to go
Thu Dec 21 08:31:44 2023: *** caught 🐠 Whirlygig Polka-Dotted Jelly-Donut Pufferfish, 152 more to go
Thu Dec 21 08:31:54 2023: *** caught 🐠 Marshmallow Pogo-Starfish, 151 more to go
Thu Dec 21 08:31:58 2023: *** caught 🐠 Jamboree Jellofish, 150 more to go
Thu Dec 21 08:32:00 2023: *** caught 🐠 Jinglefin Jellyfrizzle, 149 more to go
Thu Dec 21 08:32:02 2023: *** caught 🐠 Splendiferous Ribbontail, 148 more to go
Thu Dec 21 08:32:10 2023: *** caught 🐠 Beatleberry Fluff Guppy., 147 more to go
Thu Dec 21 08:32:22 2023: *** caught 🐠 The Rainbow Jelibelly Floatfish, 146 more to go
Thu Dec 21 08:32:38 2023: *** caught 🐠 Jolly Jambalaya Jubilee Fish, 145 more to go
Thu Dec 21 08:32:40 2023: *** caught 🐠 Bubblegum Ballistic Barracuda, 144 more to go
Thu Dec 21 08:33:18 2023: *** caught 🐠 Pizzamarine Popcorn Puffer, 143 more to go
Thu Dec 21 08:33:20 2023: *** caught 🐠 Confetti Clownfrippery Fish, 142 more to go
Thu Dec 21 08:33:54 2023: *** caught 🐠 Rainbow Jelly-Bumble Shark, 141 more to go
Thu Dec 21 08:33:56 2023: *** caught 🐠 The Bubblegum Confeetish, 140 more to go
Thu Dec 21 08:34:08 2023: *** caught 🐠 Strudel Scuttle Scalefish, 139 more to go
Thu Dec 21 08:34:10 2023: *** caught 🐠 Sushinano Sweetsquid, 138 more to go
Thu Dec 21 08:34:38 2023: *** caught 🐠 The Whiskered Watermelon Pufferfish, 137 more to go
Thu Dec 21 08:36:02 2023: *** caught 🐠 Glittering Gummy Guppy, 136 more to go
Thu Dec 21 08:36:12 2023: *** caught 🐠 Mermacorn Fish, 135 more to go
Thu Dec 21 08:36:14 2023: *** caught 🐠 Jester Gumball Pufferfish, 134 more to go
Thu Dec 21 08:37:24 2023: *** caught 🐠 Flamingo Flapjack Finaticus, 133 more to go
Thu Dec 21 08:37:34 2023: *** caught 🐠 Glaze Meringuelle, 132 more to go
Thu Dec 21 08:37:38 2023: *** caught 🐠 The Whiskered Melonfin, 131 more to go
Thu Dec 21 08:38:02 2023: *** caught 🐠 The Spotted Flutterfin Pastrytetra, 130 more to go
Thu Dec 21 08:38:10 2023: *** caught 🐠 Flutterfin Pancake Puffer., 129 more to go
Thu Dec 21 08:38:26 2023: *** caught 🐠 The Splendiferous Spaghetti Seahorsicle, 128 more to go
Thu Dec 21 08:38:34 2023: *** caught 🐠 The Chocolate Star Gingo Guppy, 127 more to go
Thu Dec 21 08:38:58 2023: *** caught 🐠 Whizzbizzle Poptuckle, 126 more to go
Thu Dec 21 08:39:26 2023: *** caught 🐠 Gummy Fizzler, 125 more to go
Thu Dec 21 08:39:28 2023: *** caught 🐠 Pizzafin Flutterbub, 124 more to go
Thu Dec 21 08:40:12 2023: *** caught 🐠 Bubblerooni WhiskerWaffle, 123 more to go
Thu Dec 21 08:40:18 2023: *** caught 🐠 The Bumblebee Doughnut Delphin, 122 more to go
Thu Dec 21 08:40:20 2023: *** caught 🐠 Jester Jellyfin, 121 more to go
Thu Dec 21 08:40:24 2023: *** caught 🐠 Sprinkfish, 120 more to go
Thu Dec 21 08:40:50 2023: *** caught 🐠 Fantail Flutterfin, 119 more to go
Thu Dec 21 08:41:20 2023: *** caught 🐠 The Whiskered Blubberberry Flapper, 118 more to go
Thu Dec 21 08:41:44 2023: *** caught 🐠 Twirly Finny Cakeling, 117 more to go
Thu Dec 21 08:42:38 2023: *** caught 🐠 Spotted Sprinkledonut Puffer, 116 more to go
Thu Dec 21 08:42:40 2023: *** caught 🐠 Polkadot Pancake Puffer, 115 more to go
Thu Dec 21 08:42:50 2023: *** caught 🐠 Rainbow Jelly-Dough Fish, 114 more to go
Thu Dec 21 08:42:56 2023: *** caught 🐠 Whiskered Lollipop Loonfish, 113 more to go
Thu Dec 21 08:43:08 2023: *** caught 🐠 The Splendiferous Spaghetti Starfin, 112 more to go
Thu Dec 21 08:43:18 2023: *** caught 🐠 Frosted Jelly Doughnut Pegasus Finfish, 111 more to go
Thu Dec 21 08:43:34 2023: *** caught 🐠 Frizzling Bubblehopper, 110 more to go
Thu Dec 21 08:43:52 2023: *** caught 🐠 Polka-Pop CandyFloss Fish, 109 more to go
Thu Dec 21 08:44:46 2023: *** caught 🐠 Aquatic JellyPuff Doughnut Shark, 108 more to go
Thu Dec 21 08:45:18 2023: *** caught 🐠 Bumblebee, Pizza-fin Jamboree, 107 more to go
Thu Dec 21 08:45:20 2023: *** caught 🐠 Fantabulous Rainbow Polka Poptartfish, 106 more to go
Thu Dec 21 08:45:42 2023: *** caught 🐠 Bumblefin Toffee Torpedo, 105 more to go
Thu Dec 21 08:45:46 2023: *** caught 🐠 TruffleBugle ZephyrFish, 104 more to go
Thu Dec 21 08:46:10 2023: *** caught 🐠 Flutterfin Falafeluncher, 103 more to go
Thu Dec 21 08:46:12 2023: *** caught 🐠 Chucklefin Clownfish, 102 more to go
Thu Dec 21 08:46:16 2023: *** caught 🐠 Bumbleberry Floatfish, 101 more to go
Thu Dec 21 08:46:20 2023: *** caught 🐠 Marzipoisson Popsicala, 100 more to go
Thu Dec 21 08:46:23 2023: *** caught 🐠 The Pristimaela Parfait Pengu-Angel, 99 more to go
Thu Dec 21 08:47:02 2023: *** caught 🐠 Sparkleberry Gobblefin, 98 more to go
Thu Dec 21 08:47:06 2023: *** caught 🐠 The Burgerwing Seahorse, 97 more to go
Thu Dec 21 08:47:42 2023: *** caught 🐠 The Lucid Lollyscale, 96 more to go
Thu Dec 21 08:48:32 2023: *** caught 🐠 Frizzle-Frizzled Jambalaya Jellyfish, 95 more to go
Thu Dec 21 08:48:36 2023: *** caught 🐠 Flutterfin Hotcheeto Penguinfish, 94 more to go
Thu Dec 21 08:48:48 2023: *** caught 🐠 The Whirling Donut Jellygator, 93 more to go
Thu Dec 21 08:48:54 2023: *** caught 🐠 Jangleroo Snackfin, 92 more to go
Thu Dec 21 08:49:54 2023: *** caught 🐠 Sparkling Gumbubble Piscadot, 91 more to go
Thu Dec 21 08:50:12 2023: *** caught 🐠 Flamango-Buzzling Sushi Swimmer, 90 more to go
Thu Dec 21 08:50:20 2023: *** caught 🐠 Flutterfin Pizzapuffer, 89 more to go
Thu Dec 21 08:50:26 2023: *** caught 🐠 Fantastical Flapjack Flipperfin, 88 more to go
Thu Dec 21 08:51:48 2023: *** caught 🐠 Flutterfin Bubblegum Gumball, 87 more to go
Thu Dec 21 08:52:00 2023: *** caught 🐠 Sprinkle Starfish Sardine, 86 more to go
Thu Dec 21 08:52:10 2023: *** caught 🐠 Jelly-Feather Macaroon Guppy, 85 more to go
Thu Dec 21 08:52:36 2023: *** caught 🐠 Oreo OctoPufferRock, 84 more to go
Thu Dec 21 08:52:44 2023: *** caught 🐠 Whiskered Whizzler, 83 more to go
Thu Dec 21 08:53:18 2023: *** caught 🐠 Blibbering Blubberwing, 82 more to go
Thu Dec 21 08:54:00 2023: *** caught 🐠 Jolly Jellydozer, 81 more to go
Thu Dec 21 08:54:54 2023: *** caught 🐠 Funfetti Flick-Flick, 80 more to go
Thu Dec 21 08:54:56 2023: *** caught 🐠 Frizzle Fish, 79 more to go
Thu Dec 21 08:55:26 2023: *** caught 🐠 The Butterfleagleberry Seahorse, 78 more to go
Thu Dec 21 08:55:58 2023: *** caught 🐠 Bumbleberry Glitterfin, 77 more to go
Thu Dec 21 08:56:30 2023: *** caught 🐠 Flutterfin Pizzacrust Glimmertail, 76 more to go
Thu Dec 21 08:56:42 2023: *** caught 🐠 Jolly Jellyjam Fish, 75 more to go
Thu Dec 21 08:56:48 2023: *** caught 🐠 Frizzle Fringe Flutterfin, 74 more to go
Thu Dec 21 08:57:46 2023: *** caught 🐠 Rhinoceros Beetle Bumble Tuna, 73 more to go
Thu Dec 21 08:57:50 2023: *** caught 🐠 Bubblegum Bumblefin, 72 more to go
Thu Dec 21 08:57:52 2023: *** caught 🐠 Frosted Donut Jellyfluff Puffer, 71 more to go
Thu Dec 21 08:58:12 2023: *** caught 🐠 Pudding Puff ParrotMoth Fish, 70 more to go
Thu Dec 21 08:59:02 2023: *** caught 🐠 Whiskered Jumblefish, 69 more to go
Thu Dec 21 08:59:14 2023: *** caught 🐠 Frizzle Frazzle Fly-n-Fish, 68 more to go
Thu Dec 21 08:59:50 2023: *** caught 🐠 Jamboree Jellydonut Jellyfish Trout, 67 more to go
Thu Dec 21 09:00:42 2023: *** caught 🐠 Bubblegum Blowfish Beetle Bug, 66 more to go
Thu Dec 21 09:01:14 2023: *** caught 🐠 Caramelotus Humming Float, 65 more to go
Thu Dec 21 09:01:38 2023: *** caught 🐠 FizzleWing PuffleGill, 64 more to go
Thu Dec 21 09:02:42 2023: *** caught 🐠 Whistlefin Wafflegill, 63 more to go
Thu Dec 21 09:02:48 2023: *** caught 🐠 Bumbleberry Poptarticus, 62 more to go
Thu Dec 21 09:03:28 2023: *** caught 🐠 Flutterfin Rainbow-Roll, 61 more to go
Thu Dec 21 09:04:02 2023: *** caught 🐠 Cuckoo Bubblegum Unicornfish, 60 more to go
Thu Dec 21 09:04:36 2023: *** caught 🐠 The Spangled Jelly-Tortle Ripplefin, 59 more to go
Thu Dec 21 09:05:10 2023: *** caught 🐠 Laughter Ligrolomia, 58 more to go
Thu Dec 21 09:05:32 2023: *** caught 🐠 Candyfloss Clownphino, 57 more to go
Thu Dec 21 09:05:52 2023: *** caught 🐠 JellyChip CuddleSwimmer, 56 more to go
Thu Dec 21 09:06:26 2023: *** caught 🐠 Flutterfin Scoopscale, 55 more to go
Thu Dec 21 09:06:52 2023: *** caught 🐠 The Hummingbrewster BumbleFlish, 54 more to go
Thu Dec 21 09:07:12 2023: *** caught 🐠 Bellychuckle Balloonfish, 53 more to go
Thu Dec 21 09:09:04 2023: *** caught 🐠 Flippity Flan Flopper, 52 more to go
Thu Dec 21 09:09:22 2023: *** caught 🐠 The Jester Jellycarafe, 51 more to go
Thu Dec 21 09:09:38 2023: *** caught 🐠 The Polka-Dot Pudding Puff, 50 more to go
Thu Dec 21 09:10:44 2023: *** caught 🐠 Biscuit Bugle-Tail Fish, 49 more to go
Thu Dec 21 09:14:32 2023: *** caught 🐠 Splashtastic Bagelback Rainbownose, 48 more to go
Thu Dec 21 09:15:06 2023: *** caught 🐠 Stripe-tailed Pepperoni Puffer, 47 more to go
Thu Dec 21 09:16:10 2023: *** caught 🐠 The ChocoChandelier Goldnipper, 46 more to go
Thu Dec 21 09:16:34 2023: *** caught 🐠 Gumball Glooperfish, 45 more to go
Thu Dec 21 09:19:14 2023: *** caught 🐠 The Gumball Guppy, 44 more to go
Thu Dec 21 09:19:26 2023: *** caught 🐠 Gelatina Ringletfin, 43 more to go
Thu Dec 21 09:22:00 2023: *** caught 🐠 Puzzletail Splashcake, 42 more to go
Thu Dec 21 09:22:38 2023: *** caught 🐠 Fantabulous Fry-Sherbert Aquapine, 41 more to go
Thu Dec 21 09:22:46 2023: *** caught 🐠 Sherbet Swooshfin, 40 more to go
Thu Dec 21 09:24:48 2023: *** caught 🐠 The Bumblebelly Polkadot Glaze-fish, 39 more to go
Thu Dec 21 09:26:20 2023: *** caught 🐠 Flutterfin Cupcake Goby, 38 more to go
Thu Dec 21 09:26:32 2023: *** caught 🐠 Fluffle-Muffin Sparklefin, 37 more to go
Thu Dec 21 09:28:14 2023: *** caught 🐠 The Bubblegum Bumblefin, 36 more to go
Thu Dec 21 09:28:50 2023: *** caught 🐠 The Flamingotuna McSprinklefin, 35 more to go
Thu Dec 21 09:30:14 2023: *** caught 🐠 Jovian Jamboree Jellydonut Jellyfish, 34 more to go
Thu Dec 21 09:31:28 2023: *** caught 🐠 Lounging Liquorice Crustacean-Nosed Berryfin, 33 more to go
Thu Dec 21 09:34:10 2023: *** caught 🐠 Jamboree Jellywing, 32 more to go
Thu Dec 21 09:34:19 2023: *** caught 🐠 Pistachio Pizzafin Puffinfly, 31 more to go
Thu Dec 21 09:38:06 2023: *** caught 🐠 JubiliFLOPinear Snorkeldonut, 30 more to go
Thu Dec 21 09:43:00 2023: *** caught 🐠 Fantastical Fusilloni Flounderfish, 29 more to go
Thu Dec 21 09:43:10 2023: *** caught 🐠 Bumbleberry Rainbow Flicorn Fish, 28 more to go
Thu Dec 21 09:43:32 2023: *** caught 🐠 The Bumbleberry Guppiesaurus, 27 more to go
Thu Dec 21 09:45:04 2023: *** caught 🐠 BumbleSquid Donutella, 26 more to go
Thu Dec 21 09:46:20 2023: *** caught 🐠 Sparkling Pizzafin Pixie-fish, 25 more to go
Thu Dec 21 09:49:32 2023: *** caught 🐠 Speckled Toastfin Snorkelback, 24 more to go
Thu Dec 21 09:54:10 2023: *** caught 🐠 Bubblegum Blowfish-Bee, 23 more to go
Thu Dec 21 09:55:52 2023: *** caught 🐠 Gumbubble Guppy, 22 more to go
Thu Dec 21 09:56:38 2023: *** caught 🐠 The Speckled Whisker-Spoon Puffer, 21 more to go
Thu Dec 21 09:57:20 2023: *** caught 🐠 ChocoSeahorsefly, 20 more to go
Thu Dec 21 10:06:00 2023: *** caught 🐠 BugBrella Aquacake, 19 more to go
Thu Dec 21 10:08:54 2023: *** caught 🐠 Twinkling Tortellini Trouterfly, 18 more to go
Thu Dec 21 10:11:20 2023: *** caught 🐠 Plaid Zephyr Cuddlefin, 17 more to go
Thu Dec 21 10:14:22 2023: *** caught 🐠 The Frambuzzle Flickerfin, 16 more to go
Thu Dec 21 10:29:06 2023: *** caught 🐠 Whiskerfroth Flutterfin, 15 more to go
Thu Dec 21 10:29:19 2023: *** caught 🐠 Whiskered Sprinkle Glider, 14 more to go
Thu Dec 21 10:33:56 2023: *** caught 🐠 The Fantabulous Gala Glazed-Guppy, 13 more to go
Thu Dec 21 10:35:50 2023: *** caught 🐠 Dandy Candy Goby, 12 more to go
Thu Dec 21 10:46:44 2023: *** caught 🐠 The Polka Dotted Jello-fish, 11 more to go
Thu Dec 21 10:57:24 2023: *** caught 🐠 Frizzleberry Flapjack Fish, 10 more to go
Thu Dec 21 11:11:40 2023: *** caught 🐠 The Fantastical Fizzbopper, 9 more to go
Thu Dec 21 11:32:22 2023: *** caught 🐠 Bumbleberry Snorkelsnout, 8 more to go
Thu Dec 21 11:35:19 2023: *** caught 🐠 Choco-Bumblefin Parrot Trout, 7 more to go
Thu Dec 21 11:57:34 2023: *** caught 🐠 The Polka-Dot-Propeller Puffling Fish, 6 more to go
Thu Dec 21 12:24:16 2023: *** caught 🐠 The Speckled Pizzafin Fizzflyer, 5 more to go
Thu Dec 21 12:30:26 2023: *** caught 🐠 Fizzgiggle Frizzlefin, 4 more to go
Thu Dec 21 13:01:26 2023: *** caught 🐠 Whirly Snuffleback Trout, 3 more to go
Thu Dec 21 15:25:04 2023: *** caught 🐠 Glittering Gummy Whipray, 2 more to go
Thu Dec 21 16:01:48 2023: *** caught 🐠 Bumblecado Finstache Hybridsail, 1 more to go
Thu Dec 21 16:45:40 2023: *** caught 🐠 Whiskered Rainbow Glidleberry, 0 more to go
```

**Achievement: BONUS! Fishing Mastery!**

Interestingly two fish species have a dot "." in their name: "Beatleberry Fluff Guppy." and "Flutterfin Pancake Puffer."

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3NzQ1NDA1NzQsMTcwOTAxOTI3LC0xMD
Y1MDUyNDcwLDk0NzkwODU1OCwtMjAwNDA2NzE4MCwxNDYwNjM4
NTgxLC0xMDI0MTk2ODAxLC0yMDEwMTkyNjNdfQ==
-->