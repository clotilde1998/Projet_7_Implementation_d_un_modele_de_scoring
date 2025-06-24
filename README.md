# Projet_7_Implementation_d_un_modele_de_scoring
projet- 7 parcours data science openclassroom

Contexte


Entreprise: "Pret à dépenser" -> Propose des crédits à la consommation pour des personnes ayant peu ou pas du tout d'historique de prêt    
Objectif: Création d'un “scoring crédit” pour calculer la probabilité qu’un client rembourse son crédit, puis classifie la demande en crédit accordé ou refusé
Importance de la transparance (souhait des clients + valeurs de l'entreprise)
Dashboard : Pour pouvoir expliquer de façon la plus transparente possible les décisions d’octroi de crédit

Objectifs


Construire un modèle de scoring qui donnera une prédiction (classification) sur la probabilité de faillite d'un client de façon automatique
Construire un dashboard permettant d'interpréter les prédictions faites par le modèle, et d’améliorer la connaissance client
Mettre en production le modèle de scoring de prédiction à l’aide d’une API, ainsi que le dashboard interactif qui appelle l’API pour les prédictions
Utiliser des kernels Kaggle (optionel) pour faciliter l’analyse exploratoire, la préparation des données et le feature engineering nécessaires à l’élaboration du modèle de scoring


Partie technique

Dahboard : FastAPI
 Deploiement sur RENDER
 Librairie evidently pour détecter du Data Drift en production
 Créer un tableau HTML pour illustrer ce data drift
 Effectuer de la Cross-Validation
 Si les scores scores AUC sont supérieurs à 0.82, le modèle possède probablement de l’overfitting
 Création d'une note technique: Présentera l’élaboration du modèle jusqu’à l’analyse du Data Drift
 

Conseils sur l'elaboration du modèle

    
Prendre en compte le déséquilibre entre le nombre de bons et de moins bons clients (utiliser une méthode au choix)

    Prendre en compte le déséquilibre du coût métier entre entre un faux négatif et un faux positif:
    Faux négatif: mauvais client prédit bon client : donc crédit accordé et perte en capital
    Faux positif: Bon client prédit mauvais : donc refus crédit et manque à gagner en marge
    Hypothèse: le coût d’un FN est dix fois supérieur au coût d’un FP

    Création d'un score "métier": Minimisation du coût d’erreur de prédiction des FN et FP
        
    Ce score permet de choisir le meilleur modèle et ses meilleurs hyperparamètres
    Attention: Minimisation score métier -> optimisation du seuil qui détermine, la classe 0 ou 1
    Utiliser aussi l'ACU et le business score pour affiner notre modèle et ses hyperparamètres

Livrables


    L’API de prédiction du score, déployée sur le cloud (lien vers l’API).
    Le notebook ou code de la modélisation (du prétraitement à la prédiction)
        Ce notebook intègre la partie MLFlow de génération du tracking d'expérimentations. 
        L’interface web "UI MLFlow" d'affichage des résultats du tracking MLFlow sera présentée en soutenance + copie d’écran dans le support de soutenance.
    Un dossier, géré via un outil de versioning de code contenant :
        Le notebook ou code de la modélisation (du prétraitement à la prédiction), intégrant via MLFlow le tracking d’expérimentations et le stockage centralisé des modèles.
        Le code permettant de déployer le modèle sous forme d'API.
        Pour l’API, un fichier introductif permettant de comprendre l'objectif du projet et le découpage des dossiers, et un fichier listant les packages utilisés seront présents dans le dossier.
    Le tableau HTML d’analyse de data drift réalisé à partir d’evidently.
    Un notebook ou une application Streamlit de test de l’API.
    Un support de présentation pour la soutenance, détaillant le travail réalisé (Powerpoint ou équivalent, 30 slides maximum), intégrant des copies écran, preuves qu’un pipeline de déploiement continu a permis de déployer l’API : 
        de l’interface web 'UI MLFlow" d'affichage des résultats du tracking MLFlow ;
        des commits ;
        du dossier Github (+ lien vers ce dossier) ;
        de l’exécution des tests unitaires ;
        de l’exécution du déploiement de l’API avec lien vers l’API sur le Cloud.



