import streamlit as st
from streamlit.components.v1 import html

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Antiqpa Solutions",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- SESSION STATE --------------------
if "section" not in st.session_state:
    st.session_state["section"] = "Inicio"

# -------------------- TUS URLs (se mantienen) --------------------
URL_HERO_BG   = "https://admin.live.ilo.org/sites/default/files/styles/desktop/public/2024-07/ai-technology-brain-background-digital-transformation-concept.jpg?itok=wI9Ia9fz"
URL_SIDEBAR   = "https://imgcdn.stablediffusionweb.com/2024/9/17/5af8326d-0ef5-4a79-9e37-9f3aeaa46c17.jpg"

URL_GAL_HERO  = "https://img.freepik.com/free-psd/futuristic-robot-using-laptop_191095-85585.jpg?semt=ais_incoming&w=740&q=80"
URL_GAL_OFF   = "https://imgcdn.stablediffusionweb.com/2024/9/17/5af8326d-0ef5-4a79-9e37-9f3aeaa46c17.jpg"
URL_GAL_PTRN  = "https://img.computing.es/wp-content/uploads/2024/01/19110432/Inteligencia-Artificial.jpg"
URL_GAL_CANVA = "https://marketplace.canva.com/MADerCgbmTs/1/thumbnail_large/canva-artificial-intelligence-and-future-concept-MADerCgbmTs.jpg"

# Equipo (tarjetas verticales)
URL_EQ_MIGUEL = "https://images.unsplash.com/photo-1534723328310-e82dad3ee43f?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8U2FsdWRhciUyMGElMjBsYSUyMHJvYiVDMyVCM3RpY2F8ZW58MHx8MHx8fDA%3D"
URL_EQ_JOSE   = "https://storage.googleapis.com/bucket-two-leobotics/product/robot-humanoide-mouvements-et-depacement-autonome-robothespian-engineered-arts-1-1.jpg"
URL_EQ_CECI   = "https://png.pngtree.com/png-clipart/20200328/ourmid/pngtree-artificial-intelligence-management-system-robot-png-image_2165259.jpg"
URL_EQ_TEAM   = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt6SMBXnRbtjxSJ7k7c43lcv4x7FnUMFjCFA&s"

# Formulario y Chatbot
GOOGLE_FORM_URL = "https://script.google.com/macros/s/AKfycbzef6VyHqRwCWrzh87gdV53Ud6GOD62emSjOSMlvUxt15cqPGVWHxpT-ce94USfB1E0mw/exec"

# Este script se ejecuta dentro del iframe del componente y "inyecta" el widget del chatbot en el documento principal

DIALOGFLOW_INJECTOR = """
<script>
(function(){
  const ensureChatbot = () => {
    const P = window.parent;
    if (!P || !P.document) return;

    if (!P.document.getElementById('df-messenger-bootstrap')) {
      const s = P.document.createElement('script');
      s.id = 'df-messenger-bootstrap';
      s.src = 'https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1';
      P.document.head.appendChild(s);
    }

    if (!P.document.getElementById('df-messenger-container')) {
      const c = P.document.createElement('div');
      c.id = 'df-messenger-container';
      c.style.position = 'fixed';
      c.style.left = '16px';
      c.style.bottom = '16px';
      c.style.zIndex = '2147483647';
      c.innerHTML = `
        <df-messenger
          intent="WELCOME"
          chat-title="Virtual Yanapaq"
          agent-id="372a5eeb-31b9-4777-bfd4-a9a2af72e162"
          language-code="es"
          chat-icon="data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='128' height='128'><text y='50%' x='50%' dominant-baseline='middle' text-anchor='middle' font-size='96'>🤖</text></svg>">
        </df-messenger>
      `;
      P.document.body.appendChild(c);
    }
  };
  document.addEventListener('DOMContentLoaded', ensureChatbot);
  setTimeout(ensureChatbot, 800);
})();
</script>
"""


# -------------------- ESTILOS GLOBALES --------------------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Source+Serif+Pro:wght@400;600;700&display=swap');

:root {{
  --bg:#0b1220;
  --bg-soft:#0f1a32;
  --panel:#121f3b;
  --panel-2:#18264a;
  --text:#ffffff;   /* texto blanco */
  --muted:#cfd6ea;  /* secundario */
  --accent:#d4b36c; /* dorado para títulos/subtítulos */
  --accent-2:#9fb8ff;
}}

html, body, [data-testid="stAppViewContainer"] {{
  background: radial-gradient(1200px 600px at 10% -10%, rgba(159,184,255,0.08), transparent 40%),
              radial-gradient(1200px 600px at 90% 0%, rgba(212,179,108,0.10), transparent 40%),
              linear-gradient(180deg, var(--bg), var(--bg-soft) 60%, var(--bg));
  color: var(--text) !important;
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Arial;
}}

