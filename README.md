# 🌊 OceanWatch — Marine Life Intelligence Platform

> A real-time marine life monitoring and overfishing prevention system built with Flask, GBIF Live API, Three.js, and Chart.js.

---

## 📌 Project Overview

OceanWatch is a web-based dashboard designed to help marine researchers, fisheries authorities, and conservationists monitor fish population health, predict species extinction risks, and take data-driven action against overfishing.

The platform pulls live data from the **Global Biodiversity Information Facility (GBIF)** API and presents it through an interactive, visually rich dashboard with 3D visuals, animated charts, an SVG world map, and an AI-style population forecasting engine.

---

## 🎯 Key Objectives

- Collect and display real-time marine species observation data
- Analyze fish population trends across global ocean regions
- Alert fisheries authorities about overfishing risk zones
- Predict species exhaustion timelines based on decline rates
- Visualize species distribution on an interactive world map

---

## ✨ Features

### 🐠 3D Animated Fish in Topbar
- Two Three.js rendered fish swim in real time inside the navigation bar
- Fish responds to clicks with burst animation
- Automatically recolors when switching between light and dark theme

### 🔬 Population Forecast Tool
- Select any of 10 tracked species from a dropdown
- Enter a target year (2025–2100)
- Instantly receive a color-coded prediction:
  - 🔴 **Critical / Exhaust** — population near zero or extinct
  - 🟠 **Declining** — intervention required
  - 🟢 **Safe / Healthy** — no exhaustion risk
- Mini animated bar chart shows the population trajectory year by year

### 🫧 Bubble Navigation
- Four circular bubble buttons replace traditional flat tabs
- Active bubble glows with a gradient fill and indicator dot
- Clicking a bubble opens the corresponding section with a smooth animation
- Sections: Overview · Population · Risk Alerts · Species Map

### 🌊 Overview Section
- 3 key fact cards (global coverage, overfishing crisis, authority action)
- Annual population trend line chart (Bluefin Tuna, Atlantic Cod, Pacific Salmon)
- Species-by-class donut chart from GBIF taxonomy data
- Full overfishing risk index table with animated progress bars
- Key events timeline (2010–2024)
- Fishing quota compliance bar chart showing exceeded vs. allowed catches

### 🐠 Population Section
- Population distribution bar chart across 7 ocean regions
- 10-year population trajectory line chart for 4 key species
- Worldwide fish categories table with 15 species including:
  - Category, common name, scientific name, ocean region
  - Estimated population, annual trend (▲/▼), health score bar, status badge

### ⚠️ Risk Alerts Section
- Year-based filter buttons (All / 2024 / 2030 / 2035 / 2040 / 2050)
- Population is projected to the selected year for each species
- Alert cards show species emoji, scientific name, region, detail text, projected population %, and projected extinction year
- Summary stat cards update dynamically based on year selection
- Species sorted by severity: Critical → High → Moderate → Safe

### 🗺️ Species Map Section
- Full SVG world map with continent shapes, equator line, and coordinate grid
- 12 species plotted with pulsing animated location markers
- Dot size proportional to population count
- Dot color indicates risk level (Red = Critical, Orange = High, Teal = Moderate, Green = Low)
- Hover tooltip shows species name, scientific name, ocean, population count, risk level, and field note
- Risk-level filter buttons (Critical / High / Moderate / Low) to toggle dots on/off
- Live GBIF observation feed below the map with real-time sighting data

### 🌗 Light / Dark Mode
- Toggle button in the topbar switches between dark ocean theme and light teal theme
- Theme preference saved in `localStorage` — persists across page reloads
- 3D fish recolors instantly on theme switch

### 📊 Analysis Page
- Species population health progress bars for 9 species
- Authority insight cards with management recommendations
- 10-year population trajectory chart
- Risk distribution pie chart
- Per-species quota compliance tracker
- Field observation records table

---

## 🗂️ Project Structure

```
MarineLife/
│
├── app.py                  # Flask backend — routes, GBIF API, data
├── activate.bat            # Windows: auto-setup venv and launch server
├── requirements.txt        # Python dependencies (optional)
│
└── templates/
    ├── base.html           # Shared layout — topbar, 3D fish, bubble nav,
    │                       # prediction bar, all 4 dashboard sections
    ├── index.html          # Dashboard page (extends base.html)
    └── analysis.html       # Deep analysis page (extends base.html)
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main dashboard with live GBIF stats |
| `GET` | `/analysis` | Deep analysis and field records page |
| `GET` | `/api/species?q=<name>&limit=<n>` | Search marine species via GBIF |
| `GET` | `/api/observations/live` | Latest 10 GBIF fish observations with coordinates |
| `GET` | `/api/risk` | JSON list of all species risk data |
| `POST` | `/api/submit` | Submit a new field observation record |
| `GET` | `/api/submissions` | Retrieve all submitted observation records |

### POST `/api/submit` — Request Body

```json
{
  "species":   "Atlantic Bluefin Tuna",
  "sci_name":  "Thunnus thynnus",
  "lat":       36.7783,
  "lng":       -74.0060,
  "count":     320,
  "risk":      "critical",
  "observer":  "Vessel HMS Marine",
  "date":      "2026-03-09",
  "notes":     "Observed near spawning grounds"
}
```

---

## 🌐 External APIs Used

| API | Usage | Authentication |
|-----|-------|---------------|
| [GBIF API](https://api.gbif.org/v1) | Live species counts, occurrence records, taxonomy search | None required (free & open) |
| Google Fonts | Playfair Display, Outfit, JetBrains Mono | None required |
| Chart.js (CDN) | Population charts, quota charts, trend lines | None required |
| Three.js (CDN) | 3D animated fish in topbar | None required |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/MarineLife.git
cd MarineLife
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install flask requests
```

