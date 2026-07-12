from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
PAGES.mkdir(exist_ok=True)

NAV = [
    ("Home", "index.html"),
    ("Story", "pages/our-story.html"),
    ("Vision", "pages/vision.html"),
    ("UniSI", "pages/unisi.html"),
    ("Ecosystem", "pages/ecosystem.html"),
    ("Roadmap", "pages/roadmap.html"),
    ("Support", "pages/support.html"),
    ("Contact", "pages/contact.html"),
]

PRODUCTS = [
    ("UniAI", "An everyday intelligence companion for creation, learning, research, and decisions.", "Personal productivity and thinking support"),
    ("UniAiBiz", "An Android-first business assistant for local shops and small businesses.", "Inventory, reminders, customer messages, and daily operations"),
    ("UniMed", "A carefully scoped medical education and records organization concept.", "Health literacy, triage guidance, and safe organization"),
    ("UniTrade", "A market assistant focused on explainable signals and risk discipline.", "Watchlists, risk notes, and decision clarity"),
    ("UniGuard", "A security intelligence layer for anomaly detection and self-healing systems.", "Protection, monitoring, and response architecture"),
    ("UniGlow", "A wellness support concept for mood, habits, and private user state.", "Calm reflection, routines, and human support"),
    ("Cognesis", "A research lab for learning, memory, creativity, and cognitive enhancement tools.", "Knowledge work, research, and cognition experiments"),
]

PAGE_DATA = {
    "our-story": {
        "title": "Our Story",
        "eyebrow": "The human origin",
        "lede": "Project Uni is built from ambition, constraint, and a belief that intelligence should not belong only to the largest institutions.",
        "emotion": "Connection, respect, and trust.",
        "sections": [
            ("Founder origin", "Explain why the project began, what problem felt personal, and why the mission deserves years of effort."),
            ("Building with limited resources", "Show the reality honestly: limited capital, high conviction, and a builder mindset instead of manufactured startup polish."),
            ("Community invitation", "Make it clear that designers, students, shop owners, researchers, engineers, and supporters all have a place."),
            ("Milestones so far", "Anchor the dream in visible progress: the Atlas identity, core layers, public website, roadmap, and support program."),
        ],
        "trust": "The story should feel human and specific, not exaggerated. Any claim about progress must be traceable to public artifacts or future proof.",
        "next": "Move from the human reason into the larger vision.",
    },
    "vision": {
        "title": "Vision",
        "eyebrow": "Why Project Uni exists",
        "lede": "Project Uni imagines a future where intelligence is useful, transparent, community-shaped, and built around people rather than locked behind a few companies.",
        "emotion": "Belief, clarity, and urgency.",
        "sections": [
            ("The problem", "AI capability is accelerating, but access, ownership, and direction are becoming centralized."),
            ("The alternative", "Project Uni proposes a community-built Synthetic Intelligence ecosystem with practical tools and transparent progress."),
            ("The promise", "Useful products first, serious research behind them, and support language that never overpromises."),
            ("Vision principles", "Community, transparency, usefulness, safety, long-term research, and founder accountability."),
        ],
        "trust": "The vision page must be inspiring without claiming guaranteed outcomes or impossible timelines.",
        "next": "Introduce Synthetic Intelligence as the idea that powers the vision.",
    },
    "future-of-intelligence": {
        "title": "Future of Intelligence",
        "eyebrow": "From tools to living systems",
        "lede": "Synthetic Intelligence is introduced as a layered digital organism: perception, memory, cognition, emotion, execution, safety, and learning working together.",
        "emotion": "Wonder, curiosity, and intellectual excitement.",
        "sections": [
            ("From chatbots to systems", "Explain the difference between a tool that answers and a system that senses, remembers, reasons, and acts with boundaries."),
            ("Living architecture", "Show the layered model in plain language so visitors understand the concept before technical depth."),
            ("Human-centered intelligence", "Make clear the goal is to assist people and small organizations, not replace their agency."),
            ("Safety boundary", "Name the limits directly, especially for medical, trading, security, and decision-support products."),
        ],
        "trust": "Future-facing language must be balanced by clear boundaries and responsible disclaimers.",
        "next": "Move into UniSI, the core engine.",
    },
    "unisi": {
        "title": "UniSI",
        "eyebrow": "Synthetic Intelligence core",
        "lede": "UniSI is the intelligence engine at the center of Project Uni: a layered system for memory, perception, cognition, execution, emotional signal, and immune defense.",
        "emotion": "Confidence, fascination, and technical trust.",
        "sections": [
            ("Genome", "Defines identity, configuration, behavioral boundaries, and the seed structure of the system."),
            ("Signal bus", "Moves events across the system so every layer can respond with context."),
            ("Perception", "Transforms input into structured signals the system can reason about."),
            ("Cognition", "Plans, evaluates, reflects, and chooses the next step with explainable traces."),
            ("Memory", "Stores useful context and retrieves it through meaningful relationships, not random recall."),
            ("Execution", "Turns decisions into actions while keeping boundaries visible."),
            ("Emotional core", "Models urgency, confidence, care, and user state as signals rather than gimmicks."),
            ("Immune system", "Detects anomalies, isolates risky behavior, remembers threats, and supports self-healing."),
        ],
        "trust": "UniSI must sound technically serious while staying understandable to non-engineers.",
        "next": "Show how UniSI becomes an ecosystem of products.",
    },
    "ecosystem": {
        "title": "Ecosystem",
        "eyebrow": "One core, many expressions",
        "lede": "The Project Uni ecosystem is not a random list of apps. Each product is a practical expression of the same UniSI core.",
        "emotion": "Scale, possibility, and clarity.",
        "sections": [(name, f"{desc} Near-term focus: {focus}.") for name, desc, focus in PRODUCTS],
        "trust": "Every product should start with one practical user and one measurable first use case before growing larger.",
        "next": "Let visitors explore the product most relevant to them.",
        "orbit": True,
    },
    "research": {
        "title": "Research",
        "eyebrow": "Ambition with discipline",
        "lede": "Research turns Project Uni from a website into a serious long-term effort: memory, emotional systems, immune architecture, and human-computer collaboration.",
        "emotion": "Curiosity, respect, and trust.",
        "sections": [
            ("Synthetic Intelligence", "Define what separates Project Uni from ordinary AI wrappers and short-term prompt products."),
            ("Graph memory", "Explore memory that can explain relationships, not just retrieve text."),
            ("Emotional core", "Study emotional signals as user-context and safety indicators."),
            ("Immune systems", "Design defense architecture for anomaly detection, isolation, and recovery."),
            ("Human collaboration", "Research interfaces that improve human agency instead of hiding decisions."),
        ],
        "trust": "Research pages must show open questions and uncertainty instead of pretending everything is solved.",
        "next": "Connect research to the roadmap.",
    },
    "roadmap": {
        "title": "Roadmap",
        "eyebrow": "Progress with sequence",
        "lede": "The roadmap makes the mission believable by showing what is complete, what is in progress, what is planned, and what must wait.",
        "emotion": "Confidence and anticipation.",
        "sections": [
            ("Phase 1 — Seed Genesis", "Completed foundation: identity, core architecture narrative, website direction, and public story."),
            ("Phase 2 — SI v2.0 Advanced", "Current focus: system demo, dashboard, memory model, CYBERLENS, and conversation layer."),
            ("Phase 3 — Ecosystem Expansion", "Validate UniAiBiz, UniMed, UniTrade, UniGuard, UniGlow, Cognesis, and UniAIOS concepts."),
            ("Phase 4 — Launch & Scale", "Launch public website, community platform, app pilots, partnerships, and research publications."),
        ],
        "trust": "Roadmap claims must be specific, dated when possible, and separated into completed, active, planned, and future work.",
        "next": "Show transparency before asking for support.",
        "timeline": True,
    },
    "transparency": {
        "title": "Transparency",
        "eyebrow": "Trust before support",
        "lede": "Project Uni must be ambitious and honest at the same time. This page explains what the project is, what it is not, and what support means.",
        "emotion": "Safety, honesty, and seriousness.",
        "sections": [
            ("What Project Uni is", "A community-built Synthetic Intelligence ecosystem and public product mission."),
            ("What Project Uni is not", "Not an investment scheme, not guaranteed medical advice, not guaranteed trading profit, and not a finished AGI claim."),
            ("Support disclaimer", "Support helps development, community, infrastructure, and public progress without equity or return promises."),
            ("Data principles", "Privacy-first direction, minimal data collection, and clear user control should guide every future product."),
            ("Claim review", "Public copy should be reviewed for hype, safety, and evidence before launch."),
        ],
        "trust": "Transparency is not a legal footnote. It is a core product feature.",
        "next": "Invite support with clarity.",
    },
    "support": {
        "title": "Support Project Uni",
        "eyebrow": "Become part of the mission",
        "lede": "Support should feel like participation in a meaningful future, never advertising, begging, or investment pressure.",
        "emotion": "Participation, pride, and responsibility.",
        "sections": [
            ("Why support matters", "Support funds development, infrastructure, public updates, community spaces, prototypes, and research documentation."),
            ("Support tiers", "Simple supporter tiers can recognize participation while keeping benefits honest and sustainable."),
            ("What support is not", "Support is not equity, not ownership, not a guaranteed return, and not a promise that every future feature will ship."),
            ("Use of funds", "Show categories like hosting, tools, app development, design, testing, and community operations."),
            ("Thank you experience", "After support, users should feel recognized and invited into the next chapter."),
        ],
        "trust": "Support conversion only works if the mission has already earned belief and boundaries are clear.",
        "next": "Let supporters join the community or contact the founder.",
    },
    "community": {
        "title": "Community",
        "eyebrow": "Built by many",
        "lede": "Project Uni grows when people contribute ideas, testing, research, design, code, stories, and feedback — not only money.",
        "emotion": "Belonging, momentum, and collaboration.",
        "sections": [
            ("Who can join", "Builders, students, designers, researchers, shop owners, early users, and supporters."),
            ("How to contribute", "Feedback, testing, writing, design, code, research, community sharing, and product interviews."),
            ("Community principles", "Respect, transparency, usefulness, humility, safety, and founder accountability."),
            ("Upcoming spaces", "Discord, public progress logs, beta groups, contributor calls, and research notes."),
        ],
        "trust": "Community should feel open but moderated by clear principles.",
        "next": "Turn belonging into direct contact or support.",
    },
    "contact": {
        "title": "Contact",
        "eyebrow": "Direct connection",
        "lede": "Contact should be simple, trustworthy, and clear about why someone is reaching out: partnership, contribution, support, media, or product interest.",
        "emotion": "Access, clarity, and confidence.",
        "sections": [
            ("Founder / team contact", "Provide a direct path to the people building Project Uni."),
            ("Reason for contact", "Separate partnership, community, media, support issue, and contributor interest."),
            ("Response expectations", "Set honest expectations for response time and current capacity."),
            ("Next best action", "If users are not ready to message, guide them to community or support."),
        ],
        "trust": "No contact page should feel like a black hole. It should make the project reachable.",
        "next": "Close the loop and keep the visitor connected.",
    },
}

