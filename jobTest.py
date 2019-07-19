from collections import Counter
import csv

jobs = "technical-test-jobs.csv"
professions = "technical-test-professions.csv"


try:
    # récupère la liste des professions
    professionsType = {}
    with open(professions, encoding="utf-8", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            professionsType.update({row["id"]: row["category_name"]})

    # récupère la liste des jobs
    jobsList = []
    with open(jobs, encoding="utf-8", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            jobsList.append([row[1], row[0]])
    # retire la première ligne de la liste (titre)
    del jobsList[0]

    # remplace les jobId par les jobCategory correspondants
    for job in jobsList:
        jobCategory = professionsType.get(job[1])
        job[1] = jobCategory
    print(jobsList)

    # prépare les coordonnées du tableau résultat

    jobsCategories = set()
    contractTypes = set()
    for job in jobsList:
        jobsCategories.add(job[1])
        contractTypes.add(job[0])

    print(jobsCategories)
    print(contractTypes)

    # compte les résultats
    count = []
    lin = 0
    for contract in contractTypes:
        col = 0
        count.append([])
        for category in jobsCategories:
            count[lin].append(0)
            for job in jobsList:
                if job[0] == contract and job[1] == category:
                    count[lin][col] += 1
            col += 1
        lin += 1

    print("---------------------------------")

    # initialise la première lignes des résultats
    count = []
    lin = 0
    for contract in contractTypes:
        col = 1
        count.append([contract])
        for category in jobsCategories:
            count[lin].append(0)
            for job in jobsList:
                if job[0] == contract and job[1] == category:
                    count[lin][col] += 1
            col += 1
        lin += 1

    for line in count:
        print(line)

finally:
    f.close()
