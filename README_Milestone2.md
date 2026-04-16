# Data Visualization – COM-480 — Milestone II

| Student's name | SCIPER |
| -------------- | ------ |
| Jaime Oliver Pastor | 356574 |
| Alexandre Majchrzak | 345483 |
| Antony Picard | 332025 |

**Team Name**: WarArchives  
**Project**: *The Skies of War — Aerial Bombing Operations across Four Conflicts*

---

## 1. General View of the Website

Our project is an interactive web application that visualizes aerial bombing operations across four major conflicts of the 20th century: **World War I**, **World War II**, the **Korean War**, and the **Vietnam War**. It is built upon the THOR (Theater History of Operations Reports) database, from which we extracted publicly available subsets on Kaggle.

The website is structured as a **single-page scrollytelling experience** that guides the user from a global overview down to detailed, conflict-specific insights. The user first lands on a hero section displaying aggregated statistics (total missions, tons dropped, sorties, number of conflicts covered), which immediately conveys the scale of aerial warfare. From there, five interconnected sections allow the user to explore the data along different dimensions: **space** (where bombs were dropped), **time** (how operations evolved month by month), **actors** (which countries conducted the missions), **means** (which aircraft types were used), and **targets** (which locations were the most bombed).

A global **war selector** acts as the main interaction element: the user can filter each visualization by conflict (or view all wars simultaneously), making direct comparisons between WWI, WWII, Korea, and Vietnam possible across every chart. This design supports two complementary exploration workflows: a **comparative workflow**, where the user contrasts conflicts side by side, and a **focused workflow**, where the user dives into a single war to understand its specificities.

---

## 2. Project Breakdown: Core Visualization and Extra Ideas

To keep the project manageable, we have split our goal into one **core visualization (MVP)** that delivers the main message of the project on its own, and a set of **extra ideas** that would enrich the experience but can be dropped without compromising the core narrative.

### 2.1 Core Visualizations (Minimum Viable Product)

The MVP is a single-page website built around **five coordinated views**, all filterable by conflict (WWI, WWII, Korea, Vietnam, or all wars combined). Each piece below is independent and can be implemented separately, but together they answer our main problematic: *how did aerial bombing evolve strategically across four 20th-century conflicts?*

#### 2.1.1 Landing Section with Aggregate Statistics

A hero block displaying the total number of missions, total tons of bombs dropped, total sorties, and number of conflicts covered. This immediately gives the user a sense of scale before diving into the visualizations.

#### 2.1.2 Geographic Heatmap

The central visualization is an interactive **world map** rendered with Leaflet on top of CARTO dark tiles. Each bombing mission is plotted as a weighted point, aggregated via a heatmap layer (`leaflet.heat`) whose intensity encodes mission density. The gradient progresses from blue (low intensity) through orange to red (hotspots), producing an intuitive "heat" metaphor. The radius of the heat points adapts dynamically to the zoom level so that patterns remain readable both at the global scale and when the user zooms into a specific theater (e.g., the Pacific or Indochina). Selecting a war from the button bar filters the points and automatically fits the map bounds to the relevant region.

#### 2.1.3 Timeline of Missions

A **multi-series line chart** (Chart.js) displays monthly mission counts for each of the four conflicts. Each war is encoded with a distinctive color (WWI: red, WWII: orange, Korea: blue, Vietnam: green), and filled areas emphasize the relative magnitude between conflicts. This view answers a core question of our problematic: *how did the strategic importance of aerial bombing evolve across the 20th century?* The chart makes visible the dramatic escalation from WWI to Vietnam.

#### 2.1.4 Who Bombed? — Countries & Aircraft

Two horizontal **bar charts** sit side by side:

- The left chart ranks the **top 10 attacking countries**, with bars colored by the war they belong to.
- The right chart ranks the **top aircraft types** deployed, again color-coded by conflict.

This juxtaposition lets the user visually connect a country's involvement with the technological means it employed.

#### 2.1.5 Most Bombed Locations

A sortable **table** lists the top 20 targeted locations for the selected conflict, showing location, country, number of missions, and total bombload (in tons). This tabular view provides the fine-grained detail that complements the aggregate map and charts — users can pinpoint the specific cities or regions that bore the brunt of each campaign.