h1, h2, h3 {{
  font-family: "Source Serif Pro", Georgia, serif;
  letter-spacing: .2px;
  color: var(--accent);  /* títulos/subtítulos dorado */
}}

h1 {{ font-size: 2.6rem; font-weight: 700; }}
h2 {{ font-size: 1.9rem; font-weight: 700; margin-top: .4rem; }}
h3 {{ font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: .8px; }}

p, li, div, span {{ color: var(--text); }}
.small {{ font-size: 0.95rem; color: var(--muted); }}
.muted {{ color: var(--muted); }}

/* Título con borde blanco en la HOME */
.hero h1.title-stroke {{
  color: var(--accent);
  -webkit-text-stroke: 2px #ffffff;
  text-shadow:
    1px 1px 0 #ffffff,
    -1px 1px 0 #ffffff,
    1px -1px 0 #ffffff,
    -1px -1px 0 #ffffff;
}}

.badge {{
  display:inline-block; padding: 6px 10px; border-radius: 999px;
  background: rgba(212,179,108,0.12); color: var(--accent);
  border: 1px solid rgba(212,179,108,0.35); font-weight: 700; font-size: 0.78rem; letter-spacing:.6px;
}}

.card {{
  background: linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px; padding: 18px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.28), inset 0 0 0 1px rgba(255,255,255,0.02);
  color: var(--text);
}}

.hero {{
  position: relative;
  border-radius: 22px;
  background:
    linear-gradient(120deg, rgba(159,184,255,0.10), rgba(212,179,108,0.06)),
    url('{URL_HERO_BG}');
  background-size: cover;
  background-position: center;
  border: 1px solid rgba(255,255,255,0.08);
  overflow: hidden;
}}
.hero .overlay-shape {{
  position:absolute; inset:-40px -20px auto auto; width:380px; height:380px;
  background: radial-gradient(closest-side, rgba(212,179,108,0.20), transparent 60%);
  filter: blur(14px); border-radius: 50%;
}}
.hero p {{ color: var(--text); max-width: 980px; font-size:1.02rem; }}

.kpis {{ display:grid; gap: 12px; grid-template-columns: repeat(4, minmax(0,1fr)); }}
.kpi {{ padding:18px; border-radius: 16px; background:var(--panel); border:1px solid rgba(255,255,255,0.08); text-align:center;}}
.kpi .v {{ font-size: 1.6rem; font-weight: 800; color: var(--accent); }}
.kpi .t {{ font-size: 0.95rem; color: var(--muted); }}

.grid-3 {{ display:grid; gap: 16px; grid-template-columns: repeat(3, minmax(0,1fr)); }}
.grid-4 {{ display:grid; gap: 16px; grid-template-columns: repeat(4, minmax(0,1fr)); }}

.figure {{
  height: 200px; border-radius: 16px; background-size: cover; background-position: center;
  border:1px solid rgba(255,255,255,0.10);
}}

/* Sidebar: "Navegación" dorado; opciones del radio en blanco */
section[data-testid="stSidebar"] {{
  background: linear-gradient(180deg, #0a0f25, #0b1230) !important;
  border-right: 1px solid rgba(255,255,255,0.06);
}}
section[data-testid="stSidebar"] h2, section[data-testid="stSidebar"] h3 {{
  color: var(--accent) !important;    /* Encabezado "Navegación" en dorado */
}}
section[data-testid="stSidebar"] [role="radiogroup"] label,
section[data-testid="stSidebar"] [role="radiogroup"] label span,
section[data-testid="stSidebar"] [role="radiogroup"] label p,
section[data-testid="stSidebar"] [role="radiogroup"] label div {{
  color: #ffffff !important;          /* opciones en blanco */
}}

/* Pricing */
.pricing {{ display:grid; gap: 16px; grid-template-columns: repeat(3, minmax(0,1fr)); }}
.pricing .tier {{
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.015));
  border:1px solid rgba(255,255,255,0.07);
  border-radius:18px; padding:18px;
}}
.tier h4 {{ font-size:1.2rem; margin:0 0 2px 0; color: var(--accent); }}
.tier .price {{ font-size:1.6rem; font-weight:800; color: var(--accent); }}
.tier ul {{ margin-top: 8px; }}
.tier li {{ margin: 4px 0; color: var(--text); }}

