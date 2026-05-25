import { useState, useEffect } from "react";

/* Contador regressivo */
function useCountdown(targetHours = 3) {
  const [timeLeft, setTimeLeft] = useState(() => {
    const saved = sessionStorage.getItem("oferta_deadline");
    if (saved) return Math.max(0, parseInt(saved, 10) - Date.now());
    const deadline = Date.now() + targetHours * 60 * 60 * 1000;
    sessionStorage.setItem("oferta_deadline", deadline);
    return targetHours * 60 * 60 * 1000;
  });

  useEffect(() => {
    const id = setInterval(() => {
      setTimeLeft((prev) => Math.max(0, prev - 1000));
    }, 1000);
    return () => clearInterval(id);
  }, []);

  const h = String(Math.floor(timeLeft / 3600000)).padStart(2, "0");
  const m = String(Math.floor((timeLeft % 3600000) / 60000)).padStart(2, "0");
  const s = String(Math.floor((timeLeft % 60000) / 1000)).padStart(2, "0");
  return { h, m, s };
}

function Pricing() {
  const { h, m, s } = useCountdown(3);

  return (
    <section id="pricing" style={{ padding: "4rem 1.5rem 5rem", background: "var(--bg-primary)" }}>
      <div style={{ maxWidth: "560px", margin: "0 auto", textAlign: "center" }}>

        {/* Label centralizada com riscos */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "1rem", marginBottom: "1.5rem" }}>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-sage)", flexShrink: 0 }} />
          <p style={{ textTransform: "uppercase", letterSpacing: "6px", fontSize: "11px", fontWeight: 500, color: "var(--accent-sage)" }}>
            Oferta especial
          </p>
          <div style={{ width: "40px", height: "1px", background: "var(--accent-sage)", flexShrink: 0 }} />
        </div>

        <h2 className="font-display" style={{ fontSize: "clamp(2.5rem,6vw,4rem)", fontWeight: 300, lineHeight: 1.1, marginBottom: "0.75rem", color: "var(--text-primary)" }}>
          Invista em
          <br />
          <em className="not-italic" style={{ fontWeight: 600, color: "var(--accent-terracotta)" }}>você mesma</em>
        </h2>

        <p style={{ fontSize: "0.95rem", lineHeight: 1.7, color: "var(--text-secondary)", marginBottom: "1.5rem" }}>
          Acesso completo a todos os módulos, materiais e suporte da comunidade.
        </p>

        {/* Checklist centralizado */}
        <ul style={{ listStyle: "none", marginBottom: "3rem", display: "inline-block", textAlign: "left" }}>
          {["6 módulos completos em vídeo", "Materiais e planilhas exclusivas", "Comunidade de apoio", "Suporte durante o curso", "Acesso vitalício ao conteúdo"].map((item, i) => (
            <li key={i} style={{ display: "flex", alignItems: "center", gap: "0.75rem", fontSize: "0.9rem", color: "var(--text-secondary)", marginBottom: "0.5rem" }}>
              <span style={{ color: "var(--accent-sage)", fontWeight: 600 }}>✓</span>
              {item}
            </li>
          ))}
        </ul>

        {/* Badge pulsante de urgência */}
        <div style={{ marginBottom: "1.25rem", display: "flex", alignItems: "center", justifyContent: "center", gap: "0.5rem" }}>
          <span className="badge-pulse" style={{ display: "inline-block", width: "8px", height: "8px", borderRadius: "50%", background: "var(--accent-terracotta)", flexShrink: 0 }} />
          <span style={{ fontSize: "12px", fontWeight: 500, color: "var(--accent-terracotta)", textTransform: "uppercase", letterSpacing: "0.06em" }}>
            Oferta por tempo limitado
          </span>
        </div>

        {/* Contador regressivo */}
        <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: "0.5rem", marginBottom: "2rem" }}>
          {[{ v: h, l: "h" }, { v: m, l: "m" }, { v: s, l: "s" }].map(({ v, l }, i) => (
            <div key={l} style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
              <div style={{ display: "flex", flexDirection: "column", alignItems: "center" }}>
                <span className="font-display" style={{ fontSize: "2rem", fontWeight: 300, lineHeight: 1, color: "var(--text-primary)", minWidth: "2.5rem", textAlign: "center" }}>
                  {v}
                </span>
                <span style={{ fontSize: "9px", textTransform: "uppercase", letterSpacing: "3px", color: "var(--text-muted)", marginTop: "2px" }}>{l}</span>
              </div>
              {i < 2 && <span className="font-display" style={{ fontSize: "1.5rem", fontWeight: 300, color: "var(--text-muted)", marginBottom: "12px" }}>:</span>}
            </div>
          ))}
        </div>

        {/* Card de preço */}
        <div className="pricing-card" style={{ textAlign: "center" }}>
          <p style={{ fontSize: "0.875rem", textDecoration: "line-through", color: "var(--text-muted)", marginBottom: "0.25rem" }}>
            De R$ 297
          </p>

          <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "center", gap: "0.25rem", marginBottom: "0.25rem" }}>
            <span className="font-display" style={{ fontSize: "1.5rem", fontWeight: 300, marginTop: "1.25rem", color: "var(--accent-terracotta)" }}>R$</span>
            <span className="font-display" style={{ fontSize: "6rem", fontWeight: 300, lineHeight: 1, color: "var(--accent-terracotta)" }}>97</span>
          </div>

          <p style={{ fontSize: "0.875rem", color: "var(--text-muted)", marginBottom: "2rem" }}>
            ou 12× de R$ 9,70
          </p>

          <div style={{ height: "1px", background: "var(--border-light)", marginBottom: "2rem" }} />

          <button className="btn-primary btn-shimmer" style={{ width: "100%", display: "block" }}>
            Garantir minha vaga
          </button>

          <p style={{ fontSize: "0.75rem", color: "var(--text-muted)", marginTop: "1rem" }}>
            Pagamento 100% seguro · 7 dias de garantia
          </p>
        </div>
      </div>
    </section>
  );
}

export default Pricing;