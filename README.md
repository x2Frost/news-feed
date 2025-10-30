# News Feed OVHcloud

Ce projet récupère automatiquement les derniers articles de différents flux RSS et génère une page HTML triée par thématique, prête à être déployée sur GitHub Pages.

## Installation

```bash
git clone <url-du-repo>
cd news-feed
python3 -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt
