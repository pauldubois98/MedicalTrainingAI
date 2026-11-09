"""Generates all the course diagrams in figures/ (SVG).

Part 1 diagrams are adapted from the LibraryConference talk (translated, medical examples).
"""

import os
import numpy as np
from svgkit import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
os.makedirs(OUT, exist_ok=True)


def out(name):
    return os.path.join(OUT, name)


# ================================================================ Part 1: how AI works
def cats_ml():
    s = SVG(1600, 640)
    ex = [("🐱", "cat", GREEN), ("🐶", "not a cat", RED), ("🐈", "cat", GREEN),
          ("🦁", "not a cat", RED), ("🐈‍⬛", "cat", GREEN), ("🐰", "not a cat", RED)]
    for i, (e, lab, c) in enumerate(ex):
        x = 90 + (i % 2) * 230
        y = 30 + (i // 2) * 180
        s.rect(x, y, 200, 170, fill=WHITE, stroke=c, sw=4)
        s.text(x + 100, y + 70, e, fs=80)
        s.text(x + 100, y + 145, lab, fs=26, color=c, weight="bold")
    s.text(320, 600, "thousands of labelled examples", fs=28, color=MUTED, italic=True)
    s.arrow(590, 300, 760, 300, sw=7)
    s.gear(920, 270, 125, VIOLET, teeth=12, spin=12)
    s.gear(1060, 395, 75, ORANGE, teeth=8, spin=-8, phase=10)
    s.text(960, 540, "training", fs=38, color=VIOLET, weight="bold")
    s.arrow(1150, 300, 1260, 300, sw=7)
    s.rect(1280, 170, 260, 260, fill=WHITE, stroke=MUTED, sw=4, dash="12 10")
    s.text(1410, 270, "🐈", fs=110)
    s.text(1410, 380, "cat: 97%", fs=32, color=GREEN, weight="bold")
    s.text(1410, 480, "new image", fs=28, color=MUTED, italic=True)
    s.save(out("cats_ml.svg"))


def neuron():
    s = SVG(1600, 720)
    xs = [(150, 190), (150, 360), (150, 530)]
    sx, sy, sr = 760, 360, 105
    heads = [(150, "inputs"), (430, "weights"), (sx, "sum"), (1130, "activation"), (1460, "output")]
    for x, t in heads:
        s.text(x, 50, t, fs=30, color=MUTED, italic=True)
    for k, (x, y) in enumerate(xs):
        s.line(x + 55, y, sx - sr + 5, sy, color=[ORANGE, RED, ORANGE][k], sw=[7, 4, 10][k])
        mx, my = x + (sx - x) * 0.42, y + (sy - y) * 0.42
        s.cbox(mx, my, 90, 52, f"w{'₁₂₃'[k]}", fill=WHITE, stroke=[ORANGE, RED, ORANGE][k], fs=30, rx=26)
        s.circle(x, y, 55, fill=LIGHT, stroke=INK)
        s.text(x, y, f"x{'₁₂₃'[k]}", fs=40)
    s.cbox(sx, 120, 170, 64, "b", fill=BLUE_L, stroke=BLUE, fs=28, rx=32)
    s.arrow(sx, 152, sx, sy - sr - 4, color=BLUE, sw=4, head=16)
    s.circle(sx, sy, sr, fill=VIOLET_L, stroke=VIOLET, sw=5)
    s.text(sx, sy - 12, "Σ", fs=80, color=VIOLET, weight="bold")
    s.arrow(sx + sr + 5, sy, 1010, sy, sw=6, head=22)
    bx, by, bw, bh = 1020, 260, 220, 200
    s.rect(bx, by, bw, bh, fill=WHITE, stroke=ORANGE, sw=5)
    s.line(bx + 15, by + bh / 2, bx + bw - 15, by + bh / 2, color="#d0d5de", sw=2)
    s.line(bx + bw / 2, by + 15, bx + bw / 2, by + bh - 15, color="#d0d5de", sw=2)
    pts = []
    for k in range(61):
        t = -6 + 12 * k / 60
        pts.append((bx + 15 + (bw - 30) * k / 60, by + bh - 25 - (bh - 50) / (1 + np.exp(-t))))
    s.raw('<polyline fill="none" stroke="%s" stroke-width="6" stroke-linecap="round" points="%s"/>'
          % (ORANGE, " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)))
    s.text(bx + bw / 2, by + bh + 40, "f", fs=36, color=ORANGE_D, weight="bold", italic=True)
    s.arrow(bx + bw + 5, sy, 1390, sy, sw=6, head=22)
    s.circle(1460, sy, 65, fill=ORANGE, stroke=None)
    s.text(1460, sy, "y", fs=46, color=INK, weight="bold")
    s.raw(f'<text x="800" y="650" font-family="{FONT}" font-size="44" fill="{INK}" text-anchor="middle">'
          f'y = <tspan fill="{ORANGE_D}" font-style="italic" font-weight="bold">f</tspan>( '
          f'<tspan fill="{ORANGE_D}">w₁</tspan>·x₁ + <tspan fill="{RED}">w₂</tspan>·x₂ + '
          f'<tspan fill="{ORANGE_D}">w₃</tspan>·x₃ + <tspan fill="{BLUE}">b</tspan> )</text>')
    s.save(out("neuron.svg"))


def scale_params():
    s = SVG(1600, 700)
    data = [("Demo\nnetwork", 10, "~10"), ("Reading digits\n(1998)", 6e4, "60,000"),
            ("GPT-2\n(2019)", 1.5e9, "1.5 billion"), ("GPT-3\n(2020)", 1.75e11, "175 billion"),
            ("Today's large\nmodels", 1e12, "~1,000 billion?")]
    base_y, top = 560, 90
    lmax = 12.5
    for i, (lab, v, txt) in enumerate(data):
        x = 130 + i * 290
        h = (base_y - top) * max(np.log10(v), 0.3) / lmax
        col = VIOLET if i == len(data) - 1 else ORANGE
        s.rect(x, base_y - h, 190, h, fill=col, rx=10)
        s.text(x + 95, base_y - h - 35, txt, fs=30, weight="bold", color=ORANGE_D if col == ORANGE else col)
        s.text(x + 95, base_y + 60, lab, fs=26)
    s.line(90, base_y, 1560, base_y, color=INK, sw=3)
    s.text(60, 300, "number of weights (log scale)", fs=24, color=MUTED, italic=True, anchor="start")
    s.save(out("scale_params.svg"))


def training_loop():
    s = SVG(1600, 780)
    cx, cy, rx, ry = 800, 400, 434, 280
    steps = [("Example\n(data)", LIGHT, INK), ("Model's\nprediction", VIOLET_L, INK),
             ("Compare with\nthe right answer", ORANGE_L, INK), ("Error", RED_L, RED),
             ("Adjust\nthe weights", GREEN_L, GREEN)]
    n, bw, bh = len(steps), 330, 120
    angles = [-np.pi / 2 + 2 * np.pi * i / n for i in range(n)]
    pts = [(cx + rx * np.cos(a), cy + ry * np.sin(a)) for a in angles]

    def outside(x, y, box, margin=14):
        return abs(x - box[0]) > bw / 2 + margin or abs(y - box[1]) > bh / 2 + margin

    for i in range(n):
        ts = np.linspace(angles[i], angles[i] + 2 * np.pi / n, 200)
        arc = [(cx + rx * np.cos(t), cy + ry * np.sin(t)) for t in ts]
        arc = [p for p in arc if outside(*p, pts[i]) and outside(*p, pts[(i + 1) % n])]
        d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in arc[:-6])
        s.raw(f'<path d="{d}" fill="none" stroke="{MUTED}" stroke-width="5" stroke-linecap="round"/>')
        s.arrow(*arc[-7], *arc[-1], color=MUTED, sw=5, head=22)
    for (x, y), (lab, fill, col) in zip(pts, steps):
        s.cbox(x, y, bw, bh, lab, fill=fill, fs=30, color=col, weight="bold")
    s.text(cx, cy - 20, "× millions of times", fs=44, weight="bold", color=ORANGE_D)
    s.save(out("training_loop.svg"))


def tokens_split():
    s = SVG(1600, 640)
    phrase = "Paracetamol reduces fever."
    rows = [("Characters", list(phrase), LIGHT, 42),
            ("Words", ["Paracetamol", "reduces", "fever", "."], ORANGE_L, None),
            ("Tokens", ["Par", "acet", "amol", " reduces", " fever", "."], VIOLET_L, None)]
    x_start, x_end = 260, 1420
    for r, (lab, units, col, fixed_w) in enumerate(rows):
        y = 50 + r * 150
        s.text(x_start - 30, y + 45, lab, fs=36, anchor="end", weight="bold")
        n = len(units)
        gap = 6 if fixed_w else 12
        lens = [max(len(u), 1) for u in units]
        avail = x_end - x_start - gap * (n - 1)
        x = x_start
        for u, L in zip(units, lens):
            w = avail * L / sum(lens)
            s.box(x, y, w, 90, u.replace(" ", "␣"), fill=col, fs=34 if not fixed_w else 30, rx=10)
            x += w + gap
        s.text(1540, y + 45, str(n), fs=44, weight="bold", color=[MUTED, ORANGE_D, VIOLET][r])
    s.text(1540, 20, "units", fs=24, color=MUTED)
    notes = [("Characters", "few symbols, but very long sequences", MUTED),
             ("Words", "short sequences, but an endless vocabulary (drug names, typos…)", ORANGE_D),
             ("Tokens", "the compromise: frequent chunks, ~50,000 to 200,000 in total", VIOLET)]
    for i, (a, b, c) in enumerate(notes):
        y = 510 + i * 44
        s.text(260, y, a + ":", fs=28, anchor="end", weight="bold", color=c)
        s.text(280, y, b, fs=28, anchor="start", color=INK)
    s.save(out("tokens.svg"))


def softmax_T(logits, T):
    z = np.array(logits) / T
    z -= z.max()
    p = np.exp(z)
    return p / p.sum()


def temperature_static():
    toks = ["fever", "cough", "fatigue", "headache", "muscle", "chills", "sore", "rash"]
    probs0 = np.array([0.55, 0.21, 0.10, 0.06, 0.04, 0.025, 0.01, 0.005])
    logits = np.log(probs0)
    s = SVG(1600, 700)
    s.text(800, 40, "“The most common symptom of flu is …”", fs=40, italic=True, color=MUTED)
    for k, (T, lab) in enumerate([(0.3, "Low temperature (0.3)"), (1.0, "Normal (1)"), (2.5, "High (2.5)")]):
        p = softmax_T(logits, T)
        x0 = 40 + k * 520
        s.text(x0 + 250, 110, lab, fs=32, weight="bold", color=[ORANGE_D, INK, VIOLET][k])
        for i, t in enumerate(toks):
            y = 160 + i * 64
            s.text(x0 + 140, y + 22, t, fs=30, anchor="end")
            s.rect(x0 + 155, y, 300 * p[i] + 2, 48, fill=[ORANGE, MUTED, VIOLET][k], rx=6)
            s.text(x0 + 165 + 300 * p[i], y + 22, f"{100 * p[i]:.0f}%", fs=26, anchor="start", color=MUTED)
    s.save(out("temperature.svg"))


def chat_as_text():
    s = SVG(1600, 700)
    s.text(380, 40, "What the user sees", fs=36, weight="bold", color=ORANGE_D)
    s.box(80, 90, 520, 90, "Can you explain the WHO 5 moments?", fill=ORANGE_L, fs=27)
    s.box(200, 200, 520, 130, "Of course! Are you preparing\na lecture or a quick quiz?", fill=LIGHT, fs=28)
    s.box(80, 350, 520, 90, "A quiz for Year 1 students.", fill=ORANGE_L, fs=28)
    s.box(200, 460, 520, 90, "…", fill=LIGHT, fs=40)
    s.arrow(760, 330, 860, 330, sw=8, head=28)
    s.text(1210, 40, "What the LLM sees", fs=36, weight="bold", color=VIOLET)
    s.rect(880, 80, 660, 520, fill=WHITE, stroke=VIOLET, sw=4)
    lines = [("A conversation between a user and a helpful assistant.", MUTED),
             ("User: Can you explain the WHO 5 moments?", INK),
             ("Assistant: Of course! Are you preparing", INK),
             ("   a lecture or a quick quiz?", INK),
             ("User: A quiz for Year 1 students.", INK),
             ("Assistant:", VIOLET)]
    for i, (l, c) in enumerate(lines):
        s.text(905, 130 + i * 62, l, fs=25, anchor="start", color=c, weight="bold" if c == VIOLET else "normal")
    s.rect(1040, 420, 36, 44, fill=VIOLET, rx=4, opacity=0.6)
    s.text(1210, 650, "one long text, continued token by token", fs=28, color=MUTED, italic=True)
    s.save(out("conversation.svg"))


def knowledge_cutoff():
    """Two sections: what the model saw during training vs what it never saw."""
    s = SVG(1600, 560)
    # seen
    s.rect(40, 30, 700, 500, fill=GREEN_L, rx=28)
    s.text(390, 95, "✅ Seen during training", fs=40, weight="bold", color=GREEN)
    s.text(390, 140, "frozen at the cutoff date", fs=26, color=MUTED, italic=True)
    for i, (e, t) in enumerate([("📚", "Books, textbooks"), ("📄", "Published articles"),
                                ("🌐", "Public websites"), ("📋", "Guidelines up to the cutoff")]):
        y = 220 + i * 82
        s.text(130, y, e, fs=48)
        s.text(190, y, t, fs=32, anchor="start")
    # unseen
    s.rect(860, 30, 700, 500, fill=RED_L, rx=28)
    s.text(1210, 95, "❌ Never seen", fs=40, weight="bold", color=RED)
    s.text(1210, 140, "the model may still invent an answer", fs=26, color=MUTED, italic=True)
    groups = [("🕒", "After the cutoff", "new guidelines, recent studies"),
              ("🔒", "Private", "your regulations, course materials, emails")]
    for i, (e, t, d) in enumerate(groups):
        y = 240 + i * 160
        s.text(950, y + 10, e, fs=56)
        s.text(1010, y - 10, t, fs=34, weight="bold", anchor="start")
        s.text(1010, y + 38, d, fs=26, color=MUTED, anchor="start")
    s.arrow(750, 280, 850, 280, sw=6, head=22)
    s.text(800, 250, "time", fs=22, color=MUTED, italic=True)
    s.save(out("knowledge_cutoff.svg"))


# ================================================================ Part 2: from manual context to RAG
def manual_context():
    s = SVG(1600, 440)
    steps = [("🔎", "1. Search", "PubMed, guidelines,\ncourse files…"),
             ("📋", "2. Copy & paste", "into the\nconversation"),
             ("💬", "3. Ask", "questions about\nthe documents")]
    for i, (e, t, d) in enumerate(steps):
        x = 120 + i * 480
        s.rect(x, 40, 400, 300, fill=LIGHT)
        s.text(x + 200, 120, e, fs=90)
        s.text(x + 200, 215, t, fs=36, weight="bold")
        s.text(x + 200, 285, d, fs=26, color=MUTED)
        if i < 2:
            s.arrow(x + 410, 190, x + 470, 190, sw=6, head=22)
    s.text(800, 405, "✓ Works well for a few documents", fs=34, color=GREEN, weight="bold")
    # the drawbacks are revealed as fragments in slides.md
    s.save(out("manual_context.svg"))


def rag_pipeline():
    s = SVG(1600, 820)
    # indexing (once)
    s.rect(30, 30, 1540, 230, fill=LIGHT, rx=24)
    s.text(60, 70, "Once: build the knowledge base", fs=30, weight="bold", color=ORANGE_D, anchor="start")
    docs = ["📄", "📋", "📚", "🗂️"]
    for i, d in enumerate(docs):
        s.text(110 + i * 85, 165, d, fs=64)
    s.text(240, 230, "articles, guidelines, courses…", fs=24, color=MUTED)
    s.arrow(470, 160, 590, 160, sw=6, head=22)
    s.text(530, 120, "split", fs=24, color=MUTED, italic=True)
    for i in range(8):
        s.rect(610 + (i % 4) * 75, 105 + (i // 4) * 60, 62, 46, fill=WHITE, stroke=MUTED, sw=2, rx=8)
    s.text(760, 235, "passages", fs=24, color=MUTED)
    s.arrow(930, 160, 1050, 160, sw=6, head=22)
    s.text(990, 120, "index", fs=24, color=MUTED, italic=True)
    s.cbox(1260, 160, 380, 130, "🗄️ Knowledge base", fill=WHITE, stroke=ORANGE, fs=34, weight="bold")
    # answering (each question)
    s.text(60, 320, "For each question", fs=30, weight="bold", color=VIOLET, anchor="start")
    s.cbox(200, 430, 300, 120, "❓ Question", fill=ORANGE_L, fs=34, weight="bold")
    s.arrow(355, 430, 470, 430, sw=6, head=22)
    s.cbox(620, 430, 280, 120, "🔎 Search", fill=VIOLET_L, fs=34, weight="bold")
    s.arrow(1260, 228, 700, 365, sw=4, head=18, dash="10 8")
    s.arrow(765, 430, 880, 430, sw=6, head=22)
    s.rect(895, 345, 300, 170, fill=WHITE, stroke=VIOLET, sw=4)
    s.text(1045, 375, "top k passages", fs=24, color=VIOLET, weight="bold")
    for i in range(3):
        s.rect(925, 400 + i * 35, 240, 26, fill=VIOLET_L, rx=6)
    s.arrow(1200, 430, 1300, 430, sw=6, head=22)
    s.cbox(1430, 430, 240, 140, "🧠 LLM", fill=VIOLET, color=WHITE, fs=40, weight="bold")
    s.raw(f'<path d="M200,495 L200,625 L1360,625" stroke="{MUTED}" stroke-width="4" stroke-dasharray="10 8" fill="none"/>')
    s.arrow(1360, 625, 1360, 505, sw=4, head=18, dash="10 8")
    # s.text(780, 600, "the question is sent too", fs=24, color=MUTED, italic=True)
    s.arrow(1480, 505, 1480, 685, sw=6, head=22)
    s.cbox(1060, 740, 900, 100, "✅ Answer grounded in the passages, with citations [1] [2]", fill=GREEN_L,
           fs=32, color=GREEN, weight="bold")
    s.save(out("rag_pipeline.svg"))


# ================================================================ Part 3: tools and agents
def chatbot_vs_agent():
    s = SVG(1600, 760)
    s.text(330, 40, "Chatbot", fs=42, weight="bold", color=ORANGE_D)
    s.cbox(330, 150, 300, 100, "User", fill=LIGHT, fs=32)
    s.arrow(330, 205, 330, 285)
    s.cbox(330, 350, 260, 110, "LLM", fill=ORANGE, color=INK, fs=40, weight="bold")
    s.arrow(330, 410, 330, 490)
    s.cbox(330, 560, 300, 110, "📝 Text", fill=ORANGE_L, fs=34)
    s.text(330, 690, "stays in the world of text", fs=28, color=MUTED, italic=True)
    s.line(680, 40, 680, 720, color=LIGHT, sw=6)
    s.text(1140, 40, "Agent", fs=42, weight="bold", color=VIOLET)
    s.cbox(1140, 150, 300, 100, "User", fill=LIGHT, fs=32)
    s.arrow(1140, 205, 1140, 285)
    s.cbox(1140, 350, 260, 110, "LLM", fill=VIOLET, color=WHITE, fs=40, weight="bold")
    tools = [("🌐", "Web"), ("📚", "PubMed"), ("🗂️", "Documents"), ("✉️", "E-mail")]
    for i, (e, t) in enumerate(tools):
        x = 810 + i * 220
        s.arrow(1140, 410, x, 500, sw=4)
        s.cbox(x, 570, 190, 130, "", fill=VIOLET_L)
        s.text(x, 545, e, fs=50)
        s.text(x, 605, t, fs=28, weight="bold")
    s.text(1140, 700, "it can look things up, and act", fs=28, color=VIOLET, italic=True, weight="bold")
    s.save(out("chatbot_vs_agent.svg"))


def human_vs_agent():
    s = SVG(1600, 700)
    rows = [("👩‍⚕️ A teacher", ORANGE_D, ORANGE_L,
             ["“I don't know”", "Look it up\n(PubMed, guideline)", "Read the\nresults", "Answer, citing\nthe source"]),
            ("🤖 An AI agent", VIOLET, VIOLET_L,
             ["Missing\ninformation", "Call a tool\n(search)", "Results added\nto its context", "Answer, citing\nthe source"])]
    for r, (who, col, fill, steps) in enumerate(rows):
        y = 70 + r * 330
        s.text(40, y + 10, who, fs=36, weight="bold", color=col, anchor="start")
        for i, st in enumerate(steps):
            x = 60 + i * 380
            s.box(x, y + 60, 320, 170, st, fill=fill, fs=30, weight="bold")
            if i < 3:
                s.arrow(x + 328, y + 145, x + 372, y + 145, sw=6, head=20)
    s.save(out("human_vs_agent.svg"))


def knowledge_sources():
    """Summary: four ways for a model to 'know' something."""
    s = SVG(1600, 640)
    cols = [("🧠", "Training", "what it learned,\nfrozen at the\ncutoff date", ORANGE_L, ORANGE_D),
            ("📋", "Pasted context", "documents you\ncopy into the\nconversation", LIGHT, INK),
            ("🗄️", "RAG", "passages retrieved\nautomatically from\na knowledge base", VIOLET_L, VIOLET),
            ("🛠️", "Tools / agents", "searches the web,\nPubMed… when it\ndecides it needs to", GREEN_L, GREEN)]
    for i, (e, t, d, fill, col) in enumerate(cols):
        x = 40 + i * 390
        s.rect(x, 40, 360, 470, fill=fill)
        s.text(x + 180, 130, e, fs=90)
        s.text(x + 180, 230, t, fs=36, weight="bold", color=col)
        s.text(x + 180, 360, d, fs=28)
    s.arrow(80, 580, 1520, 580, sw=5, head=22)
    s.text(800, 620, "more up to date, more specific… and more sources to check", fs=26, color=MUTED, italic=True)
    s.save(out("knowledge_sources.svg"))


# ================================================================ Best practices
def fake_reference():
    """Narrow layout: shown in the left column of the best-practices slide."""
    s = SVG(1000, 640)
    s.rect(20, 20, 960, 330, fill=WHITE, stroke=MUTED, sw=3)
    lines = [("Martin L, Okafor C, Lindqvist S.", False, INK),
             ("Effect of high-fidelity simulation on nursing", False, INK),
             ("students' clinical judgement: a randomized", False, INK),
             ("controlled trial. J Nurs Educ. 2021;60(4):212-219.", True, INK),
             ("doi:10.3928/01484834-20210322-99", False, BLUE)]
    for i, (t, it, c) in enumerate(lines):
        s.text(50, 80 + i * 58, t, fs=34, anchor="start", italic=it, color=c)
    notes = [(260, 400, "✓ plausible authors", GREEN), (740, 400, "✓ realistic title", GREEN),
             (260, 450, "✓ real journal", GREEN), (740, 450, "✗ article does not exist", RED)]
    for x, y, t, c in notes:
        s.text(x, y, t, fs=32, color=c, weight="bold")
    s.cbox(500, 540, 960, 80, "🔎 DOI → doi.org · title → PubMed / Scholar", fill=ORANGE_L, fs=32, weight="bold")
    s.text(500, 620, "Fabricated example, made for this course", fs=24, color=MUTED, italic=True)
    s.save(out("fake_reference.svg"))


if __name__ == "__main__":
    cats_ml()
    neuron()
    scale_params()
    training_loop()
    tokens_split()
    temperature_static()
    chat_as_text()
    knowledge_cutoff()
    manual_context()
    rag_pipeline()
    chatbot_vs_agent()
    human_vs_agent()
    knowledge_sources()
    fake_reference()
    print("figures generated in", OUT)
