import streamlit as st
from pathlib import Path

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Antiqpa Solutions",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- ASSETS --------------------
ASSETS = Path("assets")
def img(path, fallback_url):
    p = ASSETS / path
    if p.exists():
        return str(p.as_posix())
    return fallback_url

# -------------------- GLOBAL STYLES --------------------
st.markdown("""
<style>
/* Tipografías (Google Fonts): Inter + Source Serif Pro */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=Source+Serif+Pro:wght@400;600;700&display=swap');

:root{
  /* Paleta formal: azul petróleo + marfil + dorado sobrio */
  --bg:#0b1220;
  --bg-soft:#0f1a32;
  --panel:#121f3b;
  --panel-2:#18264a;
  --text:#eef1f7;
  --muted:#a7b1c7;
  --accent:#d4b36c;   /* dorado sobrio */
  --accent-2:#9fb8ff; /* acento secundario frío */
}

html, body, [data-testid="stAppViewContainer"] {
  background: radial-gradient(1200px 600px at 10% -10%, rgba(159,184,255,0.08), transparent 40%),
              radial-gradient(1200px 600px at 90% 0%, rgba(212,179,108,0.10), transparent 40%),
              linear-gradient(180deg, var(--bg), var(--bg-soft) 60%, var(--bg));
  color: var(--text) !important;
  font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Arial;
}

h1, h2 {
  font-family: "Source Serif Pro", Georgia, serif;
  letter-spacing: .2px;
}
h1 { font-size: 2.6rem; font-weight: 700; }
h2 { font-size: 1.9rem; font-weight: 700; margin-top: .4rem; }
h3 { font-size: 1.15rem; font-weight: 700; color: var(--accent); text-transform: uppercase; letter-spacing: .8px; }

.small { font-size: 0.92rem; color: var(--muted); }
.muted { color: var(--muted); }

.badge {
  display:inline-block; padding: 6px 10px; border-radius: 999px;
  background: rgba(212,179,108,0.1); color: var(--accent);
  border: 1px solid rgba(212,179,108,0.35); font-weight: 700; font-size: 0.78rem; letter-spacing:.6px;
}

.card {
  background: linear-gradient(180deg, rgba(255,255,255,0.03), rgba(255,255,255,0.02));
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px; padding: 18px;
  box-shadow: 0 12px 40px rgba(0,0,0,0.28), inset 0 0 0 1px rgba(255,255,255,0.02);
}

.hero {
  position: relative;
  border-radius: 22px;
  background:
    linear-gradient(120deg, rgba(159,184,255,0.10), rgba(212,179,108,0.06)),
    url('""" + img("pattern.jpg", "https://images.unsplash.com/photo-1520975922284-5f1a6f3d6c5a?auto=format&fit=crop&w=1600&q=80") + """');
  background-size: cover;
  background-position: center;
  border: 1px solid rgba(255,255,255,0.08);
  overflow: hidden;
}
.hero .overlay-shape {
  position:absolute; inset:-40px -20px auto auto; width:380px; height:380px;
  background: radial-gradient(closest-side, rgba(212,179,108,0.20), transparent 60%);
  filter: blur(14px); border-radius: 50%;
}
.hero h1 { margin-bottom: 0.2rem; }
.hero p { color: var(--muted); max-width: 980px; font-size:1.02rem; }

.kpis { display:grid; gap: 12px; grid-template-columns: repeat(4, minmax(0,1fr)); }
.kpi { padding:18px; border-radius: 16px; background:var(--panel); border:1px solid rgba(255,255,255,0.06); text-align:center;}
.kpi .v { font-size: 1.6rem; font-weight: 800; color: var(--accent); }
.kpi .t { font-size: 0.95rem; color: var(--muted); }

.btn a {
  text-decoration: none !important; color: #0b1220 !important; font-weight: 800;
}
.btn {
  display:inline-block; padding: 12px 18px; border-radius: 12px;
  background: linear-gradient(90deg, var(--accent), #f3d9a4);
  border: none; margin-right: 12px;
}

.grid-3 { display:grid; gap: 16px; grid-template-columns: repeat(3, minmax(0,1fr)); }
.grid-4 { display:grid; gap: 16px; grid-template-columns: repeat(4, minmax(0,1fr)); }

.figure {
  height: 180px; border-radius: 16px; background-size: cover; background-position: center;
  border:1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0a0f25, #0b1230) !important;
  border-right: 1px solid rgba(255,255,255,0.06);
}

/* Detalle formal en tablas/paquetes */
.pricing {
  display:grid; gap: 16px; grid-template-columns: repeat(3, minmax(0,1fr));
}
.pricing .tier {
  background: linear-gradient(180deg, rgba(255,255,255,0.025), rgba(255,255,255,0.015));
  border:1px solid rgba(255,255,255,0.07);
  border-radius:18px; padding:18px;
}
.tier h4 { font-size:1.2rem; margin:0 0 2px 0; }
.tier .price { font-size:1.6rem; font-weight:800; color: var(--accent); }
.tier ul { margin-top: 8px; }
.tier li { margin: 4px 0; }
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR NAV --------------------
st.sidebar.image(
    img("office.jpg", "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1400&q=80"),
    use_column_width=True
)
st.sidebar.markdown("## Navegación")
section = st.sidebar.radio(
    "Ir a la sección:",
    ["Inicio", "Quiénes somos", "Productos", "Paquetes", "Soluciones", "Equipo", "Contacto"],
    index=0
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
      <h1>Antiqpa Solutions</h1>
      <p>Soluciones de Inteligencia Artificial Generativa para organizaciones que exigen <b>precisión</b>, <b>rapidez</b> y <b>gobernanza</b>. Integramos economía, administración y comunicaciones en flujos de valor medibles.</p>
      <div style="margin-top:12px;">
        <span class="btn"><a href="#contacto">Solicitar una demo</a></span>
        <span class="btn"><a href="#productos">Ver productos</a></span>
      </div>
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

    c1, c2, c3 = st.columns([1,1,1])
    with c1:
        st.markdown("### Análisis Económico")
        st.markdown("<div class='card'>Simulación de escenarios macro (inflación, tipo de cambio), recomendaciones de pricing/promos por región y categoría.</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("### Gestión Administrativa")
        st.markdown("<div class='card'>Reportes ejecutivos automatizados, minutas inteligentes, alertas y tableros KPI integrados a ERP/CRM.</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("### Comunicación Estratégica")
        st.markdown("<div class='card'>Campañas generativas multicanal, personalización por segmento, pruebas A/B y control de tono de marca.</div>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Galería")
    st.markdown("<div class='grid-4'>", unsafe_allow_html=True)
    st.markdown(f"""
      <div class='figure' style="background-image:url('{img('hero.jpg', 'https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=1600&q=80')}');"></div>
      <div class='figure' style="background-image:url('{img('office.jpg', 'https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=1600&q=80')}');"></div>
      <div class='figure' style="background-image:url('{img('pattern.jpg', 'https://images.unsplash.com/photo-1545235617-9465d2a55698?auto=format&fit=crop&w=1600&q=80')}');"></div>
      <div class='figure' style="background-image:url('https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=1600&q=80');"></div>
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
    st.markdown("<a id='productos'></a>", unsafe_allow_html=True)
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
    st.markdown("<div class='grid-4'>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
      <div class='figure' style="background-image:url('{img('jose_botto.jpg', 'https://images.unsplash.com/photo-1607746882042-944635dfe10e?auto=format&fit=crop&w=1400&q=80')}');"></div>
      <h3 style="margin-top:10px;">José Botto</h3>
      <div class='small'>Chief AI Officer · Modelos de lenguaje y agentes</div>
      <div class='small'>Arquitectura de soluciones generativas y gobernanza.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
      <div class='figure' style="background-image:url('{img('miguel_olivero.jpg', 'https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=1400&q=80')}');"></div>
      <h3 style="margin-top:10px;">Miguel Olivero</h3>
      <div class='small'>Chief Economist · Macro aplicada y pricing</div>
      <div class='small'>Series temporales, simulación de escenarios, elasticidades.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(f"""
    <div class='card'>
      <div class='figure' style="background-image:url('{img('cecilia_sanchez.jpg', 'https://images.unsplash.com/photo-1527980965255-d3b416303d12?auto=format&fit=crop&w=1400&q=80')}');"></div>
      <h3 style="margin-top:10px;">Cecilia Sánchez</h3>
      <div class='small'>Head of Communications AI · Comunicación estratégica</div>
      <div class='small'>Personalización omnicanal, tono de marca, A/B testing.</div>
    </div>
    """, unsafe_allow_html=True)
    # cuarto slot opcional para crecer el equipo
    st.markdown(f"""
    <div class='card'>
      <div class='figure' style="background-image:url('https://images.unsplash.com/photo-1556157382-97eda2d62296?auto=format&fit=crop&w=1400&q=80');"></div>
      <h3 style="margin-top:10px;">Equipo Antiqpa</h3>
      <div class='small'>Ingeniería de datos, ML, seguridad y cumplimiento</div>
      <div class='small'>Implementación, observabilidad y soporte 24/7.</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def section_contact():
    st.markdown("<a id='contacto'></a>", unsafe_allow_html=True)
    st.markdown("## Contacto")
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Nombre completo")
            company = st.text_input("Empresa")
            email = st.text_input("Correo")
        with c2:
            phone = st.text_input("Teléfono")
            topic = st.selectbox("Interés", ["Demo", "Cotización", "Soporte", "Otro"])
            pkg = st.selectbox("Paquete de interés", ["Starter", "Business", "Enterprise"])
        message = st.text_area("Mensaje", height=120, placeholder="Cuéntanos tu necesidad...")
        submitted = st.form_submit_button("Enviar")
        if submitted:
            st.success("Gracias. Hemos recibido tu solicitud. (Demo)")

# -------------------- ROUTER --------------------
if section == "Inicio":
    section_home()
elif section == "Quiénes somos":
    section_about()
elif section == "Productos":
    section_products()
elif section == "Paquetes":
    section_packages()
elif section == "Soluciones":
    section_solutions()
elif section == "Equipo":
    section_team()
elif section == "Contacto":
    section_contact()

# Footer
st.markdown("---")
st.markdown("<div class='small'>© 2025 Antiqpa Solutions · Lima, Perú · contacto@antiqpa.com · +51 123 456 789</div>", unsafe_allow_html=True)