/* Equipo: vertical (retrato) en 3 columnas */
.team-grid {{ display:grid; gap: 16px; grid-template-columns: repeat(3, minmax(0,1fr)); }}
.team-card .figure {{ height: 260px; }}
.team-card h3 {{ color: var(--accent); }}
.team-card .small {{ color: var(--muted); }}
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.image(URL_SIDEBAR, use_column_width=True)
st.sidebar.markdown("## Navegación")
section = st.sidebar.radio(
    label="Ir a la sección:",
    options=["Inicio", "Quiénes somos", "Productos", "Paquetes", "Soluciones", "Equipo", "Contacto"],
    index=["Inicio", "Quiénes somos", "Productos", "Paquetes", "Soluciones", "Equipo", "Contacto"].index(st.session_state["section"]),
    key="section"
)
st.sidebar.markdown("---")
st.sidebar.markdown("**Sectores:** Fintech · Retail · Educación · Comunicaciones")
st.sidebar.markdown("<span class='small'>© 2025 Antiqpa Solutions</span>", unsafe_allow_html=True)

# -------------------- SECTIONS --------------------
def section_home():
    st.markdown(f"""
    <div class="hero" style="padding: 28px; margin-bottom: 16px;">
      <div class="overlay-shape"></div>
      <span class="badge">IA Generativa Empresarial</span>
      <h1 class="title-stroke">Antiqpa Solutions</h1>
      <p>Soluciones de Inteligencia Artificial Generativa para organizaciones que exigen <b>precisión</b>, <b>rapidez</b> y <b>gobernanza</b>. Integramos economía, administración y comunicaciones en flujos de valor medibles.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='kpis'>", unsafe_allow_html=True)
    st.markdown("""
      <div class='kpi'><div class='v'>+30%</div><div class='t'>Mejora en conversión</div></div>
      <div class='kpi'><div class='v'>-40%</div><div class='t'>Tiempo de reportes</div></div>
      <div class='kpi'><div class='v'>99.9%</div><div class='t'>Disponibilidad</div></div>
      <div class='kpi'><div class='v'>24/7</div><div class='t'>Agentes activos</div></div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### Galería")
    st.markdown("<div class='grid-4'>", unsafe_allow_html=True)
    st.markdown(f"""
      <div class='figure' style="background-image:url('{URL_GAL_HERO}');"></div>
      <div class='figure' style="background-image:url('{URL_GAL_OFF}');"></div>
      <div class='figure' style="background-image:url('{URL_GAL_PTRN}');"></div>
      <div class='figure' style="background-image:url('{URL_GAL_CANVA}');"></div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def section_about():
    st.markdown("## ¿Quiénes somos?")
    st.markdown("""
**Antiqpa Solutions** es una firma especializada en **Inteligencia Artificial Generativa** con sede en Lima y operación regional.
Acompañamos a organizaciones en **finanzas, retail, educación y comunicaciones** para transformar datos en decisiones de negocio
con **gobernanza, trazabilidad y seguridad**.
    """)
    st.markdown("""
**Misión**: Generar valor medible uniendo analítica económica, eficiencia administrativa y comunicación estratégica.  
**Visión**: Ser el socio líder en IA Generativa empresarial en Latinoamérica.  
**Diferenciales**: cumplimiento (GDPR/LGPD/ISO 27001), observabilidad de prompts, revisión humana en procesos sensibles
y time-to-value rápido mediante aceleradores modulares.
    """)
    st.markdown("""
**Servicios clave**: evaluación de casos de uso, integración con ERP/CRM/Data Lake, diseño de agentes, automatización de reportes,
motor de pricing dinámico, orquestación de campañas y capacitación del personal.
    """)

def section_products():
    st.markdown("## Productos")
    st.markdown("### Antiqpa Insights")
    st.markdown("<div class='card'>Reportes ejecutivos automáticos y simulación de escenarios macroeconómicos con recomendaciones accionables.</div>", unsafe_allow_html=True)
    st.markdown("### Antiqpa Admin")
    st.markdown("<div class='card'>Minutas inteligentes, tableros KPI, alertas de gestión (stock, márgenes, riesgo) y automatización documental.</div>", unsafe_allow_html=True)
    st.markdown("### Antiqpa Comms")
    st.markdown("<div class='card'>Generación de campañas multicanal, personalización por segmento, A/B testing y control de tono de marca.</div>", unsafe_allow_html=True)
    st.markdown("### Antiqpa Chat")
    st.markdown("<div class='card'>Asistente entrenado con datos internos (ERP/CRM) con retrieval seguro, trazabilidad y revisión humana.</div>", unsafe_allow_html=True)

def section_packages():
    st.markdown("## Paquetes")
    st.markdown("<div class='pricing'>", unsafe_allow_html=True)
    st.markdown("""
    <div class='tier'>
      <h4>Starter</h4>
      <div class='price'>US$ 5,000/mes</div>
      <ul>
        <li>Chatbot corporativo básico</li>
        <li>Reportes ejecutivos mensuales</li>
        <li>Hasta 100k interacciones/mes</li>
        <li>Soporte estándar</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='tier'>
      <h4>Business</h4>
      <div class='price'>US$ 15,000/mes</div>
      <ul>
        <li>Pricing dinámico</li>
        <li>Reportes semanales</li>
        <li>Campañas multicanal automáticas</li>
        <li>1M interacciones/mes · Soporte prioritario</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class='tier'>
      <h4>Enterprise</h4>
      <div class='price'>US$ 40,000/mes</div>
      <ul>
        <li>Agentes económicos y administrativos</li>
        <li>Comunicaciones hiperpersonalizadas</li>
        <li>Integración total ERP/CRM</li>
        <li>Auditorías y seguridad avanzada</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def section_solutions():
    st.markdown("## Soluciones a problemas comunes")
    st.markdown("<div class='grid-3'>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Inflación y tipo de cambio</h3><p>Motor de <b>pricing dinámico</b> con señales macro y de demanda por región.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Reportes tardíos</h3><p><b>Reportes automáticos</b> y minutas listas en minutos para comités.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Mensajes genéricos</h3><p><b>Campañas generativas</b> personalizadas por segmento y canal.</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='grid-3' style='margin-top:12px;'>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Soporte saturado</h3><p><b>Chatbots</b> entrenados con datos internos, con handoff humano.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Gobernanza</h3><p><b>Guardrails</b>, evaluación humana, trazabilidad y cumplimiento regulatorio.</p></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>Integración legacy</h3><p>Conectores seguros a <b>ERP/CRM/Data Lake</b> y APIs.</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def section_team():
    st.markdown("## Nuestro equipo")
    st.markdown("<div class='team-grid'>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card team-card'>
      <div class='figure' style="background-image:url('{URL_EQ_JOSE}');"></div>
      <h3 style="margin-top:10px;">José Botto</h3>
      <div class='small'>Chief Communications AI · Comunicación estratégica</div>
      <div class='small'>Personalización omnicanal, tono de marca, A/B testing.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card team-card'>
      <div class='figure' style="background-image:url('{URL_EQ_MIGUEL}');"></div>
      <h3 style="margin-top:10px;">Miguel Olivero</h3>
      <div class='small'>Chief AI Officer · Modelos de lenguaje y agentes</div>
      <div class='small'>Arquitectura de soluciones generativas y gobernanza.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class='card team-card'>
      <div class='figure' style="background-image:url('{URL_EQ_CECI}');"></div>
      <h3 style="margin-top:10px;">Cecilia Sánchez</h3>
      <div class='small'>Head of Economist · Macroeconomía y econometría aplicada</div>
      <div class='small'>Series temporales, simulación de escenarios, elasticidades.</div>
    </div>
    """, unsafe_allow_html=True)

    # Bloque adicional opcional
    st.markdown(f"""
    <div class='card team-card'>
      <div class='figure' style="background-image:url('{URL_EQ_TEAM}');"></div>
      <h3 style="margin-top:10px;">Equipo Antiqpa</h3>
      <div class='small'>Ingeniería de datos, ML, seguridad y cumplimiento</div>
      <div class='small'>Implementación, observabilidad y soporte 24/7.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

def section_contact():
    st.markdown("## Contacto")
    st.markdown("""
Si deseas conversar con nuestro equipo, **solicita una demo** o **déjanos un mensaje** en el formulario a continuación.
También puedes escribirnos a **contacto@antiqpa.com** o llamarnos al **+51 123 456 789**.
    """)

    # Formulario incrustado (si el dominio permite iframe)
    html(f"""
        <iframe src="{GOOGLE_FORM_URL}"
                width="100%" height="700"
                style="border:1px solid rgba(255,255,255,0.2); border-radius:12px; background:#fff;">
        </iframe>
    """, height=740)

    # Enlace alternativo por si el proveedor bloquea iframes (X-Frame-Options)
    st.markdown(
        f'<div style="margin-top:8px;"><a class="btn" href="{GOOGLE_FORM_URL}" target="_blank">Abrir formulario en una nueva pestaña</a></div>',
        unsafe_allow_html=True
    )

# -------------------- ROUTER --------------------
if st.session_state["section"] == "Inicio":
    section_home()
elif st.session_state["section"] == "Quiénes somos":
    section_about()
elif st.session_state["section"] == "Productos":
    section_products()
elif st.session_state["section"] == "Paquetes":
    section_packages()
elif st.session_state["section"] == "Soluciones":
    section_solutions()
elif st.session_state["section"] == "Equipo":
    section_team()
elif st.session_state["section"] == "Contacto":
    section_contact()

# -------------------- CHATBOT (esquina inferior izquierda, visible en todas las páginas) --------------------
# Inyectamos el widget en el documento principal para que flote por encima de la app
html(DIALOGFLOW_INJECTOR, height=0)

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("<div class='small'>© 2025 Antiqpa Solutions · Lima, Perú · contacto@antiqpa.com · +51 123 456 789</div>", unsafe_allow_html=True)
