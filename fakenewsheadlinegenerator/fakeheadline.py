import random
subjects=[
    "sarukh khan",
    "virat kholi",
    "nirmala khan",
    "autorikshaw",
    "prime minister",
]
actions=[
    "launches",
    "cancels",
    "dances",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]
places_or_things=[
    "at red fort",
    "in mumbai local train",
    "a plote of samosa",
    "inside parliament",
    "during ipl match",
    "at border",
    
    ]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)   
    places_or_thing=random.choice(places_or_things)

    headline=f"Breaking news: {subject} {action} {places_or_thing}"
    print("\n" + headline)
    user_input= input("\n Do u want another headline? (yes/no):").strip().lower()
    if user_input=="no":
        break

print("\n thanks for using the fake News Headline Generator Have a nice day thanks your for using my basic program.....")