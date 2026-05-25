import { useState } from "react";

const faqs = [
  { q: "Preciso já investir para fazer o curso?", a: "Não. O curso foi criado especialmente para iniciantes. Você vai aprender do zero, no seu ritmo." },
  { q: "Terei suporte durante o curso?", a: "Sim! Você terá acompanhamento completo durante toda a jornada, com uma comunidade para te apoiar." },
  { q: "Por quanto tempo terei acesso ao conteúdo?", a: "O acesso é vitalício. Você pode revisitar os módulos sempre que precisar, no seu ritmo." },
  { q: "O curso tem garantia?", a: "Sim. Você tem 7 dias de garantia total. Se não ficar satisfeita, devolvemos 100% do seu dinheiro." },
];

function FAQ() {
  const [openIndex, setOpenIndex] = useState(null);

  return (
    <section style={{ padding: "4rem 1.5rem 5rem", background: "var(--bg-secondary)" }}>
      <div style={{ maxWidth: "700px", margin: "0 auto", textAlign: "center" }}>

        {/* Label com risco dos dois lados, centralizada */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem", marginBottom: "1.5rem" }}>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-terracotta)", flexShrink: 0 }} />
          <p style={{ textTransform: "uppercase", letterSpacing: "6px", fontSize: "11px", fontWeight: 500, color: "var(--accent-terracotta)" }}>
            Perguntas frequentes
          </p>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-terracotta)", flexShrink: 0 }} />
        </div>

        <h2 className="font-display" style={{ fontSize: "clamp(2.5rem,6vw,4rem)", fontWeight: 300, lineHeight: 1.1, marginBottom: "3rem", color: "var(--text-primary)" }}>
          Ficou com
          <br />
          <em className="not-italic" style={{ fontWeight: 600, color: "var(--accent-sage)" }}>dúvidas?</em>
        </h2>

        {/* Accordion — texto alinhado à esquerda */}
        <div style={{ textAlign: "left" }}>
          {faqs.map((faq, index) => (
            <div key={index} style={{ borderTop: index === 0 ? "1px solid var(--border-light)" : "none", borderBottom: "1px solid var(--border-light)" }}>
              <button
                onClick={() => setOpenIndex(openIndex === index ? null : index)}
                style={{ width: "100%", display: "flex", alignItems: "center", justifyContent: "space-between", gap: "1rem", padding: "1.5rem 0", background: "transparent", border: "none", cursor: "pointer", textAlign: "left" }}
              >
                <span style={{ fontSize: "0.95rem", fontWeight: 500, color: "var(--text-primary)", flex: 1 }}>
                  {faq.q}
                </span>
                <span style={{ color: "var(--accent-terracotta)", fontSize: "1.25rem", flexShrink: 0, transition: "transform 0.3s", transform: openIndex === index ? "rotate(45deg)" : "rotate(0deg)", display: "inline-block" }}>
                  +
                </span>
              </button>
              {openIndex === index && (
                <div style={{ paddingBottom: "1.5rem" }}>
                  <p style={{ fontSize: "0.9rem", lineHeight: 1.7, color: "var(--text-secondary)" }}>
                    {faq.a}
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

export default FAQ;
