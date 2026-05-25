const testimonials = [
  { quote: "Consegui organizar minha vida financeira e fazer meu primeiro investimento em apenas 2 meses.", name: "Camila R.", detail: "Designer, 29 anos", initial: "C" },
  { quote: "Finalmente entendi como o dinheiro funciona. Sinto-me no controle da minha vida!", name: "Fernanda L.", detail: "Professora, 34 anos", initial: "F" },
  { quote: "O curso é claro, leve e muito prático. Recomendo para toda mulher que quer mudar sua vida.", name: "Isabela M.", detail: "Empreendedora, 41 anos", initial: "I" },
];

function Testimonials() {
  return (
    <section style={{ padding: "4rem 1.5rem 5rem", background: "var(--bg-tertiary)" }}>
      <div style={{ maxWidth: "1000px", margin: "0 auto", textAlign: "center" }}>

        {/* Label centralizada com riscos */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem", marginBottom: "1.5rem" }}>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-gold)", flexShrink: 0 }} />
          <p style={{ textTransform: "uppercase", letterSpacing: "6px", fontSize: "11px", fontWeight: 500, color: "var(--accent-gold)" }}>
            Depoimentos
          </p>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-gold)", flexShrink: 0 }} />
        </div>

        <h2 className="font-display" style={{ fontSize: "clamp(2.5rem,6vw,4rem)", fontWeight: 300, lineHeight: 1.1, marginBottom: "4rem", color: "var(--text-primary)" }}>
          Histórias que
          <br />
          <em className="not-italic" style={{ fontWeight: 600, color: "var(--accent-terracotta)" }}>inspiram</em>
        </h2>

        {/* Cards */}
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: "1.25rem", textAlign: "left" }}>
          {testimonials.map((item, index) => (
            <div key={index} className="testimonial-card" style={{ animationDelay: `${index * 0.15}s` }}>
              <span className="font-display" style={{ fontSize: "3.5rem", fontWeight: 300, lineHeight: 1, display: "block", marginBottom: "1rem", color: "var(--accent-blush)" }}>"</span>
              <p style={{ fontSize: "0.95rem", lineHeight: 1.7, marginBottom: "2rem", fontWeight: 300, color: "var(--text-secondary)" }}>
                {item.quote}
              </p>
              <div style={{ display: "flex", alignItems: "center", gap: "1rem", borderTop: "1px solid var(--border-light)", paddingTop: "1.5rem" }}>
                <div style={{ width: "40px", height: "40px", borderRadius: "50%", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "14px", fontWeight: 600, flexShrink: 0, background: "var(--accent-blush)", color: "var(--accent-terracotta)" }}>
                  {item.initial}
                </div>
                <div>
                  <p style={{ fontWeight: 600, fontSize: "0.875rem", color: "var(--text-primary)" }}>{item.name}</p>
                  <p style={{ fontSize: "0.75rem", color: "var(--text-muted)" }}>{item.detail}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Testimonials;
