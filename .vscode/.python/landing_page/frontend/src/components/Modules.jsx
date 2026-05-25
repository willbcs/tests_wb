import { useState } from "react";

const modules = [
  { num: "01", title: "Educação financeira", description: "Aprenda os fundamentos da organização financeira e como controlar seu dinheiro com tranquilidade." },
  { num: "02", title: "Como sair das dívidas", description: "Estratégias práticas e acessíveis para quitar dívidas e recuperar sua saúde financeira de vez." },
  { num: "03", title: "Reserva de emergência", description: "Monte sua proteção financeira para imprevistos e durma tranquila sabendo que está segura." },
  { num: "04", title: "Tesouro Direto", description: "Aprenda como investir em renda fixa com segurança, rentabilidade e confiança." },
  { num: "05", title: "Fundos imobiliários", description: "Entenda como gerar renda passiva com fundos imobiliários sem precisar comprar um imóvel." },
  { num: "06", title: "Primeiras ações", description: "Conheça os primeiros passos no mercado de ações de forma simples, clara e sem jargão." },
];

function Modules() {
  const [activeIndex, setActiveIndex] = useState(null);

  return (
    <section id="modulos" style={{ padding: "4rem 1.5rem 5rem", background: "var(--bg-primary)" }}>
      <div style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>

        {/* Label com risco dos dois lados, centralizada */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem", marginBottom: "1.5rem" }}>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-terracotta)", flexShrink: 0 }} />
          <p style={{ textTransform: "uppercase", letterSpacing: "6px", fontSize: "11px", fontWeight: 500, color: "var(--accent-terracotta)" }}>
            Conteúdo do curso
          </p>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-terracotta)", flexShrink: 0 }} />
        </div>

        <h2 className="font-display" style={{ fontSize: "clamp(2.5rem,6vw,4rem)", fontWeight: 300, lineHeight: 1.1, marginBottom: "0.75rem", color: "var(--text-primary)" }}>
          Módulos
          <br />
          <em className="not-italic" style={{ fontWeight: 600, color: "var(--accent-sage)" }}>do Curso</em>
        </h2>

        <p style={{ fontSize: "0.95rem", lineHeight: 1.7, color: "var(--text-secondary)", marginBottom: "3rem" }}>
          6 módulos estruturados para levar você do zero ao seu primeiro investimento.
        </p>

        {/* Accordion — alinhado à esquerda internamente */}
        <div style={{ textAlign: "left" }}>
          {modules.map((module, index) => (
            <div key={index} style={{ borderTop: index === 0 ? "1px solid var(--border-light)" : "none", borderBottom: "1px solid var(--border-light)" }}>
              <button
                onClick={() => setActiveIndex(activeIndex === index ? null : index)}
                style={{ width: "100%", display: "flex", alignItems: "center", gap: "1.5rem", padding: "1.5rem 0", background: "transparent", border: "none", cursor: "pointer", textAlign: "left" }}
              >
                <span className="font-display" style={{ fontSize: "13px", fontWeight: 300, color: activeIndex === index ? "var(--accent-terracotta)" : "var(--text-muted)", flexShrink: 0, width: "24px" }}>
                  {module.num}
                </span>
                <span style={{ flex: 1, fontSize: "1rem", fontWeight: 500, color: activeIndex === index ? "var(--text-primary)" : "var(--text-secondary)", transition: "color 0.3s" }}>
                  {module.title}
                </span>
                <span style={{ color: "var(--accent-terracotta)", fontSize: "1.25rem", transition: "transform 0.3s", transform: activeIndex === index ? "rotate(45deg)" : "rotate(0deg)", display: "inline-block", flexShrink: 0 }}>
                  +
                </span>
              </button>
              {activeIndex === index && (
                <div style={{ paddingBottom: "1.5rem", paddingLeft: "calc(24px + 1.5rem)" }}>
                  <p style={{ fontSize: "0.9rem", lineHeight: 1.7, color: "var(--text-secondary)" }}>
                    {module.description}
                  </p>
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Modules;