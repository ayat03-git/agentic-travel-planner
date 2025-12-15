# ✈️ Agentic Travel Planner (MCP)

**Agentic Travel Planner** est une application Python + Streamlit qui utilise un **LLM local (Ollama)** et des **outils REST** pour générer automatiquement des itinéraires de voyage et estimer le budget.  
L'application inclut un **agent critique** pour valider l'itinéraire et peut réajuster automatiquement le plan en fonction d'un **budget maximal** défini par l'utilisateur.

---

## 🔹 Fonctionnalités principales

✅ Génération automatique d'itinéraires de voyage par destination et durée  
✅ Estimation du **budget total** et **coût quotidien** via un serveur MCP local  
✅ Affichage en temps réel des appels aux outils dans l'interface  
✅ **Agent critique** intégré pour vérifier les incohérences (logistique, langage, budget)  
✅ Ajustement automatique de la durée du voyage si le budget maximal est dépassé  
✅ Interface utilisateur intuitive et responsive avec Streamlit  

---
## 🗂️ Structure du projet

<pre>
travel_agent_lab/
├── agent.py                 # Logique de l'agent LLM + outils + critique
├── app.py                   # Interface utilisateur Streamlit
├── server_mcp.py            # Serveur FastAPI pour l'estimation budgétaire
├── requirements.txt         # Dépendances Python
└── README.md                # Documentation
</pre>



---

## ⚙️ Prérequis

- **Python 3.10+**
- **Pip** (gestionnaire de paquets)
- **Ollama** installé localement avec le modèle `llama3.2:3b`
- **Virtualenv** (recommandé)

---

## 🚀 Installation et démarrage

### 1. Cloner le projet
```bash
git clone https://github.com/ton-utilisateur/agentic-travel-planner.git
cd agentic-travel-planner

# Création
python -m venv venv_ollama

# Activation (Windows)
venv_ollama\Scripts\activate

# Activation (Mac/Linux)
source venv_ollama/bin/activate

#Installer les dépendances
pip install -r requirements.txt

Exemple de requirements.txt :
streamlit
fastapi
uvicorn
requests
langchain-ollama

#Démarrer le serveur MCP (FastAPI)
python server_mcp.py
Le serveur écoute sur http://localhost:3333

#Lancer l'application Streamlit
streamlit run app.py

#🎯 Guide d'utilisation
Saisir la destination (ex. Paris)

Choisir le nombre de jours (1 à 30)

Définir un budget maximal (optionnel)

Cliquer sur Generate Travel Plan 🧳

Consulter :

L'itinéraire généré avec le budget estimé

Les appels aux outils affichés en temps réel

La critique de l'itinéraire dans la section Critic Review 📝

Les ajustements automatiques si le budget est dépassé


#🛠️ Configuration avancée
Modèle Ollama
Par défaut, l'application utilise llama3.2:3b. Pour changer de modèle :

Modifier agent.py :

python
llm = ChatOllama(model="nouveau-modele", temperature=0)
S'assurer que le modèle est téléchargé localement :

bash
ollama pull nouveau-modele
Ajouter un nouvel outil
Étendre le serveur MCP (server_mcp.py) avec un nouvel endpoint

Ajouter le wrapper dans agent.py

Mettre à jour la liste des outils dans l'agent


#⚠️ Notes importantes
Le serveur MCP doit être lancé avant l'application Streamlit

Ne pas inclure de clés API ou données sensibles dans le dépôt

Le modèle Ollama doit être disponible localement avant l'exécution

Pour un usage en production, renforcer la sécurité des endpoints