Or if you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

```
http://127.0.0.1:5000
```

---

## 🪟 Quick Start on Windows

Simply double-click **`activate.bat`** — it will:
1. Create a virtual environment if one does not exist
2. Activate it automatically
3. Install Flask and requests
4. Launch the server at `http://127.0.0.1:5000`

---

## ☁️ Running on GitHub Codespaces

1. Open the repository in GitHub Codespaces
2. In the terminal, run:
   ```bash
   pip install flask requests
   python app.py
   ```
3. Go to the **Ports** tab in VS Code
4. Make sure port `5000` is forwarded and set to **Public**
5. Click the globe 🌐 icon next to port 5000 to open the app

---

## 🖥️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3, Flask |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| 3D Graphics | Three.js (r128) |
| Charts | Chart.js 4.4.1 |
| Live Data | GBIF REST API |
| Fonts | Google Fonts |
| Templating | Jinja2 (Flask) |
| Styling | CSS Custom Properties (Variables) |

---

## 📊 Species Tracked

| Species | Scientific Name | Current Health | Risk Level |
|---------|----------------|---------------|------------|
| Atlantic Bluefin Tuna | *Thunnus thynnus* | 28% | 🔴 Critical |
| Atlantic Cod | *Gadus morhua* | 26% | 🔴 Critical |
| Swordfish | *Xiphias gladius* | 38% | 🔴 Critical |
| Hammerhead Shark | *Sphyrna lewini* | 24% | 🔴 Critical |
| Great White Shark | *Carcharodon carcharias* | 32% | 🟠 High |
| Yellowfin Tuna | *Thunnus albacares* | 54% | 🟠 High |
| Bluefin Grouper | *Epinephelus sp.* | 44% | 🟠 High |
| Bigeye Tuna | *Thunnus obesus* | 48% | 🟠 High |
| North Sea Herring | *Clupea harengus* | 62% | 🟡 Moderate |
| Pacific Halibut | *Hippoglossus stenolepis* | 73% | 🟢 Low |
| Pacific Salmon | *Oncorhynchus sp.* | 78% | 🟢 Low |
| Alaskan Pollock | *Gadus chalcogrammus* | 91% | 🟢 Low |

---

## 🔮 Prediction Model

The forecasting engine uses a linear decline model based on current annual depletion rates:

```
Projected Population (%) = Current Population (%) − (Decline Rate × Years)
```

| Result | Threshold | Indicator |
|--------|-----------|-----------|
| Extinct | ≤ 0% | ☠️ EXTINCT |
| Near Extinction | ≤ 10% | 🚨 Critical |
| Severe Depletion | ≤ 30% | ⚠️ Exhaust Risk |
| Declining | ≤ 55% | 📉 Intervention Needed |
| Stable | ≤ 80% | ✅ Monitor Closely |
| Healthy | > 80% | 🐟 No Risk |

---

## 📸 Screenshots

| Section | Description |
|---------|-------------|
| Topbar | 3D animated fish, brand, nav, forecast bar, light/dark toggle |
| Overview | Trend charts, risk index table, quota compliance, timeline |
| Population | Ocean-region bar chart, 10-year trajectory, worldwide species table |
| Risk Alerts | Year-filtered alert cards with extinction projections |
| Species Map | SVG world map with pulsing species markers and tooltips |
| Analysis | Health bars, authority insights, field records table |

---

## 🚀 Future Enhancements

- [ ] Connect to real-time satellite AIS vessel tracking for live overfishing detection
- [ ] Add user authentication for field researchers to submit observations securely
- [ ] Integrate IUCN Red List API for official conservation status
- [ ] Export reports as PDF for fisheries authority submission
- [ ] Add email/SMS alert system when species cross critical thresholds
- [ ] Machine learning-based population forecasting using historical GBIF time series
- [ ] Mobile-responsive redesign for field use on tablets and smartphones

---

## 👨‍💻 Author

**Akash**
GitHub: [@akash0810](https://github.com/akash0810)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [GBIF — Global Biodiversity Information Facility](https://www.gbif.org) for providing free, open-access marine biodiversity data
- [Chart.js](https://www.chartjs.org) for beautiful, responsive data visualizations
- [Three.js](https://threejs.org) for enabling 3D graphics in the browser
- [Flask](https://flask.palletsprojects.com) for the lightweight Python web framework
- [Google Fonts](https://fonts.google.com) for Playfair Display, Outfit, and JetBrains Mono