---

Each of these pieces can stand on its own, and losing any one of them would weaken but not break the project. Together they already tell a coherent story of **where**, **when**, **by whom**, and **with what** aerial bombings were conducted across the four wars.

### 2.2 Extra Ideas

The following extensions would enhance the visualization but can be dropped without endangering the meaning of the project. They are ordered roughly from most to least realistic given the time available.

- **Temporal animation on the map.** Instead of a static aggregate heatmap, an animated time slider could replay bombing operations month by month, letting the user *see* the war front shift across Europe in 1944 or the systematic expansion of bombing zones in Vietnam.

- **Bombload encoding toggle.** Currently the map encodes *mission count*; a toggle could switch the weight of each heat point to *tons dropped* instead, revealing a different strategic picture (a few missions with massive tonnage vs. many smaller raids).

- **Mission detail on click.** Clicking on a hotspot could open a popup with drill-down information: top targets in that area, countries involved, aircraft used, and dates of the heaviest raids.

- **Cross-filter coordination.** Selecting a country in the bar chart would filter the map and timeline accordingly, implementing a *coordinated multiple views* paradigm. This would transform the site from a sequence of visualizations into a true exploratory dashboard.

- **Scrollytelling narrative.** A guided story mode could walk the user through key events (the Blitz, Dresden, Hiroshima, Operation Rolling Thunder) with the map and charts updating as the user scrolls, combining editorial context with raw data.

- **Aircraft-to-bombload scatterplot.** A scatter visualization of (sorties per mission) × (bombload per mission) across aircraft types would surface the technological evolution — from small biplanes of WWI to B-52s of Vietnam — in a single glance.

- **Comparative small multiples.** A 2×2 grid showing the same metric (e.g., bombload per month) across the four wars at identical scales would make the staggering escalation between conflicts immediately visible.

---

## 3. Tools and Methods

The website is implemented as a **client-side single-page application** using HTML, CSS, and vanilla JavaScript, so that it can be hosted statically (e.g., on GitHub Pages).

Data preprocessing is done **offline in Python** using `pandas`. The raw THOR CSV files (four wars, several million rows for Vietnam alone) are cleaned in `DataProcessor.py` (removal of rows with missing critical fields, duplicates, and irrelevant columns), split into manageable chunks in `DataSplitter.py`, and aggregated in `DataAnalyser.py` into six compact JSON files loaded by the frontend: `map_data.json`, `timeline.json`, `stats.json`, `top_targets.json`, `by_country.json`, and `top_aircraft.json`. This offline aggregation is essential because the raw Vietnam dataset alone is far too large to load into a browser.

On the frontend, we use:

- **Leaflet 1.9.4** + **leaflet.heat** for the interactive heatmap, built on CARTO Dark Matter tiles for a somber aesthetic consistent with the subject.
- **Chart.js 4.4** for all statistical charts (timeline, country bars, aircraft bars).
- **IntersectionObserver API** for scroll-based fade-in animations between sections.
- **Pure CSS** (no framework) for layout and theming.

In terms of lectures, the project relies on concepts from **Lecture 2 (Design)** for the overall narrative layout, **Lecture 3 (Interaction)** for the filter/selector mechanisms, **Lecture 5 (Maps)** for the geographic heatmap, and will benefit from the upcoming lectures on **scrollytelling** and **D3 / advanced interaction** for the extra features described in Section 2.2.

---

## 4. Basic Skeleton

The current prototype implements the full skeleton of the final website. The landing hero loads live aggregate statistics from `stats.json`; the map section renders an interactive heatmap with working per-war filtering and dynamic radius on zoom; the timeline, country, and aircraft charts are fully functional; the targets table is filterable by war. The war selectors are already synchronized with their respective visualizations, and scroll animations are in place.

The visual identity (orange accent `#ff6b35` on dark background) is already set and consistent across sections, giving the site a cohesive, archive-like atmosphere appropriate for historical data about war. What remains for Milestone III is essentially the **enrichment** of the visualizations rather than new core features: refining the encodings, implementing the extra ideas listed in Section 2.2, and polishing responsiveness.