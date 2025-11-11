# Il codice simula una popolazione
# formata da individui che possiedono proprietà diverse per colore, taglia e velocità.

import random  # -> serve per generare caratteristiche differenti (colori, nucleotidi, taglia, ecc.)

popolazione = []  # -> creiamo una lista vuota che servirà per memorizzare gli individui

colori = ["rosso", "verde", "blu"]  # -> lista dei possibili colori
nucleotidi = ["A", "T", "G", "C"]  # -> lista delle quattro basi azotate del DNA
num_individui = 5  # -> numero iniziale di individui (in questo caso 5)
num_generazioni = 3  # -> numero di generazioni da creare (in questo caso 3)

for i in range(num_individui):  # -> ciclo che crea il numero di individui indicato
    dna = ''.join(random.choice(nucleotidi) for _ in range(20))  # -> crea una stringa di 20 caratteri
    # Ogni carattere è scelto in modo casuale tra le basi azotate.
    individuo = {
        "id": i + 1,  # -> ID è la chiave del dizionario. L’aggiunta di +1 evita ID=0,
        # quindi gli ID assegnati non sono 0,1,2,3,4 ma 1,2,3,4,5. Serve per un conteggio più comune.
        "colore": random.choice(colori),  # -> colore scelto in modo casuale
        "taglia": random.randint(1, 10),  # -> numero casuale tra 1 e 10 compresi
        "velocità": random.randint(1, 10),  # -> numero casuale tra 1 e 10 compresi
        "DNA": dna
    }  # -> le parentesi indicano che tutte queste caratteristiche fanno parte di un dizionario

    popolazione.append(individuo)  # -> aggiunge l’individuo alla lista chiamata popolazione

for _ in range(num_generazioni):  # -> ciclo che ripete il processo per il numero di generazioni
    figli = []  # -> creazione di una nuova lista per contenere i figli
    for ind in popolazione:  # -> scorre ogni individuo nella lista popolazione
        # Tramite queste istruzioni, il figlio eredita alcune caratteristiche del genitore.
        colore = ind["colore"]
        taglia = ind["taglia"]
        velocità = ind["velocità"]

        dna = list(ind["DNA"])  # -> trasforma la stringa del DNA in una lista modificabile
        posizione = random.randint(0, 19)  # -> sceglie casualmente una posizione del DNA (da 0 a 19)
        dna[posizione] = random.choice(nucleotidi)  # -> sostituisce la base in quella posizione con un nucleotido casuale.
        # In questo modo può capitare che la nuova base sia uguale alla precedente, quindi la mutazione è obbligatoria ma non sempre effettiva.
        dna_mutato = ''.join(dna)  # -> ricostruisce la stringa del DNA mutata

        # Crea il figlio
        figlio = {
            "id": len(popolazione) + len(figli) + 1,  # -> prima considera il numero di individui esistenti,
            # poi aggiunge i figli già creati in questa generazione e infine somma 1 per ottenere un numero progressivo.
            "colore": colore,  # -> nessuna mutazione
            "taglia": taglia,  # -> nessuna mutazione
            "velocità": velocità,  # -> nessuna mutazione
            "DNA": dna_mutato  # -> DNA mutato, qui entra la variazione genetica nel codice
        }
        figli.append(figlio)  # -> aggiunge il nuovo figlio alla lista dei figli
    popolazione.extend(figli)  # -> dopo aver creato tutti i figli, li aggiunge alla lista popolazione

# --- ANALISI FINALE ---
media_taglia = sum(ind["taglia"] for ind in popolazione) / len(popolazione)  # -> somma tutte le taglie e divide per il numero totale di individui
media_velocità = sum(ind["velocità"] for ind in popolazione) / len(popolazione)
print("\n=== RISULTATI FINALI ===")
print(f"Totale individui: {len(popolazione)}")
print(f"Media taglia: {media_taglia:.2f}")
print(f"Media velocità: {media_velocità:.2f}")
print("Percentuale di mutati: 100%  (tutti mutano in ogni generazione)")

print("\nEsempio DNA degli individui finali:")
for ind in popolazione:
    print(f"ID {ind['id']}: {ind['DNA']}")
# Con questa parte di codice si stampa a video il numero totale di individui,
# le loro caratteristiche medie e il DNA di ciascun individuo.
