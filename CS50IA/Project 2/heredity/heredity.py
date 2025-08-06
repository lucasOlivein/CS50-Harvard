import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    
    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # This function handles the inheritance of a gene from a parent.
    def gene_inherit(parent, transmit):

        if transmit:
            if parent in one_gene:
                # (50% chance to transmit the gene) AND (the gene does not mutate) 
                # OR (50% chance to do not pass the gene) AND (the gene does mutate)
                #   :. 50% * 99% + 50% * 1% => 50% * (99% + 1%) = 50%
                return 0.5
            elif parent in two_genes:
                # (100% chance to transmit the gene) AND (the gene does not mutate)
                return 1 - PROBS["mutation"]
            else:
                # 100% chance to do not transmit the trait gene AND the gene mutate
                return PROBS["mutation"]

        elif not transmit:
            if parent in one_gene:
                # (50% chance to transmit the gene) AND (the gene does mutate) 
                # OR (50% chance to do not transmit the gene) AND (the gene does mutate)
                return 0.5
            elif parent in two_genes:
                # 100% chance to transmit the trait gene AND the gene mutate
                return PROBS["mutation"]
            else:
                # 100% chance to do not transmit the trait gene AND the gene does not mutate
                return 1 - PROBS["mutation"]

    # This function handles the probability of a person have or not the trait.
    def trait_probability(person, has_trait):
        mother = people[person]['mother']
        father = people[person]['father']
        
        # Check if mother and father is present.
        # If yes, use the joint probability to calculate the trait probability.
        if mother != None and father != None:
            if person in one_gene:
                return PROBS["trait"][1][has_trait] * (
                    gene_inherit(mother, True) * gene_inherit(father, False) +
                    gene_inherit(mother, False) * gene_inherit(father, True)
                )
            elif person in two_genes:
                return PROBS["trait"][2][has_trait] * gene_inherit(mother, True) * gene_inherit(father, True)
            else:
                return PROBS['trait'][0][has_trait] * gene_inherit(mother, False) * gene_inherit(father, False)

        # If mother and father is not present, use the unconditional probability.
        else:
            if person in one_gene:
                return PROBS['gene'][1] * PROBS["trait"][1][has_trait]
            elif person in two_genes:
                return PROBS['gene'][2] * PROBS["trait"][2][has_trait]
            else:
                return PROBS["gene"][0] * PROBS["trait"][0][has_trait]

    scenario_probability = 1
    for person in people:
        trait = person in have_trait
        scenario_probability *= trait_probability(person, trait)
    
    return scenario_probability


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        # Check wether a person has one, two or zero gene.
        # Add 'p' to the corresponding distribution.
        if person in one_gene:
            probabilities[person]["gene"][1] += p
        elif person in two_genes:
            probabilities[person]["gene"][2] += p
        else:
            probabilities[person]["gene"][0] += p
        
        # Add 'p' to trait probability.
        probabilities[person]["trait"][person in have_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        # Sum the probability of have and not have the trait.
        trait = (probabilities[person]["trait"][True] +
                 probabilities[person]["trait"][False])
        
        # Sum the probability of have one, two and zero gene.
        gen = (probabilities[person]["gene"][1] +
               probabilities[person]["gene"][2] +
               probabilities[person]["gene"][0])
        
        # Normalize the probability of have the trait.
        probabilities[person]["trait"][True] /= trait
        probabilities[person]["trait"][False] /= trait
        
        # Normalize the probability of have the gene.
        probabilities[person]["gene"][1] /= gen
        probabilities[person]["gene"][2] /= gen
        probabilities[person]["gene"][0] /= gen
        

if __name__ == "__main__":
    main()
