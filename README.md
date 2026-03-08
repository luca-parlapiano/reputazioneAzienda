# reputazioneAzienda

Esercitazione MLOps - Monitoraggio della reputazione online di un'azienda.

## Obiettivo del progetto

L'obiettivo del progetto è realizzare un sistema di sentiment analysis per monitorare automaticamente la reputazione online di un'azienda attraverso testi provenienti dai social media.

Il sistema classifica ciascun testo in una delle seguenti classi:

- negative
- neutral
- positive

## Modello utilizzato

Per la Fase 1 è stato utilizzato il modello pre-addestrato:

`cardiffnlp/twitter-roberta-base-sentiment-latest`

Nota: nella traccia è citato FastText, ma il modello esplicitamente indicato appartiene alla famiglia dei transformer (RoBERTa). Per questo progetto è stato seguito il modello specificato nella consegna.

## Dataset

Per la valutazione del modello è stato utilizzato un dataset pubblico di sentiment analysis su tweet:

`cardiffnlp/tweet_eval` - configurazione `sentiment`

Le label del dataset sono mappate come segue:

- 0 = negative
- 1 = neutral
- 2 = positive

## Fase 1

Nella prima fase del progetto sono stati completati i seguenti passaggi:

- caricamento del modello pre-addestrato
- test di inferenza su esempi di testo
- utilizzo di un dataset pubblico
- mapping delle label
- predizione sul test set
- calcolo delle metriche di valutazione:
  - accuracy
  - macro F1-score
  - classification report
  - confusion matrix
- analisi preliminare degli errori

Il notebook della Fase 1 è disponibile nella cartella `notebooks/`.


## Fase 2 - CI/CD

Nella seconda fase del progetto è stata implementata una pipeline di **Continuous Integration (CI)** tramite **GitHub Actions**, con l'obiettivo di automatizzare la verifica del codice e garantire la riproducibilità del progetto.

La pipeline viene eseguita automaticamente ad ogni **push** o **pull request** sul repository.

Durante l'esecuzione della pipeline vengono eseguite le seguenti operazioni:

1. **Checkout del repository**
   - Il codice viene scaricato automaticamente dal repository GitHub.

2. **Configurazione dell'ambiente Python**
   - Viene installata una versione specifica di Python nel runner GitHub Actions.

3. **Installazione delle dipendenze**
   - Le librerie necessarie al progetto vengono installate tramite il file `requirements.txt`.

4. **Esecuzione dei test automatici**
   - I test vengono eseguiti utilizzando **pytest**.

5. **Validazione della funzione di inferenza**
   - I test verificano:
     - il corretto formato dell'output della funzione `predict_sentiment`
     - la presenza delle chiavi attese (`text`, `label`, `score`)
     - la validità della label di sentiment
     - la validità dell'intervallo del punteggio (`score` tra 0 e 1)
     - la gestione di input non validi.

Per rendere i test **stabili e indipendenti dalla connessione internet**, il modello Hugging Face non viene scaricato durante i test.  
Viene invece utilizzato **mocking** della funzione di caricamento del modello, simulando la risposta del classificatore.

Questo approccio permette di ottenere:

- test più veloci
- test riproducibili
- pipeline CI stabile

L'introduzione della CI garantisce quindi che ogni modifica al codice venga automaticamente verificata prima di essere integrata nel progetto.

## Fase 3 - Deploy e Monitoraggio

Nella terza fase del progetto il modello di sentiment analysis è stato reso disponibile tramite un servizio API implementato con **FastAPI**.

L'applicazione è stata containerizzata tramite **Docker** e deployata su **Hugging Face Spaces**, consentendo l'esecuzione del modello in un ambiente cloud accessibile tramite API.

L'endpoint principale consente di inviare un testo e ottenere la classificazione del sentiment.

### Endpoint API

POST /predict

Input:

{
 "text": "I love this product!"
}

Output:

{
 "text": "I love this product!",
 "label": "positive",
 "score": 0.98
}

### Demo Online

Il servizio è accessibile su Hugging Face Spaces:

https://lucatestmodel-sentiment-api.hf.space

## Struttura del repository


reputazioneAzienda/
│
├── notebooks/
│   └── analisi_sentiment.ipynb
│
├── src/
│   ├── predict.py
│   └── __init__.py
│
├── tests/
│   └── test_predict.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── README.md
└── .gitignore

## Architettura del Sistema

Il progetto segue un approccio MLOps che integra sviluppo del modello, testing automatico, containerizzazione e deploy.

Architettura:

Client
↓
FastAPI
↓
Modulo di inferenza (predict.py)
↓
Modello HuggingFace
↓
Hugging Face Spaces (deploy)

Il servizio è containerizzato tramite Docker e distribuito tramite Hugging Face Spaces.

## CI/CD Pipeline

È stata implementata una pipeline di Continuous Integration tramite GitHub Actions.

La pipeline esegue automaticamente:

- installazione delle dipendenze
- esecuzione dei test con pytest
- validazione della funzione di inferenza

Questo garantisce che ogni modifica al repository venga verificata automaticamente prima dell'integrazione.

I test utilizzano mocking per evitare il download del modello durante l'esecuzione della CI, rendendo la pipeline più veloce e stabile.

## Conclusioni

Il progetto dimostra come implementare un sistema completo di monitoraggio del sentiment sui social media utilizzando tecniche MLOps.

Le principali funzionalità includono:

- utilizzo di un modello NLP pre-addestrato
- automazione dei test tramite CI/CD
- esposizione del modello tramite API
- containerizzazione con Docker
- deploy cloud tramite Hugging Face Spaces

Questa architettura consente di rendere il modello facilmente integrabile in sistemi reali di monitoraggio della reputazione online.