for name, desc, focus in PRODUCTS:
    key = name.lower().replace(" ", "-")
    PAGE_DATA[key] = {
        "title": name,
        "eyebrow": "Project Uni product",
        "lede": desc,
        "emotion": "Usefulness, clarity, and trust.",
        "sections": [
            ("Target user", f"{name} begins with a focused user need: {focus}."),
            ("Problem it solves", "The first version must solve one concrete problem before expanding into a platform."),
            ("How UniSI powers it", "Shared memory, context, safety, and explainability connect this product back to the Project Uni core."),
            ("Prototype scope", "The MVP should be small enough to test, demo, and improve quickly."),
            ("Safety boundary", "The product must describe what it can support and what decisions remain with the human user."),
            ("Next action", "Invite early interest, community feedback, or support without making the page feel like an ad."),
        ],
        "trust": f"{name} should feel practical first and visionary second.",
        "next": "Return visitors to the ecosystem or invite them into the community.",
    }


def prefix_for(path: Path) -> str:
    return "../" if path.parent.name == "pages" else ""


def nav_html(prefix: str) -> str:
    return "".join(f'<a href="{prefix}{href}">{label}</a>' for label, href in NAV)


def card_html(title: str, text: str, index: int) -> str:
    return f'''
          <article class="card reveal">
            <span class="kicker">{index:02d}</span>
            <h3>{escape(title)}</h3>
            <p>{escape(text)}</p>
          </article>'''


