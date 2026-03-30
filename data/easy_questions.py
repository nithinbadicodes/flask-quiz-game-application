easy_questions = [
    {
        "question": "Which US president had disability?",
        "options": [
            "Harry S. Truman",
            "George Washington",
            "Franklin D. Roosevelt",
            "Herbert Hoover"
        ],
        "answer": 2,
        "hint": "He contracted polio in 1921 which left him paralyzed from the waist down."
    },
    {
        "question": "What was the first book released at the same time in Braille as it was in print?",
        "options": [
            "Charlotte’s Web",
            "Harry Potter and the Half-Blood Prince",
            "Little Women",
            "A Wrinkle in Time"
        ],
        "answer": 1,
        "hint": "‘Killing is not so easy as the innocent believe’"
    },
    {
        "question": "When is disability pride month?",
        "options": [
            "January",
            "July",
            "August",
            "October"
        ],
        "answer": 1,
        "hint": "It commemorates the signing of the Americans with Disabilities Act (ADA)."
    },
    {
        "question": "Which film featuring characters with disabilities recently became the highest grossing animated film in North America?",
        "options": [
            "The Incredibles",
            "The Lorax",
            "Inside Out",
            "Finding Dory"
        ],
        "answer": 2,
        "hint": "‘Maybe this is what happens when you grow up. You feel less joy.’"
    },
    {
        "question": "Which city had the first independent living centre in the country?",
        "options": [
            "Berkeley, CA",
            "New York, NY",
            "Providence, RI",
            "Boston, MA"
        ],
        "answer": 0,
        "hint": "Founded in 1972 by disability rights activist Ed Roberts."
    },
    {
        "question": "What year was the Americans with Disabilities Act passed?",
        "options": [
            "1968",
            "1972",
            "1990",
            "2012"
        ],
        "answer": 2,
        "hint": "It was signed by President George H.W. Bush."
    },
    {
        "question": "Which of the following artists had a disability?",
        "options": [
            "Ray Charles",
            "Maya Angelou",
            "Stevie Wonder",
            "All of the above"
        ],
        "answer": 3,
        "hint": "Each listed artist has spoken publicly about living with a disability."
    },
    {
        "question": "Cerebral Palsy is a type of:",
        "options": [
            "Neurological impairment",
            "Musculoskeletal impairment",
            "Psychotic disorder",
            "None of the above"
        ],
        "answer": 0,
        "hint": "It may be associated with intellectual disabilities, seizures, or speech issues."
    },
    {
        "question": "A child who reads ‘top’ as ‘pot’ falls in which category of learning disability?",
        "options": [
            "Dyscalculia",
            "Dyspraxia",
            "Dyslexia",
            "Dysgraphia"
        ],
        "answer": 2,
        "hint": "A specific language-based disorder."
    },
    {
        "question": "Physical barriers include:",
        "options": [
            "No ramps along with stairs for persons with locomotor disability",
            "Lack of elevators in most public places",
            "Lack of tactile path",
            "All of the above"
        ],
        "answer": 3,
        "hint": "Think about obstacles that prevent physical access to buildings."
    },
    {
        "question": "What is congenital blindness?",
        "options": [
            "Loss of vision after birth but by age five",
            "A loss of vision before or at birth",
            "Loss of vision as a result of an accident",
            "None of the above"
        ],
        "answer": 1,
        "hint": "Remember the meaning of congenital."
    },
    {
        "question": "When was the RPwD Act enacted?",
        "options": [
            "1985",
            "1995",
            "2016",
            "2005"
        ],
        "answer": 2,
        "hint": "It replaced the earlier 1995 Act in India."
    },
    {
        "question": "When did the government of India pass RPwD Act to give an effect to the United Nations Conventions on the Rights of Persons with Disabilities?",
        "options": [
            "20 December 2016",
            "27 December 2016",
            "27 December 2015",
            "20 December 2015"
        ],
        "answer": 1,
        "hint": "It was passed in the final week of December 2016."
    },
    {
        "question": "Which day every year is celebrated as World Disability Day?",
        "options": [
            "December 3",
            "December 4",
            "December 5",
            "December 2"
        ],
        "answer": 0,
        "hint": "It is observed globally at the beginning of December."
    },
    {
        "question": "If the IQ of a child is between which range are they considered to have mild intellectual disability?",
        "options": [
            "35 and 55",
            "20 and 40",
            "10 and 20",
            "55 and 70"
        ],
        "answer": 3,
        "hint": "Mild level is closest to the lower boundary of the average IQ range."
    },
    {
        "question": "The term mental retardation is replaced with which term?",
        "options": [
            "Intellectual disability",
            "Mental weakness",
            "Intellectual backwardness",
            "Intellectual disadvantage"
        ],
        "answer": 0,
        "hint": "It is the respectful and medically accepted term used today."
    },
    {
        "question": "Claustrophobia is a fear of enclosed places. It is an example of:",
        "options": [
            "Global developmental delay",
            "Obsessive-Compulsive Disorder",
            "Anxiety disorder",
            "Autism"
        ],
        "answer": 2,
        "hint": "A phobia is a type of anxiety-related condition."
    },
    {
        "question": "What’s the International Symbol of Access (ISA)?",
        "options": [
            "A person with a walking stick",
            "A wheelchair icon",
            "A hearing aid symbol",
            "A dove icon"
        ],
        "answer": 1,
        "hint": "This accessibility symbol is commonly seen on parking spaces and building entrances."
    },
    {
        "question": "Which of these could be examples of non-visible disabilities?",
        "options": [
            "Autism",
            "Dyslexia",
            "All of the above",
            "Chronic pain"
        ],
        "answer": 2,
        "hint": "Some disabilities are not immediately visible to others."
    },
    {
        "question": "Arthritis affects a person’s ability to:",
        "options": [
            "Walk",
            "Ride a bike",
            "Lift",
            "All of the above"
        ],
        "answer": 3,
        "hint": "This condition affects joints and movement in everyday activities."
    },
    {
        "question": "Which of these Indian films features a character with Dyslexia?",
        "options": ["Black", "Iqbal", "Taare Zameen Par", "Barfi!"],
        "answer": 2,
        "hint": "This popular Indian film tells the story of a child struggling with reading difficulties."
    }
]

import random
for question in easy_questions:
    random.shuffle(question['options'])
