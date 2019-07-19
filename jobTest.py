import csv


def job_offers(jobs="technical-test-jobs.csv", professions="technical-test-professions.csv"):
    try:
        # importe la liste des professions sous forme d'un dictionnaire
        professionsType = {}
        with open(professions, encoding="utf-8", newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                professionsType.update({row["id"]: row["category_name"]})

        # importe la liste des jobs
        jobsList = []
        with open(jobs, encoding="utf-8", newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                jobsList.append([row[1], row[0]])# (seules les 2 premières colonnes sont utiles)
        del jobsList[0]  # retire la première ligne de la liste (titre)

        # remplace les jobId par les jobCategory correspondants
        for job in jobsList:
            jobCategory = professionsType.get(job[1])
            job[1] = jobCategory


        # prépare les coordonnées du tableau résultat

        jobsCategories = set()
        contractTypes = set()
        for job in jobsList:
            jobsCategories.add(job[1])
            contractTypes.add(job[0])

        # compte les résultats

        # initialise la première lignes des résultats
        title = ["---JOBS---"]
        for cat in jobsCategories:
            if cat:
                title.append(cat)
            else:
                title.append("AUTRE")
        count = [title]

        lin = 1
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
    finally:
        f.close()
    return count


def display_jobs(count):
    # affichage des résultats en console
    form = "{0:15}{1:15}{2:15}{3:15}{4:15}{5:15}{6:15}{7:15}{8:15}"
    for line in count:
        print(form.format(*line))


display_jobs(job_offers())


def nb_offre(jobs="technical-test-jobs.csv"):
    # nb d'offre dans le csv
    nboffre = 0
    with open(jobs, encoding="utf-8", newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            nboffre += 1
    return nboffre-1  # retire la ligne de titre


def test_total(jobs="technical-test-jobs.csv"):
    array = job_offers()
    total = 0
    for value in array:
        total += sum([i for i in value if isinstance(i, int)])

    assert total == nb_offre(jobs)




test_total()