def shell(path: Path, title: str, description: str, body: str) -> None:
    prefix = prefix_for(path)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} — Project Uni</title>
  <meta name="description" content="{escape(description)}">
  <meta name="theme-color" content="#03040a">
  <meta property="og:title" content="{escape(title)} — Project Uni">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:type" content="website">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=Space+Grotesk:wght@500;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{prefix}assets/styles.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="site-shell">
  <nav class="nav" aria-label="Primary navigation">
    <div class="nav-inner">
      <a class="brand" href="{prefix}index.html" aria-label="Project Uni home"><span class="brand-mark" aria-hidden="true"></span><span>Project Uni</span></a>
      <button class="mobile-toggle" data-menu-toggle aria-expanded="false" aria-controls="nav-links">Menu</button>
      <div class="nav-links" id="nav-links" data-nav-links>
        {nav_html(prefix)}
        <a class="nav-cta" href="{prefix}pages/support.html">Support Project Uni</a>
      </div>
    </div>
  </nav>
  <main id="main">
{body}
  </main>
  <footer class="footer">
    <div class="footer-inner">
      <div>
        <div class="brand"><span class="brand-mark" aria-hidden="true"></span><span>Project Uni</span></div>
        <p>Community-built Synthetic Intelligence ecosystem. The mission should sell itself through clarity, trust, and usefulness.</p>
      </div>
      <div><strong>Universe</strong><a href="{prefix}pages/future-of-intelligence.html">Future of Intelligence</a><a href="{prefix}pages/unisi.html">UniSI</a><a href="{prefix}pages/ecosystem.html">Ecosystem</a></div>
      <div><strong>Trust</strong><a href="{prefix}pages/roadmap.html">Roadmap</a><a href="{prefix}pages/transparency.html">Transparency</a><a href="{prefix}pages/research.html">Research</a></div>
      <div><strong>Join</strong><a href="{prefix}pages/community.html">Community</a><a href="{prefix}pages/support.html">Support</a><a href="{prefix}pages/contact.html">Contact</a></div>
    </div>
  </footer>
