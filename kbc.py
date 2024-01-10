questionSet = [
    {
        "question": "What is the name of the first PM of Nepal?",
        "options": [
            {"option": "Bhimsim Thapa", "isCorrect": True},
            {"option": "Sudeep Koirala", "isCorrect": False},
        ]
    },
    {
        "question": "What is the name of the current president of Nepal?",
        "options": [
            {"option": "Bhimsim Thapa", "isCorrect": False},
            {"option": "Sudeep Koirala", "isCorrect": False},
            {"option": "Ran chandra Poudel", "isCorrect": True},
        ]
    },
]

for ques in questionSet:
    print(ques["question"])
    for opt in ques["options"]:
        print(opt["option"])