</div>
<script src="{prefix}assets/app.js"></script>
</body>
</html>
'''
    path.write_text(html, encoding="utf-8")


def page_body(key: str, data: dict) -> str:
    cards = "\n".join(card_html(title, text, i) for i, (title, text) in enumerate(data["sections"], 1))
    grid = "four" if len(data["sections"]) >= 7 else "three"
    body = f'''
    <section class="page-hero reveal">
      <span class="eyebrow">{escape(data["eyebrow"])}</span>
      <h1>{escape(data["title"])}</h1>
      <p class="lede">{escape(data["lede"])}</p>
      <div class="hero-actions">
        <a class="btn" href="support.html">Support Project Uni</a>
        <a class="btn secondary" href="community.html">Join the Community</a>
      </div>
    </section>
    <section class="section">
      <div class="section-head reveal">
        <h2>Why this page exists.</h2>
        <p>{escape(data["emotion"])} Every section is designed to explain the mission, strengthen trust, and guide the visitor toward the next meaningful action.</p>
      </div>
      <div class="grid {grid}">
{cards}
      </div>
    </section>
    <section class="section story-band reveal">
      <div>
        <span class="kicker">Trust standard</span>
        <h2>Built for belief, not hype.</h2>
      </div>
      <p>{escape(data["trust"])} {escape(data["next"])}</p>
    </section>'''
    if data.get("orbit"):
        planets = "\n".join(f'        <a class="planet" href="{name.lower().replace(" ", "-")}.html">{escape(name)}</a>' for name, _, _ in PRODUCTS)
        body += f'''
    <section class="section">
      <div class="orbit card reveal" aria-label="Project Uni ecosystem orbit map">
        <div class="core">UniSI</div>
{planets}
      </div>
    </section>'''
    if data.get("timeline"):
        items = "\n".join(f'        <div class="timeline-item"><h3>{escape(title)}</h3><p>{escape(text)}</p></div>' for title, text in data["sections"])
        body += f'''
    <section class="section">
      <div class="timeline reveal">
{items}
      </div>
    </section>'''
    return body

home_body = '''
    <section class="hero reveal">
      <span class="eyebrow">Welcome to the universe</span>
      <h1>The Future of Intelligence Begins Here.</h1>
      <p class="hero-subtitle">Project Uni</p>
      <p class="lede">A cinematic public gateway for a community-built Synthetic Intelligence ecosystem — designed to make visitors feel they are unlocking chapters of a mission, not reading a generic landing page.</p>
      <div class="hero-actions">
        <a class="btn" href="pages/vision.html">Enter Project Uni</a>
        <a class="btn secondary" href="pages/roadmap.html">Read the Roadmap</a>
      </div>
    </section>
    <section class="section">
      <div class="section-head reveal">
        <h2>Unlock the chapters.</h2>
        <p>The experience begins with emotion, moves into understanding, builds trust, and naturally invites people to become part of Project Uni.</p>
      </div>
      <div class="chapter-list reveal">
        <a class="chapter" href="pages/our-story.html">Our Story</a>
        <a class="chapter" href="pages/vision.html">Vision</a>
        <a class="chapter" href="pages/future-of-intelligence.html">Future of Intelligence</a>
        <a class="chapter" href="pages/unisi.html">UniSI</a>
        <a class="chapter" href="pages/ecosystem.html">Ecosystem</a>
        <a class="chapter" href="pages/research.html">Research</a>
        <a class="chapter" href="pages/roadmap.html">Roadmap</a>
        <a class="chapter" href="pages/support.html">Become Part of Project Uni</a>
      </div>
    </section>
    <section class="section">
      <div class="grid three">
        <article class="card reveal"><span class="kicker">Vision</span><h3>Not built by a few. Built by us.</h3><p>Project Uni presents intelligence as a shared future shaped by community, transparency, and useful products.</p></article>
        <article class="card reveal"><span class="kicker">Core</span><h3>UniSI powers the universe.</h3><p>Memory, perception, cognition, execution, emotion, and immune defense become one living architecture.</p></article>
        <article class="card reveal"><span class="kicker">Trust</span><h3>Support appears after belief.</h3><p>The mission earns trust first. Support is framed as participation, never pressure.</p></article>
      </div>
    </section>
    <section class="section story-band reveal">
      <div><span class="kicker">Founding principle</span><h2>The mission should sell itself.</h2></div>
      <p>Every page, animation, and CTA should help people understand Project Uni, trust the people building it, and choose to participate because the vision feels meaningful.</p>
    </section>'''

shell(ROOT / "index.html", "The Future of Intelligence Begins Here", "Project Uni public website Version 1.0 home experience.", home_body)

for key, data in PAGE_DATA.items():
    shell(PAGES / f"{key}.html", data["title"], data["lede"], page_body(key, data))
